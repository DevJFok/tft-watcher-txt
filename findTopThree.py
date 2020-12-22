import json

def findTopThreeFunction(mainfile, occuranceArray, nameArray):
    for x in mainfile:
        if x == nameArray[0]: 
            # if x is the same trait as the first trait
            if mainfile[x] > occuranceArray[0]:
                occuranceArray[0] = mainfile[x]
                nameArray[0] = x

        # if x is the same trait as the second trait
        elif x == nameArray[1]:
            if mainfile[x] > occuranceArray[0]:
                occuranceArray[1] = occuranceArray[0]
                nameArray[1] = nameArray[0]

                occuranceArray[0] = mainfile[x]
                nameArray[0] = x

            elif mainfile[x] > occuranceArray[1]:

                occuranceArray[1] = mainfile[x]
                nameArray[1] = x

        # if x is the same trait as the third trait
        elif x == nameArray[2]:
            if mainfile[x] > occuranceArray[0]:
                occuranceArray[2] = occuranceArray[1]
                nameArray[2] = nameArray[1]

                occuranceArray[1] = occuranceArray[0]
                nameArray[1] = nameArray[0]

                occuranceArray[0] = mainfile[x]
                nameArray[0] = x 

            elif mainfile[x] > occuranceArray[1]:
                occuranceArray[2] = occuranceArray[1]
                nameArray[2] = nameArray[1]

                occuranceArray[1] = mainfile[x]
                nameArray[1] = x

            elif mainfile[x] > occuranceArray[2]:

                occuranceArray[2] = mainfile[x]
                nameArray[2] = x
        # if x is not part of top 3 trait
        else:    
            if mainfile[x] > occuranceArray[0]:
                occuranceArray[2] = occuranceArray[1]
                nameArray[2] = nameArray[1]

                occuranceArray[1] = occuranceArray[0]
                nameArray[1] = nameArray[0]

                occuranceArray[0] = mainfile[x]
                nameArray[0] = x

            elif mainfile[x] > occuranceArray[1] and x !=  nameArray[1]:

                occuranceArray[2] = occuranceArray[1]
                nameArray[2] = nameArray[1]

                occuranceArray[1] = mainfile[x]
                nameArray[1] = x

            elif mainfile[x] > occuranceArray[2] and x !=  nameArray[2]:

                occuranceArray[2] = mainfile[x]
                nameArray[2] = x
            
            elif mainfile[x] == occuranceArray[2] and x !=  nameArray[2]:
                occuranceArray.append(mainfile[x])
                nameArray.append(x)

    return occuranceArray, nameArray