lst = [0,1,2,3,4,5,6,7,8,9]

print lst
print lst[2+1:7]

new = lst[:2]
new.append(5)
new.extend(lst[7+1:])
print new
