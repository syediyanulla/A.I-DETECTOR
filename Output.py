import streamlit as st
from PIL import Image
from api import process_image, process_video

# Set the title of your Streamlit app
st.title("AI Generated Detector App")

# Choose between image and video upload
file_type = st.radio("File type:", ("Image"))

# Upload file through Streamlit

uploaded_file = st.file_uploader(f"Choose a {file_type.lower()}...", type=[
    "jpg", "jpeg", "png"])

model = st.selectbox("Select Model", ("EfficientNetB4", "EfficientNetB4ST",
                     "EfficientNetAutoAttB4", "EfficientNetAutoAttB4ST"))
dataset = st.radio("Dataset", ("DFDC"))
threshold = st.slider("Select Threshold", 0.0, 1.0, 0.5)

if file_type == "Video":
    frames = st.slider("Select Frames", 0, 100, 50)
# Display the uploaded file
if uploaded_file is not None:
    if file_type == "Image":
        # Display the uploaded image
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", width=200)
        except Exception as e:
            print(e)
            st.error(f"Error: Invalid Filetype")
    else:
        st.video(uploaded_file)

    # Check if the user wants to perform the deepfake detection
    if st.button("Check for Deepfake"):
        # Convert file to bytes for API request
        if file_type == "Image":
            # uploaded_file = check_and_convert_image(uploaded_file)
            result, pred = process_image(
                image=uploaded_file, model=model, dataset=dataset, threshold=threshold)
            st.markdown(
                f'''
                <style>
                    .result{{
                        color: {'#ff4b4b' if result == 'fake' else '#6eb52f'};
                    }}
                </style>
                <h3>The given {file_type} is: <span class="result"> {result} </span> with a probability of <span class="result">{pred:.2f}</span></h3>''', unsafe_allow_html=True)

        else:
            with open(f"uploads/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.read())

            video_path = f"uploads/{uploaded_file.name}"

            result, pred = process_video(video_path, model=model,
                                         dataset=dataset, threshold=threshold, frames=frames)

            st.markdown(
                 f'''
                <style>
                    .result{{
                        color: {'#ff4b4b' if result == 'fake' else '#6eb52f'};
                    }}
                </style>
                <h3>The given {file_type} is: <span class="result"> {result} </span> with a probability of <span class="result">{pred:.2f}</span></h3>''', unsafe_allow_html=True)
else:
    st.info("Please upload a file.")


