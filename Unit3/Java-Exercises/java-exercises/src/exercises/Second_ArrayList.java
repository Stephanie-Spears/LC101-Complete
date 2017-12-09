package exercises;
import java.util.ArrayList;

public class Second_ArrayList {

    public static void main(String[] args){
        Double mySum = 0.0;

        ArrayList <Integer> myList = new ArrayList<>();
        myList.add(1);
        myList.add(2);
        myList.add(3);
        myList.add(10);
        for (int i = 0; i < myList.size(); i++){
            if (myList.get(i)%2 == 0){
                mySum += myList.get(i);

            }

        }
        System.out.println(mySum);
    }

}
