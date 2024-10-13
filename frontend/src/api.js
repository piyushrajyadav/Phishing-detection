// src/api.js

const BASE_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000'; // Set the base URL for the API

/**
 * Function to analyze a URL
 * @param {string} url - The URL to analyze
 * @returns {Promise<Object>} - The response from the server
 */
export const analyzeUrl = async (url) => {
  try {
    const response = await fetch(`${BASE_URL}/api/predict`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url }), // Send the URL as JSON
    });

    if (!response.ok) {
      throw new Error('Network response was not ok'); // Handle HTTP errors
    }

    const data = await response.json(); // Parse JSON response
    return data; // Return the prediction result
  } catch (error) {
    console.error('Error analyzing URL:', error);
    return { prediction: null }; // Return null in case of error
  }
};

/**
 * Function to submit feedback
 * @param {string} url - The URL for which feedback is provided
 * @param {string} feedback - The feedback text
 * @returns {Promise<boolean>} - Indicates whether the feedback submission was successful
 */
export const submitFeedback = async (url, feedback) => {
  try {
    const response = await fetch(`${BASE_URL}/api/feedback`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ url, feedback }), // Send URL and feedback as JSON
    });

    return response.ok; // Return true if the submission was successful
  } catch (error) {
    console.error('Error submitting feedback:', error);
    return false; // Return false if there was an error
  }
};

