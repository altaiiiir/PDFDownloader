import requests
import os
from io import BytesIO
from flask import Flask, render_template, request, send_file, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for flashing messages


@app.route("/ads.txt")
def ads_txt():
    return app.send_static_file("ads.txt")


@app.route("/robots.txt")
def robots():
    return app.send_static_file("robots.txt")


@app.route("/sitemap.xml")
def sitemap():
    return app.send_static_file("sitemap.xml")


@app.route("/", methods=["GET", "POST"])
def index():
    pdf_data = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        # Check if URL is empty
        if not url:
            flash("Please enter a URL.", "warning")
            return redirect(url_for('index'))  # Stay on the same page

        # Check if the URL ends with .pdf
        if not url.lower().endswith('.pdf'):
            flash("Invalid URL! Please provide a valid PDF URL.", "error")
            return redirect(url_for('index'))  # Stay on the same page

        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
                pdf_data = BytesIO(response.content)
                return send_file(pdf_data, as_attachment=True, download_name="downloaded.pdf")
            else:
                flash("❌ PDF is not compatible or the link is invalid.", "error")
        except Exception as e:
            flash(f"Error downloading PDF: {str(e)}", "error")

    return render_template("index.html")


if __name__ == "__main__":
    env = os.getenv("Environment", "local")
    app.run(debug=env == 'local')
