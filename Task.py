from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello flask"
@app.route('/about')
def about():
    return "Hello about"
@app.route('/contact')
def contact():
    return "Hello contact"

@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

@app.route('/hello/<name>')
def hello(name):
    return render_template("name.html",name=name)

@app.route('/form', methods =['GET','POST'])
def form():
    if request.method=='POST':
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        email = request.form['email']
        Address = request.form['Address']
        gender = request.form['gender']
        sport = request.form.get('sport','Null')
        Esport = request.form.get('Esport','Null')
        streaming = request.form.get('streaming','Null')
        vlogging = request.form.get('vlogging','Null')
        password = request.form['password']
        return render_template('result.html',FirstName=FirstName,LastName=LastName,email=email,Address=Address,gender=gender,sport=sport,Esport=Esport,streaming=streaming,vlogging=vlogging,password=password)
    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)