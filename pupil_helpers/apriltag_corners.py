import cv2

stream_window = 'RPi3 IR cam'
window_width = 240
window_height = 180
screen_width = 1680
screen_height = 1050
cv2.namedWindow(
stream_window,
flags=(cv2.WINDOW_NORMAL | cv2.WINDOW_GUI_NORMAL | cv2.WINDOW_FREERATIO))
cv2.setWindowProperty(stream_window, cv2.WND_PROP_TOPMOST, 1.0)
cv2.setWindowProperty(stream_window, cv2.WND_PROP_FULLSCREEN, 1.0)
cv2.resizeWindow(
    stream_window,
    window_width,
    window_height)
cv2.moveWindow(
    stream_window,
    screen_width - window_width,
    screen_height - window_height - 40)