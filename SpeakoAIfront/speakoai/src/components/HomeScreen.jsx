export default function HomeScreen({ onSelectFullExam, onSelectPart }) {
    return (
        <div className="w-full max-w-xs flex flex-col gap-6 items-center">
            <h1 className="text-3xl font-bold text-blue-700 mb-8">SpeakoAI</h1>
            <button className="w-full py-4 rounded-xl bg-blue-600 text-white text-lg font-semibold shadow-md transition hover:bg-blue-700" onClick={onSelectFullExam}>
                Full Mock Exam
            </button>
            <div className="w-full flex flex-col gap-3">
                <span className="text-blue-700 font-medium text-center">Or choose a part:</span>
                <button className="w-full py-3 rounded-xl bg-blue-100 text-blue-700 font-semibold transition hover:bg-blue-200" onClick={() => onSelectPart('PART 1')}>
                    Part 1
                </button>
                <button className="w-full py-3 rounded-xl bg-blue-100 text-blue-700 font-semibold transition hover:bg-blue-200" onClick={() => onSelectPart('PART 2')}>
                    Part 2
                </button>
                <button className="w-full py-3 rounded-xl bg-blue-100 text-blue-700 font-semibold transition hover:bg-blue-200" onClick={() => onSelectPart('PART 3')}>
                    Part 3
                </button>
            </div>
        </div>
    );
} 