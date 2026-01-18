"""
EduAssist AI - Rule-Based Backend Module
Deterministic content generation using templates and knowledge base
Aligned with SDG 4 - Quality Education
NO API REQUIRED - Fully offline capable
"""

from typing import Dict, List
import random


# Knowledge Base - Predefined educational content
KNOWLEDGE_BASE = {
    "photosynthesis": {
        "beginner": {
            "definition": "Photosynthesis is the process plants use to make their own food using sunlight.",
            "key_points": [
                "Plants use sunlight, water, and carbon dioxide",
                "They produce glucose (sugar) and oxygen",
                "Chlorophyll makes plants green and captures sunlight",
                "This happens mainly in the leaves"
            ]
        },
        "intermediate": {
            "definition": "Photosynthesis is a biochemical process where plants convert light energy into chemical energy stored in glucose.",
            "key_points": [
                "Occurs in chloroplasts containing chlorophyll",
                "Light-dependent reactions occur in thylakoid membranes",
                "Calvin cycle (light-independent) occurs in stroma",
                "Overall equation: 6CO₂ + 6H₂O + light → C₆H₁₂O₆ + 6O₂"
            ]
        },
        "advanced": {
            "definition": "Photosynthesis is a complex redox process involving electron transport chains, chemiosmosis, and carbon fixation.",
            "key_points": [
                "Photosystem II and I work in tandem (Z-scheme)",
                "ATP synthesis via chemiosmotic gradient across thylakoid membrane",
                "RuBisCO catalyzes carbon fixation in Calvin-Benson cycle",
                "C3, C4, and CAM pathways represent evolutionary adaptations"
            ]
        }
    },
    "default": {
        "beginner": {
            "definition": "This topic involves basic concepts and fundamental principles.",
            "key_points": [
                "Start with the basic definition and purpose",
                "Learn the main components or parts",
                "Understand simple examples from everyday life",
                "Practice with basic exercises"
            ]
        },
        "intermediate": {
            "definition": "This topic requires understanding of underlying mechanisms and relationships.",
            "key_points": [
                "Explore how different components interact",
                "Study the processes and methods involved",
                "Analyze real-world applications",
                "Connect to related concepts in the field"
            ]
        },
        "advanced": {
            "definition": "This topic involves complex theoretical frameworks and advanced analysis.",
            "key_points": [
                "Examine theoretical foundations and principles",
                "Analyze complex interactions and systems",
                "Evaluate research and current developments",
                "Apply critical thinking to solve advanced problems"
            ]
        }
    }
}


def get_topic_data(topic: str, level: str) -> Dict:
    """Retrieve topic data from knowledge base."""
    topic_key = topic.lower().strip()
    level_key = level.lower()
    
    # Check if topic exists in knowledge base
    if topic_key in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[topic_key][level_key]
    else:
        # Use default template
        return KNOWLEDGE_BASE["default"][level_key]


def generate_explanation(topic: str, level: str) -> str:
    """
    Generate a rule-based explanation using templates.
    
    Args:
        topic: The learning topic to explain
        level: Learning level (Beginner, Intermediate, Advanced)
    
    Returns:
        A formatted explanation suitable for the specified level
    """
    data = get_topic_data(topic, level)
    
    # Level-specific introduction templates
    intros = {
        "beginner": f"Let's learn about **{topic}** in a simple way!",
        "intermediate": f"Understanding **{topic}** requires exploring its key mechanisms and applications.",
        "advanced": f"An advanced analysis of **{topic}** involves examining complex theoretical frameworks."
    }
    
    intro = intros.get(level.lower(), intros["beginner"])
    definition = data["definition"]
    key_points = data["key_points"]
    
    # Build explanation
    explanation = f"{intro}\n\n"
    explanation += f"**Definition:** {definition}\n\n"
    explanation += "**Key Concepts:**\n"
    
    for i, point in enumerate(key_points, 1):
        explanation += f"{i}. {point}\n"
    
    # Add level-specific conclusion
    if level.lower() == "beginner":
        explanation += f"\n**Remember:** {topic.capitalize()} is an important concept that you'll use as you continue learning!"
    elif level.lower() == "intermediate":
        explanation += f"\n**Application:** Understanding {topic} helps you connect theory with practical applications in the field."
    else:
        explanation += f"\n**Research Direction:** Advanced study of {topic} opens pathways to cutting-edge research and innovation."
    
    return explanation


def generate_quiz(topic: str, level: str) -> List[Dict[str, any]]:
    """
    Generate rule-based quiz questions using templates.
    
    Args:
        topic: The learning topic for the quiz
        level: Learning level (Beginner, Intermediate, Advanced)
    
    Returns:
        List of dictionaries containing questions, options, and correct answers
    """
    
    # Question templates by level
    templates = {
        "beginner": [
            {
                "question": f"What is {topic}?",
                "options": [
                    "A) A process or concept in the subject area",
                    "B) A type of measurement tool",
                    "C) A mathematical formula",
                    "D) A historical event"
                ],
                "correct_answer": "A"
            },
            {
                "question": f"Why is {topic} important?",
                "options": [
                    "A) It has no practical use",
                    "B) It helps us understand fundamental concepts",
                    "C) It only matters for advanced students",
                    "D) It is outdated knowledge"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"Where do we commonly encounter {topic}?",
                "options": [
                    "A) Only in laboratories",
                    "B) In everyday life and nature",
                    "C) Only in textbooks",
                    "D) Nowhere in the real world"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"What is the first step in learning about {topic}?",
                "options": [
                    "A) Memorizing complex formulas",
                    "B) Understanding the basic definition",
                    "C) Conducting advanced research",
                    "D) Ignoring the fundamentals"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"How can you practice {topic}?",
                "options": [
                    "A) By doing simple exercises and examples",
                    "B) By avoiding all practice",
                    "C) Only through theoretical study",
                    "D) It cannot be practiced"
                ],
                "correct_answer": "A"
            }
        ],
        "intermediate": [
            {
                "question": f"What are the key mechanisms involved in {topic}?",
                "options": [
                    "A) Simple one-step processes",
                    "B) Complex interactions between multiple components",
                    "C) No mechanisms are involved",
                    "D) Only theoretical concepts"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"How does {topic} relate to other concepts in the field?",
                "options": [
                    "A) It exists in complete isolation",
                    "B) It connects to and influences related concepts",
                    "C) It has no relationship to anything else",
                    "D) Only beginners need to know connections"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"What is a practical application of {topic}?",
                "options": [
                    "A) It has no real-world applications",
                    "B) It solves problems and creates solutions in various fields",
                    "C) Only theoretical exercises",
                    "D) Applications are unknown"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"What level of understanding is needed to work with {topic}?",
                "options": [
                    "A) Only memorization is required",
                    "B) Deep conceptual understanding and analytical skills",
                    "C) No understanding is necessary",
                    "D) Basic awareness is sufficient"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"How would you explain {topic} to someone else?",
                "options": [
                    "A) By using technical jargon only",
                    "B) By breaking it down into understandable parts with examples",
                    "C) It cannot be explained",
                    "D) By avoiding all details"
                ],
                "correct_answer": "B"
            }
        ],
        "advanced": [
            {
                "question": f"What are the theoretical foundations of {topic}?",
                "options": [
                    "A) There are no theoretical foundations",
                    "B) Complex principles and established research frameworks",
                    "C) Only practical observations",
                    "D) Simple assumptions"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"How does current research approach {topic}?",
                "options": [
                    "A) Research has concluded on this topic",
                    "B) Through interdisciplinary methods and advanced analysis",
                    "C) Only through basic observation",
                    "D) Research ignores this topic"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"What are the limitations of current understanding of {topic}?",
                "options": [
                    "A) Everything is fully understood",
                    "B) There are ongoing debates and areas requiring further investigation",
                    "C) No limitations exist",
                    "D) The topic is too simple to have limitations"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"How can {topic} be applied to solve complex problems?",
                "options": [
                    "A) It cannot solve complex problems",
                    "B) Through systematic analysis and integration with other advanced concepts",
                    "C) Only through guesswork",
                    "D) Simple application is sufficient"
                ],
                "correct_answer": "B"
            },
            {
                "question": f"What future developments are expected in {topic}?",
                "options": [
                    "A) No future developments are anticipated",
                    "B) Continued research and technological advances will expand understanding",
                    "C) The field is stagnant",
                    "D) Future developments are impossible"
                ],
                "correct_answer": "B"
            }
        ]
    }
    
    level_key = level.lower()
    return templates.get(level_key, templates["beginner"])


def generate_study_plan(topic: str, level: str) -> str:
    """
    Generate a rule-based study plan using templates.
    
    Args:
        topic: The learning topic
        level: Learning level (Beginner, Intermediate, Advanced)
    
    Returns:
        A formatted study plan with timeline and milestones
    """
    
    # Duration and structure by level
    plans = {
        "beginner": {
            "duration": "2 weeks",
            "weeks": [
                {
                    "week": 1,
                    "focus": "Understanding Basics",
                    "activities": [
                        f"Learn the definition and purpose of {topic}",
                        "Watch introductory videos or read beginner-friendly articles",
                        "Create flashcards for key terms",
                        "Complete simple practice exercises"
                    ]
                },
                {
                    "week": 2,
                    "focus": "Practice and Application",
                    "activities": [
                        "Work through example problems",
                        f"Explain {topic} to someone else in your own words",
                        "Take practice quizzes",
                        "Review and summarize what you've learned"
                    ]
                }
            ],
            "resources": [
                "Khan Academy or similar educational platforms",
                "YouTube educational channels",
                "Beginner-level textbooks or online courses",
                "Study groups or online forums"
            ]
        },
        "intermediate": {
            "duration": "3-4 weeks",
            "weeks": [
                {
                    "week": 1,
                    "focus": "Core Concepts Review",
                    "activities": [
                        f"Review fundamental principles of {topic}",
                        "Identify knowledge gaps from beginner level",
                        "Read intermediate-level materials",
                        "Create concept maps showing relationships"
                    ]
                },
                {
                    "week": 2,
                    "focus": "Deep Dive into Mechanisms",
                    "activities": [
                        f"Study how {topic} works in detail",
                        "Analyze case studies and examples",
                        "Practice problem-solving with moderate difficulty",
                        "Connect concepts to real-world applications"
                    ]
                },
                {
                    "week": 3,
                    "focus": "Application and Integration",
                    "activities": [
                        "Work on projects or practical exercises",
                        f"Explore how {topic} relates to other concepts",
                        "Participate in discussions or study groups",
                        "Complete comprehensive practice problems"
                    ]
                },
                {
                    "week": 4,
                    "focus": "Assessment and Mastery",
                    "activities": [
                        "Take practice tests",
                        "Review challenging areas",
                        "Teach the concept to others",
                        "Prepare summary notes for future reference"
                    ]
                }
            ],
            "resources": [
                "University-level textbooks",
                "Academic journals (introductory articles)",
                "Online courses (Coursera, edX)",
                "Professional forums and communities"
            ]
        },
        "advanced": {
            "duration": "4-6 weeks",
            "weeks": [
                {
                    "week": 1,
                    "focus": "Theoretical Foundations",
                    "activities": [
                        f"Study the theoretical framework of {topic}",
                        "Review seminal papers and research",
                        "Analyze mathematical or conceptual models",
                        "Identify current debates in the field"
                    ]
                },
                {
                    "week": 2,
                    "focus": "Advanced Mechanisms",
                    "activities": [
                        "Deep dive into complex processes",
                        "Study advanced methodologies",
                        "Analyze research papers critically",
                        "Explore interdisciplinary connections"
                    ]
                },
                {
                    "week": 3,
                    "focus": "Research and Analysis",
                    "activities": [
                        "Conduct literature review",
                        f"Identify gaps in current understanding of {topic}",
                        "Design hypothetical experiments or studies",
                        "Engage with cutting-edge research"
                    ]
                },
                {
                    "week": 4,
                    "focus": "Synthesis and Application",
                    "activities": [
                        "Work on advanced projects or research",
                        "Apply concepts to novel problems",
                        "Collaborate with peers or mentors",
                        "Present findings or insights"
                    ]
                },
                {
                    "week": 5,
                    "focus": "Critical Evaluation",
                    "activities": [
                        "Critique existing research and theories",
                        "Develop original perspectives",
                        "Write comprehensive analysis papers",
                        "Participate in academic discussions"
                    ]
                },
                {
                    "week": 6,
                    "focus": "Mastery and Future Directions",
                    "activities": [
                        "Complete comprehensive assessment",
                        "Identify areas for continued study",
                        "Explore career or research opportunities",
                        "Contribute to the field (publications, projects)"
                    ]
                }
            ],
            "resources": [
                "Advanced textbooks and monographs",
                "Peer-reviewed academic journals",
                "Research databases (PubMed, IEEE, arXiv)",
                "Academic conferences and seminars",
                "Mentorship from experts in the field"
            ]
        }
    }
    
    level_key = level.lower()
    plan_data = plans.get(level_key, plans["beginner"])
    
    # Build study plan
    study_plan = f"# 📅 {level.capitalize()} Study Plan for {topic}\n\n"
    study_plan += f"**Duration:** {plan_data['duration']}\n\n"
    study_plan += "---\n\n"
    
    # Week-by-week breakdown
    for week_data in plan_data["weeks"]:
        study_plan += f"## Week {week_data['week']}: {week_data['focus']}\n\n"
        for activity in week_data['activities']:
            study_plan += f"- {activity}\n"
        study_plan += "\n"
    
    # Resources
    study_plan += "---\n\n"
    study_plan += "## 📚 Recommended Resources\n\n"
    for resource in plan_data['resources']:
        study_plan += f"- {resource}\n"
    
    # Assessment milestones
    study_plan += "\n---\n\n"
    study_plan += "## ✅ Assessment Milestones\n\n"
    if level_key == "beginner":
        study_plan += "- **Week 1:** Can define key terms and explain basic concepts\n"
        study_plan += "- **Week 2:** Can solve simple problems and explain to others\n"
    elif level_key == "intermediate":
        study_plan += "- **Week 2:** Can explain mechanisms and processes in detail\n"
        study_plan += "- **Week 3:** Can apply concepts to real-world scenarios\n"
        study_plan += "- **Week 4:** Can teach the topic and solve complex problems\n"
    else:
        study_plan += "- **Week 2:** Can analyze and critique research papers\n"
        study_plan += "- **Week 4:** Can design original research or projects\n"
        study_plan += "- **Week 6:** Can contribute original insights to the field\n"
    
    return study_plan


def generate_all_content(topic: str, level: str) -> Dict[str, any]:
    """
    Generate all educational content using rule-based logic.
    
    Args:
        topic: The learning topic
        level: Learning level (Beginner, Intermediate, Advanced)
    
    Returns:
        Dictionary containing explanation, quiz, and study plan
    """
    return {
        'explanation': generate_explanation(topic, level),
        'quiz': generate_quiz(topic, level),
        'study_plan': generate_study_plan(topic, level)
    }
