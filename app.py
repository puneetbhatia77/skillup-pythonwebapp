from flask import Flask, render_template
import argparse

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run the Flask application with a custom port."
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="Port number (default is 5000)"
    )
    args = parser.parse_args()
    app.run(debug=True, port=args.port)