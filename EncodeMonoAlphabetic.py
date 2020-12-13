#example keyAlphabet for quick testing: FGLMNOPHIAJXYZKQRSBCDETWVU
#basic uppercase latin alphabet for later referrence
latinAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

isInProgress = True

keyAlphabet = ''

#check that every letter is unambiuously reasigned
#if not let user input a new key and check again
def checkUnambiguous():
    print('Please enter key alphabet')
    while True:
        isUnambiguous = True
        key = input().upper()
        if len(key) != len(latinAlphabet):
            isUnambiguous = False
        for letter in latinAlphabet:
            if letter not in key:
                isUnambiguous = False

        if isUnambiguous == False:
            print("Alphabet not unambiguously encoded, please enter new encoding Alphabet")
        else:
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

    selection = input('\nPlease select what you wish to do by entering one of the following numbers\n0: Quit programm\n1: encode monoalphabetically\n2: decode monoalphabetically\n3: enter new key alphabet\n')

    if selection == '0':
        return False

    #if 1 do encodeMonoAlphabetic
    elif selection == '1':
        print('\nPlease enter Text to encode')
        originalMsg = input()
        print('\n',encodeMonoAlphabetic(originalMsg, keyAlphabet),)
        return True

    #if 2 do decodeMonoAlphabetic
    elif selection == '2':
        print('\nPlease enter Text to decode')
        recievedMsg = input()
        print('\n',decodeMonoAlphabetic(recievedMsg))
        return True

    elif selection == '3':
        print('\n')
        keyAlphabet = checkUnambiguous()
        return True
    
    else:
        print("\nPlease make a valid selection")
        return True


keyAlphabet = checkUnambiguous()
while isInProgress == True:
    isInProgress = selectMode()
