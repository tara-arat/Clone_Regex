from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form.get('test_string', '')  # Using get with default value to avoid KeyError
    regex_pattern = request.form.get('regex_pattern', '')  # Using get with default value to avoid KeyError
    matches = re.findall(regex_pattern, test_string)
    return render_template('result.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
