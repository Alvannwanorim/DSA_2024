def firstRepaeatingElemnet(num):
    table = {}
    for n in num:
        if n not in table:
            table[n] = 1
        else:
            table[n] = -1
    for n in num:
        if table[n] == -1:
            return n

print(firstRepaeatingElemnet([7,2,1,3,4,5,2,4]))



    