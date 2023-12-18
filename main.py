import cv2
from PIL import Image
from util import get_limits


colors = {'yellow': [0, 255, 255],
          'blue': [255, 0, 0],
          'red': [0, 0, 255]}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, color_value in colors.items():
        lower_limit, upper_limit = get_limits(color=color_value)

        mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

        mask_image = Image.fromarray(mask)

        bbox = mask_image.getbbox()

        if bbox is not None:
            x1, y1, x2, y2 = bbox


            if color_name == 'yellow':
                 border_color = (0, 255, 255)
            elif  color_name == 'blue':
                border_color = (255, 0, 0) 
            elif color_name == 'red':
                border_color = (0, 0, 255)

            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), border_color, 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
