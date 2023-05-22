from flask import Flask, render_template, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import os

app = Flask(__name__)

token = os.environ.get('HF_TOKEN')
apiroot = os.environ.get('API_ROOT')
if token is None:
    raise ValueError("HF_TOKEN environment variable is not set.")
if apiroot is None:
    raise ValueError("API_ROOT environment variable is not set.")

tokenizer = DistilBertTokenizer.from_pretrained('spambloq/spambloq', use_auth_token=token)
model = DistilBertForSequenceClassification.from_pretrained('spambloq/spambloq', use_auth_token=token)
model.eval()

if torch.backends.mps.is_available():
    device = torch.device('mps')
elif torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
model.to(device)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5000 per day", "250 per hour", "10 per minute"]
)

@app.route('/')
@limiter.exempt
def home():
    return render_template('index.html', apiroot=apiroot)

@app.route('/api/v1/classify', methods=['GET', 'POST'])
def classify():
    if request.method == 'POST':
        text = request.form['text']
        print("Classify via POST")
    else:
        text = request.args.get('text')
        print("Classify via GET")
    
    if text is None:
        error_message = {'error': 'Text parameter is missing'}
        print("Error: text param is missing")
        return jsonify(error_message), 400

    text = text.strip()
    if (text == ''):
        error_message = {'error': 'Text parameter is empty'}
        print("Error: text param is missing")
        return jsonify(error_message), 400
    print("=== Classifying ===")
    print(text)
    print("===================")
    # Truncate the input to 512 characters
    text = text[:512]

    # Tokenize the input text
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        truncation=True,
        max_length=512,
        return_tensors='pt'
    ).to(device)

    # Classify the input text
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        softmax = torch.softmax(logits, dim=1).tolist()[0]

    result = {
        'classification': 'ham' if softmax[0] > softmax[1] else 'spam',
        'ham': softmax[0],
        'spam': softmax[1]
    }

    return jsonify(result)

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify({'error': 'Too many requests! The current rate limit is 5000 requests per day, 250 requests per hour, and 10 requests per minute. Please slow down!'}), 429

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.getenv('SERVER_PORT', 80))

