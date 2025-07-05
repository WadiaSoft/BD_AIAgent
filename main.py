import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


api_key = os.environ.get("GEMINI_API_KEY")


def main():
    #print("Hello from aiagent!")

    verbose = False
    if len(sys.argv) == 1:
        #sys.argv[0] is the program name
        sys.exit(1)

    # len(sys.argv) is >= 2
    user_prompt = sys.argv[1]

#    print(sys.argv)

    if len(sys.argv) >= 3:
        if sys.argv[2] == "--verbose":
            verbose = True

#    print(verbose)
    
#    return

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    model = "gemini-2.0-flash-001"

    response = client.models.generate_content(model=model, contents=messages)

    print(response.text)
    if verbose:
         print(f"User prompt: {user_prompt}")
         print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
         print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
