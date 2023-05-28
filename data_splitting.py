import os
import shutil
import random

# Define the path to the directory containing your image data
data_dir = 'leaf'

# Define the path to the directory where you want to save the separated data
save_dir = 'dataset'

# Define the percentage of data to be used for validation
val_percent = 0.2

# Create the directories for training and validation data
train_dir = os.path.join(save_dir, 'train/images')
os.makedirs(train_dir, exist_ok=True)

val_dir = os.path.join(save_dir, 'val/images')
os.makedirs(val_dir, exist_ok=True)

# Get the list of all image filenames in the data directory
image_filenames = os.listdir(data_dir)

# Shuffle the list of image filenames randomly
random.shuffle(image_filenames)

# Calculate the number of images to be used for validation
num_val_images = int(val_percent * len(image_filenames))

# Separate the data into training and validation sets
train_image_filenames = image_filenames[num_val_images:]
val_image_filenames = image_filenames[:num_val_images]

# Copy the training images to the train directory
for image_filename in train_image_filenames:
    src = os.path.join(data_dir, image_filename)
    dst = os.path.join(train_dir, image_filename)
    shutil.copyfile(src, dst)

# Copy the validation images to the val directory
for image_filename in val_image_filenames:
    src = os.path.join(data_dir, image_filename)
    dst = os.path.join(val_dir, image_filename)
    shutil.copyfile(src, dst)