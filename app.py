from flask import Flask, render_template

app = Flask(__name__)

student_data = {
    1:{"name":"김민겸","score": {"국어": 80, "수학" : 100}},
    2:{"name":"김민주","score": {"국어" :100, "수학" :100}}
}

@app.route('/')
def index():
    return render_template("index.html", template_students = student_data)
#render_template에서 index.html을 불러옴과 동시에 template_students 변수 정의

@app.route("/student/<int:id>")
def studnet(id):
    return render_template("student.html",
                           template_name = student_data[id]["name"],
                           template_score = student_data[id]["score"])

if __name__ == '__main__':
    app.run(debug = True)
