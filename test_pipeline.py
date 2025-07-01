from transformers import pipeline

generator = pipeline("text-generation", model="./recipe_model", tokenizer="./recipe_model")

ingredients = "egg, tomato, onion"
prompt = f"Ingredients: {ingredients}\nRecipe Name:"
output = generator(prompt, max_length=150, truncation=True)
print(output[0]["generated_text"])
