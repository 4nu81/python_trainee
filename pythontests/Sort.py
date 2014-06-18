class Sort(object):

#section quicksort
    def Quicksort(self,args):
        temp = args
        l = len(temp)
        if len(temp) <= 1:
            return temp
        else:
            h = int(l/2)
            pivot = temp.pop(h)
            left = []
            right = []
            while len(temp) > 0:
                t = temp.pop(0)
                if t > pivot:
                    right.append(t)
                else:
                    left.append(t)
            left = self.Quicksort(left)
            right = self.Quicksort(right)
            result = left + [pivot] + right
            return result

# section mergesort
    def __merge(self, left, right):
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:                
                result.append(left.pop(0))
            else:                
                result.append(right.pop(0))
        while len(left) > 0:
            result.append(left.pop(0))
        while len(right) > 0:
            result.append(right.pop(0))
        return result

    def Mergesort(self,args):
        l = len(args)
        if l <= 1:
            return args
        else:
            h = int(l/2)
            left = args[:h]
            right = args[h:]
            left = self.Mergesort(left)
            right = self.Mergesort(right)
            return self.__merge(left, right)

#section bubblesort
    def Bubblesort(self,args):
        result = args
        l = len(result) - 1
        for i in range(0, l - 1 , 1):            
            for j in range(0, l - i ,1):
                if result[j]>result[j + 1]:
                    temp = result.pop(j)
                    result.insert(j + 1,temp)
        return result
