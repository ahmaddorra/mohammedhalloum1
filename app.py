import os
import logging

from flask import Flask, request, jsonify, render_template

from model import MultinomialNB

app = Flask(__name__)


# create instance
model = MultinomialNB()
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/classify", methods=["GET"])
def predict():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    logging.info("Predict request received!")
    text = request.args.get("news-txt")
    prediction = model.predict(text)

    logging.info("prediction from model= {}".format(prediction))
    return jsonify({"category": str(prediction)})
    
  
# Create the main driver function
port = int(os.environ.get("PORT", 5000)) # <-----
app.run(host='0.0.0.0', port=port)       # <-----
