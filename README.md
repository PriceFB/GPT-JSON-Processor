# GPT-JSON-Processor

**Developed by:** Jonathan Leyva (also known as Price)  
**Originally Developed on:** 11/11/2024  

## Description

**GPT-JSON-Processor** is a Python script designed to interface with OpenAI's API. It automates the workflow of sending JSON inputs to an OpenAI model, processing the responses, and outputting structured JSON data. This tool is ideal for developers seeking to integrate GPT models into their pipelines with ease and scalability.

---

## Features

- Create and manage OpenAI assistants, threads, and tasks.
- Seamlessly handle JSON input files and generate JSON outputs.
- Specify and manage prompts to customize OpenAI responses.
- Organized output storage for downstream use.

---

## Prerequisites

### OpenAI Account Setup  
OpenAI's API is a **paid service**. You must complete the following steps to use this script:

1. **Create an OpenAI Account**:  
   Sign up at [OpenAI's Signup Page](https://platform.openai.com/signup/).

2. **Create a Project and Generate an API Key**:  
   - Visit the [API Keys Management Page](https://platform.openai.com/account/api-keys).  
   - Create a new secret API key and store it securely.

3. **Deposit Credits**:  
   - You must deposit at least **$5** to activate your OpenAI API usage.  
   - Visit the [Billing and Payment Page](https://platform.openai.com/account/billing/overview) to add credits.

4. **Review OpenAI Models**:  
   - For a complete list of OpenAI models and their capabilities, visit the [Model Overview](https://platform.openai.com/docs/models/overview).  
   - This script uses the `gpt-3.5-turbo` model by default, but you can customize this as needed.

---

## Dependencies

Before running this script, ensure you have the required Python packages installed. 

### Required Python Packages:
1. **openai**  
   - For interacting with OpenAI's API.
2. **python-dotenv**  
   - To securely load environment variables from a `.env` file.

Use the following command to install them:

```bash
pip install openai
```

```bash
pip install python-dotenv
```

### Additional Requirements:
- **Python 3.13+**  
  This script requires Python 3.13.0 or higher.

---

## Installation and Usage

### Clone the Repository:
Clone this repository to your local machine:

```bash
git clone https://github.com/PriceFB/GPT-JSON-Processor.git
```

## Set Up Environment Variables

Create a `.env` file in the project root and add your OpenAI API credentials:

```makefile
OPENAI_API_KEY=your_api_key_here
ORG_ID=your_organization_id_here
PROJ_ID=your_project_id_here
```

## Prepare Your Input JSON

Place the JSON file you wish to process in the input/ directory, named input.json.

# Run the Script

Execute the script using:

```bash
python main.py
```

## View Output
Processed JSON output will be stored in the output/ directory, named output.json.

## Example Input and Output
Input: input/input.json
```json
{
    "task": "Summarize this text",
    "content": "OpenAI is a leading AI research lab focusing on developing friendly AI."
}
```
Output: output/output.json
```json
{
    "response": "OpenAI is an AI research lab focused on friendly AI development."
}
```
## Debugging

FileNotFoundError: Ensure input/input.json exists and is properly formatted.

Invalid JSON: Double-check your JSON input file for syntax errors.

API Key Issues: Verify that your API key and .env file are correctly set up.

## Notes
By using this script, you agree to retain attribution to the original developer in any modified or redistributed versions.
This script is provided as free and open-source software. See the LICENSE file for more details.
