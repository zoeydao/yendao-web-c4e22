from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/new_bike", methods=['GET','POST'])
def register():
    if request.method == "GET":
        return  render_template("serious_ex1.html")
    elif request.method == "POST":
        #1. Unpack data (form)
        form = request.form
        return form
        
if __name__ == '__main__':
  app.run(debug=True)