Color Detection using OpenCV This project demonstrates how to detect and highlight different colors in real-time using OpenCV. It utilizes the HSV color space and contour detection techniques to identify and draw contours around objects of specific colors. 

## Features 
- Detect and highlight four different colors: blue, red, yellow, and green 
- Draw contours around detected objects of the specified colors 
- Draw circles at the center of the detected objects 
- Display the color name on the detected objects 

## Requirements 
- Python 3.x 
- OpenCV 
- NumPy 
- imutils 

## Installation 
1. Clone the repository with `git clone` 
2. Install the required dependencies: `pip install opencv-python numpy imutils` 

## Usage 
1. Open the terminal and navigate to the project directory. 
2. Run the script: python `color_detection.py` 
3. The script will open a window displaying the real-time video feed from your camera. 
4. Objects of the specified colors (blue, red, yellow, and green) will be detected, and their contours will be drawn. 
5. Circles will be drawn at the center of the detected objects, and the color name will be displayed on the objects. 
6. Press the 'q' key to exit the program. 

## Customization 
You can customize the color ranges by modifying the colors dictionary in the script. The dictionary contains the lower and upper boundaries for each color in the HSV color space. Adjust these values as needed to detect different shades or hues of the colors. 

```python 
colors = { 'blue': [np.array([95, 255, 85]), np.array([120, 255, 255])], 'red': [np.array([161, 165, 127]), np.array([178, 255, 255])], 'yellow': [np.array([16, 0, 99]), np.array([39, 255, 255])], 'green': [np.array([33, 19, 105]), np.array([77, 255, 255])] } 
```

## Contributing 
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. 

## License 
This project is licensed under the MIT License. 

## Acknowledgments 
This project was inspired by the tutorial "Colors Detection using masks & contours in OpenCV" by Sardor Abdirayimov.
