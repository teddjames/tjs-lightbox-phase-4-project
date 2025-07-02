from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from db import db
from models import PhotographyWork, Review, Idea

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app)

@app.route('/')
def index():
    return "Welcome to Tedd's Lightbox"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # For demo: hardcoded user (replace with real DB auth later)
    if username == "admin" and password == "password":
        return jsonify({"username": "admin"}), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route("/works")
def get_works():
    works = PhotographyWork.query.all()
    return jsonify([
      {
        "id": w.id,
        "title": w.title,
        "description": w.description,
        "average_rating": w.average_rating,
        "reviews": [{"id": r.id, "rating": r.rating, "comment": r.comment} for r in w.reviews],
        "ideas": [{"id": i.id, "title": i.title, "description": i.description} for i in w.ideas]
      }
      for w in works
    ])

# POST /reviews, DELETE /reviews/<id>
@app.route("/reviews", methods=["POST"])
def add_review():
    data = request.json
    review = Review(work_id=data["work_id"], rating=data["rating"], comment=data.get("comment"))
    db.session.add(review); db.session.commit()
    return jsonify({"message":"Review added"}), 201

@app.route("/reviews/<int:id>", methods=["DELETE"])
def del_review(id):
    r = Review.query.get(id)
    if r:
        db.session.delete(r); db.session.commit()
        return jsonify({"message":"Deleted"}), 200
    return jsonify({"error":"Not found"}), 404

# POST /ideas, DELETE /ideas/<id>
@app.route("/ideas", methods=["POST"])
def add_idea():
    data = request.json
    idea = Idea(work_id=data["work_id"], title=data["title"], description=data.get("description"))
    db.session.add(idea); db.session.commit()
    return jsonify({"message":"Idea added"}),201

@app.route("/ideas/<int:id>", methods=["DELETE"])
def del_idea(id):
    i = Idea.query.get(id)
    if i:
        db.session.delete(i); db.session.commit()
        return jsonify({"message":"Deleted"}), 200
    return jsonify({"error":"Not found"}),404

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
