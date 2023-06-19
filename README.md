# Sentiment Analysis API
This project implements a Sentiment Analysis API using Django and a pre-trained sentiment analysis model.

# Project Setup
1. Ensure you have Python installed on your machine.
2. Install the necessary dependencies using the package manager of your choice (pip or Poetry).
3. Clone this repository to your local machine.
4. Navigate to the project directory:
            cd sentiment_analysis_api


# Dependencies
Dependencies
  > python: 3.9.12
  > Django: 4.2.2
  > Transformers: 4.30.2
  > Other dependencies : find on requerements.txt

Running the API Locally
  1. Start the Django development server
      python manage.py runserver
  2. The API will be accessible at http://localhost:8000/sentiment/analyze/

# API Usage
To analyze the sentiment of a text, send a POST request to the /analyze endpoint with the following payload:
{
  "text": "Insert text to be analyzed here"
}
The API will respond with a JSON object containing the sentiment analysis result:
{
  "sentiment": "positive"
}

The frontend for interacting with the API can be accessed by opening the web browser and navigating to http://127.0.0.1:8000/sentiment/analyze/

# Additional Information
 1. The frontend interface for the Sentiment Analysis API can be found in the templates/index.html file.
 2. The backend logic for sentiment analysis is implemented in the views.py file.
 3. The API endpoint for sentiment analysis is defined in the urls.py file.
