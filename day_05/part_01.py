with open("day_05/input.txt") as f:
    ls = f.read().splitlines()


def seatID(path):
    return  \
        posDetection(path[:-3],range(0,127),'F') \
        * 8 \
        + posDetection(path[-3:],range(0,7),'L')


def posDetection(path, rng, separator):
    if len(path)==1:
        return rng[0] if path == separator else rng[0]+1
    else:
        half = len(rng)//2
        if path[0] == separator:
            rng = rng[:half]     
        else:
            rng = rng[half+1:]  
    return posDetection(path[1:], rng, separator)


if __name__ == '__main__':
    print([seatID(path) for path in ls])

