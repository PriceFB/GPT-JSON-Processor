"""
Developed by: Jonathan Leyva (also known as Price)
Originally developed on 11/11/2024.

Description:
This script is designed to interact with the OpenAI API, enabling the creation and management of assistants, threads, and tasks. 
It facilitates processing of JSON input files and generates responses based on specified requirements. The output is stored in an
organized manner for easy accessibility.

License:
This script is provided as free and open-source software. You are free to use, modify, and distribute this script, provided that 
credit is given to the original developer, Jonathan Leyva (Price).

Note:
By using this script, you agree to retain the attribution to the original developer in any modified or redistributed versions.
"""

import json
import os
from openai import OpenAI
from time import sleep
from dotenv import load_dotenv

os.getcwd

load_dotenv()
    
# Edit your .env to spcify an api key, org id, and proj id. 
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    organization=os.environ.get("ORG_ID"),
    project=os.environ.get("PROJ_ID"),
    )

starting_assistant = ""
starting_thread = ""

# Customize your OpenAI assistant
def create_assistant():
    if starting_assistant == "":
        my_assistant = client.beta.assistants.create(
            instructions="print hello world.", # specify what you would like your assistant to do with the input.json file.
            name="assistant", # name your assistant
            model="gpt-3.5-turbo", # specify the GPT model you'd like your assistant to use 
            tools=[{"type": "code_interpreter"}, {"type": "file_search"}]
        )
    else:
        my_assistant = client.beta.assistants.retrieve(starting_assistant)

    return my_assistant


def create_thread():
    if starting_thread == "":
        thread = client.beta.threads.create()
    else:
        thread = client.beta.threads.retrieve(starting_thread)

    return thread


def send_message(thread_id, message):
    thread_message = client.beta.threads.messages.create(
        thread_id,
        role="user",
        content=message,
    )
    return thread_message


def run_assistant(thread_id, assistant_id):
    run = client.beta.threads.runs.create(
        thread_id=thread_id, assistant_id=assistant_id
    )
    return run


def get_newest_message(thread_id):
    thread_messages = client.beta.threads.messages.list(thread_id)
    return thread_messages.data[0]


def get_run_status(thread_id, run_id):
    run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)
    return run.status

def main():
    my_assistant = create_assistant()
    my_thread = create_thread()

    # Read flow data from a JSON file
    try:
        with open('input/input.json', 'r') as file:
            # Load the JSON file content
            input_data = json.load(file)
            # Debug: Print the JSON content
            print("Debug: Loaded JSON data:")
            print(json.dumps(input_data, indent=4))  # Pretty-print the JSON data
            # Convert the JSON data into a string format suitable for the assistant
            user_input_data = json.dumps(input_data, indent=2)
    except FileNotFoundError:
        print("Error: JSON file not found. Please make sure 'flow_data.json' exists in the repository.")
        print(os.getcwd())
        return
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file. Ensure the file contains valid JSON.")
        return

        # Example prompt
    prompt = f"""
create a prompt that specifies what you want to do with:

Input: {user_input_data}

Specify Requirements.
Specify what it your assistant should not do.
"""
    print("Debug: Prompt sent to assistant:")
    print(prompt)

    # Send the prompt to the assistant
    send_message(my_thread.id, prompt)

    # Run the assistant and wait for completion
    run = run_assistant(my_thread.id, my_assistant.id)
    while run.status != "completed":
        run.status = get_run_status(my_thread.id, run.id)
        sleep(1)
        print("⏳", end="\r", flush=True)

    sleep(0.5)

    # Initialize response variable
    response = None

    try:
        response = get_newest_message(my_thread.id)
        print("Debug: Raw response content:")
        print(response)

        # Extract the value from the response content
        if response and hasattr(response, 'content') and response.content:
            # Access the `value` attribute of the `Text` object
            gpt_response = response.content[0].text.value.strip()
            print("Response:", gpt_response)

            # Save the response to a JSON file
            output_data = {"response": gpt_response}
            output_folder = "output"
            os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
            output_file_path = os.path.join(output_folder, "output.json")

            with open(output_file_path, "w") as output_file:
                json.dump(output_data, output_file, indent=4)

            print(f"Response saved to {output_file_path}")
        else:
            print("Error: Response content is empty or invalid.")
    except AttributeError as e:
        print("Error: Unable to extract response text. Debugging content:")
        if response:
            print("Response Content Debug:", vars(response))
        else:
            print("Response is None.")
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()