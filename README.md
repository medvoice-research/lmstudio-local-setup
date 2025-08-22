# LM Studio Local Setup

A complete setup guide and example scripts for running LM Studio locally with Python SDK integration.

## Overview

This project provides:
- Step-by-step LM Studio installation and configuration
- Python examples using both LM Studio SDK and OpenAI-compatible API
- Connection testing utilities
- Sample chat completion implementations

## Prerequisites

- Python 3.13 or higher
- Windows, macOS, or Linux
- At least 8GB RAM (16GB+ recommended for larger models)

## LM Studio Installation

1. **Download LM Studio**
   - Visit [LM Studio official website](https://lmstudio.ai/)
   - Download the installer for your operating system
   - Install following the standard installation process

2. **Download a Model**
   - Launch LM Studio
   - Go to the "Discover" tab
   - Search for and download a model

3. **Start the Local Server**
   - Navigate to the "Developer" tab in LM Studio
   - Toggle "Status: Stopped" to "Status: Running"

## Python Environment Setup

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver that works great with this project.

1. **Install uv**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. **Clone this repository**
   ```bash
   git clone https://github.com/medvoice-research/lmstudio-local-setup.git
   cd lmstudio-local-setup
   ```

3. **Install dependencies with uv**
   ```bash
   uv sync
   ```

### Using Traditional pip/venv

1. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

2. **Install dependencies with pip**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Environment Variables (Optional for local testing)**
   Create a `.env` file in the project root:
    ```bash
    cp .env.example .env
    ```

    ```env
    LMSTUDIO_SERVER_HOST=localhost:1234
    LMSTUDIO_API_HOST=http://localhost:1234/v1
    LMSTUDIO_API_KEY=lm-studio
    MODEL_CHOICE=your-preferred-model-name
    ```

## Usage Examples

### 1. Test Connection
Run the comprehensive connection test:
```bash
python test_lmstudio_connection.py
```

This script will:
- Test LM Studio SDK connection
- Test OpenAI-compatible API connection
- Perform a sample chat completion
- Provide troubleshooting information if connections fail

### 2. Simple Hello World
Run the basic example:
```bash
python lmstudio_hello_world.py
```

### 3. Using OpenAI-Compatible API
```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)

response = client.chat.completions.create(
    model="your-model-name",
    messages=[
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

print(response.choices[0].message.content)
```

## Troubleshooting

See [docs/troubleshooting.md](docs/troubleshooting.md) for information on increasing VRAM on Apple Silicon.

## License

See [LICENSE](LICENSE) file for details.

## Additional Resources

- [LM Studio Documentation](https://lmstudio.ai/docs)
- [LM Studio Python SDK](https://pypi.org/project/lmstudio/)
- [OpenAI Python Library](https://github.com/openai/openai-python)

