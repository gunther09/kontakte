import openai
import os

# Initialisieren des OpenAI-Clients mit Überprüfung
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("The OPENAI_API_KEY environment variable is not set. Please set it in your .env file.")

print(f"DEBUG: Initializing OpenAI client with API key: {api_key}")

client = openai.OpenAI(api_key=api_key)

from openai_kontakt_message import create_openai_message

def extract_contact_info(email_footer):
    message = create_openai_message(email_footer)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    )
    
    response_content = response.choices[0].message.content.strip()
    
    # Split the response content into lines and parse the contact info
    lines = response_content.split('\n')
    contact_info = {
        "name": "",
        "phone": "",
        "mobile": "",
        "email": "",
        "company": "",
        "job_title": "",
        "country": ""
    }
    
    for line in lines:
        if line.startswith("Name:"):
            contact_info["name"] = line.split(":", 1)[1].strip()
        elif line.startswith("Phone:"):
            contact_info["phone"] = line.split(":", 1)[1].strip()
        elif line.startswith("Mobile:"):
            contact_info["mobile"] = line.split(":", 1)[1].strip()
        elif line.startswith("Email:"):
            contact_info["email"] = line.split(":", 1)[1].strip()
        elif line.startswith("Company:"):
            contact_info["company"] = line.split(":", 1)[1].strip()
        elif line.startswith("Job Title:"):
            contact_info["job_title"] = line.split(":", 1)[1].strip()
        elif line.startswith("Country:"):
            contact_info["country"] = line.split(":", 1)[1].strip()
    
    return contact_info
