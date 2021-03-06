package org.launchcode.controllers;

import org.launchcode.models.Category;
import org.launchcode.models.data.CategoryDao;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.Errors;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import javax.validation.Valid;

@Controller
@RequestMapping("category")
public class CategoryController {

    //    * This creates a private field categoryDao of type CategoryDao. This object will be the mechanism with which we interact with objects stored in the database.
//    * Recall that Spring will do the work of creating a class that implements CategoryDao and putting one of those objects in the categoryDao field when the application starts up. And all of this is thanks to the @Autowired annotation.
//    * This code would need to be added to each controller class that you want to have access to the persistent collections defined within categoryDao.*/
    @Autowired
    private CategoryDao categoryDao;

    @RequestMapping(value = "")
    public String index(Model model){
        //        /*the following returns a collection (actually, an Iterable) of all Category objects managed by categoryDao. Retrieves the list of categories, and then passes the list into the view by adding it to model*/
        Iterable<Category> categories = categoryDao.findAll();

        /* The index handler should correspond to the route "" (that is, the path /category), and it should retrieve the list of all categories. This is done via the categoryDao object: categoryDao.findAll() returns a collection (actually, an Iterable) of all Category objects managed by categoryDao. Use this snippet to retrieve the list of categories, and then pass the list into the view by adding it to model. Also add a "title" to the model ("Categories" works).*/
        model.addAttribute("categories", categories);
        model.addAttribute("title", "Categories");

        return "category/index";
    }

    @RequestMapping(value = "add", method = RequestMethod.GET)//do i need to specify get here?
    public String displayAddCategoryForm(Model model) {
        //        /*create a new Category object using the default constructor and pass it into the view with key "category"-->default constructor name*/
        model.addAttribute(new Category());
        model.addAttribute("title", "Add Category");

        return "category/add";
    }

    @RequestMapping(value="add", method = RequestMethod.POST)
    public String processAddCategoryForm(Model model, @ModelAttribute
    @Valid Category category, Errors errors) {

        if (errors.hasErrors()) {
            model.addAttribute("title", "Add Category");
            return "category/add";
        }

        categoryDao.save(category);
        return "redirect:";
    }

///*creates problem if category is assigned to a cheese, then that category is removed*/
    @RequestMapping(value = "remove", method = RequestMethod.GET)
    public String displayRemoveCategoryForm(Model model) {
        model.addAttribute("categories", categoryDao.findAll());
        model.addAttribute("title", "Remove Category");
        return "category/remove";
    }

    @RequestMapping(value = "remove", method = RequestMethod.POST)
    public String processRemoveCategoryForm(@RequestParam int[] categoryIds) {

        for (int categoryId : categoryIds) {
            categoryDao.delete(categoryId);
        }

        return "redirect:";
    }
}
