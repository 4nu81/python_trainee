import sys

def dec2nbr(dec, base):
    switch = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F',
        16:'G',
        17:'H',
        18:'I',
        19:'J',
        20:'K',
        21:'L',
        22:'M',
        23:'N',
        24:'O',
        25:'P',
        26:'Q',
        27:'R',
        28:'S',
        29:'T',
        30:'U',
        31:'V',
        32:'W',
        33:'X',
        34:'Y',
        35:'Z',
    }
    run = dec
    result = ''
    neg = False
    if run == 0:
        return '0'
    if run < 0:
        run *= -1
        neg = True

    while run != 0:
        unit = run%base
        run = run / base
        if unit in switch:
            unit = switch[unit]
        result = str(unit) + result

    result = neg and ('-' + result) or (result)
    return result

print dec2nbr( 40, 16)
