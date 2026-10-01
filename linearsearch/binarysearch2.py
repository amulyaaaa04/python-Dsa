b=[10,11,15,17,18,21]
def binarysearch(ar,target):
    l=0
    r=len(ar)-1
    m=l+r//2
    while l<r:
        if ar[m]==target:
            print(f'{target} is found at index {m}')
            return
        elif ar[m]<target:
            l=m
            m=(l+r)//2
        else:
            r=m
            m=(l+r)//2
        print(f'{target} is not found')
        return
binarysearch(b,12)         