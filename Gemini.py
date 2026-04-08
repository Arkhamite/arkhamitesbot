from google import genai


client = genai.Client(api_key='')

def gemini(prompt):
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite-preview", contents=prompt
    )
    return response.text

if __name__ == "__main__":
    print(gemini("gimme one fun history fact, like in one sentence"))
