# Video and Image Prediction Application

## Overview
This application is a Streamlit-based web interface that allows users to perform predictions on both images and videos using various models and datasets. It supports multiple file formats and provides flexible threshold settings for predictions.

## Features
- Image prediction support (JPG, JPEG, PNG)
- Video prediction support (MP4)
- Multiple model compatibility
- Customizable prediction thresholds
- Frame-by-frame video analysis
- Error handling and reporting

## Prerequisites
- Python 3.x
- PIL (Python Imaging Library)
- Streamlit
- Custom modules:
  - youtube (for video prediction)
  - image (for image prediction)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure
```
project/
├── main.py
├── youtube.py
├── image.py
├── uploads/
└── README.md
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Upload either an image or video file through the web interface.
3. Select the desired model and dataset.
4. Adjust the threshold value as needed.
5. For videos, specify the number of frames to analyze.
6. View the prediction results.

## File Format Support
- Images: jpg, jpeg, png
- Videos: mp4

## Functions

### `allowed_file(filename, accepted_extensions)`
Validates if the uploaded file has an allowed extension.

### `process_image(image, model, dataset, threshold)`
Processes uploaded images and returns prediction results.
- Parameters:
  - `image`: Image file object
  - `model`: Selected prediction model
  - `dataset`: Dataset to use for prediction
  - `threshold`: Prediction threshold value

### `process_video(video_path, model, dataset, threshold, frames)`
Processes uploaded videos and returns prediction results.
- Parameters:
  - `video_path`: Path to the video file
  - `model`: Selected prediction model
  - `dataset`: Dataset to use for prediction
  - `threshold`: Prediction threshold value
  - `frames`: Number of frames to analyze

## Error Handling
- The application includes comprehensive error handling for both image and video processing
- Temporary files are automatically cleaned up after processing
- Detailed error messages are provided for debugging

## Notes
- Ensure the 'uploads' directory exists in the project root
- Temporary files are automatically deleted after processing
- The application requires sufficient system resources for video processing

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Add your license information here]

## Contact
[Add your contact information here]