# 📊 Local CSV ChatBot (No API Key Required)

This is a simple chatbot built with **Streamlit** that lets you upload a CSV file and ask questions about it.  
The chatbot can calculate **averages, sums**, and generate **graphs** (line, bar, scatter, histogram).

---

## ⚡ Features
- Upload any CSV file
- Preview first rows of the dataset
- Ask natural questions like:
  - `average of Sales`
  - `sum of Profit`
  - `bar plot Month vs Sales`
  - `scatter plot Profit vs Sales`
  - `hist plot Sales`
- Supports **line, bar, scatter, and histogram** plots
- Runs **locally** (no API key needed)

---

## 📂 Project Structure
local_CSV_ChatBot/
│── chatbot.py # Main Streamlit app
│── requirements.txt # Python dependencies
│── .gitignore # Ignore venv and other junk


---

## 🛠 Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Vritisoni/local_CSV_ChatBot.git
   cd local_CSV_ChatBot

# Create and activate a virtual environment:

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies:

pip install -r requirements.txt

# Run the app:

streamlit run chatbot.py


Open your browser at:

http://localhost:8501


# 📦 Requirements

Make sure these packages are installed (already in requirements.txt):

streamlit
pandas
matplotlib

📸 Example

Upload CSV file → Ask:

bar plot Month vs Sales

average of Profit

📊 The chatbot will calculate results or show the graph instantly!

🚀 Future Improvements

Add LLM integration for more natural Q&A

Support Excel files

Export graphs as images

👨‍💻 Made with ❤️ by [vritaka soni]


---

👉 Save this as **README.md** in your project root before pushing to GitHub.  

Do you want me to also make a **requirements.txt** for you (so users can install all needed libraries easily)