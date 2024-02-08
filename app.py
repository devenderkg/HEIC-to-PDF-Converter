import streamlit as st
from PIL import Image
from fpdf import FPDF

def heic_to_pdf(heic_images, output_pdf_path, quality=75, single_page_layout=True):
    pdf = FPDF()
    
    for heic_image in heic_images:
        img = Image.open(heic_image)
        
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
        st.sidebar.subheader("Advanced Options")

        # Image Quality
        image_quality = st.sidebar.slider("Image Quality", min_value=1, max_value=100, value=75)

        # PDF Layout
        pdf_layout = st.sidebar.radio("PDF Layout", ["Single image per page", "Multiple images per page"])

        # Convert button
        if st.button("Convert to PDF"):
            # Perform conversion
            pdf_layout_single_page = pdf_layout == "Single image per page"
            heic_paths = [file.name for file in heic_files]
            output_pdf_path = "output.pdf"  # You can customize the output path/name

            heic_to_pdf(heic_paths, output_pdf_path, quality=image_quality, single_page_layout=pdf_layout_single_page)

            # Provide download link for the generated PDF
            st.success("Conversion successful! Click below to download the PDF.")
            st.markdown(f"Download [Converted PDF](./{output_pdf_path})")

if __name__ == "__main__":
    main()
