#! /usr/bin/python3

with open('input.txt','r') as body:
    arr = body.read().split('\n\n')
    #print(arr)
    list = []
    for i in arr:
        f = i.split('\n')
        f = sum([int(g) for g in f])
        list.append(f)
    print(max(list))
    list.sort(reverse=True)
    print(sum(list[:3]))