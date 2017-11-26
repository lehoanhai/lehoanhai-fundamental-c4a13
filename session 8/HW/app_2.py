from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello,to calculate your BMI, type like this form /BMI/weight/height(in meter)  "

@app.route('/BMI/<int:weight>/<int:height>')
def BMI(weight, height):
    h1 = height * 0.01
    body = weight / (h1*h1)

    if body < 16:
        return "Severely Underweight"
    elif body < 18.5:
        return "Underweight"
    elif body < 25:
        return "Normal"
    elif body < 30:
        return "Overweight"
    else: return "Oberse"

if __name__ == '__main__':
  app.run(debug=True)
