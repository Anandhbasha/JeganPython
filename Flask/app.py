from flask import Flask,render_template,request,redirect
import json

app = Flask(__name__)

def read():
    with open("newPage.json","r") as f:
        data = f.read()
        
        return json.loads(data)
    
def writeData(data):
    with open("newPage.json","w") as f:
        json.dump(data,f,indent=4)

@app.route("/")
def home():
    student = read()
    return render_template("index.html",student=student)
@app.route("/add",methods=["POST"])
def addStudent():
    name = request.form["name"]
    student = read()
    new_id = len(student)+1
    student.append({"id":new_id,"name":name})
    writeData(student)
    return redirect('/')
@app.route("/delete/<int:id>")
def deleteStu(id):
    stu = read()
    stu = [s for s in stu if s["id"]!=id]
    writeData(stu)
    return redirect("/")

# 1 arun
# 2 ajay
if __name__ =="__main__":
    app.run(debug=True)