import streamlit as st

from modules.parser import read_document
from modules.chunker import chunk_text
from modules.retriever import Retriever
from modules.answer_extractor import extract_answer


st.set_page_config(
    page_title="Simple RAG",
    layout="wide"
)

st.title("📚 Simple RAG System")
st.write(
    "Upload TXT files and ask questions."
)

uploaded_files = st.file_uploader(
    "Upload TXT Files",
    type=["txt"],
    accept_multiple_files=True
)

all_chunks = []
all_sources = []

if uploaded_files:

    for file in uploaded_files:

        text = read_document(file)

        chunks = chunk_text(
            text,
            chunk_size=100
        )

        for chunk in chunks:

            all_chunks.append(chunk)

            all_sources.append(
                file.name
            )

    retriever = Retriever()

    retriever.build_index(
        all_chunks,
        all_sources
    )

    st.success(
        f"{len(uploaded_files)} file(s) indexed successfully."
    )

    st.subheader("Document Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Files",
        len(uploaded_files)
    )

    col2.metric(
        "Chunks",
        len(all_chunks)
    )

    vocab_size = len(
        retriever.vectorizer.vocabulary_
    )

    col3.metric(
        "Vocabulary",
        vocab_size
    )

    st.divider()

    query = st.text_input(
        "Ask a Question"
    )

    if st.button("Ask"):

        if query.strip():

            results = retriever.retrieve(
                query,
                top_k=3
            )

            answer = extract_answer(
                query,
                results
            )

            st.subheader("Answer")

            st.success(answer)

            st.subheader(
                "Retrieved Chunks"
            )

            for i, result in enumerate(
                results,
                start=1
            ):

                st.markdown(
                    f"### Rank {i}"
                )

                st.write(
                    f"Source: {result['source']}"
                )

                st.write(
                    f"Similarity Score: {result['score']:.4f}"
                )

                st.write(
                    result["chunk"]
                )

                st.divider()

else:

    st.info(
        "Upload one or more TXT files to begin."
    )