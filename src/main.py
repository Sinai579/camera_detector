from camera import Camera
import cv2

def main():
    print("Starting program...")
    camera = Camera()
    print("Opening camera...")
    if not camera.open_camera():
        print("Failed to open camera.")
        return

    while True:
        frame = camera.read_frame()
        if frame is None:
            break

        camera.show_frame(frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            camera.capture_image(frame, "capture.png")

    camera.close_camera()

if __name__ == "__main__":
    main()