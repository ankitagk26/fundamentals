import java.util.Scanner;

class Student {
    private int rollno;
    private String name;
    private double marks;

    public Student(int r, String n, double m) {
        rollno=r;
        name=n;
        marks=m;
    }

    public String calculateGrade() {
        if (marks >= 90) {
            return "A+";
        } else if (marks>=80) {
            return "A";
        } else if (marks>=70) {
            return "B";
        } else if (marks>=60) {
            return "C";
        } else if (marks>=40) {
            return "D";
        } else {
            return "Needs Improvement";
        }
    }
    public void displayDetails() {
        System.out.println("\nStudent Record:");
        System.out.println("Roll No : " + rollno);
        System.out.println("Name    : " + name);
        System.out.println("Marks   : " + marks);
        System.out.println("Grade   : " + calculateGrade());
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter Roll Number: ");
        int rollNo=sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Student Name: ");
        String name=sc.nextLine();
        System.out.print("Enter Marks (out of 100): ");
        double marks=sc.nextDouble();
        Student s1=new Student(rollNo, name, marks);
        s1.displayDetails();
        sc.close();
    }
}
