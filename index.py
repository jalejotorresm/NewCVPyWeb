from flask import Flask, render_template

app = Flask(__name__,template_folder='Templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study')
def study():
    return render_template('study.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

if __name__ == '__main__':
    app.run(debug=True)