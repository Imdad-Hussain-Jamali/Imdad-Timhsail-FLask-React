from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

Table_blue_print = Blueprint ("Table_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@Table_blue_print.route("/")
def index():
    return render_template ("Table.html")