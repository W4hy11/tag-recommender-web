from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__)

def get_tags(keyword):
    url = "https://api.datamuse.com/words"
    params = {"ml": keyword, "max": 50}
    response = requests.get(url, params=params)
    data = response.json()

    tags = [keyword]
    for item in data:
        word = item['word']
        if word.lower() != keyword.lower() and word.isalpha():
            tags.append(word)
        if len(tags) == 15:
            break
    return tags

@app.route("/")
def serve_index():
    return send_file("index.html")

@app.route("/script.js")
def serve_script():
    return send_file("script.js")

@app.route("/get_tags", methods=["POST"])
def get_tags_route():
    keyword = request.json.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    tags = get_tags(keyword)
    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(debug=True)
