<div align="center">
<img src="https://github.com/spambloq/spambloq-api/assets/76186054/e0ad8204-70f1-4e61-9a57-b66137c8c044" width="200">


# Spambloq API + GUI

**Note: This is not open-sourced software! Please refer to the [license](LICENSE) for details.**

<img width="500" src="https://github.com/spambloq/spambloq-api/assets/76186054/383c55c0-b45f-4994-97a6-a6f16827f370">

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

    
</div>

```json
{
    "classification": "ham",
    "ham": 0.99,
    "spam": 0.01
}
```

<div align="center">

## License

See the [LICENSE file](LICENSE).

</div> 
