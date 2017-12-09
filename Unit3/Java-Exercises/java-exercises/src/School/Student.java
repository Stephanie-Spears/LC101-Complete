package School;

import java.util.ArrayList;
import java.util.List;

public class Student {
    public static List<Integer> studentList = new ArrayList<>();


    private static int nextStudentId = 1;
    private String name;
    private Integer studentId;
//    private final int studentId;
    private int numberOfCredits;
    private double gpa;


    public Student(String name, int studentId,
                   int numberOfCredits, double gpa) {
        this.name = name;
        this.studentId = studentId;
        this.numberOfCredits = numberOfCredits;
        this.gpa = gpa;
    }

    public Student(String name, int studentId) {
        this(name, studentId, 0, 0);
    }

    public Student(String name) {
        this(name, nextStudentId);
        nextStudentId++;
    }

    public void addGrade(int courseCredits, double grade){
        this.numberOfCredits += courseCredits;
        this.gpa += (grade * courseCredits);
    }
    public String getGradeLevel(){
        String status = "";
        if(this.numberOfCredits <= 29){
            status = "Freshman";
        }
        if(this.numberOfCredits >= 30 && this.numberOfCredits <= 59){
            status = "Sophomore";
        }
        if(this.numberOfCredits >= 60 && this.numberOfCredits <= 89){
            status = "Junior";
        }
        if(this.numberOfCredits >= 90){
            status = "Senior";
        }
        return status;
    }

    /* getters and setters */
    public String getName() {
        return name;
    }
    public void setName(String aName) {
        name = aName;
    }

    public Integer getNumberOfCredits() {
        return numberOfCredits;
    }
    public void setNumberOfCredits(int aNumberOfCredits) {
        numberOfCredits = aNumberOfCredits;
    }

    public Double getGPA() {
        return gpa;
    }
    public void setGPA(double aGPA) {
        gpa = aGPA;
    }

    public Integer getStudentId() {
        return studentId;
    }
    public void setStudentId(Integer aStudentId) {
        studentId = aStudentId;
    }


    @Override
    public String toString(){
        return ("\nID: " + studentId + "\nName: " + name + "\nNumber of Credits: " + numberOfCredits + "\nGPA: " + gpa);
    }


    @Override //do I need this?
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

        Student theStudent = (Student) o;
        return theStudent.getStudentId() == getStudentId();
    }

    @Override
    public int hashCode() {
        int result;
        long temp;
        result = name.hashCode();
        result = 31 * result + studentId;
        result = 31 * result + numberOfCredits;
        temp = Double.doubleToLongBits(gpa);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        return result;
    }

}