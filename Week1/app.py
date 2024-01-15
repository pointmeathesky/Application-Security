from flask import Flask,render_template,request

app = Flask(__name__, template_folder='templates')

@app.route('/')

def homepage():

    return render_template('index.html')


@app.route('/form', methods=['POST'])

def form():
    data = request.form['form']
    # message = "You searched for: " + data
    # return {"You searched for: " :data}
    return render_template('search.html', data=data)

if __name__ == "main":
    app.run(host='localhost', port=5000)
