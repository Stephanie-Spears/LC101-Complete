from flask import Flask, request, redirect, render_template #flask imports a "request" object, which allows us to access the data that the user submits to our server
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")  #using the tools of FLask to specify that this function should recieve requests at the root url (route "/")
def index(): #this function will recieve requests at that root path (request is being handled by index function)
    return render_template('hello_form.html')

@app.route("/hello", methods=['POST']) #this is a handler for the /hello path, handle requests to /hello.
def hello(): #takes data that the user enters into the form, which will be submitted to our server (to the /hello route on our server). This allows us to get the data, and then return a personalized greeting with the input user name
    first_name = request.form['first_name']
    return render_template('hello_greeting.html', name=first_name)


@app.route('/validate-time')
def display_time_form():
    return render_template('time_form.html')


def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''

    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}'.format(time))
    else:
        return render_template('time_form.html', hours_error=hours_error, minutes_error=minutes_error, hours=hours, minutes=minutes)

@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>'.format(time)



tasks = []

@app.route('/todos', methods=['POST', 'GET'])
def todos():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('todos.html', title="TODOs", tasks=tasks)

app.run()


#
# Notes
# As always, when staring to work on a Flask application, activate an appropriate virtual environment. Here, we do:
#
# $ source activate hello-flask
# Working with forms
# To create a form in a Python file, to be returned by a handler function in Flask, use triple-quotes """ to enclose strings that break across lines. This allows us to write large amounts of text (e.g. HTML) within a Python file.
# If this form is a global variable (i.e. it is defined outside of any function) then it can be used by multiple handler functions.
# By default, the action of a form is the same URL that the form is displayed at.
# By default, the method of a form is GET.
# The name attribute of a form element determines the key that will be used to pass the parameter to the server in the HTTP request. Thus, if an element has name='first_name' then the string 'first_name' must be used to access the value of the form element on the server.
# Accessing request data
# Accessing both GET and POST parameters within Flask requires the request object provided by Flask:
#
# from flask import request
# ACCESSING GET REQUEST PARAMETERS
#
# A query (or GET request) parameter can be accessed via request.args:
#
# form_value = request.args.get('param_name')
# GET parameters are passed in the HTTP request as part of the URL. More specifically, they make up the query string--the portion after ?--which looked like this in the lesson:
#
# http://localhost:5000/hello?first_name=Chris
# Here, the query string is ?first_name=Chris. If there were multiple query parameters, they would be separated by the & (ampersand) character.
#
# http://localhost:5000/hello?first_name=Chris&last_name=Bay
# ACCESSING POST REQUEST PARAMETERS
#
# To enable a handler function to receive POST requests, we must add a methods parameter to the @app.route decorator:
#
# @app.route('/path', methods=['POST'])
# def my_handler():
#     # request handling code
# A POST parameter can be accessed via request.form:
#
# form_value = request.form['param_name']
# 405 - Method Not Allowed
# An HTTP status of 405 - Method Not Allowed will be received if a resource/path is requested that doesn't accept requests using the given method (usually, GET or POST). This can be a common mistake when setting up a form to POST to a given path, but failing to configure the handler function to accept POST requests.
