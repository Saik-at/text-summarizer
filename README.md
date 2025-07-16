# 📝 Generative Text Summarizer

This is a Streamlit-based web application that summarizes long-form text using the `facebook/bart-large-cnn` transformer model from HuggingFace. It allows users to input any article, paragraph, or raw text and receive a concise summary within seconds.

---

## 🚀 Features

- 🔍 Real-time semantic summarization using BART
- 💬 User-friendly Streamlit interface
- ⚡ Fast and lightweight — runs locally
- 📎 HuggingFace Transformers-powered backend

---

## 📁 Project Structure
text-summarizer/
├── streamapp.py # Streamlit frontend for user interaction
├── summarizer.py # Summary generation logic using BART model
├── requirements.txt # Python dependencies
├── summary.txt # summary


---

## ⚙️ Installation

Install dependencies using:

```bash
pip install -r requirements.txt

## ▶️ Run the App
To launch the Streamlit app:

run this in terminal:
streamlit run streamapp.py
Then go to the browser window that opens (usually http://localhost:8501)

## Model Used
facebook/bart-large-cnn

This model is pre-trained for abstractive summarization and performs exceptionally well on articles and reports.

Author
Saikat Jana
📂 GitHub: Saik-at

📄 License
This project is open-source under the MIT License.
