from flask import Flask, render_template

app = Flask(__name__) # Creating Flask object  = _name_ -> _main_


@app.route('/')  #decorator  '/' is the url that this decorator will be mapped to
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ =="__main__":
    app.run(debug=True)
