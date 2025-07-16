from transformers import pipeline

# Load model once and cache
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text, max_len=130, min_len=30):
    """
    Summarizes the input text using a pre-trained BART model.

    Args:
        text (str): Input long-form text.
        max_len (int): Max summary length.
        min_len (int): Min summary length.

    Returns:
        str: The summarized text.
    """
    result = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
    return result[0]['summary_text']
