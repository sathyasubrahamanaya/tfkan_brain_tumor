import streamlit as st
import tensorflow as tf
from PIL import Image
import cv2
import numpy as np
import joblib
import os

from models import model0,model0convKAN

# Disable oneDNN optimizations (if needed)
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Load weights for both models (ensure these files exist or update the paths accordingly)
model0.load_weights('models/model_new.keras')
model0convKAN.load_weights('models/modelconvKAN.keras')

st.title("BrDX")
st.header("Brain Tumor Detection")
st.divider()
st.text("Upload MRI Image")

# Load label encoder for mapping predicted class indices to names
label_encoder = joblib.load('models/le.pkl')

uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

if uploaded_image:
    # Read and preprocess the image
    image = np.array(Image.open(uploaded_image))
    image_resized = cv2.resize(image, (64, 64)) / 255.0
    st.image(uploaded_image)

    if st.button("Detect", use_container_width=True):
        # Prediction using Model 0
        pred0 = model0.predict(np.array([image_resized]))
        pred_class_index0 = np.argmax(pred0, axis=1)
        pred_class0 = label_encoder.inverse_transform(pred_class_index0)
        # Ensure to index correctly since np.argmax returns an array
        pred_prob0 = pred0[0][pred_class_index0[0]]
        
        # Prediction using Model KAN
        predKAN = model0convKAN.predict(np.array([image_resized]))
        pred_class_indexKAN = np.argmax(predKAN, axis=1)
        pred_classKAN = label_encoder.inverse_transform(pred_class_indexKAN)
        pred_probKAN = predKAN[0][pred_class_indexKAN[0]]
        
        # Display results side by side using two columns
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Model 0 Prediction")
            if pred_class0[0] == 'no_tumor':
                st.success(f"Image has NO TUMOR with {int(pred_prob0 * 100)}% prediction accuracy")
            else:
                st.success(f"Image is {pred_class0[0].upper()} with {int(pred_prob0 * 100)}% prediction accuracy")
        
        with col2:
            st.subheader("Model KAN Prediction")
            if pred_classKAN[0] == 'no_tumor':
                st.success(f"Image has NO TUMOR with {int(pred_probKAN * 100)}% prediction accuracy")
            else:
                st.success(f"Image is {pred_classKAN[0].upper()} with {int(pred_probKAN * 100)}% prediction accuracy")
        
        st.divider()
        st.subheader("Prediction Comparison")
        st.write("### Prediction Probabilities")
        st.write(f"**Model CNN MLP:** {int(pred_prob0 * 100)}%")
        st.write(f"**Model KAN:** {int(pred_probKAN * 100)}%")