import string
import argparse

all_words = {}

class Possibility:
    def __init__(self, phrase, count):
        self.phrase = phrase
        self.count = count

    def __str__(self):
        return f"Probable phrase: '{self.phrase}' ({self.count} out of {len(self.phrase.split(' '))} words found in the dictionnary)"

    def __lt__(self, other):
        return self.count > other.count

def getAllCaesarPossibilities(phrase):
    alphabet = string.ascii_lowercase * 2
    list = []

    for i in range(0, 26):
        decoded = ''
        for letter in phrase:
            if letter.lower() in alphabet:
                if letter.isupper():
                    decoded += alphabet[alphabet.index(letter.lower()) + i].upper()
                else:
                    decoded += alphabet[alphabet.index(letter.lower()) + i]
            else:
                decoded += letter

        count = 0
        for word in decoded.split(' '):
            if word.lower() in all_words:
                count += 1

        list.append(Possibility(decoded, count))

    return list

def uncipher(phrase, all):

    res = getAllCaesarPossibilities(phrase)

    res.sort()

    for r in res if all else filter(lambda x: x.count >= res[0].count, res):
        print(r)

parser = argparse.ArgumentParser(description='Uncipher a Caesar encoded string')
parser.add_argument('input', metavar='CAESAR STRING', type=str, help='the phrase to uncipher')
parser.add_argument('--dict', default='dico_fr_full.txt', nargs='?', metavar='path/to/dictionnary', help='If you want to use a custom dictionnary. Default one is french')
parser.add_argument('--all', action='store_true', help='If you want the program to print all uncyphered phrase instead of only the most probable ones')

args = parser.parse_args()

all_words = [x[:-1] for x in open(args.dict, 'r').readlines()]
uncipher(args.input, args.all)
