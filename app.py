from flask import Flask, render_template, request, jsonify #type: ignore
from scraper.webscraper import WebScraper

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get-tags", methods=["POST"])
def get_tags():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    try:
        scraper = WebScraper(url)
        scraper.fetch()
        tags = scraper.get_tags_with_classes()
        return jsonify(tags)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/scrape", methods=["POST"])
def scrape():
    data = request.get_json()

    scraper = WebScraper(data["url"])
    scraper.fetch()

    result = scraper.extract(
        data["tag"],
        data.get("class")
    )

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
