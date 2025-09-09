# AI Text-to-Image Generator Web App

A simple web app to generate images from text prompts using **Stable Diffusion** and **Streamlit**.  
This project runs locally with **no API keys or authentication required**, leveraging the Hugging Face `diffusers` library.

---

## Features

- Generate high-quality AI images from any text prompt  
- Simple and clean Streamlit UI for instant use  
- Supports both CPU and GPU (auto-detects your hardware)  
- Download generated images directly from the app  
- Uses the open `CompVis/stable-diffusion-v1-4` model

---

## Disclaimer

- The first time you run the app, it will **download a large (~4GB) Stable Diffusion model**, so please be patient.  
- Image generation can take **several seconds to minutes** depending on your hardware:  
  - **GPU users** usually get results within seconds.  
  - **CPU users** should expect longer generation times (1-5 minutes per image).  
