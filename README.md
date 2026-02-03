# 📧 AI Email Triage Assistant

**An AI-powered email management agent for efficient inbox triage**

![GitHub](https://img.shields.io/github/license/your-username/ai-email-triage-assistant?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/ai-email-triage-assistant?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/your-username/ai-email-triage-assistant?style=for-the-badge)
![GitHub stars](https://img.shields.io/github/stars/your-username/ai-email-triage-assistant?style=for-the-badge)

[![Python](https://img.shields.io/badge/python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=flat-square&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Gemini](https://img.shields.io/badge/Gemini-8E7CC3?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)

---

## 🚀 Quick Demo

<div align="center">
  
https://github.com/your-username/ai-email-triage-assistant/assets/12345678/demo-video.mp4

*Auto-classification and intelligent email processing in action*

</div>

---

## 🔍 Overview

The **AI Email Triage Assistant** is an intelligent email management agent that automatically:

* 📥 **Fetches** emails securely via Gmail API
* 🧠 **Classifies** emails by priority (Urgent / Follow-Up / Spam)
* 🗜️ **Compresses** long email threads using ScaleDown technology
* 📝 **Summarizes** content and extracts key action items
* ✉️ **Generates** professional draft replies for urgent emails
* 📊 **Analyzes** email context with Google's Gemini LLM

The system leverages **ScaleDown** for prompt compression and **Gemini LLM** for reasoning and generation, ensuring **high efficiency, low token usage, and fast response times**.

This project demonstrates practical **agentic AI design**, combining decision-making, context optimization, and user-facing workflows.

---

## 🎯 Key Features

* **📧 Email Processing**: Secure Gmail API integration with OAuth 2.0 authentication
* **🧠 Smart Classification**: AI-powered email categorization (Urgent/Follow-up/Spam)
* **🗜️ Context Compression**: ScaleDown technology reduces token usage by 70%+
* **📝 Intelligent Summarization**: Extracts key points and action items from email threads
* **✉️ Auto Reply Generation**: Creates professional draft responses for urgent emails
* **🖥️ Interactive UI**: Clean Streamlit interface with real-time feedback
* **🔒 Privacy Focused**: Read-only Gmail access with secure token management

---

## 🏗️ System Architecture

```
┌─────────────┐
│   Gmail API │
│ (Read-only) │
└──────┬──────┘
       ↓
┌──────────────────┐
│ Email Ingestion  │
│ (gmail_service) │
└──────┬──────────┘
       ↓
┌────────────────────────────┐
│ RAG + Agent Logic          │
│ - Classification           │
│ - Summarization            │
│ - Reply Generation         │
│ (rag_engine)               │
└──────┬────────────────────┘
       ↓
┌────────────────────────────┐
│ ScaleDown API              │
│ (Prompt Compression Layer) │
└──────┬────────────────────┘
       ↓
┌────────────────────────────┐
│ Gemini LLM                 │
│ (Reasoning & Generation)   │
└──────┬────────────────────┘
       ↓
┌────────────────────────────┐
│ Streamlit UI               │
│ (User Interaction Layer)   │
└────────────────────────────┘
```

---

## 🧰 Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | Streamlit | Interactive web interface |
| **Email API** | Gmail API | Secure email access |
| **AI Engine** | Google Gemini | Natural language processing |
| **Compression** | ScaleDown API | Prompt optimization |
| **Vector Store** | FAISS | Efficient similarity search |
| **Language** | Python 3.10+ | Core application logic |

---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.10+
- Google Cloud account
- Gmail account
- API keys for Gemini and ScaleDown

### Quick Setup
```bash
# 1. Clone repository
git clone https://github.com/your-username/ai-email-triage-assistant.git
cd ai-email-triage-assistant

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Add your API keys to .env file

# 4. Set up Gmail API
# Download credentials.json from Google Cloud Console
# Place in project root directory

# 5. Run application
streamlit run app.py
```

---

## 🎮 Usage

1. **Start the app**: Open your browser to `http://localhost:8501`
2. **Authenticate**: Click "Fetch Latest Email" and complete Gmail OAuth (first run only)
3. **Process emails**: The system will automatically classify and summarize your latest email
4. **Review results**: Check classification, summary, and auto-generated reply
5. **Iterate**: Fetch more emails as needed

---

## 📊 Example Output

**Email Classification**: 🔴 Urgent
**Summary**: "Client needs immediate response regarding project timeline changes. Key action items: Confirm new deadlines, update team schedule, and communicate changes to stakeholders."
**Auto-Reply Draft**: "Thank you for your email. I understand the urgency of these timeline changes and will confirm the new deadlines within 2 hours..."

---

## 🧠 Resume-Worthy Skills Demonstrated

* **AI/ML Integration**: Real-world implementation of LLMs and RAG systems
* **API Development**: Multiple API integrations (Gmail, Gemini, ScaleDown)
* **System Design**: Layered architecture with clear separation of concerns
* **Security**: OAuth 2.0 implementation and secure credential management
* **Performance Optimization**: Context compression for cost reduction
* **User Experience**: Interactive web interface design

---

## 🚀 Future Enhancements

* **📧 Send Replies**: Direct email sending via Gmail API
* **🏷️ Auto-Labeling**: Automatic email categorization and archiving
* **📊 Analytics Dashboard**: Email processing statistics and insights
* **📱 Mobile Support**: Responsive design for mobile devices
* **🔄 Batch Processing**: Handle multiple emails simultaneously
* **🧠 Learning System**: Improve classification based on user feedback

---

## 📚 Documentation

* **Technical Documentation**: [AI_Email_Triage_Assistant_Documentation.docx](AI_Email_Triage_Assistant_Documentation.docx)
* **API References**: See individual component documentation
* **Troubleshooting Guide**: Included in technical documentation

---

## 📊 Project Stats

![Alt](https://repobeats.axiom.co/api/embed/abcdef1234567890.svg "Repobeats analytics image")

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Good First Issues
- [ ] Add support for Outlook/other email providers
- [ ] Implement email scheduling features
- [ ] Add multi-language support
- [ ] Create mobile-responsive UI

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

* [Google AI](https://ai.google.dev/) for Gemini LLM
* [ScaleDown](https://scaledown.ai/) for prompt compression
* [Streamlit](https://streamlit.io/) for the web framework
* [Google Cloud](https://cloud.google.com/) for Gmail API
* [FAISS](https://github.com/facebookresearch/faiss) for vector search

---



## Documenation 
https://docs.google.com/document/d/1CvLaKB3tZ5lJeNs1PABSAvAviK_PAI0m/edit?usp=drive_link&ouid=113157617250399139462&rtpof=true&sd=true


## Sample images
![alt text](images/I1.png) ![alt text](images/image-1.png) ![alt text](images/image-2.png) ![alt text](images/image-3.png) ![alt text](images/image.png)