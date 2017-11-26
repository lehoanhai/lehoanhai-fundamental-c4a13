from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about-me')
def about_me():
    return render_template('about_me.html')

@app.route('/school')
def school():
    return redirect('http://techkids.vn/')


if __name__ == '__main__':
  app.run(debug=True)
