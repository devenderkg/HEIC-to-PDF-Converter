import streamlit as st
from PIL import Image
from io import BytesIO
from pathlib import Path
import os
import img2pdf

# Function to convert HEIC to PDF
def heic_to_pdf(heic_images, pdf_quality="High Quality", pdf_layout="Single image per page"):
    pdfs = []

    for heic_image in heic_images:
        # Conversion logic using img2pdf
        heic_data = BytesIO(heic_image.read())
        img = Image.open(heic_data)

        pdf_data = BytesIO()
        img.save(pdf_data, format="PDF", quality=pdf_quality.lower())

        pdfs.append(pdf_data)

    return pdfs

# Streamlit app
def main():
    st.title("HEIC to PDF Converter")
    st.write("Convert HEIC images to PDF effortlessly.")

    # Choose Conversion Options on the main page
    st.sidebar.header("Conversion Options")

    # Upload area
    uploaded_files = st.file_uploader("Drag and drop HEIC files here", type=["heic"], accept_multiple_files=True)

    # Or choose files using a button
    if not uploaded_files:
        uploaded_files = st.file_uploader("Choose Files", type=["heic"], accept_multiple_files=True)

    # Conversion options panel
    with st.expander("Advanced Options"):
        pdf_quality = st.selectbox("Image Quality", ["High Quality", "Medium Quality", "Low Quality"])
        pdf_layout = st.radio("PDF Layout", ["Single image per page", "Multiple images per page", "Contact sheet layout"])

        # Additional settings for experienced users if needed

    # Convert button
    if st.button("Convert"):
        if uploaded_files:
            st.info("Converting... This may take a moment.")
            converted_pdfs = heic_to_pdf(uploaded_files, pdf_quality, pdf_layout)

            # Display converted PDFs and download links
            st.subheader("Download Converted PDFs:")
            for idx, pdf_data in enumerate(converted_pdfs):
                st.markdown(f"**File {idx + 1}** - {len(pdf_data.getvalue()) / (1024 * 1024):.2f} MB")
                st.download_button(label="Download", data=pdf_data.getvalue(), key=f"converted_pdf_{idx}.pdf")

            st.success("Conversion complete!")

    # Information section
    st.sidebar.header("Information")
    st.sidebar.write("HEIC (High-Efficiency Image Format) is a file format for individual images and image sequences. "
                     "This app allows you to convert HEIC images to PDFs with ease.")

if __name__ == "__main__":
    main()
