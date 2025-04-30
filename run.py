# run.py remains the same
from app import create_app
from flask import jsonify

app = create_app()

# ✅ Add REST API endpoint
@app.route('/api/quote')
def quote():
    return jsonify({"quote": "Success is built on consistent effort!"})

if __name__ == '__main__':
    app.run(debug=True)