ar=[11,12,13,14,15]
def linearsearch(ar,target):
    for i in range(len(ar)):
        if ar[i]==target:
            print(f'{target} is fount at index {i}')
            return
    print('not found')
    return -1
print(linearsearch(ar,10))