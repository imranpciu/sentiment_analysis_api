from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json
import torch

torch.set_default_tensor_type(torch.FloatTensor)

@csrf_exempt
def analyze(request):
    """
    API endpoint for sentiment analysis.
    Performs sentiment analysis on text input using a pre-trained model.

    Request Method:
        - POST: Accepts JSON payload with 'text' key.

    Returns:
        - JSON response with the sentiment analysis result.
    """
    try:
        if request.method == 'POST':
            # Extract the text from the JSON payload
            data = json.loads(request.body)
            if 'text' not in data:
                return JsonResponse({'error': 'Invalid request data. Missing "text" key.'}, status=400)
            text = data['text']

            # Load the pre-trained sentiment analysis model
            model_name = 'StatsGary/setfit-ft-sentinent-eval'
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForSequenceClassification.from_pretrained(model_name)

            # Tokenize the input text
            inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')

            # Perform sentiment analysis
            outputs = model(**inputs)
            predicted_class = outputs.logits.argmax().item()

            # Map predicted class to sentiment labels
            sentiment_labels = ['positive', 'negative', 'neutral']
            sentiment = sentiment_labels[predicted_class]

            # Prepare JSON response
            response = {'sentiment': sentiment}
            return JsonResponse(response)

        # Render the index.html template for GET requests
        return render(request, 'index.html')

    except Exception as e:
        return JsonResponse({'error': 'An error occurred. Please try again.'}, status=500)
