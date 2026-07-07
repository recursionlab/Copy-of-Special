from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-4-Scout-17B-16E")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-4-Scout-17B-16E",
    torch_dtype=torch.float16,
    device_map="auto",
    load_in_8bit=True
)

prompt = "Explain the theory of relativity in simple terms."
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=200,
    do_sample=True,
    top_p=0.9,
    temperature=0.7
)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)