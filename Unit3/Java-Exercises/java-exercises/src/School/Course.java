package School;
import java.util.*;

public class Course {
    private static List<Integer> courseList = new ArrayList<>();

    private String courseName;
    private int courseReferenceNumber;
    private final int numberOfCredits;

    private List<Student> studentList = new ArrayList<>();


    public Course (String courseName, int courseReferenceNumber, int numberOfCredits, List studentList){
        this.courseName = courseName;
        this.courseReferenceNumber = courseReferenceNumber;
        this.numberOfCredits = numberOfCredits;
        this.studentList = studentList;
    }

    public String getCourseName() {
        return courseName;
    }
    public void setCourseName(String aCourseName) {
        courseName = aCourseName;
    }

    public Integer getCourseRefernceNumber() {
        return courseReferenceNumber;
    }
    public void setCourseReferenceNumber(Integer aCourseReferenceNumber) {
        courseReferenceNumber = aCourseReferenceNumber;
    }

    public Integer getNumberOfCredits() {
        return numberOfCredits;
    }
//    public void setNumberOfCredits(Integer aNumberOfCredits) {
//        numberOfCredits = aNumberOfCredits;
//    }

    public List<Student> getStudentList() {
        return studentList;
    }
    public void setStudentList(List<Student> aStudentList) {
        studentList = aStudentList;
    }


    @Override
    public String toString(){
        return ("\nCRN: " + courseReferenceNumber + "\nCourse Name: " + courseName + "\nNumber of Credits: " + numberOfCredits + "\nStudent List: " + studentList);
    }


    public boolean equals(Object o) {

        if (o == this) {
            return true;
        }

        if (o == null) {
            return false;
        }

        if (o.getClass() != getClass()) {
            return false;
        }

        Course theCourse = (Course) o;
        return theCourse.getCourseRefernceNumber() == getCourseRefernceNumber();
    }

    @Override
    public int hashCode() {
        int result = courseName.hashCode();
        result = 31 * result + courseReferenceNumber;
        result = 31 * result + numberOfCredits;
        result = 31 * result + (studentList != null ? studentList.hashCode() : 0);
        return result;
    }

    public static void main(String[] args) {
//        Student stephanie = new Student("Steph", 0, 8, 4.0);
//        Student max = new Student("Max");
//
////need to connect student IDs to individual courses, so it only displays those who are registered.
//        Course history = new Course("History", 1,5, Student.studentList);
//        Course science = new Course ("Science", 2, 4, Student.studentList);
//        System.out.println(history);
//        System.out.println(science);

    }

}
