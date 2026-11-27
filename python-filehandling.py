import os
import pickle

txtfile = os.path.join("/tmp", "recordsummary.txt")
binfile = os.path.join("/tmp", "students.dat")

def save_binary_records(records, binfile):
    with open(binfile, "wb") as file:
        pickle.dump(records, file)

def load_binary_records(binfile):
    try:
        with open(binfile, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def export_text_report(records, txtfile):
    with open(txtfile, "w") as file:
        file.write("Student Marks Report\n")
        file.write("-"*24+"\n")
        for student in records:
            file.write(f"Roll: {student['roll']} | Name: {student['name']} | Marks: {student['marks']}\n")

def main():
    students=[]
    n=int(input("How many student records do you want to enter? "))
    for i in range(n):
        roll=int(input("Enter roll number: "))
        name=input("Enter name: ")
        marks=float(input("Enter marks: "))
        students.append({"roll": roll, "name": name, "marks": marks})
    save_binary_records(students,binfile)
    loaded_students=load_binary_records(binfile)
    export_text_report(loaded_students,txtfile)
    print("\nLoaded from binary file (.dat):")
    for s in loaded_students:
        print(s)
    print(f"\nSummary also written to {txtfile}:")
    with open(txtfile, "r") as file:
        print(file.read())

if __name__=="__main__":
    main()
