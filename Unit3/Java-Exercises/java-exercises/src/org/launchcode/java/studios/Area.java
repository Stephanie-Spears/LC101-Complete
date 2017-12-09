package org.launchcode.java.studios;
import java.util.Scanner;
import java.lang.Math;

public class Area {
    public static void main(String[] args) {
        boolean running = true;
        String error = "";
        while (running){
            System.out.println("Radius: ");
            Scanner userInput = new Scanner(System.in);
            if (userInput.hasNextInt()){
                int inputRadius = userInput.nextInt();
                if (inputRadius > 0){
                    double areaOfCircle = (Math.pow(inputRadius,2)) * Math.PI;
                    System.out.println("Area is: " + areaOfCircle );
                    running = false;
                }
                else{
                    error += "Positive ";

                }

            }
            else{
                error += "Numeric ";
            }
            System.out.print(error + "values only.\n");
        }
    }
}
