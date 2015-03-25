from random import randrange, choice
doors_count, iterations = 3,100000


def monty_hall(select, switch=False, doorCount=doors_count):

    doors = [False] * doorCount
    doors[randrange(doorCount)] = True
    old_select = select
    
    if not switch:
        return doors[select]
    else:
        while len(doors) > 2:
            # find a false door
            while True:
                ind_doors = range(len(doors))
                # a set makes it easier to sub values
                indexes = set(ind_doors) - set([select])
                # choice picks an item from list
                seq = choice(list(indexes))
                if doors[seq] == False:
                    break
            # remove false door
            del doors[seq]
            # select another door
            while True:
                select = randrange(len(doors))
                # we must pick a new door
                if select != old_select:
                    break

        return doors[select]

print "\nMonty Hall problem simulation:"
print doors_count, "doors,", iterations, "iterations.\n"
 
print "Not switching allows you to win",
print sum(monty_hall(randrange(doors_count), switch=False)
          for x in range(iterations)),
print "out of", iterations, "times."
print "Switching allows you to win",
print sum(monty_hall(randrange(doors_count), switch=True)
          for x in range(iterations)),
print "out of", iterations, "times.\n"
