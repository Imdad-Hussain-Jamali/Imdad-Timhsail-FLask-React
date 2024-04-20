from flask import Flask ,   blueprints,render_template , redirect , request ,Blueprint

EnterConformationcode_blue_print = Blueprint ("EnterConformationcode_blue_print" , __name__,static_folder= "Static" , template_folder= "templates")

@EnterConformationcode_blue_print.route("/")
def index():
    return render_template ("Enter_Confirmation_Code")