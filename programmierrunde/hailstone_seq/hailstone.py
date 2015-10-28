import sys

def hailstone(number):
    if number < 1:
        return []
    elif number == 1:
        return [1]
    elif number%2 == 1:
        return [number] + hailstone(number * 3 + 1)
    else:
        return [number] + hailstone(number / 2)

if __name__ == '__main__':
    assert len(sys.argv) == 2
    print hailstone(int(sys.argv[1]))