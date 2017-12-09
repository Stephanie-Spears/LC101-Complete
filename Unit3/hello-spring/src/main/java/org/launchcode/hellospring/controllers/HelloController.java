package org.launchcode.hellospring.controllers;

import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.web.bind.annotation.RestController;
//Controller and ResponseBody are replaced by RestController
//import org.springframework.stereotype.Controller;
//import org.springframework.web.bind.annotation.ResponseBody;

import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@RestController
public class HelloController {


//    request mapping maps (/) to the index() method. When invoked via browser or curl, the method returns pure text--because @restcontroller combines controller and responsebody, two annotations that result in web requests returning data and not a 'view'
    @RequestMapping(value="")
//    @ResponseBody
    public String index(HttpServletRequest request){
        String name = request.getParameter("name");
        return "Hello " + name;
    }

    @RequestMapping(value="goodbye")
//    @ResponseBody
    public String goodbye(){
        return "Goodbye";
    }

    @RequestMapping(value = "hello", method = RequestMethod.GET)
//    @ResponseBody
    public String helloForm(){
        String html = "<form method='post'>" +
                "<input type='text' name='name' />" +
                "<input type='submit' value='Oh Hai!'/>" +
                "</form>";
        return html;
    }

    @RequestMapping(value = "hello", method = RequestMethod.POST)
//    @ResponseBody
    public String helloPost(HttpServletRequest request){
        String name = request.getParameter("name");
        return "Hello " + name;
    }

    @RequestMapping(value = "hello/{name}")
//    @ResponseBody
    public String helloUrlSegment(@PathVariable String name){
        return "Hello " + name;

    }


    @RequestMapping(value = "language", method = RequestMethod.GET)
//    @ResponseBody
    public String languageForm(){
        String html =
                "<form method='post'>" +
                        "<input type='text' name='name' />" +
                        "<select id='language' name='language'>" +
                            "<option name='English' value='English' selected>English</option>" +
                            "<option name='French' value='French'>French</option>" +
                            "<option name='Japanese' value='Japanese'>Japanese</option>" +
                            "<option name='Spanish' value='Spanish'>Spanish</option>" +
                            "<option name='German' value='German'>German</option>" +
                        "</select>" +
                        "<input type='submit' value='Say Hi!'/>" +
                "</form>";
        return html;
    }

    @RequestMapping(value = "language", method = RequestMethod.POST)
//    @ResponseBody
    public String languagePost(HttpServletRequest request){
        String name = request.getParameter("name");
        String language = request.getParameter("language");
        String myMessage = createMessage(name, language);
        String html =
                "<h1 style='color: purple;'>" + myMessage + "</h1>";
        return html;
    }

    public static String createMessage(String name, String language){
        String hello = "";
        if (language.equals("English")){
            hello = "Hello";
        }
        if (language.equals("French")){
            hello = "Bonjour";
        }
        if (language.equals("Japanese")){
            hello = "Konichiwa";
        }
        if (language.equals("Spanish")){
            hello = "Hola";
        }
        if (language.equals("German")){
            hello = "Hallo";
        }
        return hello + ", " + name;
    }

}
