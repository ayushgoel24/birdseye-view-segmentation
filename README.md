# Birdseye-view with Segmentation

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![GitHub Issues](https://img.shields.io/github/issues/ayushgoel24/birdseye-view-segmentation.svg)](https://github.com/ayushgoel24/birdseye-view-segmentation/issues)
[![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-orange.svg)](https://github.com/ayushgoel24/birdseye-view-segmentation)

This repository contains the implementation of an end-to-end perception architecture for autonomous vehicles. The goal of this project is to extract semantic representations from multiple sensors and fuse them into a single "bird's-eye-view" coordinate frame for consumption by motion planning algorithms. The proposed architecture directly extracts a bird's-eye-view representation of a scene using image data from an arbitrary number of cameras.

## Project Overview

The aim of perception for autonomous vehicles is to extract semantic representations from various sensors and integrate these representations into a unified "bird's-eye-view" coordinate frame. This project proposes a new end-to-end architecture that directly extracts a bird's-eye-view representation of a scene using image data from an arbitrary number of cameras.

The core idea is to "lift" each image individually into a frustum of features for each camera and then "splat" all the frustums into a rasterized bird's-eye-view grid. By training on the entire camera rig, the model learns how to represent images and fuse predictions from all cameras into a single cohesive representation of the scene, even in the presence of calibration errors.

Additionally, the representations inferred by the model enable interpretable end-to-end motion planning by "shooting" template trajectories into a bird's-eye-view cost map output by the network.

## Key Features

- End-to-end architecture for perception in autonomous vehicles.
- Extraction of bird's-eye-view representation from image data.
- Fusion of semantic representations from multiple camera sensors.
- Robustness to calibration error.
- Outperforms baselines and prior work in object segmentation and map segmentation tasks.
- Interpretable end-to-end motion planning using the inferred representations.
- Benchmarking against lidar-based models.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ayushgoel24/birdseye-view-segmentation.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```
TODO: Update the usage section
<!-- ## Usage

1. Prepare your dataset by following the instructions in the `data/README.md` file.

2. Train the perception model:

   ```bash
   python train.py --dataset /path/to/dataset
   ```

3. Evaluate the trained model:

   ```bash
   python evaluate.py --dataset /path/to/dataset --model /path/to/saved/model
   ```

4. Run motion planning using the inferred representations:

   ```bash
   python motion_planning.py --map /path/to/birds-eye-view-cost-map
   ``` -->

<!-- ## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. For major changes, please discuss them with the repository owners before submitting.

Please make sure to follow the [Code of Conduct](CODE_OF_CONDUCT.md) in all your interactions. -->

## Results

<table>
    <tr>
        <td align = "center"> <img src="./static/gif/map_1.gif"></td>
        <td align = "center"> <img src="./static/gif/map_2.gif"></td>
    </tr>
    <tr>
        <td align = "center">Environment 1</td>
        <td align = "center">Environment 2</td>
    </tr>
</table>

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or questions, please contact [ayush.goel2427@gmail.com].

Happy coding!