import ReactMarkdown from "react-markdown";

export default function FeedbackScreen({ feedback, onNextQuestion, onHome }) {
    return (
        <div className="w-full px-4 flex flex-col gap-6 items-center">
             <div
                className="w-full max-w-md bg-blue-50 rounded-2xl p-4 shadow text-blue-900 text-sm leading-relaxed text-left break-words"
                dangerouslySetInnerHTML={{ __html: feedback || 'Your feedback will appear here!' }}
            />
            <button
                className="w-full max-w-md py-3 rounded-xl bg-white border border-blue-600 text-blue-700 text-sm font-semibold transition hover:bg-blue-100"
                onClick={onHome}
            >
                Home
            </button>
        </div>
    );
}
