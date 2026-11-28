def ch_frequency(text):
    f = {}
    for ch in text:
        if ch != " ":
            if ch in f:
                f[ch] += 1
            else:
                f[ch] = 1
    return f

def filtercutoff(students, cutoff):
    top_students = {}
    for name, marks in students.items():
        if marks>=cutoff:
            top_students[name]=marks
    return top_students

def palindrome(text):
    str1=text.replace(" ", "").lower()
    return str1==str1[::-1]

def fibonacci(n):
  fseries=[]
  a,b=0,1
  for i in range(n):
      fseries.append(a)
      a,b=b,a+b
  return fseries

def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1)

def prime(n):
    if n<=1:
        return False
    for i in range(2, n):
        if n%i==0:
            return False
    return True

while True:
    print("\nDictionaries & Logic Menu:")
    print("1. Character Frequency (Dictionary)")
    print("2. Filter Students by Cutoff Marks (Dictionary)")
    print("3. Palindrome Check")
    print("4. Fibonacci Series")
    print("5. Factorial/Prime")
    print("6. Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        s=input("Enter string: ")
        print("Character frequency:",ch_frequency(s))
    elif ch==2:
        students={}
        count=int(input("How many students? "))
        for i in range(count):
            name=input("Enter student name: ")
            marks=int(input("Enter marks: "))
            students[name]=marks
        cutoff=int(input("Enter cutoff marks: "))
        print("Students meeting cutoff:", filtercutoff(students, cutoff))
    elif ch==3:
        word=input("Enter string/number: ")
        if palindrome(word):
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")
    elif ch==4:
        n=int(input("How many Fibonacci terms? "))
        print("Fibonacci series:", fibonacci(n))
    elif ch==5:
        print("\na. Factorial")
        print("b. Prime Check")
        ab=input("Enter 'a' or 'b': ").lower()
        num=int(input("Enter a number: "))
        if ab=="a":
            if num<0:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {num} is {factorial(num)}")
        elif ab=="b":
            if prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        else:
            print("*invalid choice*")
    elif ch == 6:
        print("Program exited.")
        break
    else:
        print("*invalid choice*")
