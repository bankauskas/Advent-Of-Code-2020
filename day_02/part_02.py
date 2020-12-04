import re

validPasswords = []

with open("input.txt") as f:
    for line in f:
        lowerBound = int(re.findall(r"^\d*",line)[0])
        uperBound = int(re.findall(r"\-(\d*)\s",line)[0])
        letter = re.findall(r"\s(\w*)\:",line)[0]
        pasword = re.findall(r"\s(\w*)$",line)[0]

        if  (pasword[lowerBound-1] == letter and pasword[uperBound-1] != letter) or (pasword[lowerBound-1] != letter and pasword[uperBound-1] == letter): 
            validPasswords.append((lowerBound, uperBound, letter, pasword))


if __name__ == '__main__':
    print(len(validPasswords))
