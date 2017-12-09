package exercises;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


public class Second_HashMapStuents {
    public static void main(String[] args) {

        HashMap<Integer, String> students = new HashMap<>();
        Scanner in = new Scanner(System.in);
        String newStudent;

        System.out.println("Press Enter to Finish");
        // Get student names and grades
        do {

            System.out.print("Student: ");
            newStudent = in.nextLine();

            if (!newStudent.equals("")) {
                System.out.print("ID: ");
                Integer newID = in.nextInt();
                students.put(newID, newStudent);

                // Read in the newline before looping back
                in.nextLine();
            }

        } while(!newStudent.equals(""));

        // Print class roster
        System.out.println("\nClass Roster:");

//        String name = "jesse";
//        Integer jesseGrade = students.get(name);
        for (Map.Entry<Integer, String> student : students.entrySet()) {
            System.out.println(student.getKey() + " (" + student.getValue() + ")");
        }
//        System.out.println(jesseGrade);


    }
}
