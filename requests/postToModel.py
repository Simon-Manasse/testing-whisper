import json
import requests

def sendPrompt(model,prompt):
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

