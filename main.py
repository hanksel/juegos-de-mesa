import os
import subprocess




from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")   
    completedProcess = subprocess.run("cat /app/file.txt", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=10, universal_newlines=True)    
    return "Hello {}!".format(completedProcess)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))