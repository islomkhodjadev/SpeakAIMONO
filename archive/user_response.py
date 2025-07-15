#
#
#
# from aiogram import types, Router
# from aiogram.filters import Command
# from backend.services.requests.user import create_user
# from backend.models.schemas.schemas import UserCreateSchema
# from backend.bot.keyboards import start  # assuming `start` is a list of buttons
# import logging
#
# router = Router()
# logger = logging.getLogger(__name__)
#
# @router.message(Command(""))
# async def handle_user_response(
#         update: Update, context: ContextTypes.DEFAULT_TYPE
# ):
#     """Handle user's text response to a question"""
#     user = update.effective_user
#     response_text = update.message.text
#
#     if "waiting_for_response" not in context.user_data:
#         await update.message.reply_text(
#             "Please use /practice to start a practice session first."
#         )
#         return
#
#     question_id = context.user_data["waiting_for_response"]
#
#     try:
#         # Get user from database
#         user_data = await rq_user.get_user(tg_id=user.id)
#         if not user_data:
#             await update.message.reply_text("Please use /start to register first.")
#             return
#
#         # Create user response (with mock scores for now)
#         # In a real implementation, you'd integrate with an AI service for scoring
#         import random
#
#         mock_scores = {
#             "fluency_score": round(random.uniform(6.0, 8.5), 1),
#             "pronunciation_score": round(random.uniform(6.0, 8.5), 1),
#             "grammar_score": round(random.uniform(6.0, 8.5), 1),
#             "vocabulary_score": round(random.uniform(6.0, 8.5), 1),
#             "overall_score": round(random.uniform(6.0, 8.5), 1),
#             "ai_feedback": "Good effort! Try to expand your vocabulary and work on pronunciation. Consider using more complex sentence structures.",
#         }
#
#         response_data = {
#             "user_id": user_data["id"],
#             "question_id": question_id,
#             "response_text": response_text,
#             **mock_scores,
#         }
#
#         # Save response to database
#         saved_response = await rq_response.create_user_response(response_data)
#
#         # Generate feedback message
#         feedback_message = f"""
# 🎯 Your Response Analysis
#
# **Your Answer:**
# {response_text[:200]}{"..." if len(response_text) > 200 else ""}
#
# **Scores (IELTS Band Scale):**
# • Fluency & Coherence: {mock_scores['fluency_score']}/9.0
# • Pronunciation: {mock_scores['pronunciation_score']}/9.0
# • Grammar: {mock_scores['grammar_score']}/9.0
# • Vocabulary: {mock_scores['vocabulary_score']}/9.0
# • **Overall Band Score: {mock_scores['overall_score']}/9.0**
#
# **AI Feedback:**
# {mock_scores['ai_feedback']}
#
# **Tips for Improvement:**
# • Practice speaking for 2-3 minutes on each topic
# • Record your and listen for pronunciation
# • Expand your vocabulary with synonyms
# • Use a variety of sentence structures
#
# Ready for another question? Use /practice to continue!
#             """
#
#         await update.message.reply_text(feedback_message)
#
#         # Clear the waiting state
#         del context.user_data["waiting_for_response"]
#
#     except Exception as e:
#         logger.error(f"Error processing response: {e}")
#         await update.message.reply_text(
#             "Sorry, there was an error processing your response."
#         )
