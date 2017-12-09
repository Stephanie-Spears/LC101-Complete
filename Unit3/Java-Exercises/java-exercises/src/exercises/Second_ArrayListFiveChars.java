package exercises;
import java.util.ArrayList;

public class Second_ArrayListFiveChars {
    public static void main(String[] args){
        ArrayList <String> myList = new ArrayList<>();
        myList.add("one");
        myList.add("two");
        myList.add("three");
        myList.add("four");
        myList.add("fives");
//        myList.add("there should be three outputs");

        for (String word : myList){
            if (word.length() == 5){
                System.out.println(word);

            }
        }

    }


}
