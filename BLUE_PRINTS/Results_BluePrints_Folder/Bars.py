from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Bars_blue_print = Blueprint ("Bars_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Bars_blue_print.route("/")
def index():
    return render_template ("Bars.html")