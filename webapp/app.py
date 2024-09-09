from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Process signup form here
        # After processing the form, redirect to the home page
        return redirect(url_for('home'))  # Corrected to use the name of the view function
    return render_template('signup.html')

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/home")
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
