from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Purchase_SUccessfull_blue_print = Blueprint ("Purchase_SUccessfull_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Purchase_SUccessfull_blue_print.route("/")
def index():
    return render_template ("Purchase_Successfull.html")