from flask import Flask,render_template,  redirect,request
import  csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/<page_name>')
def all(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.csv','a',newline='') as file:
        email = data['email']
        subject = data['subject']
        message = data['message']
        spamwriter = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([email,subject,message])
@app.route('/submit_form', methods = ['POST' , 'GET'])
def submit_form():
    if request.method != 'POST':
        return 'Something went wrong :('
    else:
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')