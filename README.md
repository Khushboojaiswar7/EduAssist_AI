# EduAssist AI - Hybrid AI + Rule-Based Learning Support System

![SDG 4 - Quality Education](https://img.shields.io/badge/SDG%204-Quality%20Education-C5192D?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

## 📚 Overview

**EduAssist AI** is a full-stack **rule-based** learning support system designed to provide personalized educational content aligned with **UN Sustainable Development Goal 4: Quality Education**. 

Unlike AI-powered systems, this uses **deterministic templates and knowledge bases** - meaning:
- ✅ **No API keys required** - Works completely offline
- ✅ **Instant responses** - No waiting for API calls
- ✅ **Predictable content** - Consistent, reliable educational material
- ✅ **Privacy-first** - No data sent to external servers

The system adapts to different learning levels (Beginner, Intermediate, Advanced) and generates:

- 📖 **Personalized Explanations** - Level-appropriate content from knowledge base
- 📝 **Self-Assessment Quizzes** - 5 template-based questions per level
- 📅 **Study Plans** - Structured learning roadmaps (2-6 weeks)

## 🎯 Features

- **Rule-Based Content Generation**: Deterministic templates ensure consistent, reliable content
- **No API Required**: Works completely offline - no internet needed after installation
- **Instant Responses**: No waiting for external API calls
- **Adaptive Learning Levels**: Content complexity adjusts for Beginner/Intermediate/Advanced
- **Interactive Quizzes**: 5 multiple-choice questions tailored to each level
- **Personalized Study Plans**: Week-by-week learning roadmaps (2-6 weeks based on level)
- **Accessible Design**: Clean, minimal UI with education-friendly color palette
- **Ethical AI**: Transparent disclaimers and responsible usage
- **Privacy-First**: No data sent to external servers, no personal data stored
- **Expandable Knowledge Base**: Easy to add new topics to the system

## 🏗️ System Architecture

```
Frontend (Streamlit) ←→ Backend (Rule-Based Python) ←→ Knowledge Base (Templates)
```

- **Frontend**: Streamlit-based UI with custom CSS styling
- **Backend**: Pure Python with template-based content generation
- **Knowledge Base**: Predefined educational templates and topic data
- **No External Dependencies**: Completely self-contained system

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- **No API keys needed!** ✅

### Installation

1. **Clone or navigate to the project directory**
```bash
cd d:\EduAssist_AI
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser** to `http://localhost:8501`

That's it! No API configuration needed.

## 🎨 Design Specifications

### Color Palette

- **Primary (Buttons, Headings)**: IBM Blue `#0F62FE`
- **Secondary Background**: Soft Blue `#E8F0FE`
- **Main Background**: White `#FFFFFF`
- **Primary Text**: Dark Gray `#1F2933`
- **Secondary Text**: Gray `#6B7280`
- **Borders & Dividers**: Light Gray `#E5E7EB`

### Design Principles

- Clean and minimal interface
- High readability and accessibility
- Professional education-friendly aesthetics
- Responsive layout for all screen sizes

## 📖 Usage Guide

1. **Enter a Learning Topic**: Type any subject you want to learn about
2. **Select Your Level**: Choose Beginner, Intermediate, or Advanced
3. **Generate Content**: Click the "Generate Learning Support" button
4. **Explore Results**:
   - Read the personalized explanation
   - Take the self-assessment quiz
   - Follow the recommended study plan

### Example Topics

- Science: "Photosynthesis", "Quantum Mechanics", "DNA Replication"
- Technology: "Python Programming", "Machine Learning", "Web Development"
- History: "World War II", "Ancient Egypt", "Industrial Revolution"
- Mathematics: "Calculus", "Linear Algebra", "Statistics"

## 🔒 Ethical Considerations

EduAssist AI is designed with responsible AI principles:

- **Transparency**: Clear disclaimers about system capabilities
- **Educational Support**: Complements, not replaces, formal education
- **Privacy**: No personal data collection or storage
- **Inclusivity**: Accessible design for diverse learners
- **Quality**: Aligned with SDG 4 for quality education

## 📁 Project Structure

```
EduAssist_AI/
├── app.py                 # Streamlit frontend application
├── backend.py             # AI logic and content generation
├── requirements.txt       # Python dependencies
├── .env.example          # Environment configuration template
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## 🛠️ Technical Details

### Backend Functions

- `generate_explanation(topic, level)`: Creates level-appropriate explanations using templates
- `generate_quiz(topic, level)`: Generates 5 MCQ questions from predefined templates
- `generate_study_plan(topic, level)`: Creates structured learning timeline (2-6 weeks)
- `generate_all_content(topic, level)`: Generates all content at once

### Knowledge Base

The system includes a built-in knowledge base with:
- **Predefined Topics**: Photosynthesis (more can be added)
- **Default Templates**: Generic templates for any topic
- **Level-Specific Content**: Beginner, Intermediate, Advanced variations

### Adding New Topics

To add a new topic to the knowledge base, edit `backend.py`:

```python
KNOWLEDGE_BASE = {
    "your_topic": {
        "beginner": {
            "definition": "Simple definition...",
            "key_points": ["Point 1", "Point 2", ...]
        },
        "intermediate": { ... },
        "advanced": { ... }
    }
}
```

## 🔧 Troubleshooting

**Error: Module Not Found**
- Run `pip install -r requirements.txt`
- Ensure virtual environment is activated

**Content Seems Generic**
- The system uses templates for unknown topics
- Add specific topics to the knowledge base in `backend.py`
- See "Adding New Topics" section above

**Streamlit Won't Start**
- Check if port 8501 is already in use
- Try: `streamlit run app.py --server.port 8502`

## 🌟 Future Enhancements

- [ ] Multi-language support
- [ ] Progress tracking and analytics
- [ ] Collaborative learning features
- [ ] Mobile app version
- [ ] Offline mode with cached content
- [ ] Integration with learning management systems

## 🤝 Contributing to SDG 4

This project contributes to **UN Sustainable Development Goal 4: Quality Education** by:

- Providing free, accessible learning support
- Adapting to different learning levels
- Promoting inclusive education
- Leveraging AI for educational equity
- Supporting self-directed learning

## 📄 License

This project is created for educational purposes and aligned with global sustainability goals.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Inspired by UN SDG 4: Quality Education

---

<div align="center">

**Built with ❤️ for inclusive and quality education**

*Making AI-powered learning accessible to everyone*

</div>
