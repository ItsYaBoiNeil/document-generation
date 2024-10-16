from django.shortcuts import render
import requests
import os
from django.http import HttpResponse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors
from django.conf import settings

# def api(request):
#     if request.method == 'GET':
#         response = requests.get('https://random-word-api.herokuapp.com/word')
#         if response.status_code == 200:
#             word = response.json()[0]
#         else:
#             word = "Error fetching word"
#         request.session['random_word'] = word
#     else:
#         word = request.session.get('random_word', 'Error fetching word')
    
#     if request.method == 'POST':
#         return string2pdf(word)
    
#     return render(request, "home.html", {"word": word})


# def index(request):
#     return render(request,'home.html')

# def string2pdf(string):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="sample.pdf"'

#     #textLines = [ 
#     #string
#     #]

#     pdf = canvas.Canvas(response) 
#     pdf.setTitle("Test Document")

#     pdfmetrics.registerFont( 
#     TTFont('abc', os.path.join(settings.BASE_DIR,'static','fonts','times-new-roman.ttf')) 
#     )

#     pdf.setFont('abc', 36) 
#     pdf.drawCentredString(300, 770, "iPAM")

#     pdf.setFillColorRGB(0, 0, 0) 
#     pdf.setFont("Courier-Bold", 24) 
#     pdf.drawCentredString(290, 720, "BE Project") 

#     pdf.line(30, 710, 550, 710) 

#     text = pdf.beginText(40, 680) 
#     text.setFont("Courier", 18) 
#     text.setFillColor(colors.black)

#     #for line in textLines: 
#     #    text.textLine(line) 
#     text.textLine(string)

#     pdf.drawText(text)

#     pdf.showPage()
#     pdf.save()

#     return response
# Create your views here.

# ----------------------------------------------------------------------------------------------
import os
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors
from django.conf import settings
from mistralai import Mistral
import textwrap

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


# Fetch data from Mistral LLM
# def fetch_llm_response():
#     api_key = os.environ.get("MISTRAL_API_KEY")
#     if not api_key:
#         return "API key not found. Set the environment variable 'MISTRAL_API_KEY'."
    
#     model = "mistral-small-latest"
#     client = Mistral(api_key=api_key)
    
#     try:
#         # Making a request to Mistral LLM to get the planets of our solar system
#         chat_response = client.chat.complete(
#             model=model,
#             messages=[
#                 {
#                     "role": "user",
#                     "content": "Name the planets of our solar system",
#                 },
#             ]
#         )
#         return chat_response.choices[0].message.content
#     except Exception as e:
#         return f"Error fetching LLM response: {e}"
# -----------------------------------------------------------------------------------------------------
#New api request function:
# def fetch_llm_response():
#     # api_key = os.environ.get("MISTRAL_API_KEY")
#     api_key = '' 
#     if not api_key:
#         return "API key not found. Set the environment variable 'MISTRAL_API_KEY'."

#     # API endpoint
#     url = "https://api.mistral.ai/v1/chat/completions"

#     # Headers with Bearer token
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }

#     # Payload for the API request
#     payload = {
#         "model": "mistral-small-latest",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Give an overview of engineering colleges in Mumbai and a ranking"
#             }
#         ]
#     }

#     try:
#         # Make the request to the Mistral API
#         response = requests.post(url, json=payload, headers=headers)
#         response_data = response.json()

#         # Handle unauthorized or other errors
#         if response.status_code == 401:
#             return f"Error: Unauthorized. Check your API key."
#         elif response.status_code != 200:
#             return f"Error: {response_data.get('message', 'Unknown error')}"

#         # Get the response content
#         return response_data['choices'][0]['message']['content']
    
#     except Exception as e:
#         return f"Error fetching LLM response: {e}"




# # Django view to fetch and show the response from Mistral LLM
# def api(request):
#     if request.method == 'GET':
#         word = fetch_llm_response()
#         request.session['llm_response'] = word
#     else:
#         word = request.session.get('llm_response', 'Error fetching LLM response')
    
#     if request.method == 'POST':
#         return string2pdf(word)
    
#     return render(request, "home.html", {"word": word})

# # Function to generate PDF from string
# import textwrap

# def string2pdf(string):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="llm_response.pdf"'

#     pdf = canvas.Canvas(response)
#     pdf.setTitle("LLM Response Document")

#     pdfmetrics.registerFont(
#         TTFont('abc', os.path.join(settings.BASE_DIR, 'static', 'fonts', 'times-new-roman.ttf'))
#     )

#     pdf.setFont('abc', 36)
#     pdf.drawCentredString(300, 770, "LLM Response")

#     pdf.setFillColorRGB(0, 0, 0)
#     pdf.setFont("Courier-Bold", 24)
#     pdf.drawCentredString(290, 720, "Solar System Planets")

#     pdf.line(30, 710, 550, 710)

#     # Define the maximum width and margin
#     max_width = 500
#     margin = 40
#     text = pdf.beginText(margin, 680)
#     text.setFont("Courier", 18)
#     text.setFillColor(colors.black)

#     # Wrap text to fit within the specified width
#     wrapped_text = textwrap.fill(string, width=60)  # Adjust width as needed

#     # Add each line of wrapped text to the PDF
#     for line in wrapped_text.split('\n'):
#         text.textLine(line)

#     pdf.drawText(text)
#     pdf.showPage()
#     pdf.save()

#     return response

# ----------------------------------------------------------------------------------------------------------------

import os
from django.shortcuts import render
from django.http import HttpResponse
from huggingface_hub import InferenceClient
from reportlab.pdfgen import canvas
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def home(request):
    return render(request, 'home.html')

def process_question(request):
    if request.method == 'POST':
        question = request.POST['question']

        # Use Hugging Face InferenceClient to get the API response
        client = InferenceClient(api_key=ASTON_CASHLATINO)
        api_response = ""

        for message in client.chat_completion(
            model="mistralai/Mistral-7B-Instruct-v0.3",
            messages=[{"role": "user", "content": question}],
            max_tokens=500,
            stream=True,
        ):
            api_response += message.choices[0].delta.content

        return render(request, 'home.html', {'api_response': api_response})
    
    return render(request, 'home.html')

def download_pdf(request):
    if request.method == 'POST':
        api_response = request.POST.get('api_response', '')

        # Generate the PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter  # Set the page size

        # Set the title
        p.setFont("Helvetica-Bold", 16)
        p.drawString(100, height - 50, "API Response:")

        # Set a normal font for the response text
        p.setFont("Helvetica", 12)

        # Set a starting position for the text
        text_y = height - 80  # Starting Y position for text

        # Define a function to wrap text
        def draw_wrapped_text(x, y, text, max_width):
            # Split the text into words
            words = text.split(' ')
            line = ''
            for word in words:
                # Check if adding the next word exceeds the max width
                test_line = f"{line} {word}".strip()
                text_width = p.stringWidth(test_line, "Helvetica", 12)

                if text_width < max_width:
                    line = test_line  # Add the word to the current line
                else:
                    # Draw the current line and start a new line
                    p.drawString(x, y, line)
                    y -= 14  # Move down for the next line
                    line = word  # Start a new line with the current word

            # Draw any remaining text in the last line
            if line:
                p.drawString(x, y, line)

        # Draw the wrapped text with a maximum width of 450 (adjust as needed)
        draw_wrapped_text(100, text_y, api_response, 450)

        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and return as a response
        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')

    return render(request, 'home.html')


