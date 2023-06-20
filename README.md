# Sentiment Analysis API
This project implements a Sentiment Analysis API using Django and a pre-trained sentiment analysis model.

# Project Setup
1. Navigate to the project directory:
            "cd sentiment_analysis_api"
2. Install the necessary dependencies and create a virtual environment:
   . Virtual Environment Setup: Navigate to the project directory and run "pipenv install" to create the virtual environment and install the necessary dependencies.
   . Activate the Virtual Environment: Use "pipenv shell" to activate the virtual environment before proceeding further.
3. Run the project: "python manage.py runserver"

Note: The following instructions are intended for Git Bash. Please make sure you have Git Bash installed and used these commands accordingly.


# Dependencies
Dependencies
  > python: 3.9.1
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
