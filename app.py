
import os
from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    config_value = os.getenv("CONFIG_MODE", "not set")
    secret_value = os.getenv("API_SECRET", "no secret")
    return f"Mode: {config_value} | Secret: {secret_value}"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

