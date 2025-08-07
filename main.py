import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    MAX_ITERATIONS = 21
    
    for i in range(MAX_ITERATIONS):
        try:
            if verbose:
                print(f"\n--- Iteration {i+1} ---")
            
            # 1. Call generate_content with the entire messages list
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                ),
            )
            
            # 2. Append all response candidates to the message list
            for candidate in response.candidates:
                if candidate.content:
                    messages.append(candidate.content)
                    if verbose:
                        print("-> Appended model response to messages.")
            
            # 3. Check for final answer (response.text exists)
            if response.text:
                if verbose:
                    print("Final response:", response.text)
                return response.text
            
            # 4. Handle function calls if they exist
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_result = call_function(function_call_part, verbose)
                    
                    if (
                        not function_result.parts
                        or not function_result.parts[0].function_response
                    ):
                        raise Exception("Empty function call result")
                    
                    if verbose:
                        print(f"-> Function response: {function_result.parts[0].function_response.response}")
                    
                    # Convert function result to tool content and append to messages
                    tool_content = types.Content(
                        role="tool",
                        parts=[function_result.parts[0]]
                    )
                    messages.append(tool_content)
            
            else:
                # If no response text and no function calls, something is wrong
                if verbose:
                    print("-> No response text or function calls found.")
                raise Exception("No response text or function calls — exiting.")
        
        except Exception as e:
            if verbose:
                print(f"-> Error in iteration {i+1}: {str(e)}")
            # You might want to handle specific exceptions differently
            # For now, we'll re-raise to stop execution
            raise e
    
    # If we've reached max iterations without a final response
    raise Exception("Max iterations reached without final response.")


if __name__ == "__main__":
    main()
