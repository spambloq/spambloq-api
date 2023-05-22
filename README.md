# spambloq-api
<img width="500" src="https://github.com/spambloq/spambloq-api/assets/76186054/a6d51d29-79c7-4c8e-b63c-122692259771">

This API and GUI for Spambloq allows you to locally run a Spambloq API instance.

The following variable must be set in the environment:

- `HF_TOKEN` - You must have access to the Spambloq model through Hugging Face. If you do, please find your token [here](https://huggingface.co/settings/tokens).
- `API_ROOT` - Set this to the root of the API. If you're hosting this on Hugging Face Spaces, set this to `[username]-[spacename].hf.space`
- `SERVER_PORT` Optional (Default 80): If you're using Hugging Face Spaces, set the SDK to Gradio and set this variable to `7860`.

## Setting up on Hugging Face Spaces

1. Create a new Hugging Face Space. Click [here](https://huggingface.co/new-space?name=Spambloq&sdk=gradio) for a configuration template.
2. Download this repository
3. Upload all files in this repository to the new Space you created. To do this, go to the Files tab. Click the "Add Files" button. Under the dropdown, select "Upload Files"
4. Click the Settings tab. Scroll down until you see "Repository secrets." Click the "New Secret" button. Set `HF_TOKEN` to your Hugging Face Token. Click "Add new secret." Repeat, creating the "API_ROOT" secret (set this to `[yourusername]-[yourspacename].hf.space`) and `SERVER PORT` secret (set this to `7860`).
5. Click on the App tab and wait for the space to build.
6. Test it out with some spam!

## API Documentation

Endpoint: `https://spambloq-spambloq.hf.space/api/v1/classify`

Methods: `POST`, `GET`

Parameters:

`text`: The input text to be classified

Response:

{
    "text": "Your Input Text",
    "classification": "ham",
    "ham": 0.99,
    "spam": 0.01
}

## License

See the LICENSE file.
