from flask  import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    html = render_template('index.html')
    return html


@app.route('/post')

@app.route('/profile')
@app.route('/profile/<username>')
def show_user_profile():
    username = "aaa"
    html = render_template("profile/index.html", username = username)
    return html

if __name__ == "__main__":
    app.run()