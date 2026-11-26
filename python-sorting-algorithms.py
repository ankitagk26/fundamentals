def bubble(ar):
  length = len(ar)
  for i in range (length):
    for j in range (0,length-i-1):
      if ar[j]>ar[j+1]:
        ar[j],ar[j+1]=ar[j+1],ar[j]
  print("list sorted using bubble sort technique: ", ar)

def selection(ar):
  length = len(ar)
  for i in range (length):
    mindex=i
    for j in range (i+1,length):
      if ar[j]<ar[mindex]:
        mindex=j 
    ar[i],ar[mindex]=ar[mindex],ar[i] 
  print("list sorted using selection sort technique: ", ar) 

def insertion(ar):
  length=len(ar)
  for i in range (1,length):
    key=ar[i]
    j=i-1
    while j>=0 and key<=ar[j]:
      ar[j+1]=ar[j]
      j-=1
    ar[j+1]=key
  print("list sorted using insertion sort technique: ",ar)

def inputlist():
  ar=[]
  listlen=int(input("Enter number of elements: "))
  print("Enter the elements of the list:")
  for i in range (listlen):
    element = int(input())
    ar.append(element)
  return ar

def choice():
  ch=int(input("Enter '1' for bubble sort, '2' for selection sort, '3' for insertion sort. "))
  return ch

ar=inputlist()
print("Original list: ",ar)
while True:
  ch=choice()
  if ch==1:
    bubble(ar)
    break
  elif ch==2:
    selection(ar)
    break
  elif ch==3:
    insertion(ar)
    break
  else:
    print("*invalid choice*")
  
