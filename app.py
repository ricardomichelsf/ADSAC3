# app.py


from flask import Flask
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import BaseConfig
from models import *

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    
    name = request.form['inputName']
    categoria = request.form['inputCategoria']
    preco = request.form['inputpreco']

    
    if request.method == 'POST':
        post = Post(name, categoria, preco)
        db.session.add(post)
        db.session.commit()
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)