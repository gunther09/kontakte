def create_openai_message(email_footer):
    return f"""
    Extrahiere die folgenden Kontaktdaten aus dem folgenden E-Mail Footer:
    
    {email_footer}
    
    Format:
    Name: 
    Phone: 
    Mobile: 
    Email: 
    Company: 
    Job Title: 
    Country: 
    """
