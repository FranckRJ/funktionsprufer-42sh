#!/usr/bin/python3

def printAllStringsAliases(size, lastOldString):
    tab = ['a'] * size
    oldStr = lastOldString
    while ord(tab[-1]) <= ord('z'):
        if oldStr:
            print("alias " + oldStr + "=" + ''.join(tab))
        oldStr = ''.join(tab)

        tab[0] = chr(ord(tab[0]) + 1)

        idx = 0
        while ord(tab[idx]) > ord('z'):
            if idx >= (size - 1):
                break
            tab[idx] = 'a'
            idx += 1
            tab[idx] = chr(ord(tab[idx]) + 1)

    return oldStr


printAllStringsAliases(3, "aliasbomb")
print("aliasbomb")
