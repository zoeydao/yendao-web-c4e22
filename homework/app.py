#Setup flask server

from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/about-me")
def about_me():
    return """
    <h1>Hello, it's Yen!!</h1>
    <p>I'm working as a Project Manager</p>
    <p>My favourite thing to do when I'm free is
    <select>
    <option value="eat">eat</option>
    <option value="sleep">sleep</option>
    <option value="code">code</option>
    <option value="repeat">repeat</option>
    </select>
    </p>
    <p>That wasn't even funny (or true)....So I'm gonna insert a lame meme here:</p>
    <p><img src="https://pics.me.me/my-code-doesnt-work-ihave-no-idea-why-my-code-works-14032925.png" height="500"></p>
    """

@app.route("/school")
def school():
    return redirect("http://www.techkids.vn", code=302)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w,h):
    h = h/100
    bmi = round(w/(h*h),1)  
    if bmi < 16:
        return str(bmi) + " < 16 : Severely underweight"
    elif bmi < 18.5:
        return "16 <= " + str(bmi) + " < 18.5: Underweight"
    elif bmi < 25:
        return "18.5 <= " + str(bmi) + " < 25: Normal"
    elif bmi < 30:
        return "25 <= " + str(bmi) + " < 30: Overweight"
    else:
        return str(bmi) + " > 30: Obese"
    
@app.route("/bmi2/<int:w>/<int:h>")
def bmi2(w,h):
    return render_template("bmi.html")
    
if __name__ == "__main__": 
    app.run(debug=True)