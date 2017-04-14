from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the Home Page and method is %s' % request.method

@app.route('/about')
def about():
    return '<h2>This is the About Page</h2>'

@app.route('/profile/<username>')
def profile(username):
    return '<h2>Hi There %s</h2>' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h2>Post ID is %s</h2>' % post_id

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'GET':
        return 'Get Method, showing all posts'
    elif request.method == 'POST':
        return 'POST Method, Add New Post'










if __name__ == "__main__":
    app.run(debug=True)