from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import sys

# Pfad zur .env-Datei angeben und laden
env_path = os.path.join(os.path.dirname(__file__), '.env')
print(f"DEBUG: Looking for .env file at {env_path}")  # Debugging-Ausgabe

if not os.path.exists(env_path):
    print(f"Error: .env file not found at {env_path}")
    sys.exit(1)

load_dotenv(env_path)

# Überprüfen, ob die Umgebungsvariable gesetzt ist
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    sys.exit(1)

print(f"DEBUG: OPENAI_API_KEY is set to: {api_key}")

from kontakt_to_openai import extract_contact_info

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    email_footer = request.form['email_footer']
    contact_info = extract_contact_info(email_footer)
    # Übergabe der Daten an die Vorlage
    return render_template('result_table.html', **contact_info)

if __name__ == '__main__':
    app.run(debug=True)
