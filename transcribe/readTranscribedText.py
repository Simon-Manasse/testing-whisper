def readInPrompt():
    with open('prompt.txt') as f:
        lines = f.readlines()
        return lines[0]
    