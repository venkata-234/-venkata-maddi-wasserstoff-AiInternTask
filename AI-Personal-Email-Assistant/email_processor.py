import openai

def generate_reply(email_content):
    prompt = f"Please summarize and draft a reply to the following email: {email_content}"
    response = openai.Completion.create(
        engine="gpt-4",  
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
