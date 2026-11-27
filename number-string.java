import java.util.Scanner;

public class NumberAndString {
    public static boolean Armstrong(int num) {
        if (num<0) {
            return false;
        }
        int original=num;
        int digits=String.valueOf(num).length();
        int sum=0;
        while (num>0) {
            int digit=num % 10;
            sum+=Math.pow(digit, digits);
            num/=10;
        }
        return sum==original;
    }

    public static boolean Niven(int num) {
        if (num<=0) {
            return false;
        }
        int temp=num;
        int sum=0;
        while (temp>0) {
            sum+=temp%10;
            temp/=10;
        }
        return num%sum==0;
    }

    public static void analyzeString(String text) {
        int upper=0;
        int lower=0;
        int digits=0;
        int special=0;

        for (int i=0; i<text.length(); i++) {
            char ch=text.charAt(i);
            if (Character.isUpperCase(ch)) {
                upper++;
            } else if (Character.isLowerCase(ch)) {
                lower++;
            } else if (Character.isDigit(ch)) {
                digits++;
            } else if (!Character.isWhitespace(ch)) {
                special++;
            }
        }

        System.out.println("\nString Analysis:");
        System.out.println("Uppercase letters : " + upper);
        System.out.println("Lowercase letters : " + lower);
        System.out.println("Digits            : " + digits);
        System.out.println("Special characters: " + special);
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("Number & String Menu: ");
        System.out.println("1. Check Armstrong Number");
        System.out.println("2. Check Niven Number");
        System.out.println("3. Analyze String Characters");
        System.out.print("Enter choice: ");
        int choice=sc.nextInt();
        sc.nextLine();
        switch (choice) {
            case 1:
                System.out.print("Enter an integer: ");
                int num=sc.nextInt();
                if (Armstrong(num)) {
                    System.out.println(num + " is an Armstrong number.");
                } else {
                    System.out.println(num + " is not an Armstrong number.");
                }
                break;
            case 2:
                System.out.print("Enter an integer: ");
                int num1=sc.nextInt();
                if (Niven(num1)) {
                    System.out.println(num1 + " is a Niven number.");
                } else {
                    System.out.println(num1 + " is not a Niven number.");
                }
                break;
            case 3:
                System.out.print("Enter a string: ");
                String input=sc.nextLine();
                analyzeString(input);
                break;
            default:
                System.out.println("Invalid choice.");
        }
        sc.close();
    }
}
