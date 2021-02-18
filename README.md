## Overview
In this project, two models (Faster R-CNN and R-FCN) in TensorFlow model zoo were trained on Pascal VOC dataset. Steps and detailed descriptions on steps can be found in the files above.

## Model Architectures
![](images/faster-RCNN.png)
Faster-RCNN (Source: [Ren et al., 2016](https://arxiv.org/pdf/1506.01497.pdf))

![](images/R-FCN.png)
R-FCN (Source: [Dai et al., 2016](https://arxiv.org/pdf/1605.06409.pdf))

## Model Performances
![](images/faster-rcnn-iou50.png)  |  ![](images/faster-rcnn-iou75.png)
:-------------------------:|:-------------------------:
Faster-RCNN (mAP, IoU&ge;.50) | Faster-RCNN (mAP, IoU&ge;.75)

![](images/r-fcn-iou50.png)  |  ![](images/r-fcn-iou75.png)
:-------------------------:|:-------------------------:
R-FCN (mAP, IoU&ge;.50) | R-FCN (mAP, IoU&ge;.75)

## Some Results
| ![](images/faster-rcnn-result1.png) | ![](images/r-fcn-result1.png) | ![](images/ground-truth-result1.png) |
| :---:       |    :----:   |          :---: |
| Faster-RCNN      | R-FCN       | Ground-truth boxes   |

| ![](images/faster-rcnn-result2.png) | ![](images/r-fcn-result2.png) | ![](images/ground-truth-result2.png) |
| :---:       |    :----:   |          :---: |
| Faster-RCNN      | R-FCN       | Ground-truth boxes   |

| ![](images/faster-rcnn-result3.png) | ![](images/r-fcn-result3.png) | ![](images/ground-truth-result3.png) |
| :---:       |    :----:   |          :---: |
| Faster-RCNN      | R-FCN       | Ground-truth boxes   |
