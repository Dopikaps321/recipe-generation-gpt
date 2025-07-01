import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import re

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("./recipe_model")
model = AutoModelForCausalLM.from_pretrained("./recipe_model")

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=0)

# Streamlit UI
st.title("🍳 AI Recipe Generator")
ingredients = st.text_input("Enter ingredients (comma-separated):")

if st.button("Generate Recipe"):
    if ingredients:
        prompt = f"Ingredients: {ingredients}\nRecipe Name:"
        output = generator(prompt, max_length=300, num_return_sequences=1, truncation=True)[0]["generated_text"]

        # Extract Recipe Name and Instructions
        try:
            recipe_name = output.split("Recipe Name:")[1].split("Instructions:")[0].strip()
            raw_instructions = output.split("Instructions:")[1].split("Ingredients:")[0].strip()
        except IndexError:
            recipe_name = "N/A"
            raw_instructions = output

        # Clean list-style instructions if they look like JSON array
        if raw_instructions.startswith("["):
            # Remove brackets and quotes
            cleaned = re.findall(r'"(.*?)"', raw_instructions)
            instructions = "\n".join([f"{i+1}. {step}" for i, step in enumerate(cleaned)])
        else:
            instructions = raw_instructions.strip()

        st.markdown(f"### 🧾 {recipe_name}")
        st.text_area("📋 Instructions", instructions, height=300)
