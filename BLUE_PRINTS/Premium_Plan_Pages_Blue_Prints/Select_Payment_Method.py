from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Select_Payment_Method_blue_print = Blueprint ("Select_Payment_Method_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Select_Payment_Method_blue_print.route("/")
def index():
     return render_template ("Select_Payment_Method.html")