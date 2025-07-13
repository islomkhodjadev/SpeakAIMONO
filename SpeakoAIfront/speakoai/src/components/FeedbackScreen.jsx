export default function FeedbackScreen({ feedback, onNextQuestion, onHome }) {
    return (
        <div className="w-full max-w-xs flex flex-col gap-8 items-center">
            <div className="w-full bg-blue-100 rounded-xl p-6 shadow text-blue-900 text-lg font-medium text-center min-h-[100px] flex items-center justify-center">
                {feedback || 'Your feedback will appear here!'}
            </div>
            <button className="w-full py-3 rounded-xl bg-blue-600 text-white font-semibold transition hover:bg-blue-700" onClick={onNextQuestion}>
                Next Question
            </button>
            <button className="w-full py-3 rounded-xl bg-white border border-blue-600 text-blue-700 font-semibold transition hover:bg-blue-50" onClick={onHome}>
                Home
            </button>
        </div>
    );
} 