-- SpeakoAI Mock Data Population Script
-- Run this script in psql to populate the database with mock data

-- Clear existing data (optional - uncomment if you want to start fresh)
-- DELETE FROM feedbacks;
-- DELETE FROM user_responses;
-- DELETE FROM questions;
-- DELETE FROM users;

-- Insert mock users
INSERT INTO users (tg_id, first_name, username, created_at) VALUES
(1001, 'Alice Johnson', 'alice_j', NOW()),
(1002, 'Bob Smith', 'bob_smith', NOW()),
(1003, 'Carol Davis', 'carol_d', NOW()),
(1004, 'David Wilson', 'david_w', NOW()),
(1005, 'Emma Brown', 'emma_b', NOW())
ON CONFLICT (tg_id) DO NOTHING;

-- Insert Part 1 Questions (Personal Information)
INSERT INTO questions (part, question_text, sample_answer, category, created_at) VALUES
(1, 'Can you tell me about your hometown?', 'I''m from a small city called Brighton. It''s located on the south coast of England and is famous for its beautiful beaches and vibrant cultural scene.', 'Personal Information', NOW()),
(1, 'What do you do for work or study?', 'I''m currently studying computer science at university. I''m in my final year and really enjoying learning about artificial intelligence and machine learning.', 'Work/Study', NOW()),
(1, 'Do you enjoy reading books?', 'Yes, I love reading! I particularly enjoy science fiction and fantasy novels. I try to read at least one book a month.', 'Hobbies', NOW()),
(1, 'What''s your favorite type of food?', 'I really enjoy Italian cuisine, especially pasta dishes. I also love trying different types of international food when I can.', 'Food', NOW()),
(1, 'Do you like traveling?', 'Absolutely! I love exploring new places and experiencing different cultures. My favorite trip was to Japan last year.', 'Travel', NOW());

-- Insert Part 2 Questions (Individual Long Turn)
INSERT INTO questions (part, question_text, sample_answer, category, created_at) VALUES
(2, 'Describe a place you would like to visit. You should say: where it is, why you want to go there, what you would do there, and explain why this place interests you.', 'I''d love to visit Iceland. It''s a Nordic island country known for its dramatic landscapes with volcanoes, geysers, hot springs and lava fields. I want to go there because of its unique natural beauty and the opportunity to see the Northern Lights.', 'Places', NOW()),
(2, 'Describe a person who has influenced you. You should say: who this person is, how you know them, what they have done, and explain why they have influenced you.', 'My grandmother has been a huge influence on me. She taught me the importance of hard work and kindness. She always encouraged me to pursue my dreams and never give up.', 'People', NOW()),
(2, 'Describe an important event in your life. You should say: when it happened, what happened, how you felt about it, and explain why it was important to you.', 'Graduating from university was the most important event in my life. It happened last year and marked the end of four years of hard work. I felt incredibly proud and excited about the future.', 'Events', NOW()),
(2, 'Describe a book or film that you enjoyed. You should say: what it was about, when you read or watched it, why you enjoyed it, and explain how it affected you.', 'I recently read ''The Alchemist'' by Paulo Coelho. It''s about a young shepherd who goes on a journey to find his personal legend. I enjoyed it because it made me think about my own dreams and goals.', 'Entertainment', NOW()),
(2, 'Describe a skill you would like to learn. You should say: what the skill is, why you want to learn it, how you would learn it, and explain how it would be useful to you.', 'I''d love to learn how to play the guitar. I think it would be a great way to express myself creatively and it''s something I could enjoy for the rest of my life.', 'Skills', NOW());

-- Insert Part 3 Questions (Two-Way Discussion)
INSERT INTO questions (part, question_text, sample_answer, category, created_at) VALUES
(3, 'What are the advantages and disadvantages of living in a big city?', 'Living in a big city has many advantages like better job opportunities, cultural activities, and public transport. However, it can be expensive, crowded, and stressful.', 'Society', NOW()),
(3, 'How has technology changed the way people work?', 'Technology has revolutionized work by enabling remote working, improving communication, and automating many tasks. However, it has also created new challenges like work-life balance issues.', 'Technology', NOW()),
(3, 'Do you think education should be free for everyone?', 'I believe education should be accessible to everyone, but making it completely free might not be sustainable. A balanced approach with affordable options would be ideal.', 'Education', NOW()),
(3, 'What are the environmental challenges facing the world today?', 'Climate change, pollution, and loss of biodiversity are major challenges. We need to take immediate action through renewable energy, sustainable practices, and international cooperation.', 'Environment', NOW()),
(3, 'How important is it for people to learn a foreign language?', 'Learning foreign languages is increasingly important in our globalized world. It opens up job opportunities, helps with cultural understanding, and makes travel more enjoyable.', 'Language', NOW());

-- Insert mock user responses with realistic scores
INSERT INTO user_responses (user_id, question_id, response_text, fluency_score, pronunciation_score, grammar_score, vocabulary_score, overall_score, ai_feedback, created_at) VALUES
-- Alice's responses
(1, 1, 'I''m from London, which is the capital of England. It''s a very diverse and multicultural city with lots of history and culture. I really enjoy living there because there''s always something to do.', 7.5, 8.0, 7.0, 8.5, 7.8, 'Excellent response! Your vocabulary is very good and you speak fluently. Try to use more complex sentence structures to improve your grammar score.', NOW()),
(1, 2, 'I work as a software engineer at a tech company. I''ve been there for about three years now and I really enjoy my job. We develop mobile applications and I work with a great team.', 8.0, 7.5, 8.0, 7.5, 7.8, 'Very good answer! Your pronunciation is clear and you use appropriate vocabulary. Consider adding more details about your daily tasks.', NOW()),
(1, 3, 'I love reading books, especially science fiction. My favorite author is Isaac Asimov. I usually read before bed and I try to finish at least one book per month.', 6.5, 7.0, 7.5, 7.0, 7.0, 'Good response! Your grammar is solid. Try to speak more fluently and add more descriptive language to improve your overall score.', NOW()),

-- Bob's responses
(2, 1, 'I''m from Manchester, a city in northern England. It''s known for its industrial heritage and football culture. I love the friendly people and the vibrant music scene there.', 7.0, 7.5, 7.0, 7.5, 7.3, 'Good answer! Your pronunciation is clear. Try to speak more fluently and use more varied vocabulary.', NOW()),
(2, 4, 'My favorite food is definitely pizza! I love the combination of cheese, tomato sauce, and various toppings. I also enjoy cooking pizza at home with my family.', 7.5, 7.0, 7.5, 7.0, 7.3, 'Nice response! Your grammar is good. Work on your pronunciation, especially the word ''pizza''. Also, try to speak more smoothly.', NOW()),
(2, 5, 'Yes, I really enjoy traveling! I''ve been to several countries in Europe and Asia. My most memorable trip was to Japan last year. The culture and food were amazing.', 8.5, 8.0, 8.0, 8.0, 8.1, 'Excellent response! You speak very fluently and use good vocabulary. Your pronunciation is clear and natural. Keep up the great work!', NOW()),

-- Carol's responses
(3, 2, 'I''m a teacher at a primary school. I teach children aged 6 to 11 and I find it very rewarding. Every day is different and I love seeing my students learn and grow.', 7.0, 7.5, 7.0, 7.5, 7.3, 'Good answer! Your vocabulary is appropriate for the topic. Try to speak more fluently and add more specific details.', NOW()),
(3, 3, 'I enjoy reading mystery novels and biographies. I find them both entertaining and educational. I usually read for about an hour each evening before going to sleep.', 6.5, 7.0, 7.0, 7.5, 7.0, 'Good response! Your grammar is solid. Try to speak more fluently and add more descriptive language to improve your overall score.', NOW()),
(3, 6, 'I''d love to visit New Zealand. It''s known for its stunning natural landscapes and outdoor activities. I want to go hiking, see the fjords, and experience the Maori culture.', 7.5, 7.0, 7.5, 7.5, 7.4, 'Very good answer! Your vocabulary is good and you speak clearly. Consider adding more specific details about what you would do there.', NOW()),

-- David's responses
(4, 4, 'I really enjoy Thai food, especially pad thai and green curry. I love the combination of sweet, sour, and spicy flavors. I also enjoy cooking Thai dishes at home.', 7.0, 6.5, 7.0, 7.5, 7.0, 'Nice answer! Your vocabulary is good. Work on your pronunciation, especially the word ''curry''. Also, try to speak more smoothly.', NOW()),
(4, 5, 'I love traveling! I''ve visited many countries in Europe and South America. My favorite trip was to Peru where I hiked the Inca Trail to Machu Picchu.', 8.0, 7.5, 8.0, 8.0, 7.9, 'Excellent response! You speak very fluently and use good vocabulary. Your pronunciation is clear and natural. Keep up the great work!', NOW()),
(4, 7, 'My grandfather has been a huge influence on me. He taught me the importance of hard work and perseverance. He always encouraged me to pursue my dreams.', 7.5, 7.0, 7.5, 7.5, 7.4, 'Very good answer! Your vocabulary is good and you speak clearly. Consider adding more specific details about what he taught you.', NOW()),

-- Emma's responses
(5, 1, 'I''m from Edinburgh, the capital of Scotland. It''s a beautiful city with lots of history and culture. I love the festivals and the friendly atmosphere.', 7.5, 8.0, 7.5, 8.0, 7.8, 'Excellent response! Your vocabulary is very good and you speak fluently. Try to use more complex sentence structures to improve your grammar score.', NOW()),
(5, 2, 'I work as a graphic designer for a marketing agency. I create visual content for various clients and I really enjoy the creative aspect of my job.', 7.0, 7.5, 7.0, 7.5, 7.3, 'Good answer! Your pronunciation is clear and you use appropriate vocabulary. Consider adding more details about your daily tasks.', NOW()),
(5, 8, 'Graduating from university was the most important event in my life. It happened last year and marked the end of four years of hard work. I felt incredibly proud.', 8.0, 7.5, 8.0, 8.0, 7.9, 'Excellent response! You speak very fluently and use good vocabulary. Your pronunciation is clear and natural. Keep up the great work!', NOW());

-- Insert mock feedback for users
INSERT INTO feedbacks (user_id, ai_comment, created_at) VALUES
(1, 'Great improvement in your fluency! Keep practicing to maintain this level. Your vocabulary usage is excellent.', NOW()),
(1, 'Your pronunciation has improved significantly. Focus on intonation patterns to sound more natural.', NOW()),
(1, 'Excellent vocabulary usage. Try to incorporate more academic words in your responses.', NOW()),

(2, 'Good grammar overall. Pay attention to article usage and verb tenses.', NOW()),
(2, 'Your responses are becoming more natural. Continue with regular practice.', NOW()),

(3, 'Well done on the overall score! Your preparation is showing results.', NOW()),
(3, 'Consider using more complex sentence structures to improve your band score.', NOW()),

(4, 'Your speaking confidence has increased. Keep building on this foundation.', NOW()),
(4, 'Good use of examples and personal experiences in your answers.', NOW()),

(5, 'Your time management during responses is excellent. Well done!', NOW()),
(5, 'Great improvement in your fluency! Keep practicing to maintain this level.', NOW());

-- Display summary
SELECT 'Mock data population completed!' as status;

-- Show summary statistics
SELECT 'Users created: ' || COUNT(*) as summary FROM users WHERE tg_id IN (1001, 1002, 1003, 1004, 1005)
UNION ALL
SELECT 'Questions created: ' || COUNT(*) as summary FROM questions
UNION ALL
SELECT 'User responses created: ' || COUNT(*) as summary FROM user_responses
UNION ALL
SELECT 'Feedback entries created: ' || COUNT(*) as summary FROM feedbacks;

-- Show sample data
SELECT 'Sample Users:' as info
UNION ALL
SELECT first_name || ' (ID: ' || id || ')' FROM users WHERE tg_id IN (1001, 1002, 1003, 1004, 1005)
UNION ALL
SELECT ''
UNION ALL
SELECT 'Sample Questions by Part:' as info
UNION ALL
SELECT 'Part ' || part || ': ' || LEFT(question_text, 50) || '...' FROM questions ORDER BY part, id; 