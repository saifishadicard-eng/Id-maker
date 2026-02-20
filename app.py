import streamlit as st
from PIL import Image
import io

# Page Configuration
st.set_page_config(page_title="Smart ID Resizer", layout="centered")

st.title("🪪 Smart ID Card Resizer")
st.write("Apni ID card ki photo upload karein aur use perfect print size mein convert karein.")

# File Uploader
uploaded_file = st.file_uploader("Photo select karein (JPG, PNG, JPEG)", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    # Image Open karna
    img = Image.open(uploaded_file)
    
    # Standard ID Card Size in Pixels (at 300 DPI for high quality print)
    # 8.5 cm x 5.5 cm approx 1004 x 650 pixels hota hai
    width_px = 1004
    height_px = 650
    
    # Resize Logic
    resized_img = img.resize((width_px, height_px), Image.Resampling.LANCZOS)
    
    # Display Results
    st.subheader("✅ Aapka Resized ID Card")
    st.image(resized_img, caption="Preview: 8.5cm x 5.5cm", use_container_width=True)
    
    # Download Button taiyar karna
    buf = io.BytesIO()
    resized_img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.download_button(
        label="📥 Download Ready-to-Print ID",
        data=byte_im,
        file_name="resized_id_card.png",
        mime="image/png"
    )

st.divider()
st.info("Tip: Ise A4 sheet par print karte waqt 'Actual Size' select karein.")
