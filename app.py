from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = '(복잡한 문자열)'
#CSRF를 방지하기 위해 사용

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/register',methods=["GET","POST"])
#register URL을 회원가입으로 사용할 예정.
def register():
    form = RegistrationForm()
    if form.validate_on_submit():  #POST방식으로 요청한 경우
        flash(f'{form.username.data}님 회원가입 완료!','success')
        #부트스트랩으로 알림 메세지를 띄우기 위해 사용. (굳이 필요 x)
        return redirect(url_for('home'))
    return render_template('register.html', form=form) #GET방식으로 요청한 경우

if __name__ == '__main__':
    app.run(debug=True)