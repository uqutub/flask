from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<user>')
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


@app.route('/shopping')
def shopping():
    foods = ['Cheese', 'Butter', 'Milk', 'Mutton', 'Bread']
    return render_template("shopping.html", foods=foods)

if __name__ == "__main__":
    app.run(debug=True)