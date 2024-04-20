from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Premium_Student_Dashboard_blue_print = Blueprint ("Premium_Student_Dashboard_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Premium_Student_Dashboard_blue_print.route("/")
def index():
    return "This is Premium_Student_Dashboard_blue_print Page"