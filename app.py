# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

# INDEX --> "Login"
@app.route('/')
def home():
    return render_template('login.html')  # render a template called welcome.html

# HOME --> Page to select insights
@app.route('/home')
def welcome():
    return render_template('home.html')  # render a template

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

# REGIONS ROUTE HANDLER
@app.route('/regions')
def regions():
    return render_template('insights/regions.html')  # render a template

# RETURNS ROUTE HANDLER
@app.route('/returns')
def returns():
    return render_template('insights/returns.html')  # render a template

# SALES REPS ROUTE HANDLER
@app.route('/sales-reps')
def salesReps():
    return render_template('insights/sales-reps.html')  # render a template

# REGISTER ROUTE HANDLER
@app.route('/register')
def register():
    return render_template('insights/register.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)