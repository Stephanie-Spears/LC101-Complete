package org.launchcode.quizproject.controllers;

import org.launchcode.quizproject.models.Quiz;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import javax.validation.Valid;

@Controller
@RequestMapping(value="")
public class QuizController {


    @RequestMapping(value = "")
    public String index(Model model){
        model.addAttribute("title", "Quizzin'!");
        return "index";
    }

    @RequestMapping(value = "quiz", method = RequestMethod.GET )
    public String displayQuizForm(Model model){
        model.addAttribute("title", "Take a Quiz!");
//        model.addAttribute(new Quiz());
        return "quiz";
    }

    @RequestMapping(value="quiz", method= RequestMethod.POST)
    public String processQuizForm(Model model,Errors errors, @ModelAttribute @Valid Quiz newQuiz){
        if (errors.hasErrors()) {
            model.addAttribute("title", "Take a Quiz!");
            return "quiz";
        }
        Quiz.add(newQuiz);
        return "results";
    }


    @RequestMapping(value = "results")
    public String displayResults(Model model){
        model.addAttribute("title", "Quiz Results!");
//        model.addAttribute("results", Quiz.getAll());
        return "results";
    }


}
