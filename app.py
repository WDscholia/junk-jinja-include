from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<q>')
def home(q=''):
  return render_template('index.html', q=q)

app.run()
