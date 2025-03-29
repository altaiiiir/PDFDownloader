from flask import Flask, render_template, request, send_file, flash
import requests
from io import BytesIO

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Needed for flashing messages


@app.route("/ads.txt")
def ads_txt():
    return send_file("ads.txt", mimetype="text/plain")


@app.route("/", methods=["GET", "POST"])
def index():
    pdf_data = None

    if request.method == "POST":
        url = request.form.get("url", "").strip()
        if not url:
            flash("Please enter a URL.", "warning")
        else:
            try:
                response = requests.get(url)
                if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
                    pdf_data = BytesIO(response.content)
                    return send_file(pdf_data, as_attachment=True, download_name="downloaded.pdf")
                else:
                    flash("❌ PDF is not compatible or the link is invalid.", "error")
            except Exception as e:
                flash(f"Error downloading PDF: {str(e)}", "error")

    return render_template("index.html")


if __name__ == "__main__":
    app.run()
