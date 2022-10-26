import java.util.Scanner;

public class IFELSE{
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        // Normal form of If else :-
    
        // int age = sc.nextInt();

        // if (age > 18){
        //     System.out.println("Adult");
        // } else{
        //     System.out.println("Not Adult");
        // }

        //else if else:-

        // int x = sc.nextInt();
        // int y = sc.nextInt();

        // if (x==y){
        //     System.out.println("Equal");
        // } else{
        //     if (x>y){
        //         System.out.print("x is greater");
        //     } else{
        //         System.out.print("x is lesser ");
        //     }
        // }

        // else If :-
        int x = sc.nextInt();
        int y = sc.nextInt();

        if (x==y){
        System.out.println("Equal");
        } else if (x>y){
                System.out.print("x is greater");
            } else{
                System.out.print("x is lesser ");
            }

    }
}
