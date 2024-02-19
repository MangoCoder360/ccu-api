from flask import Flask,redirect
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

CCU = {}

@app.route("/")
def index():
    return redirect("https://github.com/MangoCoder360/ccu-api")

@app.route("/api/<string:app_id>/<string:user_id>")
def api(app_id, user_id):
    if app_id not in CCU:
        CCU[app_id] = {}
    CCU[app_id][user_id] = int(time.time())
    time.sleep(0.1)
    ccu = recalculate_ccu(app_id)
    return '{"ccu": ' + str(ccu) + '}'

def recalculate_ccu(app_id):
    for user_id in list(CCU[app_id].keys()):
        if int(time.time()) - CCU[app_id][user_id] > 8:
            del CCU[app_id][user_id]
    time.sleep(0.1)
    return len(CCU[app_id])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7780)