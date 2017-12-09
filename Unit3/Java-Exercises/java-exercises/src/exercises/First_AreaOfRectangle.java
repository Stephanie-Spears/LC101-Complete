package exercises;
import java.util.Scanner;

public class First_AreaOfRectangle {

    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);

        System.out.println("Length: ");
        int inLength = userInput.nextInt();
        System.out.println("Width: ");
        int inWidth = userInput.nextInt();
        System.out.println("Area is: " + (inLength * inWidth) );


    }
}
