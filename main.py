from dotenv import load_dotenv
import os 
import sys
load_dotenv()
from google import genai
from google.genai import types



def main():
    api_key=os.environ.get("GEMINI_API_KEY")
    client=genai.Client(api_key=api_key)
    if len(sys.argv)>1:
        x=sys.argv[1]
    else:
        raise Exception("Error")
        print("error")
        sys.exit(1)
    messages=[
        types.Content(role="user",parts=[types.Part(text=x)])
    ]

    response=client.models._generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    if "--verbose" in sys.argv:
        print(f"User prompt: {x}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)

    else: 
        print(response.text)

if __name__ == "__main__":
    main()
