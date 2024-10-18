from flask import Flask,render_template,request,redirect

from medication_reminder import store_medication,get_all_medications

app = Flask(__name__)

@app.route("/")
def index():
    medications = get_all_medications() # get_all_medications chai euta finction ho jun medication_reminder.py ko ho
    return render_template('index.html',medications = medications) # yo left side ko medications chai index.html ma use hunxa ani index.html chai frontend ho jun render template le grda front ra backedn join grxa

@app.route('/add',methods=['GET','POST'])
def add_medication():
    if request.method == 'POST':
        medication_info = {
            "name": request.form['name'], # add_medication ma vako user haleko value yeta layeko
            "dose": request.form['dose'],
            "frequency": request.form['frequency'],
            "time": request.form['time']
        }
        store_medication(medication_info)#store_medication is imporeted mathi and now stores the new medi
        return redirect('/')# retun to main page i.e index.html
    return render_template('add_medication.html')#agadi user lai ta add_medication.html dekhauna lai)