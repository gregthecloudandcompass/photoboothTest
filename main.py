import cv2
import numpy as np

WINDOW_NAME = "Image"


def open_display_window(width, height):
    """Open the cv2 window for displaying images with bounding boxeses."""
    cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(WINDOW_NAME, width, height)
    cv2.moveWindow(WINDOW_NAME, 0, 0)
    cv2.setWindowTitle(WINDOW_NAME, WINDOW_NAME)
    set_full_screen(True)


def set_full_screen(full_scrn):
    """Set display window to full screen or not."""
    prop = cv2.WINDOW_FULLSCREEN if full_scrn else cv2.WINDOW_NORMAL
    cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, prop)


def set_res(cap, x,y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))
    return str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

i = 0

def show_webcam(mirror=False):
    open_display_window(800, 800)
    set_full_screen(True)
    cam = cv2.VideoCapture(0)
    #set_res(cam,160,120)
    while True:
        i = i + 1
        ret_val, img = cam.read()
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        if mirror:
            img = cv2.flip(img, 1)
        #img = find_faces(img)
        cv2.imshow(WINDOW_NAME, img)
        cv2.imwrite('kang' + str(i) + '.jpg', frame)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
    cv2.destroyAllWindows()


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def find_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()