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
