#Setup flask server

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") #nếu ng dùng truy cập vào trang chủ thì
def homepage():
    return "Welcome to C4E Web module, enjoy"

@app.route("/quan")
def hello_quan():
    return "Hello Quan"

@app.route("/praise/linh")
def praise_linh():
    return "Linh is awesome"

@app.route("/praise/<name>")
def praise(name):
    return name + " is awesome"

@app.route("/add/<int:x>/<int:y>")
def add(x,y):
    s = x + y
    return str(s)

@app.route("/question")
def show_question():
    return render_template("question.html")

if __name__ == "__main__": #khong co nhieu y nghia khi o local, khi deploy thi script co the chay o nhieu worker => chi dinh con nao la main
    app.run(debug=True)

#loop back: app.py = server; client = webbrowser
# => client va server cung 1 may => den khi deploy = 2 may (client and server)
#IP loop back: cho phep khi card may tinh nhin thay se tu dong gui cho chinh machine do
#=> localhost (127.0.0.1)

#port: 5000 (co nhieu port trong localhost)