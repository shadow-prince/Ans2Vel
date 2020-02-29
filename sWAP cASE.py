def swap_case(s):
2
    l = ""
3
    for i in s:
4
        if i.isupper() == True:
5
            l =l + (i.lower())
6
        else:
7
          l = l +(i.upper())
8
    return l    
