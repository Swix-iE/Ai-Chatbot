from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

# API_KEY = os.getenv("API_KEY")
# print(API_KEY)
def Home(request):
    return render(request, 'home.html')