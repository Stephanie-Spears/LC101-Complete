package exercises;

import java.util.Scanner;

public class First_GoAskAlice {
    public static void main(String[] args) {
        String AliceText = "Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, 'and what is the use of a book,' thought Alice 'without pictures or conversation?'";
        String checkFound;
        Scanner userInput = new Scanner(System.in);
        System.out.println("Search: ");
        String searchTerm = userInput.nextLine();
        if (AliceText.toLowerCase().contains(searchTerm.toLowerCase())){
            checkFound = "was";
        }
        else {
            checkFound = "was not";

        }

        System.out.println("The term: " + searchTerm + " " + checkFound + " found" );
    }
}
