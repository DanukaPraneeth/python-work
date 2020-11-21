from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    # return "Hello World!"
    return render_template('index.html')

@app.route("/user/<username>")
def show_user(username):
    return "User: %s" % username
    
@app.route('/hello/<name>')
def hello_page(name):
    return render_template('index.html', name=name)    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
