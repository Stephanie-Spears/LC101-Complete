package org.launchcode.quizproject.models;

import java.util.ArrayList;

public class Quiz extends Question{
//
//    public enum QuestionType {
//        CHECKBOX("checkbox"), SELECT("select"), RADIO("radio");
//        private String type;
//        QuestionType(String type){
//            this.type = type;
//        }
//        public String getType(){
//            return type;
//        }
//    }

//    private int id;
//    private static int nextId = 1;


    /*Static fields are shared by all instances of a class--so each instance doesn't have it's own version of the data--public static final creates a constant, esentially and should be named with all caps, and generally are public since they can't be modified anyway
    * final fields, without static, can't be changed once initialized. final object fields maynot change the object that they hold once initialized, but the object may change itself.
    * instance methods rely on each object's specific data, whereas static methods must NOT rely on data from a specific object
    * you should call a static method using the class name as opposed to a specific instance of a class, so that it's clear you're using a static class method.*/
    /*
    * equals() and == test for identity, not equality. if we want to test for equality between two different objects, we override equals() method and giving our own definition.
    *
    * public boolean equals(Object o) {

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
    * the equals parameter must be of type Object
    *
    * every time you implement your own version of equals() you should also implement your own version of hashCode().
    * To do so, right-click within your class file and select Generate > equals and hashCode and follow the prompts.*/
    static ArrayList<Question> questionList = new ArrayList<>();
    private Question question = new Question();
//    private String question;

//    public String getQuestion(){
//        return question;
//    }
//    public void setQuestion(String question){
//        this.question = question;
//    }
    public ArrayList<Question> getQuestionList(){
        return questionList;
    }
    public void setQuestionList(ArrayList<Question> questionList){
        questionList.add(question);
    }
    // add
    public static void add(Question newQuestion) {
        questionList.add(newQuestion);
    }


//    QuestionType;
//    private String answer;
//    private int score;



    Quiz(){
        super();
//        this.id = nextId;
//        nextId++;

//        super();
//        QuestionType.getType();
    }
}
