tarts a flask web application
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    print helo HBNB
    """
    return "<h1>Hello, HBNB!</h1>"
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
