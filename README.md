# DetecTT
Using Yolo and other AI tools for infusing AI with Table Tennis.

# Objective
- Use Yolo to detect: players, table tennis ball and the quadrants of the table.
- Use the information to perform some analysis on videos, such as distance of player from table, ball speed, player movement speed.

# Milestones: 
[x] Create PipVenv
[x] Download and install Yolo
[x] Setup test data
[] Experiment with parameters - specifically, adjust threshold so that players aren't detected twice.
    - tricky since yolo docs define the parameters before inference,
    - post-hoc thresholding ought to be possible, though!
[] Experiment with pose estimation from Yolo - perhaps I can retrieve the angle of player's bats?
    - seems like yolo does not have an output class for `bat'.
    - perahps some model training is needed, with a new class?
        - https://medium.com/@gonzacor/ball-tracking-and-detection-in-sports-with-new-yolov5-9f30f5252cf2
[] Run Yolo on an image, and short video
[] to be continued...

# Useful Links:
https://www.ultralytics.com/yolo
https://github.com/ultralytics/ultralytics
https://medium.com/@gonzacor/ball-tracking-and-detection-in-sports-with-new-yolov5-9f30f5252cf2

# References:
https://zenodo.org/records/7347926