#example keyAlphabet for quick testing: FGLMNOPHIAJXYZKQRSBCDETWVU
#basic uppercase latin alphabet for later referrence
latinAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

isDone = False

keyAlphabet = ''

#check that every letter is unambiuously reasigned
#if not let user input a new key and check again
def checkUnambiguous(key):
    isUnambiguous = False
    print('Please enter key alphabet')
    while isUnambiguous == False:
        key = input().upper()
        for letter in latinAlphabet:
            if letter not in key.upper() or len(key) != len(latinAlphabet):
                print("Alphabet not unambiguously encoded, please enter new encoding Alphabet")
                break
            if "Z" in key.upper():
                isUnambiguous = True
    return key

#encode an inputed message using the key
def encodeMonoAlphabetic(message, key):
    encodedMsg = ''

    for letter in message.upper():
        #append the n th letter (corresponding to the n th letter of the latin script) of the key alphabet to the encoded message
        if letter in latinAlphabet:
            encodedMsg += key[latinAlphabet.find(letter)].upper()
        else:
            encodedMsg += letter.upper()

    return(encodedMsg)

#execute ecodeMonoAlphabetic in reverse
def decodeMonoAlphabetic(message):
    global latinAlphabet
    decodedMsg = ''

    for letter in message.upper():
        if letter in latinAlphabet:
            decodedMsg += latinAlphabet[keyAlphabet.find(letter)]
        else:
            decodedMsg += letter.upper()

    return(decodedMsg)

#Select wheter you wish to quit, encode, decode,...
def selectMode():
    global keyAlphabet
    #this is really awkward, must change so that selectionOptions can be created automatically instead of by hand (as that is awkward and prone to human error)
    slectionOptions = ['0', '1', '2', '3']
    print("Please select what you wish to do by entering one of the following numbers")
    print("0: Quit programm")
    print("1: encode monoalphabetically")
    print("2: decode monoalphabetically")
    print("3: enter new key alphabet")
    selection = input()

    #check that the selection is a possible option
    if selection not in slectionOptions:
        print("Please make a valid selection")
        return False

    if selection == '0':
        return True

    #if 1 do encodeMonoAlphabetic
    if selection == '1':
        print('Please enter Text to encode')
        originalMsg = input()
        print(encodeMonoAlphabetic(originalMsg, keyAlphabet))
        return False
    
    #if 2 do decodeMonoAlphabetic
    if selection == '2':
        print('Please enter Text to decode')
        recievedMsg = input()
        print(decodeMonoAlphabetic(recievedMsg))
        return False

    if selection == '3':
        keyAlphabet = checkUnambiguous(keyAlphabet)
        return False


keyAlphabet = checkUnambiguous(keyAlphabet)
while isDone == False:
    isDone = selectMode()
