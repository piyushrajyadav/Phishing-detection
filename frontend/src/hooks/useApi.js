import { useState } from 'react';

const useApi = (urlToAnalyze) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [prediction, setPrediction] = useState(null);

    const fetchPrediction = async () => {
        setLoading(true);
        setError(null); // Reset error state

        try {
            const response = await fetch('http://127.0.0.1:5000/api/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: urlToAnalyze }),
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            setPrediction(result.prediction); // Update prediction state
        } catch (err) {
            console.error('Error fetching prediction:', err);
            setError('Error: Could not retrieve result');
        } finally {
            setLoading(false);
        }
    };

    return { fetchPrediction, loading, error, prediction };
};

export default useApi;
