import streamlit as st
from gmail_service import fetch_emails
from rag_engine import (
    build_vector_db,
    classify_email,
    summarize_thread,
    generate_reply
)

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Email Triage Assistant",
    page_icon="",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("📬 Controls")

fetch_btn = st.sidebar.button("📥 Fetch Latest Email", use_container_width=True)

st.sidebar.divider()
st.sidebar.caption("AI-powered inbox assistant")

# ---------------- Header ----------------
st.title("AI Email Triage Assistant")
st.caption("Smart inbox management using Gmail API, ScaleDown & Gemini")
st.divider()

# ---------------- Fetch Email ----------------
if fetch_btn:
    with st.spinner("Fetching latest email from Gmail..."):
        emails = fetch_emails(1)  # ✅ ONLY ONE EMAIL

    if not emails:
        st.warning("No emails found.")
    else:
        st.session_state["emails"] = emails
        st.session_state["db"] = build_vector_db(emails)

        st.success("Fetched 1 email successfully.")

# ---------------- Display Email ----------------
if "emails" in st.session_state:
    email = st.session_state["emails"][0]
    db = st.session_state["db"]

    st.divider()
    st.markdown("## 📨 Latest Email")

    left, right = st.columns([2, 1])

    # ---------- Email Content ----------
    with left:
        with st.expander("📄 View Email Content", expanded=True):
            st.text(email)

    # ---------- AI Analysis ----------
    with right:
        with st.spinner("Analyzing email with AI..."):
            category = classify_email(email)
            summary = summarize_thread(db)

            if category.lower() == "urgent":
                reply = generate_reply(summary)
            else:
                reply = None

        st.markdown("### 📌 Category")
        if category.lower() == "urgent":
            st.error("🔴 Urgent")
        elif category.lower() == "follow-up":
            st.warning("🟡 Follow-Up")
        else:
            st.info("⚪ Spam / Low Priority")

    # ---------- Summary ----------
    st.markdown("### 📝 Summary")
    st.write(summary)

    # ---------- Auto Reply ----------
    st.markdown("### ✉️ Auto-Draft Reply")
    if reply:
        st.text_area(
            "Generated Reply",
            value=reply,
            height=180
        )
    else:
        st.caption("No reply needed for this email.")
