from google import genai
import json

# Create client
client = genai.Client(api_key="AIzaSyB05YGW8YVhIG6QsghBa7Ug6o1GehTgjsM")

def extract_controls(text):
    prompt = f"""
    Extract security controls from the text.

    Return ONLY valid JSON:
    [
      {{
        "description": "",
        "category": ""
      }}
    ]

    Categories:
    Access Control, Authentication, Monitoring, Data Protection

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    output = response.text.strip()

    # 🔥 Clean JSON (important)
    if "```" in output:
        output = output.split("```")[1]
        if output.startswith("json"):
            output = output[4:]

    try:
        return json.loads(output)
    except:
        print("⚠️ JSON Error. Raw output:")
        print(output)
        return []