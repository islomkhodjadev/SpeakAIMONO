import { useState } from 'react';

export default function QuestionScreen({ part, question, questionId, onSubmitAnswer, loading }) {
    const [answer, setAnswer] = useState('');
    const [submitting, setSubmitting] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!answer.trim()) return;
        setSubmitting(true);
        await onSubmitAnswer(answer);
        setSubmitting(false);
        setAnswer('');
    };

    if (loading) {
        return (
            <div className="w-full max-w-xs flex flex-col items-center justify-center min-h-[200px]">
                <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
                <div className="text-blue-700 font-semibold">Loading questions...</div>
            </div>
        );
    }

    return (
        <form className="w-full max-w-xs flex flex-col gap-8 items-center" onSubmit={handleSubmit}>
            <div className="text-blue-700 font-semibold text-center">{part}</div>
            <div className="w-full bg-blue-50 rounded-xl p-6 shadow text-blue-900 text-lg font-medium text-center min-h-[100px] flex items-center justify-center">
                {question}
            </div>
            <textarea
                className="w-full rounded-lg border border-blue-300 p-3 min-h-[80px] focus:outline-none focus:ring-2 focus:ring-blue-400"
                placeholder="Type your answer here..."
                value={answer}
                onChange={e => setAnswer(e.target.value)}
                disabled={submitting}
                required
            />
            <button
                className="w-full py-3 rounded-xl bg-blue-600 text-white font-semibold transition hover:bg-blue-700 disabled:opacity-60"
                type="submit"
                disabled={submitting || !answer.trim()}
            >
                {submitting ? 'Submitting...' : 'Submit Answer'}
            </button>
        </form>
    );
} 