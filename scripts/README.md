# Scripts & Workflow Configuration

This directory contains helper scripts used by the n8n workflows.

## Workflow Configuration: Using OpenRouter for Cost-Effective AI

The `Video Clip Automation` workflow is configured to use [OpenRouter.ai](https://openrouter.ai/) to take advantage of free and cost-effective AI models.

### Required Setup:

1.  **Get an OpenRouter API Key:**
    *   Sign up for a free account at [OpenRouter.ai](https://openrouter.ai/).
    *   Go to your **Account Settings** and create a new API key.

2.  **Add API Key to n8n:**
    *   In your n8n instance, go to the **Credentials** section.
    *   Create a new "Header Auth" credential.
    *   Name it `OpenRouter API Key` (or similar).
    *   Set the **Name** field to `Authorization`.
    *   Set the **Value** field to `Bearer YOUR_API_KEY_HERE`, replacing `YOUR_API_KEY_HERE` with the key you generated.

3.  **Connect Credentials in the Workflow:**
    *   Open the `Video Clip Automation` workflow.
    *   In both the "Transcribe Video (OpenRouter)" and "Identify Key Moments (OpenRouter)" nodes, select the credential you just created from the "Authentication" dropdown.

### Models Used:
*   **Transcription:** `openai/whisper-large-v3`
*   **Analysis:** `google/gemini-pro`

## Script Dependencies

### `ffmpeg`

The `clip_video.py` script requires `ffmpeg` to be installed and available in the system's PATH.

#### Installation

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS (using Homebrew):**
```bash
brew install ffmpeg
```

**Windows (using Chocolatey):**
```bash
choco install ffmpeg
```

After installation, you can verify it's working by running:
```bash
ffmpeg -version
```
