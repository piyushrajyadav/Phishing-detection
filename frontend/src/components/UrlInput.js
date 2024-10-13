// import React, { useState } from 'react';
// import ResultsDisplay from './ResultsDisplay';

// const UrlInput = () => {
//     const [url, setUrl] = useState(''); // URL input state
//     const [prediction, setPrediction] = useState(null); // Prediction state, initialized as null
//     const [loading, setLoading] = useState(false); // Loading state
//     const [error, setError] = useState(null); // Error state

//     const handleSubmit = async (e) => {
//         e.preventDefault(); // Prevent default form submission behavior
//         setLoading(true); // Start loading
//         setError(null); // Reset error state
//         setPrediction(null); // Clear previous prediction before making new request

//         try {
//             const response = await fetch('http://127.0.0.1:5000/api/predict', {
//                 method: 'POST',
//                 headers: {
//                     'Content-Type': 'application/json',
//                 },
//                 body: JSON.stringify({ url }), // Send the URL to the backend
//             });

//             if (!response.ok) {
//                 throw new Error('Network response was not ok'); // If response is not ok, throw an error
//             }

//             const result = await response.json(); // Parse JSON result
//             if (result.prediction !== undefined) {
//                 setPrediction(result.prediction); // Update prediction state with the backend result
//             } else {
//                 throw new Error('No prediction returned from API'); // Handle case where prediction is missing
//             }
//         } catch (err) {
//             setError('Error: Could not retrieve result'); // Set error state if request fails
//         } finally {
//             setLoading(false); // Stop loading when the request is done
//         }
//     };

//     return (
//         <div>
//             <h2>Phishing Detection Tool</h2>
//             <form onSubmit={handleSubmit}>
//                 <input
//                     type="text"
//                     value={url}
//                     onChange={(e) => setUrl(e.target.value)} // Update URL state on input change
//                     placeholder="Enter URL to analyze"
//                     required
//                 />
//                 <button type="submit">Analyze</button>
//             </form>
//             {/* ResultsDisplay will only show the result once prediction is available */}
//             <ResultsDisplay prediction={prediction} loading={loading} error={error} />
//         </div>
//     );
// };

// export default UrlInput;


import React, { useState } from 'react';
import ResultsDisplay from './ResultsDisplay';
import useApi from '../hooks/useApi';

const UrlInput = ({ onUrlSubmit }) => {
    const [url, setUrl] = useState('');
    const { fetchPrediction, loading, error, prediction } = useApi(url);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setUrl(url); // Update the URL state
        await fetchPrediction(); // Call the fetch function
        if (onUrlSubmit) {
            onUrlSubmit(url); // Call the onUrlSubmit prop to pass the URL to the parent
        }
    };

    return (
        <div>
            <h2>Phishing Detection Tool</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter URL to analyze"
                    required
                />
                <button type="submit">Analyze</button>
            </form>
            <ResultsDisplay prediction={prediction} loading={loading} error={error} />
        </div>
    );
};

export default UrlInput;

