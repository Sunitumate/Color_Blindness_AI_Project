from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/result', methods=['POST'])
def result():
    answers = request.form
    if answers.get('img1') == '12' and answers.get('img2') != '8':
        result = "You may have Deuteranopia"
    else:
        result = "Normal Vision"
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
