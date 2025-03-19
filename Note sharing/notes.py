from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the Notes model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Serve the frontend UI
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/notes", methods=["GET"])
def get_all_notes():
    notes = Note.query.all()
    return jsonify([{"id": note.id, "title": note.title, "content": note.content} for note in notes])

@app.route("/share", methods=["POST"])
def share_note():
    data = request.json
    title = data.get("title")
    content = data.get("content")

    if not title or not content:
        return jsonify({"error": "Title and content are required"}), 400

    new_note = Note(title=title, content=content)
    db.session.add(new_note)
    db.session.commit()

    return jsonify({"message": "Note shared successfully", "id": new_note.id}), 201

@app.route("/update/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data = request.json
    content = data.get("content")

    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    note.content = content
    db.session.commit()

    return jsonify({"message": "Note updated successfully"})

@app.route("/delete/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    note = Note.query.get(note_id)
    if not note:
        return jsonify({"error": "Note not found"}), 404

    db.session.delete(note)
    db.session.commit()

    return jsonify({"message": "Note deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
