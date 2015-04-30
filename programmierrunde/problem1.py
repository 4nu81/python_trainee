import sys

romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'C': 100,
    'M': 1000,
    'L': 50,
    'D': 500
}

def fromRoman(roman):
    nmbr = 0
    indexes = range(len(roman))
    while indexes:
        index = indexes[0]
        if len(indexes) > 1:
            if roman[index] in ['I','X','C']:
                if romans[roman[index+1]] > romans[roman[index]]:
                    nmbr += romans[roman[index+1]] - romans[roman[index]]
                    indexes.remove(index+1)
                    indexes.remove(index)
                    continue
        nmbr += romans[roman[index]]
        indexes.remove(index)
    return nmbr

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print fromRoman(sys.argv[1])
