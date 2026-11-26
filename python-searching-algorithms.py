def lsearch(ar,target):
    for i in range(len(ar)):
        if ar[i]==target:
            return i
    return -1

def bsearch(ar,target):
    low=0
    high=len(ar)-1
    while low<=high:
        mid=(low+high)//2
        if ar[mid]==target:
            return mid
        elif ar[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

def input_list():
    ar=[]
    n=int(input("Enter number of elements: "))
    print("Enter the elements of the list:")
    for i in range(n):
        ar.append(int(input()))
    return ar

def choice():
    while True:
        ch = int(input("Enter '1' for linear search, '2' for binary search: "))
        if ch in (1, 2):
            return ch
        print("*invalid choice*")

numlist = input_list()
print("List entered:", numlist)
target = int(input("Enter element to search: "))
ch = choice()
if ch == 1:
    pos = lsearch(numlist, target)
    if pos != -1:
        print(f"Element {target} found at position {pos} using linear search.")
    else:
        print(f"Element {target} not found in the list.")
elif ch == 2:
  sortednumlist = sorted(numlist)
  print("Sorted list for binary search:", sortednumlist)
  pos = bsearch(sortednumlist, target)
  if pos != -1:
      print(f"Element {target} found at poition {pos} in sorted list using binary search.")
  else:
      print(f"Element {target} not found in the list.")
