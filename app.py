import streamlit as st
from PIL import Image
from fpdf import FPDF
import pyheif
import io

def heic_to_pdf(heic_images, output_pdf_path, quality=75, single_page_layout=True):
    pdf = FPDF()
    
    for heic_image in heic_images:
        heif_file = pyheif.read(heic_image.read())
        img = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Resize the image to maintain aspect ratio and reduce file size
        img.thumbnail((1024, 1024))
        
        pdf.add_page()
        
        if single_page_layout:
            pdf.image(img, x=10, y=10, w=190)
        else:
            pdf.image(img, x=10, y=10, w=90)
            pdf.ln(90)
        
    pdf.output(output_pdf_path)

def main():
    st.title("HEIC to PDF Converter")
    st.write("Convert HEIC images to PDF effortlessly.")

    # Upload HEIC files
    heic_files = st.file_uploader("Drag and drop HEIC files here", type=["heic"], accept_multiple_files=True)

    if heic_files:
        # Display file details
        st.write("Files to convert:")
        for file in heic_files:
            st.write(f"- {file.name} ({round(file.size / 1e6, 2)} MB)")

        # Advanced Options
        st.write("\n**Advanced Options**")

        # Image Quality
        image_quality = st.slider("Image Quality", min_value=1, max_value=100, value=75)

        # PDF Layout
        pdf_layout = st.radio("PDF Layout", ["Single image per page", "Multiple images per page"])

        # Convert button
        if st.button("Convert to PDF"):
            # Perform conversion
            pdf_layout_single_page = pdf_layout == "Single image per page"
            heic_paths = heic_files
            output_pdf_path = "output.pdf"  # You can customize the output path/name

            heic_to_pdf(heic_paths, output_pdf_path, quality=image_quality, single_page_layout=pdf_layout_single_page)

            # Provide download link for the generated PDF
            st.success("Conversion successful! Click below to download the PDF.")
            st.markdown(f"Download [Converted PDF](./{output_pdf_path})")

if __name__ == "__main__":
    main()
