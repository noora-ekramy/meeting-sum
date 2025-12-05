# 📝 Meeting Summarizer

A beautiful Streamlit application that allows you to upload meeting transcripts and get AI-powered summaries using Cohere AI.

## ✨ Features

- 📄 **Transcript Support**: Upload TXT files or paste text directly
- 🤖 **AI-Powered Summaries**: Uses Cohere AI for intelligent summarization
- 💬 **Interactive Chat**: Ask questions about the summary (e.g., "Who must do what?")
- ⚡ **Streaming Responses**: Real-time word-by-word chat responses
- 🎨 **Beautiful Dark UI**: Modern, sleek dark theme interface
- 📜 **History Tracking**: All summaries are automatically saved to history
- 💾 **Session Management**: Load previous sessions from sidebar
- 📥 **Export**: Download summaries as text files

## 🚀 Installation

1. Clone or download this repository

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

4. Add your Cohere API key to the `.env` file:
```
COHERE_API_KEY=your_cohere_api_key_here
```

## 📖 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown (usually `http://localhost:8501`)

3. Either:
   - Upload a text file (.txt or .docx), or
   - Paste a transcript in the text area

4. Click "Generate Summary" and wait for processing

5. View your AI-generated summary

6. Click "💬 Chat with Summary" to ask questions like:
   - "Who must do what?"
   - "What are the action items?"
   - "What decisions were made?"

7. Download or access your summary from the history sidebar!

## ⚙️ Configuration

- **Cohere API Key**: Required. Set in `.env` file as `COHERE_API_KEY`
- **History Folder**: Summaries are automatically saved to the `history/` folder

## 📋 Requirements

- Python 3.8+
- Cohere API key (get one at [cohere.ai](https://cohere.ai))

## 🎨 Features

- Modern dark theme design
- Glassmorphic UI elements
- Session history in sidebar
- One-click session loading
- Delete old sessions
- Auto-save every summary

## 📁 Project Structure

```
.
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this)
├── .env.example       # Example environment file
├── history/           # Auto-created folder for session history
└── README.md          # This file
```

## 📝 Notes

- All sessions are automatically saved to the `history/` folder
- The API key is loaded from the `.env` file (not entered in the UI)
- Audio/video upload UI is present but only for display (not functional)
- Only text input and text file uploads are processed

## 🤝 Contributing

Feel free to submit issues or pull requests!

## 📄 License

MIT License

