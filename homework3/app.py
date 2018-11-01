from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/new_bike", methods=['GET','POST'])
def new_bike():
    if request.method == "GET":
        return  render_template("serious_ex1.html")
    elif request.method == "POST":
        form = request.form
        print(form)
        return "Success"           

if __name__ == '__main__':
  app.run(debug=True)