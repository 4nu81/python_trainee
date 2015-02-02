from random import shuffle

x = [i for i in range(10)]
shuffle(x)


# Merge Sort
def merge(left,right):
    count = 0
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
        count +=1
    while len(left) > 0:
        result.append(left.pop(0))
        count +=1
    while len(right) > 0:
        result.append(right.pop(0))
        count +=1
    return result, count

def merge_sort(liste, count = 0):
    size = len(liste)
    if size == 1:
        return liste, 1
    l_l, count_l = merge_sort(liste[:size/2], count)
    l_r, count_r = merge_sort(liste[size/2:], count)
    
    count += count_l + count_r
    
    result, count_m = merge(l_l, l_r)
    return result, count + count_m

# Bubble Sort
def bubble_sort(liste):
    count = 0
    for n in range(len(liste)-1,0,-1):
        for i in range(n):
            count += 1
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
    return liste, count


ms, mc = merge_sort(x)
print 'sort_merge = ', ms
print 'steps_merge = ', mc

bs, bc = bubble_sort(x)
print 'sort_bubble = ', bs
print 'steps_bubble = ', bc
