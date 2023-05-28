import os
import json
import cv2
import shutil
import numpy as np

data_dir = 'dataset'
splits = ["train", "val"]

for split in splits:
    # Loop over each image in the dataset
    image_dir = os.path.join(data_dir, split, "images")

    mask_dir = os.path.join(data_dir, split, "masks")
    os.makedirs(mask_dir, exist_ok=True)

    box_dir = os.path.join(data_dir, split, "boxes")
    os.makedirs(box_dir, exist_ok=True)

    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg'):
            # Load the image
            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            _, thresh = cv2.threshold(gray, 8, 255, cv2.THRESH_BINARY)

            # Find the contours in the binary image
            contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Find the bounding box of the object mask
            # mask = cv2.bitwise_not(thresh)
            areas = [cv2.contourArea(c) for c in contours]
            max_index = np.argmax(areas)
            cnt=contours[max_index]
            x, y, w, h = cv2.boundingRect(cnt)
            bbox = [x, y, x + w, y + h]
            # Save the object mask and bounding box to disk
            mask_path = os.path.join(mask_dir, filename.replace('.jpg', '.png'))
            cv2.imwrite(mask_path, thresh)

            box_path = os.path.join(box_dir, filename.replace('.jpg', '.json'))
            with open(box_path, 'a') as f:
                json.dump({'boxes': [bbox]}, f)