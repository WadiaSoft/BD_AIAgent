import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.get_files_info import schema_get_files_info

api_key = os.environ.get("GEMINI_API_KEY")


def main():
    #print("Hello from aiagent!")
    system_prompt = "I'M JUST A ROBOT"

    system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

    #print(system_prompt)
    #xit(0)

    #print(len(sys.argv))
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

    available_functions = types.Tool(function_declarations=[schema_get_files_info,])


    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    model = "gemini-2.0-flash-001"

    response = client.models.generate_content(model=model, 
                                              contents=messages, 
                                              config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),)

    print(response.text)
    if verbose:
         print(f"User prompt: {user_prompt}")
         print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
         print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    function_call_part = None

    for part in response.candidates[0].content.parts:
        if hasattr(part, "function_call"):
            function_call_part = part.function_call
            break

    #if function_call_part:
    #    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    #else:
    #    print("No function call returned.")

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")

if __name__ == "__main__":
    main()
