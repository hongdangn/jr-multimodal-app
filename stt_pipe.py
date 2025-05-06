import torch
from transformers import pipeline

# config
model_name = "kotoba-tech/kotoba-whisper-v2.1"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
device = "cuda:0" if torch.cuda.is_available() else "cpu"
# model_kwargs = {"attn_implementation": "sdpa"} if torch.cuda.is_available() else {}
generate_kwargs = {"language": "ja", "task": "transcribe"}

pipe = pipeline(
    model=model_name,
    torch_dtype=torch_dtype,
    device_map={"": device},
    batch_size=16,
    trust_remote_code=True,
    punctuator=True
)