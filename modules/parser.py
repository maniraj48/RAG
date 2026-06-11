def read_document(uploaded_file):
    """
    Reads uploaded txt file and returns text.
    """

    try:
        text = uploaded_file.read().decode("utf-8")
        return text

    except Exception:
        return ""