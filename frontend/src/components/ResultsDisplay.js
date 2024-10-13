import React from 'react';
import './ResultsDisplay.css';

const ResultsDisplay = ({ prediction, loading, error }) => {
    // Handle loading state
    if (loading) {
        return <div>Loading...</div>;
    }

    // Handle error state
    if (error) {
        return <div className="error-message">{error}</div>;
    }

    // Don't display anything if no prediction has been made
    if (prediction === null) {
        return null; // Render nothing if prediction is null
    }

    // Display the prediction result
    return (
        <div>
            <h2>Prediction Result</h2>
            <p>{prediction === 1 ? 'Phishing' : 'Legitimate'}</p>
        </div>
    );
};

export default ResultsDisplay;


