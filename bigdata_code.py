

from pymongo import MongoClient
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from functools import partial
import pprint
from bson.code import Code
from pywebio import start_server,config
import time
import random as r
from pywebio.session import run_js
from pywebio.session import set_env
from pywebio.output import put_html
import base64


def convert_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        base64_str = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_str


def background_home():
    # Path to your image
    image_path = "D:\output.png"

    # Convert image to base64
    base64_str = convert_image_to_base64(image_path)

    # Define the HTML with inline CSS for background image
    html_content = f'''
    <html>
    <head>
        <style>
            body {{
                background-image: url(data:image/jpeg;base64,{base64_str});
                background-size: 700px;
                background-position: right;
                background-repeat:no-repeat;
            }}
        </style>
    </head>
    <body>
    </body>
    </html>
    '''

    # Put the HTML content to the web page
    put_html(html_content)


dba = MongoClient().aggregation_example
from bson.son import SON
from pymongo import DESCENDING, ASCENDING

######conection#######
client = MongoClient('localhost', 27017)
dbs = client.list_database_names()
db = client.get_database('mydb')
collection_names = db.list_collection_names()
p_collection = db.get_collection("patient_info")
cursor = p_collection.find()
e_collection = db.get_collection("exercises_info")
cursor = e_collection.find()
t_collection = db.get_collection("Taget")
cursor = t_collection.find()
d_collection = db.get_collection("Doctors")


def background_page(image_path,size,position="center"):
    # Path to your image
    # Convert image to base64

    base64_str = convert_image_to_base64(image_path)

    # Define the HTML with inline CSS for background image
    html_content = f'''
    <html>
    <head>
        <style>
            body {{
                background-image: url(data:image/jpeg;base64,{base64_str});
                background-size: {size}px;
                background-position: {position};
                background-repeat:no-repeat;
                
            }}
        </style>
    </head>
    <body>
    </body>
    </html>
    '''

    # Put the HTML content to the web page
    put_html(html_content)


def background_page2(image_path1,image_path2,size1=250,size2=200,position1="250px 300px",position2="1000px 450px"):
    # Path to your image
    # Convert image to base64

    base64_str1 = convert_image_to_base64(image_path1)
    base64_str2 = convert_image_to_base64(image_path2)

    # Define the HTML with inline CSS for background image
    html_content = f'''
    <html>
    <head>
        <style>
            body {{
                background-image: url(data:image/jpeg;base64,{base64_str1}), url(data:image/jpeg;base64,{base64_str2});
            background-size: {size1}px , {size2}px ;  /* Adjust size for both images */
            background-position:  {position1} ,{position2}; /* Position first image on the left, second on the right */
            background-repeat: no-repeat, no-repeat;

            }}
        </style>
    </head>
    <body>
    </body>
    </html>
    '''

    # Put the HTML content to the web page
    put_html(html_content)



def main_form():
  
    put_text("Welcome to the main form!")
    put_buttons(['Back to Main'], onclick=lambda btn_val: main_form())


#custom css styling for our buttons
css = """
#pywebio-scope-background button{
    width:40%;
    height:10%;
    position:relative; 
    left:32%;
    
}
"""

#configure the theme and styling to our buttons 
config(theme='minty')
@config(css_style=css)
def bground():
    hide_footer_css = """
    <style>
    .pywebio_footer {
        display: none;
    }
    </style>
    """
    put_html(hide_footer_css)
    
    
    set_env(title='Patient Management System')
    put_scope("background").style('''padding-top:5px;padding-bottom:5%;left:1%;position:fixed;
            border-radius:20px; background: rgb(84,121,128);background: 
            linear-gradient(0deg, rgba(84,121,128,1) 32%, rgba(45,150,152,1) 49%, rgba(153,153,153,1) 69%, rgba(47,149,153,1) 89%);
            ''')
    with use_scope("background"):
        #app Title Header
        put_html("<br/>")
        put_html("<h1> WELCOME TO <br/> The Ultimate patient Management System </h1>").style('''text-align:center;font-weight:650px; 
        font-style:bold;font-size:40px;color:#ffffff;text-shadow: 1.5px 1.5px #ff0000;''')


        #create a scope for call to Action buttons
        with use_scope("CTA",clear=True):
            put_html("<br/><br/>")
            put_button("Home page", onclick= lambda: b_click())

                 
           
    with use_scope("name1"):
        
        H="""<div class="txt" style="text-align: center;width:50%;background-color:#eff7fa;color:black;font-weight:200px;font-size:20px;border-radius:20px;left:3%;bottom:5%;justify-content:center;position:fixed" >
                    <h3 style="">Goal of project</h3>
                    <p class="asd" style="font-style:bold;">
                       In this project, we analyze a dataset containing a range of health metrics from heart patients, including age, blood pressure, heart rate, and other relevant factors.
 The primary objective is to develop a predictive model that can accurately identify individuals at risk of heart disease.
 Given the serious implications of failing to diagnose heart disease, our key focus is on maximizing the model's ability to identify all potential cases.
 Therefore, recall for the positive class—correctly identifying all patients with heart disease—is the most crucial performance metric for our model.
                    </p>
                   
                </div>"""
        put_html(H)
        background_home()



########insert#######
def Insert_click():
    put_button("Home",onclick=b_click)

    clear("display")

    #idCode = r.randint(1000,1500)
    new = input_group(
        "Insert Data",
        [
            input('ID', name='ID', type='number', style=" width: 150px;", help_text="Enter the ID of the patient"),
            input('Age', name='Age', type='number', style=" width: 150px;", help_text="Enter the Agr of the patient"),
            input('Sex', name='Sex', type='number', style=" width: 150px;",
                  help_text="Enter the gender of the patient :\n 0 for males \n 1 for females"),
            input('chest pain ', name='Cp', type='number', style=" width: 150px;",
                  help_text="Four types of chest pain are present"),
            input('Trestbps', name='Trestbps', type='number', style=" width: 150px;", help_text="blood pressure"),
            input('Chol', name='Chol', type='number', style=" width: 150px;",help_text="cholesterol level\n"),
            input('Fbs', name='Fbs', type='number', style=" width: 150px;",
                  help_text="fasting blood suger\n 0 for less than 120 mg/dl and 1  gor greater than 120 mg/dl"),
            input('Restecg', name='Restecg', type='number', style=" width: 150px;",
                  help_text="Three unique results are present\n  from 0 to 2"),
            input('Thalach', name='Thalach', type='number', style=" width: 150px;", help_text="heart rate"),
            input('Exang', name='Exang', type='number', style=" width: 150px;",
                  help_text="only to values 1 and 0 for no exercise-induced angina"),
            input('OldPeak', name='OldPeak', type='float', style=" width: 150px;",
                  help_text="ST depression induced by exercise"),
            input('Slope', name='Slope', type='number', style=" width: 150px;",
                  help_text="Three unique slopes are present from 0 to 2"),
            input('Ca', name='Ca', type='number', style=" width: 150px;",
                  help_text="There are five unique values for the number of major vessels colored by fluoroscopy from 0 to 4"),
            input('Thal', name='Thal', type='number', style=" width: 150px;",
                  help_text="reversible defect\n Four unique values from 0 to 3"),
            input('Target', name='Target', type='number', style=" width: 150px;",
                  help_text="Two unique values indicate the presence(1) or absence(0) of heart disease"),
        ]
    )

    patient_document = {'_id': new['ID'], 'age': new['Age'], 'sex': new['Sex'], 'E_IDD': new['ID'], 'T_IDD': new['ID']}
    e_document = {'_id': new['ID'], 'cp': new['Cp'], 'trestbps': new['Trestbps'], 'chol': new['Chol'],
                  'fbs': new['Fbs'], 'restecg': new['Restecg'], 'thalach': new['Thalach'], 'exang': new['Exang'],
                  'P_id': new['ID'], 't_id': new['ID']}
    t_document = {'_id': new['ID'], 'oldpeak': new['OldPeak'], 'slope': new['Slope'], 'ca': new['Ca'],
                  'thal': new['Thal'], 'target': new['Target'], 'e_id': new['ID'], 'P_id': new['ID']}
    doc=p_collection.find()
    flage=False
    for id in doc:
        if id["_id"]==new["ID"]:
            flage=True
            popup("Duplicated ID",[put_button("OK",onclick=close_popup)])
    if flage==False:
     try:
        res1 = p_collection.insert_one(patient_document)
        res2 = e_collection.insert_one(e_document)
        res3 = t_collection.insert_one(t_document)
        popup("Successfuly Inserted", [put_button("ok", onclick=close_popup)])
     except:
        p_collection.delete_one({'_id': new['ID']})
        e_collection.delete_one({'_id': new['ID']})
        t_collection.delete_one({'_id': new['ID']})
        popup("Invalid or empty data", [put_button("ok", onclick=close_popup)])


def delete_click():
    #put_button("Home",onclick=b_click)
    clear()
    #background_page("D:\\basket.png",280,"500px 300px")
    put_button("Home", onclick=b_click)
    background_page2("D:\\cleaner.jpg", "D:\\basket_new.png")

    btn_vall = select("Choose the operation",
                     options=["Delete One by Choosing field", "Delete Many by Choosing field", "Delete by choosing query"])
    return btn_vall

def del_click(btn_val):
    clear()
    background_page2("D:\\cleaner.jpg", "D:\\basket_new.png")

    if btn_val == "Delete One by Choosing field":

        #put_button("Back", onclick=delete_click)
        put_button("Home", onclick=b_click)
        put_text("choose field\n")
        felid = select('choose Feild',
                       ["ID", "Age", "Sex", "Cp", "Trestbps", "Chol", "Fbs", "Restecg", "Thalach", "Exang", "OldPeak",
                        "Slope", "Ca", "Thal", "Target"])
        if felid == "ID":
            new = input_group("delete", [
                input('ID', name="ID", type='number', help_text="enter the ID that we want to delete it\n Empty feild means 0")])
            doc=p_collection.find()
            flage=False
            for id in doc:
              if id["_id"]==new["ID"]:
                flage=True
            if flage==True:
              p_collection.delete_one({'_id': new['ID']})
              e_collection.delete_one({'_id': new['ID']})
              t_collection.delete_one({'_id': new['ID']})
              popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of ID is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Age":
            new = input_group("delete", [
                input('Age', name="Age", type='number', help_text="enter the Age that we want to delete it\n Empty feild means 0")])
            doc=p_collection.find()
            flage=False
            for age in doc:
              if age["age"]==new["Age"]:
                flage=True
            if flage==True:
             id = p_collection.find_one({'age': new['Age']})
             p_collection.delete_one({'_id':id["_id"] })
             e_collection.delete_one({'_id':id['E_IDD']})
             t_collection.delete_one({'_id': id["T_IDD"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Age is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Sex":
            new = input_group("delete", [
                input('Sex', name="Sex", type='number', help_text="enter the Sex that we want to delete it\n Empty feild means 0")])
            doc=p_collection.find()
            flage=False
            for sex in doc:
              if sex["sex"]==new["Sex"]:
                flage=True
            if flage==True:
             id = p_collection.find_one({'sex': new['Sex']})
             p_collection.delete_one({'_id':id["_id"]})
             e_collection.delete_one({'_id': id['E_IDD']})
             t_collection.delete_one({'_id': id["T_IDD"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Sex is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Cp":
            new = input_group("delete", [
                input('Cp', name="Cp", type='number', help_text="enter the Cp that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for cp in doc:
              if cp["cp"]==new["Cp"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'cp': new['Cp']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Cp is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Trestbps":
            new = input_group("delete", [input('Trestbps', name="Trestbps", type='number',
                                               help_text="enter the Trestbps that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for trestbps in doc:
              if trestbps["trestbps"]==new["Trestbps"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'trestbps': new['Trestbps']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Trestbps is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Chol":
            new = input_group("delete", [
                input('Chol', name="Chol", type='number', help_text="enter the Chol that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Chol in doc:
              if Chol["chol"]==new["Chol"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'chol': new['Chol']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Chol is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Fbs":
            new = input_group("delete", [
                input('Fbs', name="Fbs", type='number', help_text="enter the Fbs that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Fbs in doc:
              if Fbs["fbs"]==new["Fbs"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'fbs': new['Fbs']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Fbs is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Restecg":
            new = input_group("delete", [input('Restecg', name="Restecg", type='number',
                                               help_text="enter the Restecg that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Restecg in doc:
              if Restecg["restecg"]==new["Restecg"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'restecg': new['Restecg']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Restecg is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Thalach":
            new = input_group("delete", [input('Thalach', name="Thalach", type='number',
                                               help_text="enter the Thalach that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Thalach in doc:
              if Thalach["thalach"]==new["Thalach"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'thalach': new['Thalach']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Thalach is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Exang":
            new = input_group("delete", [
                input('Exang', name="Exang", type='number', help_text="enter the Exang that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Exang in doc:
              if Exang["exang"]==new["Exang"]:
                flage=True
            if flage==True:
             id = e_collection.find_one({'exang': new['Exang']})
             e_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             t_collection.delete_one({'_id': id["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Exang is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Slope":
            new = input_group("delete", [
                input('Slope', name="Slope", type='number', help_text="enter the Slope that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Slope in doc:
              if Slope['slope']==new["Slope"]:
                flage=True
            if flage==True:
             id = t_collection.find_one({'slope': new['Slope']})
             t_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             e_collection.delete_one({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Slope is not found",[put_button("OK",onclick=close_popup)])
        if felid == "OldPeak":
            new = input_group("delete", [input('OldPeak', name="OldPeak", type='number',
                                               help_text="enter the OldPeak that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for OldPeak in doc:
              if OldPeak['oldpeak']==new["OldPeak"]:
                flage=True
            if flage==True:
             id = t_collection.find_one({'oldpeak': new['OldPeak']})
             t_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             e_collection.delete_one({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the OldPeak is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Ca":
            new = input_group("delete", [
                input('Ca', name="Ca", type='number', help_text="enter the Ca that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Ca in doc:
              if Ca['ca']==new["Ca"]:
                flage=True
            if flage==True:
             id = t_collection.find_one({'ca': new['Ca']})
             t_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             e_collection.delete_one({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Ca is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Thal":
            new = input_group("delete", [
                input('Thal', name="Thal", type='number', help_text="enter the Thal that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Thal in doc:
              if Thal['thal']==new["Thal"]:
                flage=True
            if flage==True:
             id = t_collection.find_one({'thal': new['Thal']})
             t_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             e_collection.delete_one({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Thal is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Target":
            new = input_group("delete", [
                input('Target', name="Target", type='number', help_text="enter the Target that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Target in doc:
              if Target['target']==new["Target"]:
                flage=True
            if flage==True:
             id = t_collection.find_one({'target': new['Target']})
             t_collection.delete_one({'_id': id["_id"]})
             p_collection.delete_one({'_id': id["P_id"]})
             e_collection.delete_one({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Target is not found",[put_button("OK",onclick=close_popup)])
    elif btn_val == "Delete Many by Choosing field":
        clear()
        #put_button("Back", onclick=delete_click)
        put_button("Home", onclick=b_click)

        put_text("choose field\n")
        felid = select('choose Feild',

                       [ "Age", "Sex", "Cp", "Trestbps", "Chol", "Fbs", "Restecg", "Thalach", "Exang", "OldPeak",
                        "Slope", "Ca", "Thal", "Target"])
        if felid == "Age":
            new = input_group("delete", [
                input('Age', name="Age", type='number', help_text="enter the Age that we want to delete it\n Empty feild means 0")])
            doc=p_collection.find()
            flage=False
            for age in doc:
              if age["age"]==new["Age"]:
                flage=True
            if flage==True:
             id = p_collection.find({'age': new['Age']})
             for doc in id:
               p_collection.delete_many({'_id':doc["_id"] })
               e_collection.delete_many({'_id':doc['E_IDD']})
               t_collection.delete_many({'_id': doc["T_IDD"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Age is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Sex":
            new = input_group("delete", [
                input('Sex', name="Sex", type='number', help_text="enter the Sex that we want to delete it\n Empty feild means 0")])
            doc=p_collection.find()
            flage=False
            for sex in doc:
              if sex["sex"]==new["Sex"]:
                flage=True
            if flage==True:
             id = p_collection.find({'sex': new['Sex']})
             for doc in id:
               p_collection.delete_many({'_id':doc["_id"]})
               e_collection.delete_one({'_id': doc['E_IDD']})
               t_collection.delete_many({'_id': doc["T_IDD"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Sex is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Cp":
            new = input_group("delete", [
                input('Cp', name="Cp", type='number', help_text="enter the Cp that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for cp in doc:
              if cp["cp"]==new["Cp"]:
                flage=True
            if flage==True:
             id = e_collection.find({'cp': new['Cp']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Cp is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Trestbps":
            new = input_group("delete", [input('Trestbps', name="Trestbps", type='number',
                                               help_text="enter the Trestbps that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for trestbps in doc:
              if trestbps["trestbps"]==new["Trestbps"]:
                flage=True
            if flage==True:
             id = e_collection.find({'trestbps': new['Trestbps']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Trestbps is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Chol":
            new = input_group("delete", [
                input('Chol', name="Chol", type='number', help_text="enter the Chol that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Chol in doc:
              if Chol["chol"]==new["Chol"]:
                flage=True
            if flage==True:
             id = e_collection.find({'chol': new['Chol']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Chol is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Fbs":
            new = input_group("delete", [
                input('Fbs', name="Fbs", type='number', help_text="enter the Fbs that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Fbs in doc:
              if Fbs["fbs"]==new["Fbs"]:
                flage=True
            if flage==True:
             id = e_collection.find({'fbs': new['Fbs']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Fbs is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Restecg":
            new = input_group("delete", [input('Restecg', name="Restecg", type='number',
                                               help_text="enter the Restecg that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Restecg in doc:
              if Restecg["restecg"]==new["Restecg"]:
                flage=True
            if flage==True:
             id = e_collection.find({'restecg': new['Restecg']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Restecg is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Thalach":
            new = input_group("delete", [input('Thalach', name="Thalach", type='number',
                                               help_text="enter the Thalach that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Thalach in doc:
              if Thalach["thalach"]==new["Thalach"]:
                flage=True
            if flage==True:
             id = e_collection.find({'thalach': new['Thalach']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Thalach is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Exang":
            new = input_group("delete", [
                input('Exang', name="Exang", type='number', help_text="enter the Exang that we want to delete it\n Empty feild means 0")])
            doc=e_collection.find()
            flage=False
            for Exang in doc:
              if Exang["exang"]==new["Exang"]:
                flage=True
            if flage==True:
             id = e_collection.find({'exang': new['Exang']})
             for doc in id:
               e_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               t_collection.delete_many({'_id': doc["t_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Exang is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Slope":
            new = input_group("delete", [
                input('Slope', name="Slope", type='number', help_text="enter the Slope that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Slope in doc:
              if Slope['slope']==new["Slope"]:
                flage=True
            if flage==True:
             id = t_collection.find({'slope': new['Slope']})
             for doc in id:
               t_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               e_collection.delete_many({'_id': doc["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Slope is not found",[put_button("OK",onclick=close_popup)])
        if felid == "OldPeak":
            new = input_group("delete", [input('OldPeak', name="OldPeak", type='float',
                                               help_text="enter the OldPeak that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for OldPeak in doc:
              print(OldPeak['oldpeak'])
              if OldPeak['oldpeak']==new['OldPeak']:
                flage=True
            if flage==True:
             id = t_collection.find({'oldpeak': new['OldPeak']})
             for doc in id:
               t_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               e_collection.delete_many({'_id': doc["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the OldPeak is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Ca":
            new = input_group("delete", [
                input('Ca', name="Ca", type='number', help_text="enter the Ca that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Ca in doc:
              if Ca['ca']==new["Ca"]:
                flage=True
            if flage==True:
             id = t_collection.find({'ca': new['Ca']})
             for doc in id:
               t_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               e_collection.delete_many({'_id': doc["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Ca is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Thal":
            new = input_group("delete", [
                input('Thal', name="Thal", type='number', help_text="enter the Thal that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Thal in doc:
              if Thal['thal']==new["Thal"]:
                flage=True
            if flage==True:
             id = t_collection.find({'thal': new['Thal']})
             for doc in id:
               t_collection.delete_many({'_id': id["_id"]})
               p_collection.delete_many({'_id': id["P_id"]})
               e_collection.delete_many({'_id': id["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Thal is not found",[put_button("OK",onclick=close_popup)])
        if felid == "Target":
            new = input_group("delete", [
                input('Target', name="Target", type='number', help_text="enter the Target that we want to delete it\n Empty feild means 0")])
            doc=t_collection.find()
            flage=False
            for Target in doc:
              if Target['target']==new["Target"]:
                flage=True
            if flage==True:
             id = t_collection.find({'target': new['Target']})
             for doc in id:
               t_collection.delete_many({'_id': doc["_id"]})
               p_collection.delete_many({'_id': doc["P_id"]})
               e_collection.delete_many({'_id': doc["e_id"]})
             popup("Deleted Successfuly",[put_button("OK",onclick=close_popup)])
            elif flage==False:
                popup("The Value of the Target is not found",[put_button("OK",onclick=close_popup)])
    elif btn_val== "Delete by choosing query":
        clear()
        #put_button("Back", onclick=delete_click)
        put_button("Home", onclick=b_click)
        Query = select("choose collection", ['Q1:Delete all patient when age >70 and oldpeak =0', 'Q2:Delete all patient when Gender is male and the Fbs<120', 'Q3:Delete all patient when Trestbps <=250 and slope =0','Q4:Delete all patient when age >60 and thalch >150 and oldpeak<=1'])
        if Query=='Q1:Delete all patient when age >70 and oldpeak =0':
            doc1 =p_collection.find({'age':{'$gt':70}})
            for Q1 in doc1:
              doc2=t_collection.find({'$and':[{'_id':Q1['T_IDD']},{'oldpeak':0}]})
              for Q2 in doc2:
                p_collection.delete_one({"_id":Q2['P_id']})
                e_collection.delete_one({"_id":Q2['e_id']})
                t_collection.delete_one({"_id":Q2['_id']})
            popup("Successfuly Deleted",[put_buttob("OK",onclick=close_popup)])
        if Query=='Q2:Delete all patient when Gender is male and the Fbs<120':
            doc1 =p_collection.find({'sex':0})
            for Q1 in doc1:
              doc2=e_collection.find({'$and':[{'_id':Q1['E_IDD']},{'fbs':0}]})
              for Q2 in doc2:
                p_collection.delete_one({"_id":Q2['P_id']})
                e_collection.delete_one({"_id":Q2['_id']})
                t_collection.delete_one({"_id":Q2['t_id']})
            popup("Successfuly Deleted",[put_buttob("OK",onclick=close_popup)])
        if Query== 'Q3:Delete all patient when Trestbps <=250 and slope =0':
            doc1 =e_collection.find({'trestbps':{'$lte':250}})
            for Q1 in doc1:
              doc2=t_collection.find({'$and':[{'_id':Q1['t_id']},{'slope':0}]})
              for Q2 in doc2:
                p_collection.delete_one({"_id":Q2['P_id']})
                e_collection.delete_one({"_id":Q2['e_id']})
                t_collection.delete_one({"_id":Q2['_id']})
            popup("Successfuly Deleted",[put_buttob("OK",onclick=close_popup)])
        if Query=='Q4:Delete all patient when age >60 and thalch >150 and oldpeak<=1':
            doc1 =p_collection.find({'age':{'$gt':60}})
            for Q1 in doc1:
                 doc2 =e_collection.find({"$and":[{'thalach':{'$gt':150}},{'_id':Q1['E_IDD']}]})
                 for Q3 in doc2:
                     doc3=t_collection.find({"$and":[{'oldpeak':{'$lte':1}},{'_id':Q3['t_id']}]})
                     for Q3 in doc3:
                      p_collection.delete_one({"_id":Q3['P_id']})
                      e_collection.delete_one({"_id":Q3['e_id']})
                      t_collection.delete_one({"_id":Q3['_id']})
            popup("Successfuly Deleted",[put_buttob("OK",onclick=close_popup)])



def update_click():
    clear()

    put_button("Home",onclick=b_click)
    background_page("D:\\update.jpg",800,"700px 250px")
    re = select("choose the operation",
             options=["Update One", "Update Many", "Update by typing query in one collection","Update by typing query in two collections", "Update by  choosing query"])
    return re


def upd_click(btn_val):
    clear()
    #put_button("Back", onclick=update_click)
    put_button("Home", onclick=b_click)
    background_page("D:\\update.jpg", 800, "700px 250px")
    if btn_val == "Update One":
        felid = select('choose Feild',
                       ["Age", "Sex", "Cp", "Trestbps", "Chol", "Fbs", "Restecg", "Thalach", "Exang", "OldPeak",
                        "Slope", "Ca", "Thal", "Target"])
        if felid == "Age":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Age "),
                                         input('new', name="new", type='number', help_text="enter the  new Age ")])
            doc= p_collection.find()
            flage=False
            for d in doc:
                if d["age"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"age": new['old']}
              update = {"$set": {"age": new['new']}}
              try:
                p_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Sex":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Sex "),
                                         input('new', name="new", type='number', help_text="enter the  new Sex ")])
            doc= p_collection.find()
            flage=False
            for d in doc:
                if d["sex"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"sex": new['old']}
              update = {"$set": {"sex": new['new']}}
              try:
                p_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Cp":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Cp "),
                                         input('new', name="new", type='number', help_text="enter the  new Cp ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["cp"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"cp": new['old']}
              update = {"$set": {"cp": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Trestbps":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Trestbps "),
                                         input('new', name="new", type='number', help_text="enter the  new Trestbps ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["trestbps"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"trestbps": new['old']}
              update = {"$set": {"trestbps": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Chol":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Chol "),
                                         input('new', name="new", type='number', help_text="enter the  new Chol ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["chol"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"chol": new['old']}
              update = {"$set": {"chol": new['new']}}
              try:
                e_collection.update_one(filter, update)
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
              popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Fbs":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Fbs "),
                                         input('new', name="new", type='number', help_text="enter the  new Fbs ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["fbs"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"fbs": new['old']}
              update = {"$set": {"fbs": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Restecg":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Restecg "),
                                         input('new', name="new", type='number', help_text="enter the  new Restecg ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["restecg"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"restecg": new['old']}
              update = {"$set": {"restecg": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Thalach":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Thalach "),
                                         input('new', name="new", type='number', help_text="enter the  new Thalach ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["thalach"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"thalach": new['old']}
              update = {"$set": {"thalach": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Exang":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Exang "),
                                         input('new', name="new", type='number', help_text="enter the  new Exang ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["exang"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"exang": new['old']}
              update = {"$set": {"exang": new['new']}}
              try:
                e_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "OldPeak":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old OldPeak "),
                                         input('new', name="new", type='number', help_text="enter the  new OldPeak ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["oldpeak"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"oldpeak": new['old']}
              update = {"$set": {"oldpeak": new['new']}}
              try:
                t_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Slope":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Slope "),
                                         input('new', name="new", type='number', help_text="enter the  new Slope ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["slope"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"slope": new['old']}
              update = {"$set": {"slope": new['new']}}
              try:
                t_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Ca":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Ca "),
                                         input('new', name="new", type='number', help_text="enter the  new Ca ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["ca"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"ca": new['old']}
              update = {"$set": {"ca": new['new']}}
              try:
                t_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Thal":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Thal "),
                                         input('new', name="new", type='number', help_text="enter the  new Thal ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["thal"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"thal": new['old']}
              update = {"$set": {"thal": new['new']}}
              try:
                t_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Target":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Target "),
                                         input('new', name="new", type='number', help_text="enter the  new Target ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["target"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"target": new['old']}
              update = {"$set": {"target": new['new']}}
              try:
                t_collection.update_one(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])

    elif btn_val == "Update Many":
        felid = select('choose Feild',
                       ["Age", "Sex", "Cp", "Trestbps", "Chol", "Fbs", "Restecg", "Thalach", "Exang", "OldPeak",
                        "Slope", "Ca", "Thal", "Target"])
        if felid == "Age":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Age "),
                                         input('new', name="new", type='number', help_text="enter the  new Age ")])
            doc= p_collection.find()
            flage=False
            for d in doc:
                if d["age"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"age": new['old']}
              update = {"$set": {"age": new['new']}}
              try:
                p_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Sex":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Sex "),
                                         input('new', name="new", type='number', help_text="enter the  new Sex ")])
            doc= p_collection.find()
            flage=False
            for d in doc:
                if d["sex"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"sex": new['old']}
              update = {"$set": {"sex": new['new']}}
              try:
                p_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Cp":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Cp "),
                                         input('new', name="new", type='number', help_text="enter the  new Cp ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["cp"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"cp": new['old']}
              update = {"$set": {"cp": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Trestbps":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Trestbps "),
                                         input('new', name="new", type='number', help_text="enter the  new Trestbps ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["trestbps"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"trestbps": new['old']}
              update = {"$set": {"trestbps": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Chol":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Chol "),
                                         input('new', name="new", type='number', help_text="enter the  new Chol ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["chol"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"chol": new['old']}
              update = {"$set": {"chol": new['new']}}
              try:
                e_collection.update_many(filter, update)
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
              popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Fbs":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Fbs "),
                                         input('new', name="new", type='number', help_text="enter the  new Fbs ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["fbs"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"fbs": new['old']}
              update = {"$set": {"fbs": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Restecg":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Restecg "),
                                         input('new', name="new", type='number', help_text="enter the  new Restecg ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["restecg"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"restecg": new['old']}
              update = {"$set": {"restecg": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Thalach":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Thalach "),
                                         input('new', name="new", type='number', help_text="enter the  new Thalach ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["thalach"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"thalach": new['old']}
              update = {"$set": {"thalach": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Exang":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Exang "),
                                         input('new', name="new", type='number', help_text="enter the  new Exang ")])
            doc= e_collection.find()
            flage=False
            for d in doc:
                if d["exang"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"exang": new['old']}
              update = {"$set": {"exang": new['new']}}
              try:
                e_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "OldPeak":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old OldPeak "),
                                         input('new', name="new", type='number', help_text="enter the  new OldPeak ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["oldpeak"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"oldpeak": new['old']}
              update = {"$set": {"oldpeak": new['new']}}
              try:
                t_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Slope":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Slope "),
                                         input('new', name="new", type='number', help_text="enter the  new Slope ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["slope"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"slope": new['old']}
              update = {"$set": {"slope": new['new']}}
              try:
                t_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Ca":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Ca "),
                                         input('new', name="new", type='number', help_text="enter the  new Ca ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["ca"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"ca": new['old']}
              update = {"$set": {"ca": new['new']}}
              try:
                t_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Thal":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Thal "),
                                         input('new', name="new", type='number', help_text="enter the  new Thal ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["thal"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"thal": new['old']}
              update = {"$set": {"thal": new['new']}}
              try:
                t_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
        if felid == "Target":
            new = input_group("Update", [input('old', name="old", type='number', help_text="enter the  old Target "),
                                         input('new', name="new", type='number', help_text="enter the  new Target ")])
            doc= t_collection.find()
            flage=False
            for d in doc:
                if d["target"]==new["old"]:
                    flage=True
            if flage==True:
              filter = {"target": new['old']}
              update = {"$set": {"target": new['new']}}
              try:
                t_collection.update_many(filter, update)
                popup("Successfuly updated", [put_button("ok", onclick=close_popup)])
              except:
                  popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
            elif flage==False: 
                popup("invalid data,no updating", [put_button("ok", onclick=close_popup)])
    elif btn_val == "Update by typing query in one collection":
        collection = select("choose collection", ['ONE:patien collection', 'ONE:exercises collection', 'ONE:Targrt collection',
                                                  'MANY:patien collection', 'MANY:exercises collection', 'MANY:Target collection',])
        if collection == "ONE:patien collection":
             new = input_group("query", [input("old", name="old"), input("new", name="new")])
             try:
               filter = eval(new["old"])
               update = eval(new['new'])
               p_collection.update_one(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
             except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
        if collection == 'ONE:exercises collection':
             new = input_group("query", [input("old", name="old"), input("new", name="new")])
             try:
               filter = eval(new["old"])
               update = eval(new['new'])
               e_collection.update_one(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
             except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
        if collection=="ONE:Targrt collection":
            new = input_group("query", [input("old", name="old"), input("new", name="new")])
            try:
               filter = eval(new["old"])
               update = eval(new['new'])
               t_collection.update_one(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
            except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
        if collection=='MANY:patien collection':
            new = input_group("query", [input("old", name="old"), input("new", name="new")])
            try:
               filter = eval(new["old"])
               update = eval(new['new'])
               p_collection.update_many(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
            except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
        if collection=='MANY:exercises collection':
            new = input_group("query", [input("old", name="old"), input("new", name="new")])
            try:
               filter = eval(new["old"])
               update = eval(new['new'])
               e_collection.update_one(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
            except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
        if collection=='MANY:Target collection':
            new = input_group("query", [input("old", name="old"), input("new", name="new")])
            try:
               filter = eval(new["old"])
               update = eval(new['new'])
               t_collection.update_one(filter, {'$set': update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
            except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
    elif btn_val=="Update by typing query in two collections":
          opt=select("Choose option",["Update ONE patien collection based on condition in exercises collection","Update ONE patien collection based on condition in Target collection",
                                       "Update MANY patien collection based on condition in exercises collection","Update MANY patien collection based on condition in Target collection",
                                       "Update ONE exercises collection based on condition in patien collection","Update ONE exercises collection based on condition in Target collection",
                                       "Update MANY exercises collection based on condition in patien collection","Update MANY exercises collection based on condition in Target collection",
                                        "Update ONE Target collection based on condition in patien collection","Update ONE Target collection based on condition in exercises collection",
                                       "Update MANY Target collection based on condition in patien collection","Update MANY Target collection based on condition in exercises collection"])
          if opt=="Update ONE patien collection based on condition in exercises collection":
             new = input_group("query", [input("exercises_query", name="exercises_query"), input("patien_query", name="patien_query")])
             try:
               f= eval(new['exercises_query'])
               update = eval(new['patien_query'])
               id=e_collection.find_one(f)
               p_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
             except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update ONE patien collection based on condition in Target collection":
              new = input_group("query", [input("target_query", name="target_query"), input("patien_query", name="patien_query")])
              try:
               f= eval(new['target_query'])
               update = eval(new['patien_query'])
               id=t_collection.find_one(f)
               p_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY patien collection based on condition in exercises collection":
              new = input_group("query", [input("exercises_query", name="exercises_query"), input("patien_query", name="patien_query")])
              try:
               f= eval(new['exercises_query'])
               update = eval(new['patien_query'])
               id=e_collection.find(f)
               for i in id:
                 p_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY patien collection based on condition in Target collection":
              new = input_group("query", [input("target_query", name="target_query"), input("patien_query", name="patien_query")])
              try:
               f= eval(new['target_query'])
               update = eval(new['patien_query'])
               id=t_collection.find(f)
               for i in id:
                 p_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update ONE exercises collection based on condition in patien collection":
              new = input_group("query", [input("patien_query", name="patien_query"), input("exercises_query", name="exercises_query")])
              try:
               f= eval(new['patien_query'])
               update = eval(new['exercises_query'])
               id=p_collection.find_one(f)
               e_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update ONE exercises collection based on condition in Target collection":
              new = input_group("query", [input("target_query", name="target_query"), input("exercises_query", name="exercises_query")])
              try:
               f= eval(new['target_query'])
               update = eval(new['exercises_query'])
               id=t_collection.find_one(f)
               e_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY exercises collection based on condition in patien collection":
              new = input_group("query", [input("patien_query", name="patien_query"), input("exercises_query", name="exercises_query")])
              try:
               f= eval(new['patien_query'])
               update = eval(new['exercises_query'])
               id=p_collection.find(f)
               for i in id:
                 e_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY exercises collection based on condition in Target collection":
              new = input_group("query", [input("target_query", name="target_query"), input("exercises_query", name="exercises_query")])
              try:
               f= eval(new['target_query'])
               update = eval(new['exercises_query'])
               id=t_collection.find(f)
               for i in id:
                 e_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update ONE Target collection based on condition in patien collection":
              new = input_group("query", [input("patien_query", name="patien_query"), input("target_query", name="target_query")])
              try:
               f= eval(new['patien_query'])
               update = eval(new['target_query'])
               id=p_collection.find_one(f)
               t_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update ONE Target collection based on condition in exercises collection":
              new = input_group("query", [input("exercises_query", name="exercises_query"), input("target_query", name="target_query")])
              try:
               f= eval(new['exercises_query'])
               update = eval(new['target_query'])
               id=e_collection.find_one(f)
               t_collection.update_one({"_id":id['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY Target collection based on condition in patien collection":
              new = input_group("query", [input("patien_query", name="patien_query"), input("target_query", name="target_query")])
              try:
               f= eval(new['patien_query'])
               update = eval(new['target_query'])
               id=p_collection.find(f)
               for i in id:
                 t_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
          if opt=="Update MANY Target collection based on condition in exercises collection":
              new = input_group("query", [input("exercises_query", name="exercises_query"), input("target_query", name="target_query")])
              try:
               f= eval(new['exercises_query'])
               update = eval(new['target_query'])
               id=e_collection.find(f)
               for i in id:
                 t_collection.update_one({"_id":i['_id']},{'$set':update})
               popup("DONE",[put_button("OK",onclick=close_popup)])
              except:
                popup("Invalid Data",[put_button("OK",onclick=close_popup)])
    elif btn_val == "Update by  choosing query":
        query = select('choose query', ["Q1:update all patient that having age greater than 50 ,their sex will be 50",
                                        "Q2:update all patient that having age less than 50 ,their sex will be 999",
                                        "Q3:"])
        if query == "Q1:update all patient that having age greater than 50 ,their sex will be 50":
            p_collection.update_many({"age": {"$gt": 50}}, {"$set": {"sex": 50}})
        elif query == "Q2:update all patient that having age less than 50 ,their sex will be 999":
            p_collection.update_many({"age": {"$lt": 50}}, {"$set": {"age": 999}})


def relation_click():
    clear()
    put_button("Home", onclick=b_click)
    background_page("D:\\relation_doctor.jpeg", 800, "700px 250px")
    opt = select('choose option', ["one Doctor", "All Doctors", "Relation with patien"])
    if opt == "one Doctor":
        id = input_group("doctor", [input("ID", type='number', name="ID")])
        did = {"_id": id["ID"]}
        try:
            D = db.Doctors.find_one(did)
            put_text(D)
        except:
            popup("not found", [put_button("ok", onclick=close_popup)])
    if opt == "All Doctors":
        D = db.Doctors.find({})
        for d in D:
            put_text(d)
    if opt == "Relation with patien":
        id = input_group("doctor", [input("ID", type='number', name="ID")])
        did = {"_id": id["ID"]}
        try:
            pid = db.Doctors.find_one(did)['p_id']
            patients = db.patient_info.find({'_id': {"$in": pid}})
            for p in patients:
                if len(p)!=0:
                  put_text(p)
                else:
                    put_text(" patient data has been deleted ")
        except:
            popup("not found", [put_button("ok", onclick=close_popup)])


def agregation_click():
    clear()
    put_button("Home", onclick=b_click)
    background_page("D:\\aggregation.jpeg", 800, "700px 250px")
    re=select('choose option', ["Patient Collection", "Exercieses Collection", "Target Collection", "Doctors Collection","Type an Aggregation","Aggregation in two collections"])
    return re

def agr_click(btn_val):
    clear("display")
    background_page("D:\\aggregation.jpeg", 800, "700px 250px")
    if btn_val == "Patient Collection":
        opt = select('choose option', ["count Gender", "see tha distinct values of gender"])
        if opt == "count Gender":
            put_text("This is the number of times male (0) and female (1) gender to appear")
            pipeline = [{"$group": {"_id": "$sex", "count": {"$sum": 1}}},
                        {"$sort": SON([("count", 1), ("_id", 1)])}]
            put_text(list(db.patient_info.aggregate(pipeline)))
        if opt == "see tha distinct values of gender":
            put_text(p_collection.distinct("sex"), "male (0) and female (1)")
    if btn_val == "Exercieses Collection":
        opt = select('choose option', ["Distinct Values", "Count the unique numbers",
                                       "minimun value for tresthps based on each value of restecg",
                                       "Average of trestbps for each value of Cp",
                                       "Max of chol for each value of fbs",
                                       "Average of thalach for each value of exang when restecg is (1)",
                                       "Matching all chol with value >200 ,limit(100)"])
        if opt == "Distinct Values":
            f = select("choose feild", ["Cp", "Fbs", "Restecg", "Exang"])
            if f == "Cp":
                put_text(e_collection.distinct("cp"))
                put_text(" Four unique types of chest pain are present")
            if f == "Fbs":
                put_text(e_collection.distinct("fbs"))
                put_text("There are two categories indicating fasting blood sugar ")
            if f == "Restecg":
                put_text(e_collection.distinct("restecg"))
                put_text("Three unique results are present")
            if f == "Exang":
                put_text(e_collection.distinct("exang"))
                put_text("There are two unique values for  exercise-induced angina")
        if opt == "Count the unique numbers":
            f = select("choose feild", ["Cp", "Fbs", "Restecg", "Exang"])
            if f == "Cp":
                pipeline = [{"$group": {"_id": "$cp", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.exercises_info.aggregate(pipeline)))
                put_text(" Four unique types of chest pain are present")
            if f == "Fbs":
                pipeline = [{"$group": {"_id": "$fbs", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.exercises_info.aggregate(pipeline)))
                put_text("There are two categories indicating fasting blood sugar ")
            if f == "Restecg":
                pipeline = [{"$group": {"_id": "$restecg", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.exercises_info.aggregate(pipeline)))
                put_text("Three unique results are present")
            if f == "Exang":
                pipeline = [{"$group": {"_id": "$exang", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.exercises_info.aggregate(pipeline)))
                put_text("There are two unique values for  exercise-induced angina")
        if opt=="minimun value for tresthps based on each value of restecg":
            c = db.exercises_info.aggregate([{"$group": {"_id": "$restecg", "mintresthps": {"$min": "$tresthps"}}}])
            for i in c:
                put_text(i)
        if opt == "Max of chol for each value of fbs":
            c = db.exercises_info.aggregate([{"$group": {"_id": "$fbs", "maxchol": {"$max": "$chol"}}}])
            for i in c:
                put_text(i)
        if opt == "Average of trestbps for each value of Cp":
            c = db.exercises_info.aggregate(
                [{"$group": {"_id": "$cp", "Avgtrestbps": {"$avg": "$trestbps"}}}, {"$sort": {"Avgtrestbps": 1}},
                 {"$project": {"Avg_trestbps": "$Avgtrestbps"}}])
            for i in c:
                put_text(i)
        if opt == "Average of thalach for each value of exang when restecg is (1)":
            c = db.exercises_info.aggregate(
                [{"$match": {"restecg": 1}}, {"$group": {"_id": "$exang", "Avgthalach": {"$avg": "$thalach"}}},
                 {"$sort": {"Avgthalach": 1}}, {"$project": {"Avg_thalach": "$Avgthalach"}}])
            for i in c:
                put_text(i)
        if opt=="Matching all chol with value >200 ,limit(100)":
                c = db.exercises_info.aggregate([{"$match": {"chol": {"$gt": 200}}}, {'$limit': 100}])
                for i in c:
                     put_text(i)
    if btn_val == "Target Collection":
        opt = select("Choose option", ["Distinct Values", "Matching oldpeak when the value >=0.5 ,limit equal 100"])
        if opt == "Distinct Values":
            f = select("choose feild", ["Target", "Thal", "Ca", "slope"])
            if f == "Target":
                put_text(t_collection.distinct("target"))
                put_text(" Two unique types of chest pain are present\n")
                put_text("and the count of them:\n")
                pipeline = [{"$group": {"_id": "$target", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.Taget.aggregate(pipeline)))
            if f == "Thal":
                put_text(t_collection.distinct("thal"))
                put_text(" four unique types of chest pain are present\n") ######
                put_text("and the count of them:\n")
                pipeline = [{"$group": {"_id": "$thal", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.Taget.aggregate(pipeline)))
            if f == "Ca":
                put_text(t_collection.distinct("ca"))
                put_text(" four unique types of chest pain are present\n")
                put_text("and the count of them:\n")
                pipeline = [{"$group": {"_id": "$ca", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.Taget.aggregate(pipeline)))
            if f == "slope":
                put_text(t_collection.distinct("slope"))
                put_text(" three unique types of chest pain are present\n")
                put_text("and the count of them:\n")
                pipeline = [{"$group": {"_id": "$slope", "count": {"$sum": 1}}},
                            {"$sort": SON([("count", 1), ("_id", 1)])}]
                put_text(list(db.Taget.aggregate(pipeline)))
        if opt == "Matching oldpeak when the value >=0.5 ,limit equal 100":
            Q = db.Taget.aggregate([{"$match": {"oldpeak": {"$gt": 0.5}}}, {'$limit': 100}])
            for i in Q:
                put_text(i)
    if btn_val == "Doctors Collection":
        put_text("This is the number of patient appearance in Doctors collection")
        pipeline = [
            {"$unwind": "$p_id"}, {"$group": {"_id": "$p_id", "count": {"$sum": 1}}},
            {"$sort": SON([("count", 1), ("_id", 1)])}]
        put_text(list(db.Doctors.aggregate(pipeline)))
    if btn_val=="Type an Aggregation":
       f=select('choose field', ["Patient Collection", "Exercieses Collection", "Target Collection"])
       if f=="Target Collection":
           new = input_group("Aggregation", [input('query', name="query",help_text="enter query"),input('query2', name="query2",help_text="enter query")])
           Q1=new['query']
           Q2=new['query2']
           try:
             st1=eval(Q1)
             st2=eval(Q2)
             Q=db.Taget.aggregate([st1,st2])
             for i in Q:
                put_text(i)
           except:
               popup("Invalid data",[put_button("OK",onclick=close_popup)])
       if f=="Patient Collection":
           new = input_group("Aggregation", [input('query', name="query",help_text="enter query"),input('query2', name="query2",help_text="enter query")])
           Q1=new['query']
           Q2=new['query2']
           try:
            st1=eval(Q1)
            st2=eval(Q2)
            Q=db.patient_info.aggregate([st1,st2])
            for i in Q:
                put_text(i)
           except:
               popup("Invalid data",[put_button("OK",onclick=close_popup)])
       if f=="Exercieses Collection":
           new = input_group("Aggregation", [input('query', name="query",help_text="enter query"),input('query2', name="query2",help_text="enter query")])
           Q1=new['query']
           Q2=new['query2']
           try:
             st1=eval(Q1)
             st2=eval(Q2)
             Q=db.exercises_info.aggregate([st1,st2])
             for i in Q:
                put_text(i)
           except:
               popup("Invalid data",[put_button("OK",onclick=close_popup)])
    if btn_val=="Aggregation in two collections":
        Aggregation=select("Choose Collections",["Exercieses Collection and Target Collection:Average for oldpeak for each value of chest pain","Patient Collection and Exercieses Collection:Average of trestbps for each gender",
                                                  "Target Collection and Exercieses Collection:Max of oldpeak in each value of fbs"])
        if Aggregation=="Exercieses Collection and Target Collection:Average for oldpeak for each value of chest pain":
            res=db.exercises_info.aggregate([{'$lookup':{'from':'Taget',
                    'localField':'_id',
                     'foreignField':'e_id',
                     'as':'j'
                    }},{'$unwind':'$j'},
            {"$group":{"_id":"$fbs" ,"avg_oldpeak": {"$avg": "$j.oldpeak"}}}])
            for r in res:
                   put_text(r)
        if Aggregation=="Patient Collection and Exercieses Collection:Average of trestbps for each gender":
            res2=db.patient_info.aggregate([{'$lookup':{'from':'exercises_info',
                    'localField':'_id',
                     'foreignField':'P_id',
                     'as':'joined'
                    }},{'$unwind':'$joined'},
            {"$group":{"_id":"$sex" ,"avg_trestbps": {"$avg": "$joined.trestbps"}}}])
            for r in res2:
                      put_text(r)
        if Aggregation=="Target Collection and Exercieses Collection:Max of oldpeak in each value of fbs":
            res3=db.exercises_info.aggregate([{'$lookup':{'from':'Taget',
                    'localField':'_id',
                     'foreignField':'e_id',
                     'as':'j'
                    }},{'$unwind':'$j'},
            {"$group":{"_id":"$fbs" ,"max_oldpeak": {"$max": "$j.oldpeak"}}}])
            for r in res3:
                  put_text(r)


def Indexing_click():
    clear()
    background_page("D:\indexing.png", 450, "550px 250px")
    put_button("Home",onclick=b_click)
    index = select("Choose index", ["Ascending by Age", "Descending by Age", "Ascending by patient ID as multi key",
                                    "Ascending by trestbps and ID ,descending by thalach ",
                                    "Descending by oldpeak and Ascending by ID",
                                    "Descending by chol and Ascending by ID ",
                                    "See indexes of Patient Collection",
                                    "See indexes of Target Collection",
                                    "See indexes of exercises Collection",
                                    "Drop an index","Create an index","find index"])
    if index=="See indexes of Patient Collection":
        indexes = db.patient_info.list_indexes()
        for index in indexes:
               put_text(index)
    if index=="See indexes of exercises Collection":
        indexes = db.exercises_info.list_indexes()
        for index in indexes:
            put_text(index)
    if index== "See indexes of Target Collection":
        indexes = db.Taget.list_indexes()
        for index in indexes:
              put_text(index)
    if index=="Create an index":
        collection=select("Choose Field",["Patient collection","exercises Collection","Target Collection"])
        if collection=="Patient collection":
            feild=select("Choose field",["ID","Age"])
            order=select("Choose order",["1","-1"])
            ord=int(order)
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              db.patient_info.create_index([(feild ,ord)], name=new['name']) 
            except:
                popup("invalid name",[put_button("OK",onclick=close_popup)])
        if collection=="exercises Collection":
            feild=select("Choose field",["cp","trestbps","chol","restecg","thalach"])
            order=select("Choose order",["1","-1"])
            ord=int(order)
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              db.exercises_info.create_index([(feild ,ord)], name=new['name']) 
            except:
                popup("invalid name",[put_button("OK",onclick=close_popup)])
        if collection=="Target Collection":
            feild=select("Choose field",["oldpeak","ca","slope","thal"])
            order=select("Choose order",["1","-1"])
            ord=int(order)
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              db.Taget.create_index([(feild ,ord)], name=new['name']) 
            except:
                popup("invalid name",[put_button("OK",onclick=close_popup)])
    if index=="Drop an index":
        collection=select("Choose collection",["Patient","Exercieses","Target"])
        if collection=="Patient":
            new = input_group("Index", [input('name', name="name",help_text="enter the name")])
            print(new['name'])
            try:
              db.patient_info.drop_index(new['name'])
              put_text("Done\n")
            except:
                popup("The name of the index is not found",[put_button("ok",onclick=close_popup)])
        if collection=="Exercieses":
            new = input_group("Index", [input('name', name="name",help_text="enter the name")])
            try:
              db.exercises_info.drop_index(new['name'])
              put_text("Done\n")
            except:
                popup("The name of the index is not found",[put_button("ok",onclick=close_popup)])
        if collection=="Target":
            new = input_group("Index", [input('name', name="name",help_text="enter the name")])
            try:
              db.Taget.drop_index(new['name'])
              put_text("Done\n")
            except:
                popup("The name of the index is not found",[put_button("ok",onclick=close_popup)])
    if index == "Ascending by Age":
        try:
          result = db.patient_info.find().hint('AgeIndex_1')
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index == "Descending by Age":
        try:
          result = db.patient_info.find().hint('AgeIndex_2')
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index == "Ascending by patient ID as multi key":
        try:
          result = db.Doctors.find().hint('multiIndex')
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index == "Ascending by trestbps and ID ,descending by thalach ":
        try:
          result = db.exercises_info.find().hint('trestbps:ascending,ID:ascending,thalach:descending')
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index == "Descending by oldpeak and Ascending by ID":
        try:
          result = db.Taget.find().hint("oldpeak:ascending,ID:ascending")
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index=="Descending by chol and Ascending by ID ":
        try:
          result = db.exercises_info.find().hint("Chol")
          for doc in result:
            put_text(doc)
        except:
            popup("The index is not found",[put_button("OK",onclick=close_popup)])
    if index=="find index":
        collection=select("Choose Field",["Patient collection","exercises Collection","Target Collection"])
        if collection=="Patient collection":
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              result = db.patient_info.find().hint(new['name'])
              for doc in result:
                 put_text(doc)
            except:
                popup("Not Found",[put_button("OK",onclick=close_popup)])
        if collection=="exercises Collection":
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              result = db.exercises_info.find().hint(new['name'])
              for doc in result:
                 put_text(doc)
            except:
                popup("Not Found",[put_button("OK",onclick=close_popup)])
        if collection=="Target Collection":
            new = input_group("Index name", [
                input('name', name="name",  help_text="enter the name of the index")])
            try:
              result = db.Taget.find().hint(new['name'])
              for doc in result:
                 put_text(doc)
            except:
                popup("Not Found",[put_button("OK",onclick=close_popup)])


def search_click():
    clear()
    put_button("Home", onclick=b_click)
    background_page("D:\search.png", 550, "550px 250px")
    ####type
    query = select("choose Query", ["Q1", "Q2", "Q3",'Q4'])
    if query == "Q1":
        res = p_collection.find({'age': {"$gte": 60}})
        put_text("ID", "\t", "Age")
        for r in res:
            put_text(r['_id'], "\t", r['age'])
    if query == "Q2":
        res = e_collection.find({'$and': [{'cp': 2}, {'chol': {'$gt': 200}}]})
        put_text("ID", "\t", "Cp", "\t", "Chol")
        for r in res:
            put_text(r['_id'], "\t", r['cp'], "\t", r['chol'])
    if query == "Q3":
        res = t_collection.find({'$or': [{'ca': {'$in': [0, 2]}}, {'olpeak': {'$lt': 0.5}}]})
        put_text("ID", "\t", "Ca", "\t", "Oldpeak")
        for r in res:
            put_text(r['_id'], "\t", r['ca'], "\t", r['oldpeak'])
    if query=='Q4':
        new = input_group("query", [input("exercises_query", name="exercises_query"), input("patien_query", name="patien_query")])
        try:
               e= eval(new['exercises_query'])
               p = eval(new['patien_query'])
               ids=e_collection.find(e)
               for i in ids:
                 res=p_collection.find_one({'$and':[{'_id':i['P_id']},p]})
                 if res!=None:
                    put_text(res)
                
        except:
              popup("Invalid Data",[put_button("OK",onclick=close_popup)])

def mapreduce():
    clear()
    put_button("Home", onclick=b_click)
    background_page("D:\mapreduce.png", 500, "550px 250px")

    opt=select("Choose Operation of mapreduce",["The sum of each value of Gender","The maximum of age for each gender","The average of thalach for each value of restecg",
                                                "The average of trestbps for each value of cp","Minimum  value of oldpeak based on slope","Average of oldpeak based on target value"])
    if opt=="The sum of each value of Gender":
        map_function= Code("""
        function(){emit(this.sex,1);
            }""")
        reduce_function= Code("""
        function(key,values)
        {return Array.sum(values);
        }""")
        result= db.command({"mapReduce":"patient_info",
            "map":map_function,
            "reduce":reduce_function,
            "out":"res_sum_sex"})
        res=db.res_sum_sex.find()
        for r in res:
               put_text(r)
    if opt=="The maximum of age for each gender":
        map_function= Code("""
        function(){emit(this.sex,this.age);
        }""")
        reduce_function= Code("""
        function(key,values)
        {return Math.max.apply(null,values);
        }""")
        result= db.command({"mapReduce":"patient_info",
                  "map":map_function,
                  "reduce":reduce_function,
                  "out":"res_max_age"})
        res=db.res_max_age.find()
        for r in res:
              put_text(r)
    if opt=="The average of thalach for each value of restecg":
        map_function= Code("""
        function(){emit(this.restecg,this.thalach);
        }""")
        reduce_function= Code("""
        function(key,values)
        {return Array.avg(values);
        }""")
        result= db.command({"mapReduce":"exercises_info",
                  "map":map_function,
                  "reduce":reduce_function,
                  "out":"res_avg_thalach"})
        res=db.res_avg_thalach.find()
        for r in res:
           put_text(r)
    if opt=="The average of trestbps for each value of cp":
        map_function= Code("""
        function(){emit(this.cp,this.trestbps);
        }""")
        reduce_function= Code("""
        function(key,values)
        {return Array.avg(values);
        }""")
        result= db.command({"mapReduce":"exercises_info",
                  "map":map_function,
                  "reduce":reduce_function,
                  "out":"res_avg_trestbps"})
        res=db.res_avg_trestbps.find()
        for r in res:
             put_text(r)
    if opt=="Minimum  value of oldpeak based on slope":
        map_function= Code("""
        function(){emit(this.slope,this.oldpeak);
        }""")
        reduce_function= Code("""
        function(key,values)
        {return Math.min.apply(null,values);
        }""")
        result= db.command({"mapReduce":"Taget",
                  "map":map_function,
                  "reduce":reduce_function,
                  "out":"res_min_oldpeak"})
        res=db.res_min_oldpeak.find()
        for r in res:
             put_text(r)
    if opt=="Average of oldpeak based on target value":
        map_function= Code("""
        function(){emit(this.target,this.oldpeak);
        }""")
        reduce_function= Code("""
        function(key,values)
        {return Array.avg(values);
        }""" )   
        result= db.command({"mapReduce":"Taget",
                  "map":map_function,
                  "reduce":reduce_function,
                  "out":"res_avg_oldpeak"})
        res=db.res_avg_oldpeak.find() 
        for r in res:
               put_text(r)

def b_click():
    clear()

    def selectt():
        background_page("D:\\thinking.jpg",600,"center bottom")

        re=select("choose the operation",options=["Insert", "Delete", "Update", "Relations(Doctor Collection)", "Agregation", "Indexing","Visualization", "Search","Map Reduce","close"])

        return re
    btn_val=selectt()
    while btn_val != "close" :
        clear()
        if btn_val=="close":
            break
        elif btn_val == "Insert":
            Insert_click()

        elif btn_val == "Indexing":
            Indexing_click()
            btn_val=selectt()

        elif btn_val == "Delete":
            x=delete_click()
            del_click(x)
            
            
        elif btn_val == "Update":
            x=update_click()
            upd_click(x)


        elif btn_val =="Map Reduce":
            mapreduce()
            btn_val=selectt()
            
        elif btn_val == "Relations(Doctor Collection)":
            relation_click()
            btn_val=selectt()
            
        elif btn_val == "Agregation":
            x=agregation_click()
            agr_click(x)
            btn_val=selectt()
            
        elif btn_val == "Search":
            search_click()
            btn_val=selectt()
        elif btn_val== "Visualization":
            display_visualization()
            
        elif btn_val == "Back":
            clear()

def Home():

    bground()


def pos():
    #this function returns and focuses on the display scope
    scroll_to("display", position='top')

def display_visualization():
    clear()
    put_button("Home", onclick=b_click)
    background_page("D:\\visualization.jpg",550,"800px 250px")
    put_text("Addtional information to understand the data and thier relations")
    operation = ""
    while operation != "Home":
        operation = select("Choose the plot", options=["Correlation", "Histogram", "Boxplot", "Heatmap"])
        if operation == "Correlation":
            put_text("This is the Correlation between fields")
            image_path = "D:\\mapreduce.png"
        elif operation == "Histogram":
            operation = select("Choose the histograme", options=["Age", "trestbps", "chol", "thalach", "old peak"])
            if operation == "Age":

                put_text("This is the Age Histogram")
                image_path = "C:/Users/Sohila/Downloads/Documents/AgeH.png"
            elif operation == "trestbps":
                put_text("This is the trestbps Histogram")
                image_path = "C:/Users/Sohila/Downloads/Documents/treH.png"
            elif operation == "chol":
                put_text("This is the Chol Histogram")
                image_path = "C:/Users/Sohila/Downloads/Documents/Cholh.png"
            elif operation == "thalach":
                put_text("This is the thalach Histogram")
                image_path = "C:/Users/Sohila/Downloads/Documents/thalachH.png"
            elif operation == "old peak":
                put_text("This is the old peak Histogram")
                image_path = "C:/Users/Sohila/Downloads/Documents/oldpeakH.png"
        elif operation == "Boxplot":
            operation = select("Choose the box plot",
                               options=["Age-Sex", "Cp-thalah", "target-old peak", "exang-old peak", "ca-chol"])
            if operation == "Age-Sex":

                put_text("This is the Age-Sex Box Plot")
                image_path = "C:/Users/Sohila/Downloads/Documents/Age-Sex.png"
            elif operation == "Cp-thalah":

                put_text("This is the Cp-thalah Box Plot")
                image_path = "C:/Users/Sohila/Downloads/Documents/Cp-thalah.png"
            elif operation == "target-old peak":

                put_text("This is the target-old peak Box Plot")
                image_path = "C:/Users/Sohila/Downloads/Documents/target-old peak.png"
            elif operation == "exang-old peak":

                put_text("This is the exang-old peak Box Plot")
                image_path = "C:/Users/Sohila/Downloads/Documents/exang-old peak.png"
            elif operation == "ca-chol":

                put_text("This is the ca-chol Box Plot")
                image_path = "C:/Users/Sohila/Downloads/Documents/ca-chol.png"
        elif operation == "Heatmap":
            operation = select("Choose the Heatmap",
                               options=["target-cp", "fbs-restecg", "restecg-exang", "slope-ca", "ca-thal"])
            if operation == "target-cp":

                put_text("This is the target-cp Heatmap\n the most relevent field for target")
                image_path = "C:/Users/Sohila/Downloads/Documents/target-cp.png"
            elif operation == "fbs-restecg":

                put_text("This is the fbs-restecg Heatmap")
                image_path = "C:/Users/Sohila/Downloads/Documents/fbs-restecg.png"
            elif operation == "restecg-exang":

                put_text("This is the restecg-exang Heatmap")
                image_path = "C:/Users/Sohila/Downloads/Documents/restecg-exang.png"
            elif operation == "slope-ca":

                put_text("This is the slope-ca Heatmap")
                image_path = "C:/Users/Sohila/Downloads/Documents/slope-ca.png"
            elif operation == "ca-thal":

                put_text("This is the ca-thal Heatmap")
                image_path = "C:/Users/Sohila/Downloads/Documents/ca-thal.png"
        background_page2(image_path, "D:\\visualization.jpg", 400, 550, "350px 350px",
                         "800px 250px")

if __name__ == "__main__":
    
    #do set debug = False in production
    start_server(bground,debug=True)
    
    
   

