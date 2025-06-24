from rest_framework.decorators import api_view
from rest_framework.response import Response
from transformers import pipeline

model = pipeline("text2text-generation", model="google/flan-t5-base")

@api_view(["POST"])
def extract_keywords(request):
    text = request.data.get("text", "")
    prompt = f"Extract keywords from this text: {text}"
    result = model(prompt, max_length=64, do_sample=False)
    return Response({"keywords": result[0]["generated_text"]})