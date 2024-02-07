import streamlit as st
import os
from PIL import Image
import pyheif
from img2pdf import convert

def convert_heic_to_pdf(heic_files, image_quality, pdf_layout):
    # ... (unchanged)

    def main():
        st.sidebar.title("Unlocking the Power of HEIC: Convert to PDF with Ease!")
        st.sidebar.markdown(
            "Tired of compatibility issues with HEIC images?\n\n"
            "Introducing the HEIC to PDF Converter, your one-stop solution for seamless file conversion! "
            "Whether you're sharing photos with friends on different devices or submitting documents for work, "
            "our app makes things effortless and efficient.\n\n"
            "Here's why you'll love us:\n\n"
            "- **Simple drag-and-drop:** No complicated steps. Just drag your HEIC files and watch them magically transform. ✨\n"
            "- **Quality you can trust:** Choose from high, medium, or low compression levels to maintain perfect image quality or smaller file sizes.\n"
            "- **Customize your PDFs:** Arrange your images in single or multi-page layouts to suit your needs. ️\n"
            "- **Fast and secure:** Your conversions happen in a flash, with complete data security guaranteed.\n"
            "- **Accessible from anywhere:** Use our app from any device, anytime you need it.\n"
            "- **Free and easy to use:** No sign-ups required, just start converting in seconds!\n\n"
            "Don't get locked out by incompatible formats! Convert your HEIC images to universal PDFs with the HEIC to PDF Converter today!"
        )

        st.title("HEIC to PDF Converter")
        st.markdown("Convert HEIC files to PDF with ease!")

        # Upload HEIC files
        heic_files = st.file_uploader("Drag and drop HEIC files here or click to choose files", type=["heic"], accept_multiple_files=True)

        # Conversion options
        with st.expander("Conversion Options"):
            image_quality = st.selectbox("Image Quality:", ["High Quality", "Medium Quality", "Low Quality"], index=0)
            pdf_layout = st.radio("PDF Layout:", ["Single image per page", "Multiple images per page", "Contact sheet"], index=0)

        # Convert button
        if st.button("Convert"):
            if heic_files:
                st.info("Converting... Please wait.")
                pdf_files = convert_heic_to_pdf(heic_files, image_quality, pdf_layout)
                st.success("Conversion successful!")

                # Display and allow download of converted PDFs
                for pdf_file in pdf_files:
                    st.markdown(f"Download [**{os.path.basename(pdf_file)}**](./{pdf_file})")
            else:
                st.warning("Please upload HEIC files first.")

    # Call the main function to run the Streamlit app
    if __name__ == "__main__":
main()
