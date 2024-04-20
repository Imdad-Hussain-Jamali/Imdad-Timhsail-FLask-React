from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Premium_Teacher_Dashboard_blue_print = Blueprint ("Premium_Teacher_Dashboard_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Premium_Teacher_Dashboard_blue_print.route("/")
def index():
    return "This is Premium_Teacher_Dashboard_blue_print Page"