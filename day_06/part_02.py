data = open('day_06/input.txt') \
    .read() \
    .split('\n\n')

data = [line.split('\n') for line in data]

def possitive_answers(ls):
    return len(set.intersection(*map(set,ls)))

if __name__ == '__main__':
    print(sum([possitive_answers(i) for i in data]))