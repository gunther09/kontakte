# Kontakte

Kleine Flask-App: Fügt man eine E-Mail-Signatur ein, extrahiert OpenAI (gpt-4o) daraus Name, Telefon, Mobil, E-Mail, Firma, Position und Land.

## Start

```bash
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
python kontakte.py   # http://localhost:5000
```

## Dateien

- `kontakte.py` – Flask-App (`/` Formular, `/extract` Ergebnis)
- `kontakt_to_openai.py` – OpenAI-Aufruf und Parsing
- `openai_kontakt_message.py` – Prompt
- `templates/` – HTML-Vorlagen
