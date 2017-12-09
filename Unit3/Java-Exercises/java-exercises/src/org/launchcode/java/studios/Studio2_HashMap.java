package org.launchcode.java.studios;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class Studio2_HashMap {

    static void characterCount(String inputString)
    {
        //Creating a HashMap containing char as a key and occurrences as  a value
        HashMap<Character, Integer> charCountMap = new HashMap<Character, Integer>();

        //Converting given string to char array
        char[] strArray = inputString.toCharArray();

        //checking each char of strArray
        for (char c : strArray)
        {
            if(charCountMap.containsKey(c))
            {
                //If char is present in charCountMap, incrementing it's count
                charCountMap.put(c, charCountMap.get(c)+1);
            }
            else
            {
                //If char is not present in charCountMap, initialize and set value to 1
                charCountMap.put(c, 1);
            }
        }

        //Printing the charCountMap
        System.out.println("\n\n" + charCountMap);
    }

    public static String printFile() {
        //modified to return string object to main

        String rootPath = "/Users/wolfmac/Desktop/LC101/Unit3/";
        Scanner userInput = new Scanner(System.in);
        System.out.println("Enter text file name: ");
        rootPath += userInput.nextLine();
        rootPath += ".txt";
        File file = new File(rootPath);
        FileInputStream fis = null;
        String text = "";

        try {
            fis = new FileInputStream(file);
            System.out.println("Total file size to read (in bytes): " + fis.available() + "\n");
            int content;
            while ((content = fis.read()) != -1) {
                //convert to char and display
                System.out.print((char) content);
                text += (char) content;
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (fis != null)
                    fis.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }
        System.out.println("\n\nWould you like the count ot be case-insensitive?(Y/N): ");
//        char caseChoice = userInput.next(".").charAt(0);
        char caseChoice = userInput.next().charAt(0);
        caseChoice = Character.toUpperCase(caseChoice);
        if (caseChoice == 'Y'){
            text = text.toUpperCase();
        }
        else if (caseChoice == 'N'){
            return text;
        }
        else{
            System.out.println("Error in case choice");
        }

        return text;
    }


    public static void main(String[] args)
    {
        Scanner userInput = new Scanner(System.in);
        System.out.println("1. Input text from file\n 2. Type custom input\n");
        int in = userInput.nextInt();

        if (in == 1){
            String text = printFile();
            characterCount(text);

        }
        else if (in == 2){

        }
        else{
            System.out.println("Error");
        }

    }
}
