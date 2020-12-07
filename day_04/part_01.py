# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)

data = open('day_04/input.txt') \
    .read() \
    .split('\n\n')
requirements = {'byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:'}
validID = []

def IDisValid (ID, requirements):
    return all([field in ID for field in requirements])

for ID in data:
    if IDisValid(ID, requirements):
        validID.append(ID)

if __name__ == '__main__':
print(len(validID))
