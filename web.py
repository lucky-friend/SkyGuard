from flask import Flask, render_template,request
import subprocess

app = Flask(__name__,template_folder='../plane_detection',static_folder='statics')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run_command():
    command = request.form.get('command')
    output = subprocess.check_output(command, shell=True).decode('utf-8')
    return {'output': output}

if __name__ == '__main__':
    app.debug = True
    print(app.template_folder)
    app.run(host="0.0.0.0",port=5000)