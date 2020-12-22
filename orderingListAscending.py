from collections import OrderedDict
import json

def orderingListAscendingFunction(mainfile):

    list_name_ordered = []
    list_occurance_ordered = []
    
    for x in mainfile:
        if mainfile[x] == 0:
            list_occurance_ordered.append(mainfile[x])
            list_name_ordered.append(x)

    if len(list_occurance_ordered) < 3:
        for x in mainfile:
            if mainfile[x] == 1:
                list_occurance_ordered.append(mainfile[x])
                list_name_ordered.append(x)

    if len(list_occurance_ordered) < 3:
        while len(list_occurance_ordered) < 3:
            list_occurance_ordered.append(100)
            list_name_ordered.append(' ')

        for y in mainfile:
            if mainfile[y] < list_occurance_ordered[0]:
                list_occurance_ordered[2] = list_occurance_ordered[1]
                list_name_ordered[2] = list_name_ordered[1]

                list_occurance_ordered[1] = list_occurance_ordered[0]
                list_name_ordered[1] = list_name_ordered[0]

                list_occurance_ordered[0] = mainfile[y]
                list_name_ordered[0] = y

            elif mainfile[y] < list_occurance_ordered[1]:
                list_occurance_ordered[2] = list_occurance_ordered[1]
                list_name_ordered[2] = list_name_ordered[1]

                list_occurance_ordered[1] = mainfile[y]
                list_name_ordered[1] = y

            elif mainfile[y] < list_occurance_ordered[2]:
                list_occurance_ordered[2] = mainfile[y]
                list_name_ordered[2] = y

            elif mainfile[y] == list_occurance_ordered[2]:
                list_occurance_ordered.append(mainfile[y])
                list_name_ordered.append(y)
            

    return list_name_ordered, list_occurance_ordered