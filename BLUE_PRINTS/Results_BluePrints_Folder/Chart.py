from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Chart_blue_print = Blueprint ("Chart_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Chart_blue_print.route("/")
def index():
    return render_template ("Charts.html")