import sys
import os

MORSE_DICT = {'/': ' ', '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
              '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
              '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
              '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
              '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '--..--': ', ', '.-.-.-': '.',
              '..--..': '?', '-..-.': '/', '-....-': '-', '-.--.': '(', '-.--.-': ')'}
FILE_PATH = sys.argv[1]

def connect(lst):
    s = ''
    for i in lst:
        s+=i
    return s
def main():
    with open(os.getcwd() + FILE_PATH, 'r') as f:
        l = f.read().replace('\n', '').split(' ')
    txt = ''
    hist_letters = ['' for x in l]
    try:
        for i in l:
            letter = MORSE_DICT[i]
            txt += letter
            if letter == ' ':
                continue
            not_in_list = True
            for j in range(len(hist_letters)):
                if letter in hist_letters[j]:
                    not_in_list = False
                    hist_letters[j] = hist_letters[j].replace(letter, '')
                    hist_letters[j + 1] += letter
                    break
            if not_in_list:
                hist_letters[1] += letter

    except:
        print('Error in Morse Code')
    else:
        print(txt)
        for i in range(len(hist_letters))[::-1]:
            if hist_letters[i] != '':
                print(connect(sorted(hist_letters[i])), '-', i)


if __name__ == '__main__':
    main()
