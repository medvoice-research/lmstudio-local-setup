# Guide: Running Advanced MLX Models

When dealing with cutting-edge or very large MLX models, you may encounter errors within GUI applications like LM Studio if the app's internal MLX backend doesn't support the model's specific quantization format.

This guide provides instructions on how to run these models directly using Apple's `mlx-lm` Python library, bypassing the GUI loader.

## Prerequisites

Ensure your Python environment is set up and you have installed the necessary dependencies from `requirements.txt`. You will also need to install the core MLX libraries.

```bash
# Make sure you have synced your environment
uv sync

# Install mlx-lm
pip install mlx-lm
```

## Running the Model with a Python Script

The following script shows how to load the `GreenBitAI/DeepSeek-R1-671B-layer-mix-bpw-4.0-mlx` model and run inference.

1.  **Create the Python script:**
    Save the following code as `run_deepseek_mlx.py` in the root of this project.

    ```python
    import mlx.core as mx
    from mlx_lm import load, generate
    import time

    # --- Configuration ---
    MODEL_NAME = "GreenBitAI/DeepSeek-R1-671B-layer-mix-bpw-4.0-mlx"
    PROMPT = "Hello, who are you?"
    MAX_TOKENS = 200
    TEMP = 0.7

    print(f"Loading model: {MODEL_NAME}...")
    print("This may take a few minutes for a large model...")

    # Record start time
    start_time = time.time()

    # Load the model and tokenizer
    # This will download the model from Hugging Face on the first run
    model, tokenizer = load(MODEL_NAME)

    # Record end time and calculate duration
    end_time = time.time()
    print(f"Model loaded in {end_time - start_time:.2f} seconds.")

    print("\n--- Generating Response ---")
    
    # Generate a response
    response = generate(
        model,
        tokenizer,
        prompt=PROMPT,
        max_tokens=MAX_TOKENS,
        temp=TEMP,
        verbose=True
    )

    print("\n--- End of Response ---")

    ```

2.  **Run the script:**
    Execute the script from your terminal:
    ```bash
    python run_deepseek_mlx.py
    ```

    The first time you run it, `mlx-lm` will download the model files from Hugging Face, which may take a significant amount of time. Subsequent runs will load the model from the local cache.

## Important: System Memory Configuration (`sysctl`)

For a model of this size (360GB), you **must** ensure that macOS allocates enough RAM to the GPU. Even with 512GB of total RAM, the default limit is too low.

-   **Set the VRAM limit:** Before running the script, set the `iogpu.wired_limit_mb` to a value higher than the model size. For a 360GB model, a value of 400GB (409,600 MB) is a safe starting point.

    ```bash
    # Set VRAM limit to 400GB. This resets on reboot.
    sudo sysctl iogpu.wired_limit_mb=409600
    ```

-   **Make it persistent:** To ensure this setting survives a reboot, add it to `/etc/sysctl.conf`. See the main `troubleshooting.md` for more details.

This approach gives you a direct way to work with the most advanced models, ensuring you are always using the latest MLX capabilities.

## References

- [Apple's MLX Examples on GitHub](https://github.com/ml-explore/mlx-examples)
- [Hugging Face: GreenBitAI/DeepSeek-R1-671B-layer-mix-bpw-4.0-mlx](https://huggingface.co/GreenBitAI/DeepSeek-R1-671B-layer-mix-bpw-4.0-mlx)
- [Adjusting VRAM/RAM split on Apple Silicon (GitHub Discussion)](https://github.com/ggml-org/llama.cpp/discussions/2182)
