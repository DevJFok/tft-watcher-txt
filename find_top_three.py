import json

def findTopThreeFunction(mainfile, occurance_array, name_array):
    for x in mainfile:
        if x == name_array[0]: 
            # if x is the same trait as the first trait
            if mainfile[x] > occurance_array[0]:
                occurance_array[0] = mainfile[x]
                name_array[0] = x

        # if x is the same trait as the second trait
        elif x == name_array[1]:
            if mainfile[x] > occurance_array[0]:
                occurance_array[1] = occurance_array[0]
                name_array[1] = name_array[0]

                occurance_array[0] = mainfile[x]
                name_array[0] = x

            elif mainfile[x] > occurance_array[1]:

                occurance_array[1] = mainfile[x]
                name_array[1] = x

        # if x is the same trait as the third trait
        elif x == name_array[2]:
            if mainfile[x] > occurance_array[0]:
                occurance_array[2] = occurance_array[1]
                name_array[2] = name_array[1]

                occurance_array[1] = occurance_array[0]
                name_array[1] = name_array[0]

                occurance_array[0] = mainfile[x]
                name_array[0] = x 

            elif mainfile[x] > occurance_array[1]:
                occurance_array[2] = occurance_array[1]
                name_array[2] = name_array[1]

                occurance_array[1] = mainfile[x]
                name_array[1] = x

            elif mainfile[x] > occurance_array[2]:

                occurance_array[2] = mainfile[x]
                name_array[2] = x
        # if x is not part of top 3 trait
        else:    
            if mainfile[x] > occurance_array[0]:
                occurance_array[2] = occurance_array[1]
                name_array[2] = name_array[1]

                occurance_array[1] = occurance_array[0]
                name_array[1] = name_array[0]

                occurance_array[0] = mainfile[x]
                name_array[0] = x

            elif mainfile[x] > occurance_array[1] and x !=  name_array[1]:

                occurance_array[2] = occurance_array[1]
                name_array[2] = name_array[1]

                occurance_array[1] = mainfile[x]
                name_array[1] = x

            elif mainfile[x] > occurance_array[2] and x !=  name_array[2]:

                occurance_array[2] = mainfile[x]
                name_array[2] = x
            
            elif mainfile[x] == occurance_array[2] and x !=  name_array[2]:
                occurance_array.append(mainfile[x])
                name_array.append(x)

    return occurance_array, name_array