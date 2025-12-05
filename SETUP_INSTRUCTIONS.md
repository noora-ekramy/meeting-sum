# Setup Instructions

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Create .env File**
   Create a file named `.env` in the project root directory with:
   ```
   COHERE_API_KEY=your_cohere_api_key_here
   ```
   **⚠️ REQUIRED:** Replace `your_cohere_api_key_here` with your actual Cohere API key.

3. **Run the App**
   ```bash
   streamlit run app.py
   ```

## Features

✅ **Cohere AI Integration** - Uses Cohere API for intelligent summaries
✅ **Auto-Save History** - All summaries saved to `history/` folder
✅ **Session Management** - Load previous sessions from sidebar
✅ **Interactive Chat** - Ask questions about the summary
✅ **Dark Theme UI** - Modern, sleek interface
✅ **No API Key in UI** - API key loaded from .env file

## Usage

1. Paste your meeting transcript in the text area
2. Click "Generate Summary"
3. View your AI-generated summary
4. Click "💬 Chat with Summary" to ask questions
5. Ask things like "Who must do what?" or "What are the action items?"
6. Download or access from history sidebar

## History Management

- All sessions automatically saved
- View last 10 sessions in sidebar
- Click to load previous session
- Delete unwanted sessions with 🗑️ button
- Click "New Session" to start fresh

## Chat Features

- Click "💬 Chat with Summary" button after generating a summary
- Ask questions about the meeting:
  - "Who must do what?"
  - "What are the action items?"
  - "What decisions were made?"
  - "What are the deadlines?"
- AI maintains context from the transcript and summary
- Clear chat history with "Clear Chat" button
- Chat history persists during the session

## Example Questions

- "Who is responsible for the marketing campaign?"
- "What tasks were assigned to John?"
- "What are the next steps?"
- "When is the project deadline?"
- "What were the main concerns discussed?"

Enjoy! 🚀

