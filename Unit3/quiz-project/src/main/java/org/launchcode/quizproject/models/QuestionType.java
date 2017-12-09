package org.launchcode.quizproject.models;

public enum QuestionType {

    CHECKBOX("checkbox"),
    SELECT("select"),
    RADIO("radio");

    private final String type;

    QuestionType(String type){
        this.type = type;
    }

    public String getType(){
        return type;
    }
}
