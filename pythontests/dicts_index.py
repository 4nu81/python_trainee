
dictionaire = [1,2,'+',4,'+','*',6]

i = dictionaire.index('+')

left = dictionaire[:i]
right = dictionaire[i+1:]

print dictionaire
print left
print right
