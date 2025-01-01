from flask import Flask, render_template, redirect, url_for, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import google.auth
import os
import helper

app = Flask(__name__)

# Set the environment variable for credentials
cred_path = "personal-blog-446418-fc63a29b1c27.json"
if os.path.exists(cred_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = cred_path
    cred = credentials.Certificate(cred_path)
    DEVELOPMENT_MODE = True
else:
    DEVELOPMENT_MODE = False

# Initialize Firebase Admin SDK
credentials, project_id = google.auth.default()
firebase_admin.initialize_app()
db = firestore.client()


@app.route("/")
def home():
    essay_id = ""
    if DEVELOPMENT_MODE:
        ip_address = "58.231.118.25"
    else:
        ip_address = request.remote_addr

    helper.add_visitor(db, ip_address, essay_id)

    return render_template("index.html")

@app.route("/<essay_id>")
def essay(essay_id):
    # Determine the IP address
    if DEVELOPMENT_MODE:
        ip_address = "58.231.118.25"
    else:
        ip_address = request.remote_addr

    # Check if essay exists
    essay_data = helper.check_essay_id(db, essay_id)
    if not essay_data:
        # If no essay found, redirect to home
        return redirect(url_for('home'))
    
    # Add visitor to database
    try:
        helper.add_visitor(db, ip_address, essay_id)
    except Exception as e:
        # Log error and return a fallback response (could be 500 error)
        print(f"Error adding visitor: {e}")
        return "An error occurred while adding your visit."

    # Get the file name associated with the essay
    file_name = essay_data.get("file_name")
    if not file_name:
        # If no file name exists, handle gracefully
        return "Error: Essay file not found."

    # Render the corresponding essay template
    return render_template(file_name)

if __name__ == '__main__':
    app.run(debug=True)