import { useState, useRef } from 'react';
import { getTelegramId } from '../utils/telegram';
const API_BASE = 'http://localhost:8000/api';

function getPartNumber(part) {
    if (typeof part === 'number') return part;
    if (part === 'PART 1') return 1;
    if (part === 'PART 2') return 2;
    if (part === 'PART 3') return 3;
    return 1;
}

export default function QuestionScreen({ part, question, questionId, onAnswerSent, onNextQuestion, onEvaluate, loading,isMockMode  }) {
    const [isRecording, setIsRecording] = useState(false);
    const [mediaRecorder, setMediaRecorder] = useState(null);
    const [audioURL, setAudioURL] = useState(null);
    const [sending, setSending] = useState(false);
    const [answerSent, setAnswerSent] = useState(false);
    const audioChunks = useRef([]);

    const handleStartRecording = async () => {
        if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
            alert('Audio recording is not supported in this browser.');
            return;
        }
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        const recorder = new window.MediaRecorder(stream);
        recorder.ondataavailable = (e) => {
            if (e.data.size > 0) {
                audioChunks.current.push(e.data);
            }
        };
        recorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks.current, { type: 'audio/webm' });
            setAudioURL(URL.createObjectURL(audioBlob));
            await sendAudioAnswer(audioBlob);
            audioChunks.current = [];
        };
        audioChunks.current = [];
        setMediaRecorder(recorder);
        recorder.start();
        setIsRecording(true);
    };

    const handleStopRecording = () => {
        if (mediaRecorder) {
            mediaRecorder.stop();
            setIsRecording(false);
        }
    };

    const sendAudioAnswer = async (audioBlob) => {
        setSending(true);
        setAnswerSent(true); // Always show Next/Evaluate after recording
        const tg_id = getTelegramId();
        const formData = new FormData();
        formData.append('user_id', tg_id || 'test_user');
        formData.append('part', getPartNumber(part)); // ensure integer
        formData.append('question', questionId);
        formData.append('file', audioBlob, 'answer.webm'); // field must be 'file'
        try {
            const res = await fetch(`${API_BASE}/ai/add-answer`, {
                method: 'POST',
                body: formData
            });
            onAnswerSent && onAnswerSent();
            if (!res.ok) {
                alert('Failed to send answer.');
            }
        } catch (e) {
            alert('Error sending answer.');
        }
        setSending(false);
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
        <div className="w-full max-w-xs flex flex-col gap-8 items-center">
            <div className="text-blue-700 font-semibold text-center">{part}</div>
            <div className="w-full bg-blue-50 rounded-xl p-6 shadow text-blue-900 text-lg font-medium text-center min-h-[100px] flex items-center justify-center">
                {question}
            </div>
            <div className="flex flex-col items-center gap-2">
                {!isRecording && (
                    <button
                        className={`w-32 py-3 rounded-xl bg-blue-600 text-white font-semibold transition hover:bg-blue-700 shadow-lg active:scale-95 focus:outline-none border-b-4 border-blue-800 ${sending ? 'opacity-60 cursor-not-allowed' : ''}`}
                        onClick={handleStartRecording}
                        disabled={sending || loading}
                    >
                        Start Recording
                    </button>
                )}
                {isRecording && (
                    <button
                        className="w-32 py-3 rounded-xl bg-red-600 text-white font-semibold transition hover:bg-red-700 animate-pulse shadow-lg active:scale-95 focus:outline-none border-b-4 border-red-800"
                        onClick={handleStopRecording}
                    >
                        Stop Recording
                    </button>
                )}
                {audioURL && (
                    <audio controls src={audioURL} className="mt-2" />
                )}
                {(sending || loading) && (
                    <div className="flex items-center gap-2 mt-2">
                        <span className="text-blue-700 font-semibold">Processing</span>
                        <span className="flex space-x-1">
                            <span className="inline-block w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0s' }}></span>
                            <span className="inline-block w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                            <span className="inline-block w-2 h-2 bg-blue-600 rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
                        </span>
                    </div>
                )}
                {answerSent && (
                    <button
                        className={`w-32 py-3 rounded-xl bg-green-600 text-white font-semibold transition hover:bg-green-700 mt-4 shadow-lg active:scale-95 focus:outline-none border-b-4 border-green-800 ${sending || loading ? 'opacity-60 cursor-not-allowed' : ''}`}
                        onClick={onNextQuestion}
                        disabled={sending || loading}
                    >
                        Next
                    </button>
                )}
             {((isMockMode && getPartNumber(part) === 3) || !isMockMode) && (
                <button
                    className={`w-32 py-3 rounded-xl bg-purple-600 text-white font-semibold transition hover:bg-purple-700 mt-2 shadow-lg active:scale-95 focus:outline-none border-b-4 border-purple-800 ${(sending || loading || isRecording) ? 'opacity-60 cursor-not-allowed' : ''}`}
                    onClick={onEvaluate}
                    disabled={sending || loading || isRecording}
                >
                    {loading ? (
                    <span className="flex items-center justify-center">
                        <span>Evaluate</span>
                        <span className="flex space-x-1 ml-2">
                        <span className="inline-block w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '0s' }}></span>
                        <span className="inline-block w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></span>
                        <span className="inline-block w-2 h-2 bg-white rounded-full animate-bounce" style={{ animationDelay: '0.4s' }}></span>
                        </span>
                    </span>
                    ) : (
                    'Evaluate'
                    )}
                </button>
                )}


            </div>
        </div>
    );
} 