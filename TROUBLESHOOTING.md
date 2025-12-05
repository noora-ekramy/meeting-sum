# 🔧 Troubleshooting Guide

## Common Errors and Solutions

### 1. "COHERE_API_KEY not found in environment variables"

**Error Message:**
```
ValueError: COHERE_API_KEY not found in environment variables. Please add it to your .env file.
```

**Solution:**
1. Create a `.env` file in the project root
2. Add your API key:
   ```
   COHERE_API_KEY=your_actual_api_key_here
   ```
3. Restart the Streamlit app

**How to get an API key:**
- Visit https://cohere.ai
- Sign up or log in
- Go to Dashboard → API Keys
- Copy your key

---

### 2. "Sorry, I encountered an error while streaming the response"

**Possible Causes:**
- Missing or invalid API key
- Network connection issues
- Cohere API is down
- Rate limit exceeded

**Solutions:**

**A. Check API Key**
```bash
# View your .env file
cat .env

# Should show:
COHERE_API_KEY=your_key_here
```

**B. Verify .env file location**
```bash
# Make sure .env is in project root
ls -la /Users/nora/Desktop/sara/.env
```

**C. Restart Streamlit**
```bash
# Stop the app (Ctrl+C) and restart
streamlit run app.py
```

**D. Check Network**
```bash
# Test connection to Cohere
ping api.cohere.ai
```

---

### 3. Empty or Partial Summaries

**Symptoms:**
- Summary only shows first few sentences
- Summary is incomplete

**Solutions:**

**A. Check Token Limits**
The app uses 4000 tokens for summaries. Very long transcripts might be truncated.

**B. Verify API Response**
Check terminal for warnings about API errors.

**C. Try Smaller Input**
Start with a shorter transcript to test.

---

### 4. Chat Not Appearing

**Symptoms:**
- "💬 Chat with Summary" button doesn't show
- Chat section doesn't appear

**Solution:**
1. Make sure summary was generated first
2. Check that `st.session_state.summary` is not None
3. Try clicking "🚀 Generate Summary" again

---

### 5. Module Import Errors

**Error:**
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solution:**
```bash
# Install all requirements
pip install -r requirements.txt

# Or install individually
pip install streamlit cohere python-docx python-dotenv
```

---

### 6. API Rate Limit Errors

**Error:**
```
429 Too Many Requests
```

**Solution:**
- Wait a few minutes before trying again
- Check your Cohere dashboard for usage limits
- Trial accounts have limited calls (20 total, 1000 monthly)

---

### 7. Streaming Stops Mid-Response

**Symptoms:**
- Response starts but doesn't finish
- Partial text appears

**Solutions:**

**A. Network Issue**
- Check internet connection
- Try again

**B. Timeout**
- Streamlit default timeout might be hit
- Restart the app

**C. API Issue**
- Check Cohere status page
- Try again in a few minutes

---

### 8. History Not Saving

**Symptoms:**
- Sessions don't appear in sidebar
- History folder is empty

**Solutions:**

**A. Check Folder Exists**
```bash
ls -la history/
```

**B. Check Permissions**
```bash
# Make sure history folder is writable
chmod 755 history/
```

**C. Generate a Summary**
- History only saves after successful summary generation

---

### 9. File Upload Not Working

**Symptoms:**
- Can upload but nothing happens
- No text extracted

**Solutions:**

**A. For Audio/Video Files**
These are UI-only features. They won't work. Use text files or paste transcript directly.

**B. For Text Files**
- Make sure file is `.txt` format
- Check file encoding (should be UTF-8)
- Try pasting content directly instead

**C. For DOCX Files**
Install python-docx:
```bash
pip install python-docx
```

---

### 10. Dark Theme Not Showing

**Symptoms:**
- App looks plain
- Missing gradients/styling

**Solutions:**

**A. Clear Browser Cache**
- Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)

**B. Check Streamlit Version**
```bash
pip install --upgrade streamlit
```

**C. Try Different Browser**
- Chrome, Firefox, Safari all supported

---

## Debugging Steps

### Enable Debug Mode

**1. Check Environment Variables**
```python
# Add to top of app.py temporarily
import os
print("API Key present:", "COHERE_API_KEY" in os.environ)
print("API Key length:", len(os.getenv("COHERE_API_KEY", "")))
```

**2. Check Streamlit Logs**
Look at terminal output when running the app.

**3. Test API Connection**
```python
# Test file
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("COHERE_API_KEY")
print(f"Key loaded: {bool(api_key)}")

if api_key:
    co = cohere.Client(api_key)
    response = co.chat(
        model='command-r-08-2024',
        message='Hello!'
    )
    print("API works:", response.text)
```

---

## Getting Help

### Before Asking for Help

1. ✅ Check this troubleshooting guide
2. ✅ Verify `.env` file exists with valid key
3. ✅ Check terminal for error messages
4. ✅ Try restarting the app
5. ✅ Check internet connection

### Information to Provide

When asking for help, include:
- Error message (full text)
- Steps to reproduce
- Operating system
- Python version (`python --version`)
- Streamlit version (`streamlit version`)
- Whether API key is set

### Common Quick Fixes

```bash
# Complete reset
rm -rf history/*
rm .env
touch .env
echo "COHERE_API_KEY=your_key" > .env
pip install -r requirements.txt
streamlit run app.py
```

---

## Prevention Tips

### Best Practices

1. ✅ Keep API key in `.env` only
2. ✅ Don't commit `.env` to git
3. ✅ Restart app after changing `.env`
4. ✅ Monitor API usage in Cohere dashboard
5. ✅ Keep dependencies updated

### Regular Maintenance

```bash
# Update packages monthly
pip install --upgrade -r requirements.txt

# Clean old history files
# (keep only recent sessions)
find history -type f -mtime +30 -delete
```

---

## Still Having Issues?

1. Check the README.md for setup instructions
2. Review SETUP_INSTRUCTIONS.md for step-by-step guide
3. Read SECURITY_NOTES.md for API key configuration
4. Try the examples in CHAT_GUIDE.md

The app has been thoroughly tested and should work with proper setup! 🚀

