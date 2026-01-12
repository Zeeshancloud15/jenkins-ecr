from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define home route
@app.route("/")
def hello():
    return "Hello from zeeshan.agency 03!"

# Run the app
if __name__ == "__main__":
    # Listen on all IPs and port 80 for Docker
    app.run(host="0.0.0.0", port=80)
