morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def morse_to_text(morse):
    text = ''
    morse_words = morse.split('/')
    for morse_word in morse_words:
        morse_chars = morse_word.split(' ')
        for morse_char in morse_chars:
            for key, value in morse_code.items():
                if value == morse_char:
                    text += key
                    break
        text += ' '
    return text.strip()

choice = input("Enter '1' to convert text to Morse code or '2' to convert Morse code to text: ")
if choice == '1':
    text = input("Enter the text to convert to Morse code: ")
    morse = text_to_morse(text)
    print(f"Morse code: {morse}")
elif choice == '2':
    morse = input("Enter the Morse code to convert to text: ")
    text = morse_to_text(morse)
    print(f"Text: {text}")
else:
    print("Invalid choice.")
