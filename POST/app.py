from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')


@app.route('/result', methods=['GET', 'POST'])
def hello():
    return render_template('result.html', name=request.form['name'])


if __name__ == '__main__':
   app.run(debug = True)