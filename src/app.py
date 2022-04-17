from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# get host and ip address
def getDetails():
    hostName = socket.gethostname()
    hostIp = socket.gethostbyname(hostName)
    return str(hostName), str(hostIp)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status = "Up"
    )

@app.route("/details")
def details():
    hostName, Ip = getDetails()
    return render_template("index.html", HOST = hostName, IP = Ip)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)