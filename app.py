import streamlit as st
import os
import tempfile
from pathlib import Path
import json
from datetime import datetime
from dotenv import load_dotenv
try:
    import cohere
except:
    pass

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Meeting Summarizer",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, .stApp {
        background-color: #161616;
        font-family: 'Inter', sans-serif;
        height: 100%;
        margin: 0;
        padding: 0;
    }
    
    .stApp {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    
    .header {
        font-size: 48px;
        font-weight: bold;
        color: #FFFFFF;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    
    .tagline {
        font-size: 20px;
        font-weight: 500;
        color: #FFFFFF;
        text-align: center;
        margin-bottom: 30px;
        opacity: 0.8;
    }
    
    .content-container {
        padding: 1rem;
        border-radius: 1.5rem;
        margin-bottom: 1rem;
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0px 0.84px 0px 0px #FFFFFF14 inset;
        box-shadow: 2px 2px 19px 0px #FFFFFF1A;
    }
    
    .summary-box {
        padding: 1.5rem;
        border-radius: 1.5rem;
        margin: 1.5rem 0;
        background: linear-gradient(180deg, rgba(17, 17, 17, 0.02) 0%, rgba(32, 32, 32, 0.02) 100%),
        linear-gradient(0deg, rgba(82, 82, 82, 0.2), rgba(82, 82, 82, 0.2));
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0px 0.84px 0px 0px #FFFFFF14 inset;
        box-shadow: 2px 2px 19px 0px #FFFFFF1A;
        color: #FFFFFF;
    }
    
    .info-box {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1rem;
        margin: 1rem 0;
        color: #FFFFFF;
    }
    
    .stSidebar {
        background: linear-gradient(304deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        backdrop-filter: blur(87.27272033691406px);
        box-shadow: 0px 0.84px 0px 0px #FFFFFF14 inset;
        box-shadow: 2px 2px 19px 0px #FFFFFF1A;
    }
    
    .stTextInput > div > div > input {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 8px;
    }
    
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05);
        color: white;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
    }
    
    header[data-testid="stHeader"] {
        background-color: #38383880;
    }
    
    div[data-baseweb="notification"] {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 12px;
    }
    
    .stButton>button {
        background: linear-gradient(105.13deg, #292929 41.52%, rgba(63, 63, 63, 0) 100%);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 12px 24px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background: linear-gradient(105.13deg, #3a3a3a 41.52%, rgba(63, 63, 63, 0) 100%);
        box-shadow: 0px 0.84px 0px 0px #FFFFFF14 inset;
        box-shadow: 2px 2px 19px 0px #FFFFFF1A;
    }
    
    .stDownloadButton>button {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 12px;
    }
    
    .upload-text {
        color: #FFFFFF;
        font-size: 14px;
        opacity: 0.7;
    }
    
    /* File uploader styling */
    section[data-testid="stFileUploader"] {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        border: 2px dashed rgba(255, 255, 255, 0.2);
        border-radius: 16px;
        padding: 2rem;
    }
    
    section[data-testid="stFileUploader"] label {
        color: #FFFFFF !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        color: white;
        border-radius: 12px;
    }
    
    /* Markdown text color */
    .stMarkdown {
        color: #FFFFFF;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }
    
    p {
        color: #FFFFFF;
    }
    
    label {
        color: #FFFFFF !important;
    }
    
    /* Chat styling */
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 1rem;
    }
    
    /* Form styling */
    .stForm {
        background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 1rem;
    }
    
    /* Better form buttons */
    .stForm button[kind="formSubmit"] {
        background: linear-gradient(105.13deg, #292929 41.52%, rgba(63, 63, 63, 0) 100%);
        color: white;
        border: 2px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
    }
    
    .stForm button[kind="formSubmit"]:hover {
        background: linear-gradient(105.13deg, #3a3a3a 41.52%, rgba(63, 63, 63, 0) 100%);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'summary' not in st.session_state:
    st.session_state.summary = None
if 'transcript' not in st.session_state:
    st.session_state.transcript = None
if 'current_session_id' not in st.session_state:
    st.session_state.current_session_id = None
if 'chat_messages' not in st.session_state:
    st.session_state.chat_messages = []
if 'show_chat' not in st.session_state:
    st.session_state.show_chat = False

# Create history folder if it doesn't exist
HISTORY_FOLDER = Path("history")
HISTORY_FOLDER.mkdir(exist_ok=True)

def get_cohere_api_key():
    """Get Cohere API key from Streamlit secrets or environment"""
    # Try Streamlit secrets first
    try:
        if hasattr(st, 'secrets') and 'COHERE_API_KEY' in st.secrets:
            return st.secrets['COHERE_API_KEY']
    except:
        pass
    
    # Fallback to environment variable
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("COHERE_API_KEY not found. Please add it to Streamlit secrets or .env file.")
    return api_key

def generate_summary(text):
    """Generate summary using Cohere Chat API"""
    try:
        api_key = get_cohere_api_key()
        co = cohere.Client(api_key)
        
        message = f"""Please provide a comprehensive summary of the following meeting transcript. Focus on:
- Key points discussed
- Important decisions made
- Action items and who is responsible
- Main takeaways
- Deadlines and timelines

Transcript:
{text}

Please provide a detailed summary:"""
        
        response = co.chat(
            model='command-r-08-2024',
            message=message,
            temperature=0.7,
            max_tokens=4000
        )
        
        return response.text.strip()
    except ValueError as e:
        # API key not found - re-raise to show error to user
        raise e
    except Exception as e:
        # Fallback: Simple summary extraction
        st.warning(f"Could not connect to AI service: {str(e)}. Using basic summary.")
        try:
            sentences = text.split('.')
            if len(sentences) > 10:
                # Take first 5 and last 5 sentences
                summary = '. '.join(sentences[:5] + ['...'] + sentences[-5:])
                return summary + "."
            return text[:1000] + "..." if len(text) > 1000 else text
        except:
            return text[:1000] + "..." if len(text) > 1000 else text

def save_to_history(transcript, summary):
    """Save session to history folder"""
    try:
        session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        session_data = {
            "id": session_id,
            "timestamp": datetime.now().isoformat(),
            "transcript": transcript,
            "summary": summary
        }
        
        file_path = HISTORY_FOLDER / f"{session_id}.json"
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)
        
        return session_id
    except Exception:
        return None

def load_history():
    """Load all history sessions"""
    try:
        history_files = sorted(HISTORY_FOLDER.glob("*.json"), reverse=True)
        sessions = []
        
        for file_path in history_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    session = json.load(f)
                    sessions.append(session)
            except:
                continue
        
        return sessions
    except:
        return []

def load_session(session_id):
    """Load a specific session"""
    try:
        file_path = HISTORY_FOLDER / f"{session_id}.json"
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def delete_session(session_id):
    """Delete a session from history"""
    try:
        file_path = HISTORY_FOLDER / f"{session_id}.json"
        if file_path.exists():
            os.remove(file_path)
            return True
    except:
        pass
    return False

def chat_with_summary_stream(question, transcript, summary, chat_history):
    """Chat about the summary using Cohere Chat API with streaming"""
    try:
        api_key = get_cohere_api_key()
        co = cohere.Client(api_key)
        
        # Build context with transcript and summary
        preamble = f"""You are a helpful AI assistant that answers questions about meeting transcripts and summaries.

Meeting Transcript:
{transcript[:3000]}

Summary:
{summary}

Please answer questions accurately based on the information above. Focus on being specific about who is responsible for what tasks, deadlines, decisions made, and action items."""
        
        # Build chat history in Cohere format
        chat_history_formatted = []
        for msg in chat_history[-6:]:  # Last 6 messages (3 pairs)
            if msg['role'] == 'user':
                chat_history_formatted.append({
                    'role': 'USER',
                    'message': msg['content']
                })
            else:
                chat_history_formatted.append({
                    'role': 'CHATBOT',
                    'message': msg['content']
                })
        
        # Return the streaming response
        stream = co.chat_stream(
            model='command-r-08-2024',
            message=question,
            preamble=preamble,
            chat_history=chat_history_formatted,
            temperature=0.7,
            max_tokens=1000
        )
        
        return stream
    except ValueError as e:
        # API key not found
        raise e
    except Exception as e:
        # Other errors
        st.error(f"Error connecting to Cohere API: {str(e)}")
        return None

def main():
    # Title Section
    st.markdown("""
        <div class="header">📝 Meeting Summarizer</div>
        <div class="tagline">Transform your transcripts into concise summaries</div>
    """, unsafe_allow_html=True)
    
    # Sidebar Configuration
    with st.sidebar:
        st.markdown("### 📜 History")
        
        # Load history
        history_sessions = load_history()
        
        if history_sessions:
            for session in history_sessions[:10]:  # Show last 10 sessions
                session_id = session.get('id', 'Unknown')
                timestamp = session.get('timestamp', '')
                
                # Format timestamp
                try:
                    dt = datetime.fromisoformat(timestamp)
                    display_time = dt.strftime("%b %d, %Y %I:%M %p")
                except:
                    display_time = session_id
                
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    if st.button(f"📄 {display_time}", key=f"load_{session_id}", use_container_width=True):
                        loaded = load_session(session_id)
                        if loaded:
                            st.session_state.transcript = loaded.get('transcript', '')
                            st.session_state.summary = loaded.get('summary', '')
                            st.session_state.current_session_id = session_id
                            st.rerun()
                
                with col2:
                    if st.button("🗑️", key=f"del_{session_id}"):
                        if delete_session(session_id):
                            st.rerun()
        else:
            st.markdown("""
            <div style="color: #FFFFFF; opacity: 0.6; text-align: center; padding: 1rem;">
            No history yet
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # New session button
        if st.button("➕ New Session", use_container_width=True):
            st.session_state.transcript = None
            st.session_state.summary = None
            st.session_state.current_session_id = None
            st.session_state.chat_messages = []
            st.session_state.show_chat = False
            st.rerun()
    
    # Main Content Area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📤 Upload Your Content")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a file",
            type=['mp3', 'wav', 'm4a', 'mp4', 'mov', 'avi', 'txt', 'docx'],
            help="Upload audio, video, or transcript file"
        )
        
        # Text input option
        st.markdown("---")
        st.markdown("### ✍️ Or Paste Transcript")
        transcript_text = st.text_area(
            "Enter your meeting transcript here",
            height=200,
            placeholder="Paste your meeting transcript or notes here..."
        )
    
    with col2:
        st.markdown("### 📊 Summary")
        
        # Process button
        process_button = st.button(
            "🚀 Generate Summary",
            type="primary",
            use_container_width=True
        )
        
        if process_button:
            text_to_summarize = None
            
            # Handle file upload
            if uploaded_file is not None:
                try:
                    file_ext = Path(uploaded_file.name).suffix.lower()
                    
                    # Audio/Video files - show message but don't process
                    if file_ext in ['.mp4', '.mov', '.avi', '.mp3', '.wav', '.m4a']:
                        st.info("📝 Please paste your transcript in the text area below. Audio/video processing is not available.")
                        text_to_summarize = None
                    
                    # Text file - process it
                    elif file_ext == '.txt':
                        try:
                            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext, mode='w') as tmp_file:
                                tmp_file.write(uploaded_file.getvalue().decode('utf-8'))
                                tmp_path = tmp_file.name
                            
                            with open(tmp_path, 'r', encoding='utf-8') as f:
                                text_to_summarize = f.read()
                            
                            if os.path.exists(tmp_path):
                                os.unlink(tmp_path)
                        except Exception:
                            try:
                                text_to_summarize = uploaded_file.getvalue().decode('utf-8')
                            except Exception:
                                pass
                    
                    # DOCX file - try to process
                    elif file_ext == '.docx':
                        try:
                            from docx import Document
                            with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp_file:
                                tmp_file.write(uploaded_file.read())
                                tmp_path = tmp_file.name
                            
                            doc = Document(tmp_path)
                            text_to_summarize = '\n'.join([para.text for para in doc.paragraphs])
                            
                            if os.path.exists(tmp_path):
                                os.unlink(tmp_path)
                        except Exception:
                            st.info("📝 Please paste your transcript in the text area below.")
                            text_to_summarize = None
                    
                except Exception:
                    text_to_summarize = None
            
            # Handle text input
            if not text_to_summarize and transcript_text.strip():
                text_to_summarize = transcript_text
            
            if not text_to_summarize:
                st.warning("⚠️ Please paste a transcript in the text area!")
            
            # Generate summary
            if text_to_summarize:
                try:
                    st.session_state.transcript = text_to_summarize
                    
                    with st.spinner("✨ Generating summary with Cohere AI..."):
                        summary = generate_summary(text_to_summarize)
                        st.session_state.summary = summary
                        
                        # Save to history
                        session_id = save_to_history(text_to_summarize, summary)
                        if session_id:
                            st.session_state.current_session_id = session_id
                    
                    st.success("✅ Summary generated successfully!")
                except Exception:
                    pass
        
        # Display summary
        if st.session_state.summary:
            st.markdown("""
                <div class="summary-box">
                    <h3 style="margin-top: 0; color: #FFFFFF;">📋 Summary</h3>
                    <div style="color: #FFFFFF; opacity: 0.9; line-height: 1.6;">
            """ + st.session_state.summary.replace('\n', '<br>') + """
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Action buttons
            col_btn1, col_btn2 = st.columns(2)
            with col_btn1:
                st.download_button(
                    label="📥 Download Summary",
                    data=st.session_state.summary,
                    file_name="summary.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with col_btn2:
                if st.button("💬 Chat with Summary", use_container_width=True):
                    st.session_state.show_chat = not st.session_state.show_chat
                    if st.session_state.show_chat:
                        st.session_state.chat_messages = []
        
        # Display transcript if available
        if st.session_state.transcript:
            with st.expander("📄 View Full Transcript"):
                st.text_area("Transcript", st.session_state.transcript, height=300, disabled=True)
    
    # Chat Interface (full width below the columns)
    if st.session_state.show_chat and st.session_state.summary:
        st.markdown("---")
        st.markdown("### 💬 Chat with Summary")
        st.markdown("""
        <div style="color: #FFFFFF; opacity: 0.7; margin-bottom: 1rem;">
        Ask questions about the summary, like "Who must do what?" or "What are the action items?"
        </div>
        """, unsafe_allow_html=True)
        
        # Chat messages container
        chat_container = st.container()
        
        with chat_container:
            # Display chat history
            for message in st.session_state.chat_messages:
                role = message['role']
                content = message['content']
                
                if role == 'user':
                    st.markdown(f"""
                    <div style="background: linear-gradient(105.13deg, #1C1C1C 41.52%, rgba(63, 63, 63, 0) 100%);
                                border: 1px solid rgba(255, 255, 255, 0.1);
                                border-radius: 12px;
                                padding: 1rem;
                                margin: 0.5rem 0;
                                margin-left: 20%;">
                        <div style="color: #65daff; font-weight: 600; margin-bottom: 0.5rem;">You</div>
                        <div style="color: #FFFFFF;">{content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                    <div style="background: linear-gradient(180deg, rgba(17, 17, 17, 0.02) 0%, rgba(32, 32, 32, 0.02) 100%),
                                linear-gradient(0deg, rgba(82, 82, 82, 0.2), rgba(82, 82, 82, 0.2));
                                border: 1px solid rgba(255, 255, 255, 0.1);
                                border-radius: 12px;
                                padding: 1rem;
                                margin: 0.5rem 0;
                                margin-right: 20%;">
                        <div style="color: #65daff; font-weight: 600; margin-bottom: 0.5rem;">🤖 AI Assistant</div>
                        <div style="color: #FFFFFF; line-height: 1.6;">{content}</div>
                    </div>
                    """, unsafe_allow_html=True)
        
        # Chat input
        with st.form(key="chat_form", clear_on_submit=True):
            user_question = st.text_input(
                "Ask a question",
                placeholder="e.g., Who must do what? What are the action items?",
                label_visibility="collapsed"
            )
            
            col1, col2, col3 = st.columns([1, 1, 4])
            with col1:
                submit_button = st.form_submit_button("Send", use_container_width=True)
            with col2:
                clear_button = st.form_submit_button("Clear Chat", use_container_width=True)
            
            if submit_button and user_question.strip():
                # Add user message
                st.session_state.chat_messages.append({
                    'role': 'user',
                    'content': user_question
                })
                
                # Get AI response with streaming
                try:
                    stream = chat_with_summary_stream(
                        user_question,
                        st.session_state.transcript,
                        st.session_state.summary,
                        st.session_state.chat_messages
                    )
                    
                    if stream:
                        # Create placeholder for streaming response
                        response_placeholder = st.empty()
                        full_response = ""
                        
                        # Stream the response
                        try:
                            for event in stream:
                                if event.event_type == "text-generation":
                                    full_response += event.text
                                    # Update the placeholder with streaming text
                                    response_placeholder.markdown(f"""
                                    <div style="background: linear-gradient(180deg, rgba(17, 17, 17, 0.02) 0%, rgba(32, 32, 32, 0.02) 100%),
                                                linear-gradient(0deg, rgba(82, 82, 82, 0.2), rgba(82, 82, 82, 0.2));
                                                border: 1px solid rgba(255, 255, 255, 0.1);
                                                border-radius: 12px;
                                                padding: 1rem;
                                                margin: 0.5rem 0;
                                                margin-right: 20%;">
                                        <div style="color: #65daff; font-weight: 600; margin-bottom: 0.5rem;">🤖 AI Assistant</div>
                                        <div style="color: #FFFFFF; line-height: 1.6;">{full_response}</div>
                                    </div>
                                    """, unsafe_allow_html=True)
                            
                            # Add final response to chat history
                            if full_response.strip():
                                st.session_state.chat_messages.append({
                                    'role': 'assistant',
                                    'content': full_response.strip()
                                })
                            else:
                                st.session_state.chat_messages.append({
                                    'role': 'assistant',
                                    'content': "I received an empty response. Please try again."
                                })
                        except Exception as e:
                            st.session_state.chat_messages.append({
                                'role': 'assistant',
                                'content': f"Streaming error: {str(e)}"
                            })
                    else:
                        st.session_state.chat_messages.append({
                            'role': 'assistant',
                            'content': "Unable to connect to AI service. Please check your API key in the .env file."
                        })
                        
                except ValueError as e:
                    # API key not found
                    st.error(str(e))
                    st.session_state.chat_messages.append({
                        'role': 'assistant',
                        'content': "⚠️ API key not configured. Please add COHERE_API_KEY to your .env file."
                    })
                except Exception as e:
                    st.session_state.chat_messages.append({
                        'role': 'assistant',
                        'content': f"Error: {str(e)}"
                    })
                
                st.rerun()
            
            if clear_button:
                st.session_state.chat_messages = []
                st.rerun()

if __name__ == "__main__":
    main()

