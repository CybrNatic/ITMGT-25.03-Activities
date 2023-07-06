'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer. 
    if letter == " ": # If the input is a blank space.
        return " "
    else:
        offset = ord("A") # ASCII offset for the letter A (65).
        num_alphabet_letters = 26 # Number of letters in the alphabet.
        shifted_ascii = (ord(letter) - offset + shift) % num_alphabet_letters # ASCII value for the shifted letter, factoring in shifts greater than 26.
        shifted_letter = chr(shifted_ascii + offset) # The shifted letter.
        
        return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shifted_string = "" # Initializing the string to append the letters to.
    
    for letter in message:
        if letter == " ": # If the input is a blank space.
            shifted_string += letter # Appends the blank to the shifted string.
        else:
            offset = ord("A") # ASCII offset for the letter A (65).
            num_alphabet_letters = 26 # Number of letters in the alphabet.
            shifted_ascii = (ord(letter) - offset + shift) % num_alphabet_letters # ASCII value for the shifted letter, factoring in shifts greater than 26.
            shifted_letter = chr(shifted_ascii + offset) # The shifted letter.
            shifted_string += shifted_letter # Appends the shifted letter to the shifted string.
            
    return shifted_string

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ": # If the input is a blank space.
        return " "
    else:
        offset = ord("A") # ASCII offset for the letter A (65).
        shift = ord(letter_shift) - offset # The ASCII value for the shift.
        shifted_ascii = (ord(letter) - offset + shift) % 26 + 65 # ASCII value for the shifted letter, converts the letter shift into ASCII and subtracts the offset for A.
        shifted_letter = chr(shifted_ascii) # The shifted letter.
        
        return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    key_extended = key * (len(message) // len(key)) + key[:len(message) % len(key)] # Creates the extended key for the cipher by multiplying the key string to the floor function of the message length and key length, then adding the remaining key length if the message length is not an exact multiple of the key length by getting the remainder of the message length and key length.
    vigenere_message = "" # Initializing the string
    
    for i in range(len(message)):
        if message[i] == " ": # A case if the space is blank.
            vigenere_message += " " # Appends a space if blank.
        else:
            offset = ord("A") # ASCII offset for the letter A (65).
            shift = ord(key_extended[i]) - offset # The ASCII value for the shift.
            shifted_ascii = (ord(message[i]) - offset + shift) % 26 + 65 # ASCII value for the shifted letter in the message, converts the letter shift from the key into ASCII and subtracts the offset for A.
            shifted_letter = chr(shifted_ascii) # The shifted letter.
            vigenere_message += shifted_letter # Appends the shifted letter to the string.
            
    return vigenere_message

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    scytale_message = "" # Initializes the scytale string.
    message_length = len(message) # Gets the length of the message to use in checking if the message's length is a multiple of the shift.
    if message_length % shift != 0: # Checks if the message's length is a multiple of the shift by using the modulo operator.
        message += "_" * (shift - (message_length % shift)) # Adds "_" until the message's length is a multiple of the shift.
        
    for i in range(len(message)):
        scytale_index = (i % shift) * (len(message) // shift) + (i // shift)
        scytale_message += message[scytale_index]
        
    return scytale_message

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    deciphered_scytale_message = "" # Initializing the deciphered scytale message.
    message_length = len(message) # Gets the length of the message for the loop range using the amount of characters.
    while message_length % shift != 0:
        deciphered_scytale_message += "_"
        message_length += 1
    for i in range(len(message)):
        scytale_index = (i % (message_length // shift)) * shift + (i // (message_length // shift)) # Reverses the scytale cipher.
        deciphered_scytale_message += message[scytale_index] # Appends a deciphered character from the scytale message to the deciphered message.
        
    return deciphered_scytale_message