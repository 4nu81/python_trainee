import sys

def hailstoneRecursive(number):
    if number < 1:
        return []
    elif number == 1:
        return [1]
    elif number%2 == 1:
        return [number] + hailstoneRecursive(number * 3 + 1)
    else:
        return [number] + hailstoneRecursive(number / 2)

def hailstone(number):
    seq = []
    if number >= 1:
        seq.append(number)
    while number > 1:
        number = 3 * number + 1 if number & 1 else number//2
        seq.append(number)
    return seq

if __name__ == '__main__':
    assert len(sys.argv) == 2
    print hailstone(int(sys.argv[1]))