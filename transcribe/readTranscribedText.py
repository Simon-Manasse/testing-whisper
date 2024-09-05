def readInPrompt():
    """
    Reads the first line from the file 'prompt.txt'.

    This function opens the file 'prompt.txt', reads all lines, and returns the first line 
    as a string. It assumes that the file exists and contains at least one line.

    Returns:
        str: The first line of the file 'prompt.txt'.
    
    Raises:
        FileNotFoundError: If 'prompt.txt' does not exist.
        IndexError: If 'prompt.txt' is empty and does not contain any lines.
    """
    
    # Open the file 'prompt.txt' for reading
    with open('prompt.txt') as f:
        # Read all lines from the file
        lines = f.readlines()
        # Return the first line from the file
        return lines[0]
