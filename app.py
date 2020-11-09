from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<q>')
def home(q=''):
  return render_template('index.html', q=q)


@app.route('/author/<q>')
def show_author(q='Q20980928'):
  return render_template('author.html', q=q)


@app.route('/topic/<q>')
def show_topic(q='Q2013'):
  return render_template('topic.html', q=q)


app.run(debug=True)
