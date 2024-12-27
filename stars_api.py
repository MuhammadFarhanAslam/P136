from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('data.py', 'r') as f:
    data = json.load(f)

@app.route('/stars', methods=['GET'])
def get_all_stars():
    return jsonify(data)

@app.route('/stars/<int:star_id>', methods=['GET'])
def get_star_by_id(star_id):
    star = next((star for star in data if star['Unnamed: 0'] == star_id), None)
    if star is None:
        return jsonify({"error": "Star not found"}), 404
    return jsonify(star)

if __name__ == '__main__':
    app.run(debug=True)
