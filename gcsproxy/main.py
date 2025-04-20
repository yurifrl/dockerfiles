import os
from flask import Flask, send_file, abort
from google.cloud import storage

app = Flask(__name__)
bucket_name = os.environ.get("GCS_BUCKET", "your-bucket")
client = storage.Client.from_service_account_json("/key.json")
bucket = client.bucket(bucket_name)

@app.route('/<path:filename>')
def fetch_file(filename):
    blob = bucket.blob(filename)
    if not blob.exists():
        abort(404)
    tmp_path = f"/tmp/{filename.replace('/', '_')}"
    blob.download_to_filename(tmp_path)
    return send_file(tmp_path)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)