data = open('day_06/input.txt') \
    .read() \
    .split('\n\n')

def sum_of_answers(list_of_answers):
    return sum([len(set(line)-set('\n')) for line in list_of_answers])

if __name__ == '__main__':
    print(sum_of_answers(data))