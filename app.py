from flask import Flask, render_template, request, jsonify
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
def index():
    return render_template("index.html")

@app.route("/get_tags", methods=["POST"])
def get_tags_route():
    keyword = request.json.get("keyword")
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    tags = get_tags(keyword)
    return jsonify({"tags": tags})

if __name__ == "__main__":
    app.run(debug=True)
