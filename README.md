# AI-Powered Document Study Assistant

A practical Generative AI application built to satisfy the Mini Project curriculum requirement. This application allows users to upload any PDF document (notes, textbooks, research papers) and interact with it via a clean chat interface using Retrieval-Augmented Generation principles.

## 🚀 Features
- **Smart PDF Processing:** Dynamically extracts and parses text from uploaded files using `pypdf`.
- **Context-Aware Answers:** Anchors responses strictly to the document contents using the Gemini 2.5 Flash model.
- **Interactive UI:** Leverages Streamlit's native chat layout for a smooth conversational user experience.

## 🛠️ Tech Stack
- **Language:** Python
- **AI Engine:** Google Gemini 2.5 Flash
- **Web UI:** Streamlit
- **PDF Extraction:** PyPDF

## 📦 Local Installation & Setup

1. **Clone this repository:**
   ```bash
   git clone <your-github-repo-url>
   cd ai-pdf-chatbot
   ```

2. **Install the required Python modules:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the web interface application:**
   ```bash
   streamlit run app.py
   ```

## ⚙️ How to Use
1. Obtain a free API Key from **Google AI Studio**.
2. Input the key in the sidebar panel.
3. Drag and drop your target PDF file into the uploader area.
4. Begin typing questions in the chat box at the bottom.
