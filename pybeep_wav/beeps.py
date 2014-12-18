from sound import SoundFile

def fibun(count):
    result = [1,1]
    if count > 2:
        for i in range(count - 2):
            result.append(result[i] + result[i+1])
    return result

lst = []

for item in fibun(40):
    freq = 110 + item%10 * 11
    lst.append((freq,0.5))

#lst = [(110,0.5),(220,0.5),(330,0.5),(440,0.5),(550,0.5),]

s = SoundFile(lst)
