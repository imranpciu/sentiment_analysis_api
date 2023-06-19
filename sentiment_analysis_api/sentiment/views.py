from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import json
import torch

torch.set_default_tensor_type(torch.FloatTensor)

@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        if 'text' not in data:
            return JsonResponse({'error': 'Invalid request data. Missing "text" key.'}, status=400)
        
        text = data['text']
        model_name = 'StatsGary/setfit-ft-sentinent-eval'
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSequenceClassification.from_pretrained(model_name)
        inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')
        outputs = model(**inputs)
        predicted_class = outputs.logits.argmax().item()
        sentiment_labels = ['positive', 'negative', 'neutral']
        sentiment = sentiment_labels[predicted_class]
        response = {'sentiment': sentiment}
        return JsonResponse(response)
    return JsonResponse({'error': 'Invalid request method'})
