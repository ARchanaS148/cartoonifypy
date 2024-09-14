import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to cartoonify an image
def cartoonify_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Step 1: Apply bilateral filter to smooth the image
    color = cv2.bilateralFilter(img_rgb, d=9, sigmaColor=300, sigmaSpace=300)

    # Step 2: Convert to grayscale and detect edges using median blur and adaptive threshold
    gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=9, C=2)

    # Step 3: Combine the edges and the color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Displaying the results
    plt.figure(figsize=(10, 10))

    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(img_rgb)

    plt.subplot(1, 3, 2)
    plt.title("Edges")
    plt.imshow(edges, cmap='gray')

    plt.subplot(1, 3, 3)
    plt.title("Cartoon Image")
    plt.imshow(cartoon)

    plt.show()

# Path to the input image
image_path = 'C:/Users/Archana Sundar/Downloads/dogcv.jpeg'

# Call the function to cartoonify the image
cartoonify_image(image_path)
