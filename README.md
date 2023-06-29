# Multiview Camera Calibration for Ground Plane Estimation

The camera calibration pipeline involves the computation of camera intrinsics and extrinsics. The user provides as input checkerboard footage from each camera and multiple-view footage, including data from an omnidirectional camera. OpenCV is used to calculate the camera intrinsics. For extrinsics calibration, OpenSfM is utilised. The resulting extrinsics are adjusted and aligned by employing a user-selected set of 4–10 ground points in each view. These points are also used to determine a region of interest, enabling the adjustment, scaling, and rotation of the ground plane projection. This process ensures that the projection focuses accurately on the desired area.

This is part of the pipeline developed for Multi-view tracking based on optical flow found at: https://github.com/wgrosche/MVTracking
 
## Environment Setup

Environment setup is described in [setup.md](docs/setup.md).


## Calibration
A step by step guide to calibrating the cameras is described in [calibration.md](docs/calibration.md).

### 3D Reconstruction

<p align="center">
<img src="/images/reconstruction.gif" alt="Example reconstruction visualisation." width="60%"/>
</p>


### Ground Plane Estimation

<p align="center">
<img src="/images/scaled_groundplane.jpg" alt="Example ground plane projection." width="60%"/>
</p>


#### Reference

If you found this code useful, please cite us:

```
@misc{mvcamcalibration2023,
  author        = {Grosche, Wilke and Engilberge, Martin and Fua, Pascal},
  year          = {2023},
  title         = {Multiview Camera Calibration for Ground Plane Estimation},
  howpublished = {\url{https://github.com/wgrosche/MultiviewCameraCalibration/}}
}
```
#### License

By downloading this program, you commit to comply with the license as stated in the LICENSE file.


