package exercises;
import java.util.Scanner;


public class First_MilesPerGallon {
    public static void main(String[] args) {
        Scanner userInput = new Scanner(System.in);
        System.out.println("Miles: ");
        int inMiles = userInput.nextInt();
        System.out.println("Gas (gallons): ");
        int inGallons = userInput.nextInt();
        System.out.println("Miles per Gallon: " + (inMiles / inGallons) );
    }
}
