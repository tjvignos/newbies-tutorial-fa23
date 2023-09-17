import os
import base64

ALPHA_MAP = {'a': '█▀▀█ \n█▄▄█ \n▀──▀ ', 'b': '█▀▀▄ \n█▀▀▄ \n▀▀▀─ ', 'c': '█▀▀ \n█── \n▀▀▀ ', 'd': '█▀▀▄ \n█──█ \n▀▀▀─ ', 'e': '█▀▀ \n█▀▀ \n▀▀▀ ', 'f': '█▀▀ \n█▀▀ \n▀── ', 'g': '█▀▀▀ \n█─▀█ \n▀▀▀▀ ', 'h': '█──█ \n█▀▀█ \n▀──▀ ', 'i': '─▀─ \n▀█▀ \n▀▀▀ ', 'j': '──▀ \n──█ \n█▄█ ', 'k': '█─█ \n█▀▄ \n▀─▀ ', 'l': '█── \n█── \n▀▀▀ ', 'm': '█▀▄▀█ \n█─▀─█ \n▀───▀ ', 'n': '█▀▀▄ \n█──█ \n▀──▀ ', 'o': '█▀▀█ \n█──█ \n▀▀▀▀ ', 'p': '█▀▀█ \n█──█ \n█▀▀▀ ', 'q': '█▀▀█ \n█──█ \n▀▀▀█ ', 'r': '█▀▀█ \n█▄▄▀ \n▀─▀▀ ', 's': '█▀▀ \n▀▀█ \n▀▀▀ ', 't': '▀▀█▀▀ \n──█── \n──▀── ', 'u': '█──█ \n█──█ \n─▀▀▀ ', 'v': '▀█─█▀ \n─█▄█─ \n──▀── ', 'w': '█───█ \n█▄█▄█ \n─▀─▀─ ', 'x': '█─█ \n▄▀▄ \n▀─▀ ', 'y': '█──█ \n█▄▄█ \n▄▄▄█ ', 'z': '▀▀█ \n▄▀─ \n▀▀▀ ', ',': '── \n▄▄ \n─█ ', ' ': '   \n   \n   ', '@': '▀ ▄ ▀\n▄   ▄\n ▀▀▀ '} #'▄ ▀▄ \n─ ─█ \n▀ ▄▀', 
PW = b'RkEyMw=='

def b64_to_s(input):
    return str(base64.b64decode(input),encoding='utf-8')

if input("Password: ").upper() != b64_to_s(PW):
    print("Incorrect password :(")
else:
    found = False
    for filename in filter(os.path.isfile, os.listdir( os.curdir ) ):
        if ".txt" in filename:
            found = True
            print()
            with open(filename, "r") as file:
                name = filename[:filename.find(".")]
                if not name.isalpha():
                    print(f"Oops! Your file {filename} has special characters, please use a-z only.")
                else:
                    name = name + " @" # @ is smile
                    input = [b64_to_s(b'V0VMQ09NRQ=='), b64_to_s(b'VE8gQVBQREVW'), name]
                    for word in input:
                        output = ["","",""]
                        for letter in word:
                            t, m, b = ALPHA_MAP[letter.lower()].split("\n")
                            output[0] += t
                            output[1] += m
                            output[2] += b
                        for line in output:
                            print(line)
                        print()
            break
    if not found:
        print("Couldn't find a text file with your name, e.g. noah.txt")



