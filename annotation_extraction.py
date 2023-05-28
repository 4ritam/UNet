import json
import os

root_folder = "dataset"
splits = ["train", "val"]


for split in splits:

    annotation_path = os.path.join(root_folder, split, "annotations.json")
    # Path to dataset folders
    image_folder = os.path.join(root_folder, split, "images")
    mask_folder = os.path.join(root_folder, split, "masks")
    box_folder = os.path.join(root_folder, split, "boxes")

    annotations = {
        "images": []
    }

    # Loop over images in folder
    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg"):
            # Get image ID
            image_id = os.path.splitext(filename)[0]
            
            # Get image filename
            image_filename = os.path.join(image_folder, filename)
            
            # Get mask filename
            mask_filename = os.path.join(mask_folder, f"{image_id}.png")
            
            # Get box filename
            box_filename = os.path.join(box_folder, f"{image_id}.json")
            
            # Load box coordinates from JSON file
            with open(box_filename, "r") as f:
                boxes = json.load(f)
            
            # Create image dictionary
            image_dict = {
                "id": image_id,
                "file_name": image_filename,
                "objects": []
            }
            
            # Loop over boxes and add them to image dictionary
            for box in boxes["boxes"]:
                # Get object class name or ID (assuming it's in the box dictionary)
                class_name = 1
                
                # Get bounding box coordinates
                bbox = box
                
                # Add object dictionary to image dictionary
                image_dict["objects"].append({
                    "class": class_name,
                    "box": bbox
                })
            
            # Add image dictionary to annotations dictionary
            annotations["images"].append(image_dict)


    with open(annotation_path, "w") as f:
        json.dump(annotations, f, indent=4)
