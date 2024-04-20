from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Select_Plan_blue_print = Blueprint ("Select_Plan_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Select_Plan_blue_print.route("/")
def index():
    return render_template ("Selectplan.html")