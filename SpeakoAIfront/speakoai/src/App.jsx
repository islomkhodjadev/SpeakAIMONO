import { useState, useEffect } from 'react';
import HomeScreen from './components/HomeScreen';
import QuestionScreen from './components/QuestionScreen';
import FeedbackScreen from './components/FeedbackScreen';

const API_BASE = 'http://localhost:8000/api';

const screens = {
  HOME: 'HOME',
  QUESTION: 'QUESTION',
  FEEDBACK: 'FEEDBACK',
  COMPLETE: 'COMPLETE',
  PART_TRANSITION: 'PART_TRANSITION',
};

const PARTS = ['PART 1', 'PART 2', 'PART 3'];

function getPartNumber(part) {
  if (typeof part === 'number') return part;
  if (part === 'PART 1') return 1;
  if (part === 'PART 2') return 2;
  if (part === 'PART 3') return 3;
  return 1;
}

export default function App() {
  const [screen, setScreen] = useState(screens.HOME);
  const [mode, setMode] = useState(null); // 'MOCK' or 'SECTION'
  const [currentPart, setCurrentPart] = useState(null); // 'PART 1', etc.
  const [questionIdx, setQuestionIdx] = useState(0);
  const [feedback, setFeedback] = useState('');
  const [showPartTransition, setShowPartTransition] = useState(false);
  const [mockPartIdx, setMockPartIdx] = useState(0);
  const [mockQuestionIdx, setMockQuestionIdx] = useState(0);
  const [questions, setQuestions] = useState([]);
  const [mockQuestions, setMockQuestions] = useState([[], [], []]);
  const [loading, setLoading] = useState(false);

  // Fetch questions for a part
  const fetchQuestions = async (part) => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE}/questions/part/${getPartNumber(part)}`);
      const data = await res.json();
      setQuestions(data);
    } catch (e) {
      setQuestions([]);
    }
    setLoading(false);
  };

  // Fetch all parts for mock
  const fetchAllParts = async () => {
    setLoading(true);
    try {
      const results = await Promise.all([
        fetch(`${API_BASE}/questions/part/1`).then(r => r.json()),
        fetch(`${API_BASE}/questions/part/2`).then(r => r.json()),
        fetch(`${API_BASE}/questions/part/3`).then(r => r.json()),
      ]);
      setMockQuestions(results);
    } catch (e) {
      setMockQuestions([[], [], []]);
    }
    setLoading(false);
  };

  // Handlers for HomeScreen
  const handleSelectFullExam = async () => {
    setMode('MOCK');
    setMockPartIdx(0);
    setMockQuestionIdx(0);
    setCurrentPart(PARTS[0]);
    setScreen(screens.PART_TRANSITION);
    await fetchAllParts();
    setTimeout(() => setScreen(screens.QUESTION), 1200);
  };

  const handleSelectPart = async (partName) => {
    setMode('SECTION');
    setCurrentPart(partName);
    setQuestionIdx(0);
    setScreen(screens.QUESTION);
    await fetchQuestions(partName);
  };

  // Handlers for QuestionScreen
  const handleSubmitAnswer = async (answer) => {
    // Find current question and part
    let q = '';
    let p = 1;
    let qid = null;
    if (mode === 'SECTION' && currentPart && questions.length > 0) {
      q = questions[questionIdx]?.question_text || '';
      p = getPartNumber(currentPart);
      qid = questions[questionIdx]?.id;
    } else if (mode === 'MOCK' && currentPart && mockQuestions[mockPartIdx].length > 0) {
      q = mockQuestions[mockPartIdx][mockQuestionIdx]?.question_text || '';
      p = getPartNumber(currentPart);
      qid = mockQuestions[mockPartIdx][mockQuestionIdx]?.id;
    }

    // Call backend for feedback
    try {
      const res = await fetch(`${API_BASE}/ai/score`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q, answer, part: p })
      });
      const data = await res.json();
      setFeedback(data.score || 'No feedback received.');
    } catch (e) {
      setFeedback('Error getting feedback.');
    }
    setScreen(screens.FEEDBACK);

    // Optionally, save the response to backend
    // await fetch(`${API_BASE}/responses/`, {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ user_id: 1, question_id: qid, response_text: answer, ai_feedback: data.score })
    // });
  };

  const handleNext = () => {
    if (mode === 'SECTION') {
      if (questionIdx < questions.length - 1) {
        setQuestionIdx(q => q + 1);
        setScreen(screens.QUESTION);
      } else {
        setScreen(screens.COMPLETE);
      }
    } else if (mode === 'MOCK') {
      if (mockQuestionIdx < mockQuestions[mockPartIdx].length - 1) {
        setMockQuestionIdx(q => q + 1);
        setScreen(screens.QUESTION);
      } else if (mockPartIdx < PARTS.length - 1) {
        setMockPartIdx(p => p + 1);
        setMockQuestionIdx(0);
        setCurrentPart(PARTS[mockPartIdx + 1]);
        setScreen(screens.PART_TRANSITION);
        setTimeout(() => setScreen(screens.QUESTION), 1200);
      } else {
        setScreen(screens.COMPLETE);
      }
    }
  };

  const handleHome = () => {
    setScreen(screens.HOME);
    setMode(null);
    setCurrentPart(null);
    setQuestionIdx(0);
    setMockPartIdx(0);
    setMockQuestionIdx(0);
    setFeedback('');
    setQuestions([]);
    setMockQuestions([[], [], []]);
  };

  // Get current question
  let question = '';
  let questionId = null;
  if (mode === 'SECTION' && currentPart && questions.length > 0) {
    question = questions[questionIdx]?.question_text || '';
    questionId = questions[questionIdx]?.id;
  } else if (mode === 'MOCK' && currentPart && mockQuestions[mockPartIdx].length > 0) {
    question = mockQuestions[mockPartIdx][mockQuestionIdx]?.question_text || '';
    questionId = mockQuestions[mockPartIdx][mockQuestionIdx]?.id;
  }

  return (
    <div className="min-h-screen bg-white flex flex-col items-center justify-center px-4 py-6">
      {screen === screens.HOME && (
        <HomeScreen
          onSelectFullExam={handleSelectFullExam}
          onSelectPart={handleSelectPart}
        />
      )}
      {screen === screens.PART_TRANSITION && (
        <div className="w-full max-w-xs flex flex-col items-center justify-center animate-fade-in">
          <div className="text-blue-700 text-2xl font-bold mb-4">Now {currentPart}</div>
        </div>
      )}
      {screen === screens.QUESTION && (
        <QuestionScreen
          part={currentPart}
          question={question}
          questionId={questionId}
          onSubmitAnswer={handleSubmitAnswer}
          loading={loading}
        />
      )}
      {screen === screens.FEEDBACK && (
        <FeedbackScreen
          feedback={feedback}
          onNextQuestion={handleNext}
          onHome={handleHome}
        />
      )}
      {screen === screens.COMPLETE && (
        <div className="w-full max-w-xs flex flex-col gap-8 items-center">
          <div className="w-full bg-blue-100 rounded-xl p-6 shadow text-blue-900 text-lg font-bold text-center min-h-[100px] flex items-center justify-center">
            {mode === 'MOCK' ? 'Mock Exam Complete!' : 'Section Complete!'}
          </div>
          <button className="w-full py-3 rounded-xl bg-blue-600 text-white font-semibold transition hover:bg-blue-700" onClick={handleHome}>
            Home
          </button>
        </div>
      )}
    </div>
  );
}
