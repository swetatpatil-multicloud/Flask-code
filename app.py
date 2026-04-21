from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# DEBUG: Check if MONGO_URI is loading
mongo_uri = os.getenv("MONGO_URI")
print("MONGO_URI FROM ENV:", mongo_uri)

# If not found, stop app immediately
if not mongo_uri:
    raise ValueError("MONGO_URI not found in .env file")

# Configure app
app.config["MONGO_URI"] = mongo_uri
app.secret_key = os.getenv("SECRET_KEY", "defaultsecret")

# Initialize MongoDB
mongo = PyMongo(app)

# ---------------- ROUTES ---------------- #

# Home page -> list students
@app.route('/')
def index():
    try:
        students = mongo.db.students.find()
        return render_template('index.html', students=students)
    except Exception as e:
        return f"MongoDB Error: {e}"

# Add student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        mongo.db.students.insert_one({
            "name": name,
            "email": email,
            "course": course
        })

        return redirect(url_for('index'))

    return render_template('add_student.html')

# Update student
@app.route('/update/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    student = mongo.db.students.find_one({"_id": ObjectId(student_id)})

    if request.method == 'POST':
        new_name = request.form['name']
        new_email = request.form['email']
        new_course = request.form['course']

        mongo.db.students.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": {
                "name": new_name,
                "email": new_email,
                "course": new_course
            }}
        )

        return redirect(url_for('index'))

    return render_template('update_student.html', student=student)

# Delete student
@app.route('/delete/<student_id>')
def delete_student(student_id):
    mongo.db.students.delete_one({"_id": ObjectId(student_id)})
    return redirect(url_for('index'))

# Run app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)