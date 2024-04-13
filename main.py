# This file will run Yolo on an image/video for object detection.
#Current Task: Import Yolo and Run on an image

from ultralytics import YOLO

def main():
    model = YOLO('yolov8n.pt') # pre-trained yolo model
    # model.cuda() # to make the model run on gpu
    results = model("./images/table_tennis_singles_mens_cropped.jpg") # The example given by ultralytics - let's try it out!
    
    # let's explore results
    for result in results:
        boxes = result.boxes
        masks = result.masks
        keypoints = result.probs
        probs = result.probs
        result.show()






if __name__ == '__main__':
    main()