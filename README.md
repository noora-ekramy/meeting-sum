# 📝 Meeting Summarizer

AI-powered meeting transcript summarizer with interactive chat using Cohere AI.

## Features

- 🤖 AI-Powered Summaries using Cohere command-r-08-2024
- 💬 Interactive Chat with streaming responses
- 📜 Session History management
- 🎨 Modern dark theme UI
- 📥 Export summaries

## Quick Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

**Option A: Using Streamlit Secrets (Recommended for deployment)**

Create `.streamlit/secrets.toml`:
```toml
COHERE_API_KEY = "your_cohere_api_key_here"
```

**Option B: Using .env file (Local development)**

Create `.env`:
```
COHERE_API_KEY=your_cohere_api_key_here
```

Get your API key from [cohere.ai](https://cohere.ai)

### 3. Run

```bash
streamlit run app.py
```

## Usage

1. Paste your meeting transcript
2. Click "Generate Summary"
3. Click "💬 Chat with Summary" to ask questions
4. Ask things like:
   - "Who must do what?"
   - "What are the action items?"
   - "What decisions were made?"

## Deployment

### Streamlit Cloud

1. Push to GitHub
2. Connect to Streamlit Cloud
3. Add `COHERE_API_KEY` to Secrets in dashboard
4. Deploy!

## Project Structure

```
.
├── app.py              # Main application
├── requirements.txt    # Dependencies
├── .gitignore         # Git ignore rules
├── history/           # Session storage (auto-created)
└── README.md          # This file
```

## License

MIT
