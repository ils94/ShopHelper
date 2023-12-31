import os
import cv2
import numpy as np
import pyautogui
import globalVariables


def is_image_on_screen():
    create_images_directory()

    image_files = []

    # Specify the external directory path
    external_directory = globalVariables.image_detection_path

    # Iterate over files in the external directory
    for filename in os.listdir(external_directory):
        # Check if the file has a common image file extension (e.g., jpg, png, jpeg)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # If it's an image file, add it to the list
            image_files.append(os.path.join(external_directory, filename))

    for image_path in image_files:
        if globalVariables.start:
            image_to_detect = cv2.imread(image_path)

            screenshot = pyautogui.screenshot()

            screenshot_np = np.array(screenshot)
            screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

            result = cv2.matchTemplate(screenshot_cv, image_to_detect, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

            if max_val > 0.7:
                # If the image is found, move the mouse to its location
                image_height, image_width, _ = image_to_detect.shape
                center_x = max_loc[0] + image_width // 2
                center_y = max_loc[1] + image_height // 2
                pyautogui.moveTo(center_x, center_y)


def create_images_directory():
    if not os.path.exists(globalVariables.image_detection_path):
        os.makedirs(globalVariables.image_detection_path)
