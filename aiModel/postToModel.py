import json
import requests

def sendPrompt(model,prompt):
    """
    Sends a prompt to a model and prints the generated response.

    This function sends a POST request to a local API endpoint with the specified model and prompt.
    It handles the response text, which is received in multiple lines, splits the text by new lines,
    parses each line as JSON (except the last line), and combines the responses into a single string.

    The function performs the following steps:
    1. Sets the URL of the model API endpoint.
    2. Configures the request parameters with the model and prompt.
    3. Sends a POST request to the API.
    4. Receives and processes the raw response text.
    5. Splits the response text by new lines, excluding the last line.
    6. Parses each line (except the last) as JSON and collects the responses.
    7. Combines all responses into a single string.
    8. Prints the model being used, the prompt sent, and the combined response.

    Args:
        model (str): The model identifier to use for the API request.
        prompt (str): The prompt text to send to the model.

    Returns:
        None

    Raises:
        requests.RequestException: If there is an issue with the HTTP request.
        json.JSONDecodeError: If a line in the response cannot be parsed as JSON.
    """
    
    # Setting the url of the models
    URL = "http://localhost:10001/api/generate"
    # Setting the parameters
    PARAMS = {
        "model":model,
        "prompt":prompt
        }
    # Making the request to the model
    r = requests.post(url=URL, json=PARAMS)

    # Receiving the raw text, there is no json response in the body
    # So we will have to deal with it
    text = r.text

    # We are splitting the text by every new line
    splitTextByNewLines= text.split('\n')

    # We get all the responses but the last one
    # That's because it just tells the model to stop generating
    # We convert them into actual json so we can work with them
    # Then we append all of the lines into an array
    arrayOfText = []
    for line in splitTextByNewLines[0:-1]:
        jsonResponse=json.loads(line)
        arrayOfText.append(jsonResponse)

    # We just put the text together
    # so it's more readable :3
    fullText=""
    for line in arrayOfText:
        fullText+=line["response"]
        
    print(f'The model being used was: {model}\nThe prompt that was created: {prompt}\nResponse:\n\n{fullText}')
    pass

