# GPT-3 Federal Health Cooperative Agreement Performance Measure Analysis

The provided Jupyter Notebook contains a script to analyze performance measure data through OpenAI's GPT-3 API. The code is segmented into cells which aim to:

Set up and authenticate the OpenAI API<br>
Define GPT-3 setup<br>
Provide examples of utilizing GPT-3 to derive themes from customer feedback<br>
Handle and analyze an Excel file containing further feedback<br>

### Prerequisites

Ensure you have the following Python libraries:

openai<br>
openpyxl<br>
pandas<br>

For formatting inputs and outputs so that the model can effectively pattern-match, ensure you have the following cloned to your repository: Shreya Shankar GPT-3 Sandbox (https://github.com/shreyashankar/gpt3-sandbox/)

API Key
For interacting with GPT-3, you need to have an API key from OpenAI. Ensure to replace the provided API key with your own valid key for any real usage.

Warning!!
The notebook contains sensitive information (API Key).  Store and handle this information securely using environment variables or secure vaults especially when sharing or publishing your code.<br>
API Requests: Ensure to keep track of API usage to avoid unexpected charges as GPT-3 is a paid API.<br>
Data Privacy: Ensure that all data handled by the notebook adheres to relevant data protection regulations.

### Usage

How to use this notebook:<br>
Setting up the API: Ensure to replace the API Key (openai.api_key) with your own. You can create your own by creating an account with OpenAI and requesting your api key. 

Proof of Concept: <br>
The notebook contains proof of concepts where sanitized performance measure data is sent to the GPT-3 API to derive themes and analyze text. You can use these as a template for your own analysis.

File Analysis: <br>
Towards the end of the notebook, there's code for handling feedback from an Excel file. Ensure that the Excel file is in the correct path and the column names match those specified in the code.

## Authors

* **Gillian Schriever** - [gschriever](https://github.com/gschriever)
* Contact: gillianschriever@pitt.edu

