from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Login_blue_print = Blueprint ("Login_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Login_blue_print.route("/")
def index():
    return render_template ("login.html")