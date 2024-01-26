from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLALCHEMY

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

@app.route("/")

# Define the user model
class User(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    publication_year = db.Column(db.String(50), nullable=False)

def create_db():
    with app.app_context():
        db.create_all()


# Create the routes

@app.route("/", methods=["GET","POST"])
def index():
    users = User.query.all()
    return render_template("books.html", users=users)

@app.route("/books", methods=["GET","POST"])
def new_user():
    if request.method == "POST":
        title = request.form["firstname"]
        author = request.form["lastname"]
        publication_year = request.form["email"]
        
        
        add_book = User(title=title, author=author, publication=publication)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_book.html", title="Add a Book")

@app.route("/books/<int:book_id>", methods=["GET","POST"])
def edit_user(book_id):
    if request.method == "POST":
        title = request.form["firstname"]
        author = request.form["lastname"]
        publication_year = request.form["year"]
        
        
        user = User.query.get(book_id)
        user.title= title
        user.author = author
        user.publication_year = publication_year
        
        db.session.commit()
        return redirect(url_for("index"))
    user = User.query.get(book_id)
    return render_template("edit_user.html", user=user)


if __name__ == "__main__":
    create_db()
    app.run(port=5001, debug=True)
