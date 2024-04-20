from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

StartTestPage_blue_print = Blueprint ("StartTestPage_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@StartTestPage_blue_print.route("/")
def index():
    return render_template ("StartTest.html")