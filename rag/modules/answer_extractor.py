def extract_answer(query, retrieved_chunks):
    """
    Extract answer using keyword overlap.
    """

    query_words = set(
        query.lower().split()
    )

    best_sentence = ""

    best_score = -1

    for item in retrieved_chunks:

        chunk = item["chunk"]

        sentences = chunk.split(".")

        for sentence in sentences:

            sentence_words = set(
                sentence.lower().split()
            )

            score = len(
                query_words.intersection(
                    sentence_words
                )
            )

            if score > best_score:

                best_score = score

                best_sentence = sentence.strip()

    if best_sentence:
        return best_sentence

    return "No answer found."