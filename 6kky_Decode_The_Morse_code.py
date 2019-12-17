MORSE_CODE = []
def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

decodeMorse('.... . -.--   .--- ..- -.. .')
#'HEY JUDE'