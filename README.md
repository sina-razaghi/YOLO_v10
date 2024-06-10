# Object Detection using YOLOv10

This project provides a real-time object detection application using the YOLOv10 model and a live webcam. It is trained on a small custom 5-class dataset and shows promising results.

A research article titled "YOLOv10: Real-Time End-to-End Object Detection" was published in May 2024. Initial results indicate that its performance is significantly better than previous YOLO models.
![111](https://github.com/sina-razaghi/YOLO_v10/assets/47954697/cb215fbe-b4ce-42d2-b50b-4010546f7aff)


## Key Innovations:
Dual Label Assignment without NMS: YOLOv10 utilizes a dual label assignment strategy, incorporating both one-to-one and one-to-many matches during training, resulting in richer supervision and improved accuracy in inference.
Performance-Accuracy-based Model Design: YOLOv10 includes several optimizations to balance between performance and accuracy, including lightweight classification heads, separate spatial-channel sampling, and design of directed ranking blocks.

## Advantages:
Superior Accuracy and Speed: Compared to previous YOLO models, including YOLOv9, YOLOv10 shows significantly better performance across various object detection tasks, including COCO.
Small Object Detection: This model is specifically designed to improve small object detection.
Better Localization Accuracy: YOLOv10 can localize objects with higher precision in images and videos.
Enhanced Efficiency: This model is optimized for real-time applications with high performance.

## Disadvantages:
Not Yet Released: YOLOv10 has not been officially released yet, and its code is not publicly available.
Need for Further Research: Further research is needed to validate the performance of YOLOv10 in real-world scenarios and various applications.

=> Overall, YOLOv10 is a promising object detection model with the potential to offer better accuracy and speed compared to previous YOLO generations. However, keep in mind that this model is still in early stages of development and its paper has not been published in any journals or conferences.

<img src="https://github.com/sina-razaghi/YOLO_v10/assets/47954697/ec33ab8b-b9db-46c5-8b08-1058746c9d5a" width="400" />

### Notes
- You can use different datasets with more classes to train the model.
- You can train the YOLOv10 model with different hyperparameters to improve performance.
- You can customize the code for your specific needs.

### Prerequisites
- opencv_contrib_python==4.7.0.72
- opencv_python==4.10.0.82
- opencv_python_headless==4.9.0.80
- supervision==0.21.0
- ultralytics==8.1.34

### Resources
- YOLOv10 paper: https://arxiv.org/abs/2405.14458
- YOLOv10 GitHub repository: https://github.com/THU-MIG/yolov10
- YOLO website: https://docs.ultralytics.com/
