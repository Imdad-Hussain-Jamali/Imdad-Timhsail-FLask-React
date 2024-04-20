from flask import Flask,redirect,url_for,render_template,request 
#User Authnteication Blue Prints  
from BLUE_PRINTS.User_Authentication_BluePrints.Login import Login_blue_print
from BLUE_PRINTS.User_Authentication_BluePrints.Register import Register_blue_print
from BLUE_PRINTS.User_Authentication_BluePrints.IncorrectPassword import IncorrectPasssword_blue_print
from BLUE_PRINTS.User_Authentication_BluePrints.forgotpassword import FORGOTPASSWORD_blue_print
from BLUE_PRINTS.User_Authentication_BluePrints.Enterconfrimationcode import EnterConformationcode_blue_print
#test page Blue_Prints
from BLUE_PRINTS.TestPages.StartTestPage import StartTestPage_blue_print
from BLUE_PRINTS.TestPages.TestContne import TestContinue_blue_print
# Results Page Blue_prints
from BLUE_PRINTS.Results_BluePrints_Folder.MainResults import MainResults_blue_print
from BLUE_PRINTS.Results_BluePrints_Folder.Chart import Chart_blue_print
from BLUE_PRINTS.Results_BluePrints_Folder.Bars import Bars_blue_print
from BLUE_PRINTS.Results_BluePrints_Folder.Table import Table_blue_print
# Premium_Plan_Pages_Blue_Prints
from BLUE_PRINTS.Premium_Plan_Pages_Blue_Prints.Selectplan import Select_Plan_blue_print
from BLUE_PRINTS.Premium_Plan_Pages_Blue_Prints.Select_Payment_Method import Select_Payment_Method_blue_print
from BLUE_PRINTS.Premium_Plan_Pages_Blue_Prints.Purchase_Successfull import Purchase_SUccessfull_blue_print

# Users Dashboard
from BLUE_PRINTS.Userashboard_BluePrints.free_User_Dashobard.free_User_Dashborad import FreeUser_Dashboard_blue_print
from BLUE_PRINTS.Userashboard_BluePrints.Premium_Student_User_Dashboard.Premium_Student_User_Dashboard import Premium_Student_Dashboard_blue_print
from BLUE_PRINTS.Userashboard_BluePrints.Premium_Teacher_Dashboard.Premium_Teacher_Dashobaord import Premium_Teacher_Dashboard_blue_print

app = Flask (__name__)


#User Authentication Blue Printts
app.register_blueprint(Login_blue_print, url_prefix="/Login")
app.register_blueprint(Register_blue_print, url_prefix="/Register")
app.register_blueprint(IncorrectPasssword_blue_print, url_prefix="/IncorrectPassword")
app.register_blueprint(FORGOTPASSWORD_blue_print, url_prefix="/ForgotPassword")
app.register_blueprint(EnterConformationcode_blue_print, url_prefix="/EnterConfirmationCode")
#Test Pages Blue Printts
app.register_blueprint(StartTestPage_blue_print,url_prefix="/StartTestPage")
app.register_blueprint(TestContinue_blue_print,url_prefix="/TestContinue")
#Results Pages Blue Printts
app.register_blueprint(MainResults_blue_print,url_prefix="/MainResult")
app.register_blueprint(Chart_blue_print,url_prefix="/Chart")
app.register_blueprint(Bars_blue_print,url_prefix="/Bars")
app.register_blueprint(Table_blue_print,url_prefix="/Table")
#Results Pages Blue Printts
app.register_blueprint(Select_Plan_blue_print, url_prefix="/Select_Plan_blue_print")
app.register_blueprint(Select_Payment_Method_blue_print, url_prefix="/Select_Payment_Method_blue_print")
app.register_blueprint(Purchase_SUccessfull_blue_print,url_prefix = "/Purchase_SUccessfull_blue_print")
#User_Dashboard_BluePrints
app.register_blueprint(FreeUser_Dashboard_blue_print,url_prefix = "/FreeUser_Dashboard_blue_print")
app.register_blueprint(Premium_Student_Dashboard_blue_print,url_prefix = "/Premium_Student_Dashboard_blue_print")
app.register_blueprint(Premium_Teacher_Dashboard_blue_print,url_prefix = "/Premium_Teacher_Dashboard_blue_print")


#Indexroute
@app.route("/")
def index ():
    return render_template ("index.html")

#App Run Part



if __name__ == '__main__':
    app.run(debug=True)