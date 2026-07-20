"""
=========================================================
File: camera.py

Project:
    Camera Detector

Description:
    Handles all camera operations including initialization,
    frame acquisition, image capture, and resource management.

Author:
    Sinai Cabrera Retana

Created:
    July 2026
=========================================================
"""

from config import FRAME_HEIGHT, FRAME_WIDTH, WINDOW_NAME, FPS, CAMERA_INDEX
import cv2
import os


class Camera:
    # Camera management class that encapsulates all operations related to camera handling.

    def __init__(self):
        self.camera = None
        self.width = FRAME_WIDTH
        self.height = FRAME_HEIGHT
        self.window_name = WINDOW_NAME
        self.image_counter = 0  # Counter for naming captured images


    def open_camera(self) -> bool:
        """
        Opens the configured camera and applies the initial settings for resolution and frame rate.
        Returns:
            bool: True if the camera was successfully opened, False otherwise.
        """
        self.camera = cv2.VideoCapture(CAMERA_INDEX)

        if not self.camera.isOpened():
            print("Error: Could not open camera.")
            return False
        
        self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.camera.set(cv2.CAP_PROP_FPS, FPS)
        
        return True

    def close_camera(self):
        """
        Closes the camera and releases all associated resources. Also destroys any OpenCV windows that were created.
        """
        if self.camera:
            self.camera.release()
        cv2.destroyAllWindows()

    def read_frame(self):
        """
        Reads a single frame from the camera.add()
        Returns:
            numpy.ndarray: The captured frame, or None if the camera is not open or an error occurred.
        """
        if not self.camera:
            return None
        ret, frame = self.camera.read()
        if not ret:
            print("Error: Could not read frame.")
            return None
        return frame

    def show_frame(self, frame):
        """
        Shows the provided frame in a window. If the 'Esc' key is pressed, the camera will be closed.
        Args:
            frame (numpy.ndarray): The frame to display.
        """
        if frame is not None:
            cv2.imshow(self.window_name, frame)
            #if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
                #self.close_camera()

    def capture_image(self, frame, folder='dataset'):
        """
        Saves the current frame with an automatic sequential filename.
        Args:
            frame (numpy.ndarray): The frame to save.
            folder (str): The name of the folder where the image will be saved.
        """
        if frame is None:
            return False
        os.makedirs(folder, exist_ok=True)
        filename = os.path.join(
            folder,
            f"img_{self.image_counter:04}.jpg"
        )
        success = cv2.imwrite(filename, frame)

        if success:
            print(f"Image saved as {filename}")
            self.image_counter += 1
        return success

    def change_resolution(self, width, height):
        """
        Changes the resolution of the camera to the specified width and height.
        Args:
            width (int): The desired width of the camera frame.
            height (int): The desired height of the camera frame.
        """
        self.width = width
        self.height = height
        if self.camera:
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    def is_open(self) -> bool:
        """
        Checks if the camera is currently open and ready for use.
        Returns:
            bool: True if the camera is open and ready, False otherwise.
        """
        return self.camera is not None and self.camera.isOpened()
    