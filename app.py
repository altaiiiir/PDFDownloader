import streamlit as st
import requests
from io import BytesIO

st.set_page_config(page_title="PDF Downloader", layout="centered")

with open("styles/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📄 Instant PDF Downloader")

url = st.text_input("Paste a direct .pdf URL:")
pdf_data = None

if st.button("Load PDF") and url:
    try:
        response = requests.get(url)
        if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
            pdf_data = BytesIO(response.content)
        else:
            st.error("❌ PDF is not compatible or the link is invalid.")
    except Exception as e:
        st.error(f"Error downloading PDF: {e}")
elif not url:
    st.warning("Please enter a URL.")

if pdf_data:
    st.download_button("📥", data=pdf_data, file_name="downloaded.pdf", mime="application/pdf", help="Download PDF")
