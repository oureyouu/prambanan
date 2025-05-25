from flask import Flask, render_template, request, redirect, url_for

# Variabel HARUS bernama 'app' atau 'application'
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/extractor', methods=['GET', 'POST'])
def extractor():
    return render_template('extractor.html')
@app.route('/service', methods=['GET', 'POST'])
def service():
    return render_template('service.html')

if __name__ == '__main__':
    app.run(debug=True)