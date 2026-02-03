from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
from scaledown import compress_with_scaledown
from gemini_llm import call_llm
import numpy as np


class SimpleEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [np.random.rand(384).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(384).tolist()


def build_vector_db(emails):
    embeddings = SimpleEmbeddings()
    return FAISS.from_texts(emails, embeddings)


def safe_llm_call(prompt: str) -> str:
    """
    Prevents Gemini crashes when prompt is empty
    """
    if not prompt or not prompt.strip():
        return "Unable to generate response due to empty input."
    return call_llm(prompt)


def classify_email(email_text):
    base_prompt = """
Classify the email into ONE category:
Urgent  requires immediate action or has a strict deadline
Follow-Up  informational, newsletters, announcements, or non-urgent updates
Spam  promotions, ads, or irrelevant content
Return only the category name.
"""


    compressed_prompt = compress_with_scaledown(
        context=email_text,
        prompt=base_prompt
    )

    if not compressed_prompt or not compressed_prompt.strip():
        compressed_prompt = f"{base_prompt}\n\nEmail:\n{email_text}"

    return safe_llm_call(compressed_prompt)


def summarize_thread(db):
    docs = db.similarity_search("email discussion", k=3)
    context = "\n".join([doc.page_content for doc in docs])

    base_prompt = """
Summarize the email thread.
Provide:
- Short summary
- Action items
"""

    compressed_prompt = compress_with_scaledown(
        context=context,
        prompt=base_prompt
    )

    if not compressed_prompt or not compressed_prompt.strip():
        compressed_prompt = f"{base_prompt}\n\nThread:\n{context}"

    return safe_llm_call(compressed_prompt)


def generate_reply(summary):
    base_prompt = "Write a professional and polite email reply."

    compressed_prompt = compress_with_scaledown(
        context=summary,
        prompt=base_prompt
    )

    if not compressed_prompt or not compressed_prompt.strip():
        compressed_prompt = f"{base_prompt}\n\nSummary:\n{summary}"

    return safe_llm_call(compressed_prompt)
