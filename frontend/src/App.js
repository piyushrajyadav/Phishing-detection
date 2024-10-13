import React, { useState } from 'react';
import FeedbackForm from './components/FeedbackForm';
import ResultsDisplay from './components/ResultsDisplay';
import UrlInput from './components/UrlInput';
import useApi from './hooks/useApi'; // Custom hook for fetching predictions

function App() {
    const [url, setUrl] = useState('');
    const { fetchPrediction, loading, error, prediction } = useApi(url);

    const handleUrlSubmit = async (submittedUrl) => {
        setUrl(submittedUrl); // Set the submitted URL
        await fetchPrediction(); // Call the fetch function
    };

    return (
        <div className="App">
            <h1>Phishing Detection Tool</h1>
            <UrlInput onUrlSubmit={handleUrlSubmit} />
            <FeedbackForm url={url} onSubmit={() => console.log('Feedback submitted')} />
            <ResultsDisplay prediction={prediction} loading={loading} error={error} />
            <footer className="footer">
                <p>© SafeSurf. All rights reserved.</p>
                <p>Developed by Piyush Yadav</p>
            </footer>
        </div>
    );
}

export default App;

