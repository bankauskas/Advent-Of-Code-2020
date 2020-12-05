import re

pattern = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')
validPasswords = []

with open("day_02/input.txt") as f:
    for line in f:

        lowerBound, uperBound, letter, password = pattern.match(line).groups()
        if  (password[int(lowerBound)-1] == letter and password[int(uperBound)-1] != letter) or (password[int(lowerBound)-1] != letter and password[int(uperBound)-1] == letter): 
            validPasswords.append((lowerBound, uperBound, letter, password))

if __name__ == '__main__':
    print(len(validPasswords))
