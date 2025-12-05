# API Update Notes

## Cohere API Migration

**Date:** December 5, 2025

### What Changed

Cohere deprecated their `Generate API` and `command` model on September 15, 2025. The app has been updated to use:
- New `Chat API` (instead of Generate API)
- New `command-r-08-2024` model (verified and secured)

### Updates Made

1. **Summary Generation**
   - Changed from `co.generate()` to `co.chat()`
   - Updated model from `command` to `command-r-08-2024`
   - Increased max_tokens from 500 to 4000 for comprehensive summaries
   - Now provides more detailed summaries with action items and responsibilities
   - Supports up to 128K input tokens (very long transcripts)

2. **Chat Feature**
   - Migrated from `co.generate()` to `co.chat()`
   - Updated model from `command` to `command-r-08-2024`
   - Increased max_tokens to 1000 for detailed responses
   - Better conversation context handling
   - Maintains up to 6 messages (3 conversation pairs)
   - Uses preamble for better context awareness

3. **Error Handling**
   - Improved fallback summaries (first 5 + last 5 sentences)
   - Better error messages
   - More robust exception handling

### Benefits

✅ **Better Summaries** - Up to 4000 tokens (was 500)
✅ **Improved Chat** - Up to 1000 tokens (was 300)
✅ **Larger Context** - 128K input tokens supported
✅ **Modern API** - Using latest Cohere API standards
✅ **Cost Effective** - $0.15/$0.6 per 1M tokens
✅ **Production Ready** - Verified and secured model

### Testing

Please test the following:
1. Generate a summary from a transcript
2. Verify the summary contains action items and responsibilities
3. Use the chat feature to ask "Who must do what?"
4. Check that chat maintains conversation context

All features should work correctly with the new API.

