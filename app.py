"""
EduAssist AI - Streamlit Frontend
AI-Powered Learning Support System
Aligned with SDG 4 - Quality Education
"""

import streamlit as st
from backend import generate_all_content

# Page configuration
st.set_page_config(
    page_title="EduAssist AI - Learning Support",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for color palette and styling
st.markdown("""
<style>
    /* Color Palette */
    :root {
        --primary-blue: #0F62FE;
        --soft-blue: #E8F0FE;
        --white: #FFFFFF;
        --dark-gray: #1F2933;
        --gray: #6B7280;
        --light-gray: #E5E7EB;
    }
    
    /* Main container */
    .main {
        background-color: var(--white);
    }
    
    /* Headers */
    h1 {
        color: var(--primary-blue) !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: var(--dark-gray) !important;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    h3 {
        color: var(--primary-blue) !important;
        font-weight: 600;
    }
    
    /* Text */
    p, li, label {
        color: var(--dark-gray) !important;
        line-height: 1.6;
    }
    
    /* Input fields */
    .stTextInput > div > div > input {
        border: 2px solid var(--light-gray);
        border-radius: 8px;
        padding: 0.75rem;
        color: var(--dark-gray);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: var(--primary-blue);
        box-shadow: 0 0 0 2px rgba(15, 98, 254, 0.1);
    }
    
    /* Radio buttons */
    .stRadio > label {
        color: var(--dark-gray) !important;
        font-weight: 600;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: var(--primary-blue);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #0353E9;
        box-shadow: 0 4px 12px rgba(15, 98, 254, 0.3);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 8px;
        border-left: 4px solid var(--primary-blue);
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: var(--soft-blue);
        border-radius: 8px;
        color: var(--dark-gray) !important;
        font-weight: 600;
    }
    
    /* Dividers */
    hr {
        border-color: var(--light-gray);
        margin: 2rem 0;
    }
    
    /* Card-like sections */
    .output-section {
        background-color: var(--soft-blue);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid var(--light-gray);
    }
    
    /* Quiz styling */
    .quiz-question {
        background-color: white;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid var(--primary-blue);
    }
    
    /* Disclaimer box */
    .disclaimer {
        background-color: #FFF4E6;
        border-left: 4px solid #F59E0B;
        padding: 1rem;
        border-radius: 8px;
        margin: 1.5rem 0;
    }
    
    .disclaimer p {
        color: #92400E !important;
        margin: 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("📚 EduAssist AI")
st.markdown("### AI-Powered Learning Support System")
st.markdown("*Aligned with SDG 4 – Quality Education*")

# Ethical Disclaimer
st.markdown("""
<div class="disclaimer">
    <p><strong>⚠️ Ethical Disclaimer:</strong> EduAssist AI is a learning support tool designed to enhance your educational journey. 
    It does not replace teachers, formal education systems, or professional educational guidance. 
    Use this tool as a supplement to your studies, and always verify information with authoritative sources.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Input Section
st.markdown("## 🎯 Start Your Learning Journey")

col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input(
        "What would you like to learn about?",
        placeholder="e.g., Photosynthesis, Python Programming, World War II...",
        help="Enter any topic you want to explore"
    )

with col2:
    level = st.radio(
        "Select your learning level:",
        ["Beginner", "Intermediate", "Advanced"],
        help="Choose the level that matches your current knowledge"
    )

# Generate button
generate_clicked = st.button("🚀 Generate Learning Support", use_container_width=True)

# Output Section
if generate_clicked:
    if not topic or topic.strip() == "":
        st.error("⚠️ Please enter a learning topic to continue.")
    else:
        with st.spinner(f"🤖 Generating personalized learning content for '{topic}' at {level} level..."):
            try:
                # Generate all content
                content = generate_all_content(topic, level)
                
                st.success("✅ Learning content generated successfully!")
                st.markdown("---")
                
                # 1. Personalized Explanation
                st.markdown("## 📖 Personalized Explanation")
                with st.expander("Click to view explanation", expanded=True):
                    st.markdown(content['explanation'])
                
                st.markdown("---")
                
                # 2. Self-Assessment Quiz
                st.markdown("## 📝 Self-Assessment Quiz")
                st.markdown("*Test your understanding with these questions:*")
                
                quiz_questions = content['quiz']
                
                for idx, q in enumerate(quiz_questions, 1):
                    st.markdown(f"""
                    <div class="quiz-question">
                        <strong>Question {idx}:</strong> {q.get('question', 'N/A')}
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Display options
                    for option in q.get('options', []):
                        st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{option}")
                    
                    # Show answer in expander
                    with st.expander(f"Show Answer for Question {idx}"):
                        st.markdown(f"**Correct Answer:** {q.get('correct_answer', 'N/A')}")
                
                st.markdown("---")
                
                # 3. Recommended Study Plan
                st.markdown("## 📅 Recommended Study Plan")
                with st.expander("Click to view your personalized study plan", expanded=True):
                    st.markdown(content['study_plan'])
                
                # Encouragement message
                st.markdown("---")
                st.info("💡 **Keep Learning!** Remember to practice regularly and don't hesitate to explore additional resources.")
                
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}")
                st.info("💡 **Troubleshooting Tips:**\n- Check if your `.env` file contains a valid Gemini API key\n- Ensure you have internet connectivity\n- Verify that all dependencies are installed")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6B7280; padding: 2rem 0;'>
    <p>Built with ❤️ for inclusive and quality education | Powered by Google Gemini AI</p>
    <p style='font-size: 0.9rem;'>Contributing to <strong>UN Sustainable Development Goal 4: Quality Education</strong></p>
</div>
""", unsafe_allow_html=True)
