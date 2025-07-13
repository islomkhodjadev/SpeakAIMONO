export default function MicButton({ onClick, isRecording }) {
    return (
        <button
            className={`w-20 h-20 rounded-full flex items-center justify-center shadow-lg focus:outline-none transition-all duration-200 
        ${isRecording ? 'bg-red-600 animate-pulse' : 'bg-blue-600 animate-pulse'}
      `}
            onClick={onClick}
            aria-label={isRecording ? 'Stop Recording' : 'Start Recording'}
            type="button"
        >
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="white" className="w-10 h-10">
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 18.75v1.5m0 0h3.75m-3.75 0H8.25m3.75-1.5A6.75 6.75 0 015.25 12V9a6.75 6.75 0 1113.5 0v3a6.75 6.75 0 01-6.75 6.75z" />
            </svg>
        </button>
    );
} 