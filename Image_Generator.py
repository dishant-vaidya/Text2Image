import streamlit as st
from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
import io

# Load Model

@st.cache_resource
def load_model():
    model_id = "CompVis/stable-diffusion-v1-4"
    
    if torch.cuda.is_available():
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16
        ).to("cuda")
    else:
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32
        ).to("cpu")

    return pipe

pipe = load_model()


# Streamlit UI

st.set_page_config(page_title="AI-Image Generator", layout="centered")
st.title("Text-to-Image Generator")
prompt = st.text_input("Enter a prompt")

# Generate and Download Button

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating image..."):
            try:
                image = pipe(prompt).images[0]
                st.image(image, caption="Generated Image", use_container_width=True)

                # Download button

                img_bytes = io.BytesIO()
                image.save(img_bytes, format='PNG')
                st.download_button(
                    label="Download Image",
                    data=img_bytes.getvalue(),
                    file_name="generated.png",
                    mime="image/png"
                )
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Enter a prompt.")
else:
    st.info("Enter a prompt and click 'Generate'.")

st.markdown("<center>---<center>", unsafe_allow_html=True)
st.markdown("<center>Dishant Vaidya</center>", unsafe_allow_html=True)
st.markdown("<center>vaidya.dishant@gmail.com</center>", unsafe_allow_html=True)