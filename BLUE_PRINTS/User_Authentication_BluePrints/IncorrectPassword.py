from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

IncorrectPasssword_blue_print = Blueprint ("IncorrectPasssword_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@IncorrectPasssword_blue_print.route("/")
def index():
    return render_template ("Incorrect-Password-Re-Enter-Password.html")