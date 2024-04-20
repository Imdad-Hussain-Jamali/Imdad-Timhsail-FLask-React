from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

TestContinue_blue_print = Blueprint ("TestContinue_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@TestContinue_blue_print.route("/")
def index():
    return "This is TestContinue_ Page"