from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/from')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST'])
def data():
    return render_template('data.html', form_data = form_data)

app.run(host='localhost', port=2500)
