
import flask
from flask import request
 
app = flask.Flask(__name__)
 
# One list per topic to store posts in memory
generalP = []
gamesP = []
tvP = []
booksP = []
 
@app.route('/')
def home():
  return flask.render_template('index.html')
 
@app.route('/general', methods=['GET', 'POST'])
def general():
  if request.method == 'POST':
    # request.json is the JSON object sent by index.js's send() function
    generalP.append(request.json)
  return flask.render_template('general.html', posts=generalP)
 
@app.route('/games', methods=['GET', 'POST'])
def games():
  if request.method == 'POST':
    gamesP.append(request.json)
  return flask.render_template('games.html', posts=gamesP)
 
@app.route('/tv', methods=['GET', 'POST'])
def tv():
  if request.method == 'POST':
    tvP.append(request.json)
  return flask.render_template('tv.html', posts=tvP)
 
@app.route('/books', methods=['GET', 'POST'])
def books():
  if request.method == 'POST':
    booksP.append(request.json)
  return flask.render_template('books.html', posts=booksP)
 
@app.route('/about')
def about():
  return flask.render_template('about.html')
 
if __name__ == "__main__":
  #In visual studio, this line can just be "app.run()"
  app.run(host='0.0.0.0', port=8080)
 
