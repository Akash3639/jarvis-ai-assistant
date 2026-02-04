from transformers import AutoTokenizer, AutoModelForCausalLM

def load_llm():
    model_name = "microsoft/phi-2"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        device_map="auto"
    )
    return tokenizer, model
