from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services-list.db'
with app.app_context():
    db = SQLAlchemy(app)

class Srvc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    

    def __repr__(self):
        return '<Service %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        service_title = request.form['title']
        service_content = request.form['content']
        new_service = Srvc(title=service_title, content=service_content)

        try:
            db.session.add(new_service)
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue creating service.'
    else:
        services = Srvc.query.order_by(Srvc.title).all()
        return render_template('index.html', services=services)

@app.route('/delete/<int:id>')
def delete(id):
    service_to_delete = Srvc.query.get_or_404(id)

    try:
        db.session.delete(service_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Issue deleting service.'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    service = Srvc.query.get_or_404(id)
    if request.method == 'POST':
        service.title = request.form['title']
        service.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue updating service.'
    else:
        return render_template('update.html', service=service)

if (__name__) == "__main__":
    app.run(host='0.0.0.0',port=80)(debug=True)