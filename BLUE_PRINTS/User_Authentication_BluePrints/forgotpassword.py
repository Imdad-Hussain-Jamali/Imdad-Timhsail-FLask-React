from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

FORGOTPASSWORD_blue_print = Blueprint ("FORGOTPASSWORD_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@FORGOTPASSWORD_blue_print.route("/")
def index():
    return render_template ("forgot-password")