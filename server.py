from flask import Flask, request, jsonify

app = Flask(__name__)
banlist = set()
ADMIN_KEY = "secret123"

@app.route("/ban", methods=["POST"])
def ban_user():
    key = request.args.get("key")
    uid = request.args.get("user_id")
    if key != ADMIN_KEY:
        return jsonify({"status": "unauthorized"})
    if not uid:
        return jsonify({"status": "missing user_id"})
    banlist.add(str(uid))
    return jsonify({"status": "banned", "user_id": uid})

@app.route("/unban", methods=["POST"])
def unban_user():
    key = request.args.get("key")
    uid = request.args.get("user_id")
    if key != ADMIN_KEY:
        return jsonify({"status": "unauthorized"})
    banlist.discard(str(uid))
    return jsonify({"status": "unbanned", "user_id": uid})

@app.route("/check", methods=["GET"])
def check_user():
    uid = request.args.get("user_id")
    banned = str(uid) in banlist
    return jsonify({"user_id": uid, "banned": banned})

@app.route("/")
def home():
    return "🚀 Flask Ban System Active!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
