from flask import Flask
from flask_cors import CORS
import nltk

# Download NLTK data at startup
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

from routes.hate_routes import hate_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(hate_bp)

@app.route('/')
def index():
    return "Server is running successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
