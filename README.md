# 🧠 AI Recipe Generator with GPT

This project is a GPT-powered recipe generation app where users can input ingredients and receive a unique recipe with a name and step-by-step instructions. It's built using the Hugging Face Transformers library and Streamlit for the web UI.

## 🌟 Features

- 🍳 Generate recipe names and instructions from user-provided ingredients
- 🤖 Fine-tuned GPT model for creative and relevant recipe results
- 🖥️ Simple Streamlit interface
- 🧼 Clean and lightweight GitHub repo (model files excluded)

## 📂 Dataset

- **Mini_Cleaned_Recipe_dataset.csv**: Contains columns for `Ingredients`, `Recipe_Name`, and `Instruction`.
- Preprocessed into formatted text for GPT training.

## ⚙️ Tech Stack

- Python
- Hugging Face Transformers
- Streamlit
- PyTorch (or TensorFlow as backend)

## 🚀 How to Run

### 1. Clone the Repository


git clone https://github.com/Dopikaps321/recipe-generation-gpt.git
cd recipe-generation-gpt

## 2. Install Dependencies

pip install -r requirements.txt
If requirements.txt doesn't exist, install manually:

pip install streamlit transformers torch
## 3. Run the App

streamlit run app.py
## 4. Use It
Enter ingredients like:
tomato, onion, garlic, chicken, rice

Get a creative recipe name and instructions!


