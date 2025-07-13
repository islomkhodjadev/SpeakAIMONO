# SpeakoAI Mock Data Population

This directory contains scripts to populate the SpeakoAI backend with realistic mock data for testing and development.

## 📁 Files

- `populate_mock_data.py` - Main Python script that creates mock data
- `populate_data.sh` - Linux/Mac shell script to run the population
- `populate_data.bat` - Windows batch file to run the population

## 🚀 Quick Start

### Windows Users
```bash
# Navigate to the SpeakoAI directory
cd SpeakoAI

# Run the Windows batch file
populate_data.bat
```

### Linux/Mac Users
```bash
# Navigate to the SpeakoAI directory
cd SpeakoAI

# Make the script executable (if needed)
chmod +x populate_data.sh

# Run the shell script
./populate_data.sh
```

### Manual Docker Command
```bash
# If you prefer to run manually
docker-compose exec backend python populate_mock_data.py
```

## 📊 What Data is Created

### Users (5 mock users)
- Alice Johnson (tg_id: 1001)
- Bob Smith (tg_id: 1002)
- Carol Davis (tg_id: 1003)
- David Wilson (tg_id: 1004)
- Emma Brown (tg_id: 1005)

### Questions (15 total)
- **Part 1**: 5 questions (Personal Information, Work/Study, Hobbies, Food, Travel)
- **Part 2**: 5 questions (Places, People, Events, Entertainment, Skills)
- **Part 3**: 5 questions (Society, Technology, Education, Environment, Language)

### User Responses
- Multiple responses per user with realistic IELTS scores
- Scores include: Fluency, Pronunciation, Grammar, Vocabulary, Overall
- AI feedback for each response

### Feedback
- 2-3 feedback entries per user
- Realistic coaching comments and suggestions

## 🎯 Sample Questions

### Part 1 Examples
- "Can you tell me about your hometown?"
- "What do you do for work or study?"
- "Do you enjoy reading books?"

### Part 2 Examples
- "Describe a place you would like to visit."
- "Describe a person who has influenced you."
- "Describe an important event in your life."

### Part 3 Examples
- "What are the advantages and disadvantages of living in a big city?"
- "How has technology changed the way people work?"
- "Do you think education should be free for everyone?"

## 🔧 Requirements

- Docker and Docker Compose must be installed
- Backend container must be running
- Database must be accessible

## 🚨 Troubleshooting

### Backend not running
```bash
# Start the backend first
docker-compose up -d backend
```

### Permission denied (Linux/Mac)
```bash
# Make script executable
chmod +x populate_data.sh
```

### Database connection issues
```bash
# Check if database is running
docker-compose ps

# Restart backend if needed
docker-compose restart backend
```

## 📈 After Running

Once the script completes successfully, you can:

1. **Test the Frontend**: The frontend will now have real questions to display
2. **Test AI Scoring**: Submit answers through the frontend to test the AI scoring
3. **View Data**: Check the database to see all created mock data

## 🔄 Re-running

You can run the script multiple times. It will:
- Create new users (if they don't exist)
- Create new questions (if they don't exist)
- Create new responses and feedback

The script is designed to be idempotent - running it multiple times won't create duplicate data.

## 🎯 Next Steps

After populating the data:
1. Start your frontend: `cd SpeakoAIfront/speakoai && npm run dev`
2. Start your backend: `docker-compose up -d`
3. Test the full application with real data! 