from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('hellodb', 27017)
# client = MongoClient('localhost', 27017)
db = client.mydata


@app.route('/', methods=['GET'])
def helloindex():
    _items = db.hello.find()
    items = [it for it in _items]
    return render_template('index.html', items=items)


@app.route('/new', methods=['POST'])
def addnew():
    it_new = {"username": request.form['uname'],
              "useremail": request.form['uemail']}
    db.hello.insert_one(it_new)
    return redirect(url_for('helloindex'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,  debug=True)
