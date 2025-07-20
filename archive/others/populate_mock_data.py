#!/usr/bin/env python3
"""
Mock Data Population Script for SpeakoAI Backend
This script populates the database with realistic mock data for testing and development.
"""

import asyncio
import random
from datetime import datetime, timedelta
from typing import List

# Import backend modules
from backend.models.schemas.schemas import (
    UserCreateSchema,
    QuestionCreateSchema,
    UserResponseCreateSchema,
    FeedbackCreateSchema
)
from backend.services.requests import user as user_service
from backend.services.requests import question as question_service
from backend.services.requests import user_response as response_service
from backend.services.requests import feedback as feedback_service


# Mock data constants
MOCK_USERS = [
    {"tg_id": 1001, "first_name": "Alice Johnson", "username": "alice_j"},
    {"tg_id": 1002, "first_name": "Bob Smith", "username": "bob_smith"},
    {"tg_id": 1003, "first_name": "Carol Davis", "username": "carol_d"},
    {"tg_id": 1004, "first_name": "David Wilson", "username": "david_w"},
    {"tg_id": 1005, "first_name": "Emma Brown", "username": "emma_b"},
]

# IELTS Speaking Part 1 Questions (Personal Information)
PART1_QUESTIONS = [
    {
        "question_text": "Can you tell me about your hometown?",
        "part": 1,
        "category": "Personal Information",
        "sample_answer": "I'm from a small city called Brighton. It's located on the south coast of England and is famous for its beautiful beaches and vibrant cultural scene."
    },
    {
        "question_text": "What do you do for work or study?",
        "part": 1,
        "category": "Work/Study",
        "sample_answer": "I'm currently studying computer science at university. I'm in my final year and really enjoying learning about artificial intelligence and machine learning."
    },
    {
        "question_text": "Do you enjoy reading books?",
        "part": 1,
        "category": "Hobbies",
        "sample_answer": "Yes, I love reading! I particularly enjoy science fiction and fantasy novels. I try to read at least one book a month."
    },
    {
        "question_text": "What's your favorite type of food?",
        "part": 1,
        "category": "Food",
        "sample_answer": "I really enjoy Italian cuisine, especially pasta dishes. I also love trying different types of international food when I can."
    },
    {
        "question_text": "Do you like traveling?",
        "part": 1,
        "category": "Travel",
        "sample_answer": "Absolutely! I love exploring new places and experiencing different cultures. My favorite trip was to Japan last year."
    }
]

# IELTS Speaking Part 2 Questions (Individual Long Turn)
PART2_QUESTIONS = [
    {
        "question_text": "Describe a place you would like to visit. You should say: where it is, why you want to go there, what you would do there, and explain why this place interests you.",
        "part": 2,
        "category": "Places",
        "sample_answer": "I'd love to visit Iceland. It's a Nordic island country known for its dramatic landscapes with volcanoes, geysers, hot springs and lava fields. I want to go there because of its unique natural beauty and the opportunity to see the Northern Lights."
    },
    {
        "question_text": "Describe a person who has influenced you. You should say: who this person is, how you know them, what they have done, and explain why they have influenced you.",
        "part": 2,
        "category": "People",
        "sample_answer": "My grandmother has been a huge influence on me. She taught me the importance of hard work and kindness. She always encouraged me to pursue my dreams and never give up."
    },
    {
        "question_text": "Describe an important event in your life. You should say: when it happened, what happened, how you felt about it, and explain why it was important to you.",
        "part": 2,
        "category": "Events",
        "sample_answer": "Graduating from university was the most important event in my life. It happened last year and marked the end of four years of hard work. I felt incredibly proud and excited about the future."
    },
    {
        "question_text": "Describe a book or film that you enjoyed. You should say: what it was about, when you read or watched it, why you enjoyed it, and explain how it affected you.",
        "part": 2,
        "category": "Entertainment",
        "sample_answer": "I recently read 'The Alchemist' by Paulo Coelho. It's about a young shepherd who goes on a journey to find his personal legend. I enjoyed it because it made me think about my own dreams and goals."
    },
    {
        "question_text": "Describe a skill you would like to learn. You should say: what the skill is, why you want to learn it, how you would learn it, and explain how it would be useful to you.",
        "part": 2,
        "category": "Skills",
        "sample_answer": "I'd love to learn how to play the guitar. I think it would be a great way to express myself creatively and it's something I could enjoy for the rest of my life."
    }
]

# IELTS Speaking Part 3 Questions (Two-Way Discussion)
PART3_QUESTIONS = [
    {
        "question_text": "What are the advantages and disadvantages of living in a big city?",
        "part": 3,
        "category": "Society",
        "sample_answer": "Living in a big city has many advantages like better job opportunities, cultural activities, and public transport. However, it can be expensive, crowded, and stressful."
    },
    {
        "question_text": "How has technology changed the way people work?",
        "part": 3,
        "category": "Technology",
        "sample_answer": "Technology has revolutionized work by enabling remote working, improving communication, and automating many tasks. However, it has also created new challenges like work-life balance issues."
    },
    {
        "question_text": "Do you think education should be free for everyone?",
        "part": 3,
        "category": "Education",
        "sample_answer": "I believe education should be accessible to everyone, but making it completely free might not be sustainable. A balanced approach with affordable options would be ideal."
    },
    {
        "question_text": "What are the environmental challenges facing the world today?",
        "part": 3,
        "category": "Environment",
        "sample_answer": "Climate change, pollution, and loss of biodiversity are major challenges. We need to take immediate action through renewable energy, sustainable practices, and international cooperation."
    },
    {
        "question_text": "How important is it for people to learn a foreign language?",
        "part": 3,
        "category": "Language",
        "sample_answer": "Learning foreign languages is increasingly important in our globalized world. It opens up job opportunities, helps with cultural understanding, and makes travel more enjoyable."
    }
]

# Mock user responses with realistic scores and feedback
MOCK_RESPONSES = [
    {
        "response_text": "I'm from London, which is the capital of England. It's a very diverse and multicultural city with lots of history and culture. I really enjoy living there because there's always something to do.",
        "fluency_score": 7.5,
        "pronunciation_score": 8.0,
        "grammar_score": 7.0,
        "vocabulary_score": 8.5,
        "overall_score": 7.8,
        "ai_feedback": "Excellent response! Your vocabulary is very good and you speak fluently. Try to use more complex sentence structures to improve your grammar score."
    },
    {
        "response_text": "I work as a software engineer at a tech company. I've been there for about three years now and I really enjoy my job. We develop mobile applications and I work with a great team.",
        "fluency_score": 8.0,
        "pronunciation_score": 7.5,
        "grammar_score": 8.0,
        "vocabulary_score": 7.5,
        "overall_score": 7.8,
        "ai_feedback": "Very good answer! Your pronunciation is clear and you use appropriate vocabulary. Consider adding more details about your daily tasks."
    },
    {
        "response_text": "I love reading books, especially science fiction. My favorite author is Isaac Asimov. I usually read before bed and I try to finish at least one book per month.",
        "fluency_score": 6.5,
        "pronunciation_score": 7.0,
        "grammar_score": 7.5,
        "vocabulary_score": 7.0,
        "overall_score": 7.0,
        "ai_feedback": "Good response! Your grammar is solid. Try to speak more fluently and add more descriptive language to improve your overall score."
    },
    {
        "response_text": "My favorite food is Italian cuisine, especially pasta and pizza. I love the rich flavors and fresh ingredients. I also enjoy cooking Italian dishes at home sometimes.",
        "fluency_score": 7.0,
        "pronunciation_score": 6.5,
        "grammar_score": 7.0,
        "vocabulary_score": 7.5,
        "overall_score": 7.0,
        "ai_feedback": "Nice answer! Your vocabulary is good. Work on your pronunciation, especially the word 'cuisine'. Also, try to speak more smoothly."
    },
    {
        "response_text": "Yes, I really enjoy traveling! I've been to several countries in Europe and Asia. My most memorable trip was to Japan last year. The culture and food were amazing.",
        "fluency_score": 8.5,
        "pronunciation_score": 8.0,
        "grammar_score": 8.0,
        "vocabulary_score": 8.0,
        "overall_score": 8.1,
        "ai_feedback": "Excellent response! You speak very fluently and use good vocabulary. Your pronunciation is clear and natural. Keep up the great work!"
    }
]

# Mock feedback comments
MOCK_FEEDBACK_COMMENTS = [
    "Great improvement in your fluency! Keep practicing to maintain this level.",
    "Your pronunciation has improved significantly. Focus on intonation patterns.",
    "Excellent vocabulary usage. Try to incorporate more academic words.",
    "Good grammar overall. Pay attention to article usage and verb tenses.",
    "Your responses are becoming more natural. Continue with regular practice.",
    "Well done on the overall score! Your preparation is showing results.",
    "Consider using more complex sentence structures to improve your band score.",
    "Your speaking confidence has increased. Keep building on this foundation.",
    "Good use of examples and personal experiences in your answers.",
    "Your time management during responses is excellent. Well done!"
]


async def create_mock_users():
    """Create mock users"""
    print("Creating mock users...")
    created_users = []
    
    for user_data in MOCK_USERS:
        try:
            user_schema = UserCreateSchema(**user_data)
            user = await user_service.create_user(user_schema)
            created_users.append(user)
            print(f"Created user: {user.first_name}")
        except Exception as e:
            print(f"Error creating user {user_data['first_name']}: {e}")
    
    return created_users


async def create_mock_questions():
    """Create mock questions for all parts"""
    print("Creating mock questions...")
    created_questions = []
    
    all_questions = PART1_QUESTIONS + PART2_QUESTIONS + PART3_QUESTIONS
    
    for question_data in all_questions:
        try:
            question_schema = QuestionCreateSchema(**question_data)
            question = await question_service.create_question(question_schema)
            created_questions.append(question)
            print(f"Created question: {question.question_text[:50]}...")
        except Exception as e:
            print(f"Error creating question: {e}")
    
    return created_questions


async def create_mock_responses(users, questions):
    """Create mock user responses"""
    print("Creating mock user responses...")
    created_responses = []
    
    # Create responses for each user
    for user in users:
        # Select random questions for this user
        user_questions = random.sample(questions, min(5, len(questions)))
        
        for question in user_questions:
            # Select a random mock response
            mock_response = random.choice(MOCK_RESPONSES)
            
            response_data = {
                "user_id": user.id,
                "question_id": question.id,
                "response_text": mock_response["response_text"],
                "fluency_score": mock_response["fluency_score"],
                "pronunciation_score": mock_response["pronunciation_score"],
                "grammar_score": mock_response["grammar_score"],
                "vocabulary_score": mock_response["vocabulary_score"],
                "overall_score": mock_response["overall_score"],
                "ai_feedback": mock_response["ai_feedback"]
            }
            
            try:
                response_schema = UserResponseCreateSchema(**response_data)
                response = await response_service.create_user_response(response_schema)
                created_responses.append(response)
                print(f"Created response for user {user.first_name} to question {question.id}")
            except Exception as e:
                print(f"Error creating response: {e}")
    
    return created_responses


async def create_mock_feedback(users):
    """Create mock feedback for users"""
    print("Creating mock feedback...")
    created_feedback = []
    
    for user in users:
        # Create 2-3 feedback entries per user
        num_feedback = random.randint(2, 3)
        
        for _ in range(num_feedback):
            feedback_data = {
                "user_id": user.id,
                "ai_comment": random.choice(MOCK_FEEDBACK_COMMENTS)
            }
            
            try:
                feedback_schema = FeedbackCreateSchema(**feedback_data)
                feedback = await feedback_service.create_feedback(feedback_schema)
                created_feedback.append(feedback)
                print(f"Created feedback for user {user.first_name}")
            except Exception as e:
                print(f"Error creating feedback: {e}")
    
    return created_feedback


async def main():
    """Main function to populate all mock data"""
    print("Starting mock data population...")
    
    try:
        # Create users
        users = await create_mock_users()
        print(f"Created {len(users)} users")
        
        # Create questions
        questions = await create_mock_questions()
        print(f"Created {len(questions)} questions")
        
        # Create responses (only if we have both users and questions)
        if users and questions:
            responses = await create_mock_responses(users, questions)
            print(f"Created {len(responses)} responses")
        
        # Create feedback
        if users:
            feedback = await create_mock_feedback(users)
            print(f"Created {len(feedback)} feedback entries")
        
        print("\n✅ Mock data population completed successfully!")
        print(f"Summary:")
        print(f"- Users: {len(users)}")
        print(f"- Questions: {len(questions)}")
        print(f"- Responses: {len(responses) if 'responses' in locals() else 0}")
        print(f"- Feedback: {len(feedback) if 'feedback' in locals() else 0}")
        
    except Exception as e:
        print(f"❌ Error during mock data population: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main()) 