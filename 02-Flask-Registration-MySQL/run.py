from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash
from model import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:arup#123@localhost/flasklearning'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("register.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # Code to take care of registration
        user = User(username=request.form['username'], email=request.form['email'], password=generate_password_hash(request.form['password']))
        db.session.add(user)
        try:
            db.session.commit()
        except:
            return "Something went wrong...", 404
    
    return render_template('register.html')

if __name__=='__main__':
    app.run(debug=True, port=3000)