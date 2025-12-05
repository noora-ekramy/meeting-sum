# 🔒 Security Notes

## API Key Security

### ✅ What We Did

**Removed hardcoded API key** - The Cohere API key is now **only** read from the `.env` file.

### Before (Insecure):
```python
def get_cohere_api_key():
    return os.getenv("COHERE_API_KEY", "7sKG0a1mvd6T3Yy8jRKrWKP8bZ8QnGSL7aChJhzo")
    #                                    ^ Hardcoded fallback key
```

### Now (Secure):
```python
def get_cohere_api_key():
    api_key = os.getenv("COHERE_API_KEY")
    if not api_key:
        raise ValueError("COHERE_API_KEY not found in environment variables.")
    return api_key
```

## Why This Matters

### Security Risks of Hardcoded Keys:

❌ **Version Control Exposure** - Keys visible in git history
❌ **Code Sharing** - Keys exposed when sharing code
❌ **GitHub/Public Repos** - Keys scraped by bots
❌ **Unauthorized Usage** - Anyone with code can use your API
❌ **Cost Risk** - Unexpected charges from key misuse

### Benefits of Environment Variables:

✅ **Gitignored** - `.env` file never committed
✅ **User-specific** - Each user has their own key
✅ **Easily rotated** - Change key without changing code
✅ **Secure storage** - Keys stay local
✅ **Best practice** - Industry standard for secrets

## Setting Up Securely

### 1. Create .env File

```bash
# In the project root
touch .env
```

### 2. Add Your API Key

```bash
echo "COHERE_API_KEY=your_actual_key_here" > .env
```

### 3. Verify .gitignore

The `.gitignore` file already includes:
```
.env
*.env
```

This prevents `.env` from being committed to git.

## Error Handling

### If API Key is Missing:

The app will show a clear error:
```
ValueError: COHERE_API_KEY not found in environment variables. 
Please add it to your .env file.
```

This is **intentional** - better to fail clearly than silently use a hardcoded key.

## Best Practices

### ✅ DO:
- Keep API keys in `.env` file
- Add `.env` to `.gitignore`
- Use different keys for dev/prod
- Rotate keys regularly
- Keep `.env` file local only

### ❌ DON'T:
- Hardcode keys in source code
- Commit `.env` to git
- Share your `.env` file
- Post API keys in screenshots
- Email keys in plain text

## Getting Your API Key

1. Sign up at [cohere.ai](https://cohere.ai)
2. Go to Dashboard → API Keys
3. Create or copy your key
4. Add to `.env` file
5. Never share it!

## Key Rotation

If your key is compromised:

1. **Revoke old key** - In Cohere dashboard
2. **Generate new key** - Create replacement
3. **Update .env** - Replace old with new
4. **Restart app** - Reload environment

No code changes needed!

## Sharing Your Project

When sharing this project:

### Include:
✅ All source code files
✅ `requirements.txt`
✅ `.env.example` with placeholders
✅ Setup instructions

### DON'T Include:
❌ `.env` file
❌ Any files with actual API keys
❌ `history/` folder (contains user data)

### For Recipients:

They need to:
1. Clone/download the project
2. Create their own `.env` file
3. Add their own API key
4. Run the app

## Monitoring Usage

Check your Cohere dashboard regularly for:
- API call counts
- Unexpected usage patterns
- Cost tracking
- Rate limit status

## Environment Variables

Currently used:
- `COHERE_API_KEY` - Required for all API calls

Future additions might include:
- `COHERE_MODEL` - Override default model
- `MAX_TOKENS` - Configure token limits
- `DEBUG_MODE` - Enable debugging

## Summary

✅ **API key removed from code**
✅ **Only reads from .env file**
✅ **Clear error if missing**
✅ **Follows security best practices**
✅ **Safe to share code publicly**

Your API key is now secure! 🔒

