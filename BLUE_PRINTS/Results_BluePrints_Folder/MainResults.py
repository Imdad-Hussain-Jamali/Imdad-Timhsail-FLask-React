from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

MainResults_blue_print = Blueprint ("MainResults_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@MainResults_blue_print.route("/")
def index():
    return render_template ("MainResults.html")