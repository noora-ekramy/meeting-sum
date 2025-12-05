# Cohere Model Information

## Current Model: `command-r-08-2024`

### About Command-R-08-2024

**Command-R-08-2024** is Cohere's verified production model optimized for general purpose tasks including summarization and chat.

### Features

✅ **Large Context** - 128K input tokens, 128K output tokens
✅ **Cost Effective** - $0.15 per 1M input / $0.6 per 1M output
✅ **Coding Support** - Yes
✅ **Verified Status** - Production ready
✅ **Secured Availability** - Reliable uptime

### Model Comparison

| Model | Input Price | Output Price | Max Output | Status |
|-------|-------------|--------------|------------|--------|
| `command-r-08-2024` | $0.15 | $0.6 | 128K | ✅ **Current** |
| `command-r7b-12-2024` | $0.0375 | $0.15 | 128K | ✅ Cheaper |
| `command-a-03-2025` | $2.5 | $10 | 8K | ✅ Most powerful |
| `c4ai-aya-expanse-32b` | $0.5 | $1.5 | 128K | ✅ Multilingual |
| `c4ai-aya-expanse-8b` | $0.5 | $1.5 | 128K | ✅ Smaller |

### Why Command-R-08-2024?

We use `command-r-08-2024` because:
1. **Best balance** - Great performance at reasonable cost
2. **Large context** - 128K tokens for both input and output
3. **Production ready** - Verified and secured
4. **Good for summaries** - Excellent at extracting key info
5. **Chat capable** - Works well with conversations

### Alternative Models

**For Lower Cost:** `command-r7b-12-2024`
- 4x cheaper ($0.0375/$0.15 vs $0.15/$0.6)
- Same context size (128K)
- Good for simple summaries

**For Higher Quality:** `command-a-03-2025`
- Most powerful model
- 256K input tokens
- Best for complex analysis
- 16x more expensive

**Change model in app.py:**
```python
# Find these lines and change the model:
model='command-r-08-2024'

# Change to:
model='command-r7b-12-2024'  # For cheaper
# OR
model='command-a-03-2025'    # For better quality
```

### API Limits

With your trial API key:
- Monthly call limit: 1000 calls
- Trial endpoint calls: 20 total
- Remaining: Check response headers

### Migration Notes

The app was updated from:
- API: `co.generate()` → `co.chat()`
- Model: `command` → `command-r-08-2024`
- Max tokens: Increased to 4000 for summaries, 1000 for chat

Both changes ensure compatibility with Cohere's current API (Dec 2025).

### Token Limits

**Summary Generation:**
- Max output: 4000 tokens (~3000 words)
- Max input: 128,000 tokens (very long transcripts supported)

**Chat Responses:**
- Max output: 1000 tokens (~750 words)
- Max input: 128,000 tokens

### Documentation

For more info: https://docs.cohere.com/docs/models

