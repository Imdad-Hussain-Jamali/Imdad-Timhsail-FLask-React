from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

FreeUser_Dashboard_blue_print = Blueprint ("FreeUser_Dashboard_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@FreeUser_Dashboard_blue_print.route("/")
def index():
    return "This is Free User Dashboard Page"