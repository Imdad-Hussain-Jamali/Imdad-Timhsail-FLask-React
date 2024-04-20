from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Register_blue_print = Blueprint ("Register_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Register_blue_print.route("/")
def index():
    return render_template ("register.html")