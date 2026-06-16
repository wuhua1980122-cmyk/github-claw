import os, uuid
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route("/api/compress", methods=["POST"])
def compress():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    f = request.files["file"]
    ext = f.filename.rsplit(".", 1)[-1].lower() if "." in f.filename else ""
    out_name = f"compressed_{uuid.uuid4().hex}.{ext or 'bin'}"
    out_path = os.path.join(UPLOAD_DIR, out_name)
    f.save(out_path)
    return send_file(out_path, as_attachment=True, download_name=f"compressed_{f.filename}")

@app.route("/api/convert", methods=["POST"])
def convert():
    if "file" not in request.files:
        return jsonify({"error": "No file"}), 400
    target = request.form.get("format", "")
    if not target:
        return jsonify({"error": "No target format"}), 400
    f = request.files["file"]
    out_name = f"{uuid.uuid4().hex}.{target}"
    out_path = os.path.join(UPLOAD_DIR, out_name)
    f.save(out_path)
    return send_file(out_path, as_attachment=True, download_name=f"converted.{target}")

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "version": "1.0.0"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)