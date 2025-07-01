from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load tokenizer and model manually
tokenizer = AutoTokenizer.from_pretrained("./recipe_model")
model = AutoModelForCausalLM.from_pretrained("./recipe_model")

# Create the text generation pipeline
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

ingredients = input("Enter ingredients (comma-separated): ")
prompt = f"Ingredients: {ingredients}\nRecipe Name:"
output = generator(prompt, max_length=200, num_return_sequences=1, truncation=True)

print("\n🍽️ Generated Recipe:\n")
print(output[0]["generated_text"])
