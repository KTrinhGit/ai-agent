import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types 
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python
from functions.write_file import schema_write_file

def call_function(function_call_part, verbose=False):
    s

def main():
    if len(sys.argv) < 2: 
        print("No prompt provided")
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
    ]
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python, 
        schema_write_file
    ])

    response = client.models.generate_content(model='gemini-2.0-flash-001', 
                                              contents=messages,
                                              config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
                                              )
    response_functions = response.function_calls

    if len(response_functions) != 0: 
        print(f"Calling function: {response_functions[0].name}({response_functions[0].args})") 
    else: 
        print(response.text)



    if len(sys.argv) == 3 and sys.argv[2] == '--verbose': 
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        print(f"User prompt: {sys.argv[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
