package org.launchcode.quizproject.models;

import java.util.ArrayList;

//public abstract class Question {
public class Question {
    private int id;
    private static int nextId = 1;
    private String aQuestion;
    private String anAnswer;
    private QuestionType type;

    public int getId() {
        return id;
    }

    //should set as final?
    public void setId(int id) {
        this.id = id;
    }

    public String getQuestion() {
        return aQuestion;
    }

    public void setQuestion(String aQuestion) {
        this.aQuestion = aQuestion;
    }

    public String getAnswer() {
        return anAnswer;
    }

    public void setAnswer(String anAnswer) {
        this.anAnswer = anAnswer;
    }

    public QuestionType getType() {
        return type;
    }

    public void setType(QuestionType type) {
        this.type = type;
    }

    //each question object should be stored in Quiz's arrayList. each object should have an id/question/type/answer(0 or 1)?

    private enum QuestionType {
        CHECKBOX, SELECT, RADIO;
    }

    Question() {
        this.id = nextId;
        nextId++;
    }

    Question(String aQuestion, QuestionType type, String anAnswer) {
        this();
        this.aQuestion = aQuestion;
        this.type = type;
        this.anAnswer = anAnswer;
    }
}

//        //set id for each object extending Question by adding super() in constructor
//        protected int id;
//        public Question() {
//            this.id = getNextId();
//        } //is this the only constructor that gets called when i do super?
//
//        public int getId() {
//            return id;
//        }
//        protected static int index = 0;
//
//        protected static int getNextId() {
//            return ++index;
//        }


        //require all subclasses to define their own questionType implementation ... am I using enum right here?
//        abstract public QuestionType getQuestionType();
        //can i make private or protected?
//        public enum QuestionType {
//            CHECKBOX("checkbox"), SELECT("select"), RADIO("radio");
//            private String type;
//            QuestionType(String type){
//                this.type = type;
//            }
//            public String getType(){
//                return type;
//            }
//        }


        //set/get number of questions


        //set/get question strings

        //set/get question answers

        //set/get correct values

        //set/get results score


//}
/*
* Static methods in java belong to the class (not an instance of it). They use no instance variables and will usually take input from the parameters, perform actions on it, then return some result. Instances methods are associated with objects and, as the name implies, can use instance variables.
* */


/*
*
* Abstract classes let you define some behaviors; they force your subclasses to provide others. For example, if you have an application framework, an abstract class may provide default services such as event and message handling. Those services allow your application to plug in to your application framework. However, there is some application-specific functionality that only your application can perform. Such functionality might include startup and shutdown tasks, which are often application-dependent. So instead of trying to define that behavior itself, the abstract base class can declare abstract shutdown and startup methods. The base class knows that it needs those methods, but an abstract class lets your class admit that it doesn't know how to perform those actions; it only knows that it must initiate the actions. When it is time to start up, the abstract class can call the startup method. When the base class calls this method, Java calls the method defined by the child class.
*
* */