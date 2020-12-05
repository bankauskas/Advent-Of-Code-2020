import re

pattern = re.compile('(\d+)-(\d+) ([a-z]): ([a-z]+)')
validPasswords = []

with open("day_02/input.txt") as f:
    for line in f:

        lowerBound, uperBound, letter, password = pattern.match(line).groups()
        if  password.count(letter) >= int(lowerBound) and password.count(letter) <= int(uperBound): 
            validPasswords.append((lowerBound, uperBound, letter, password))

if __name__ == '__main__':
    print(len(validPasswords))
