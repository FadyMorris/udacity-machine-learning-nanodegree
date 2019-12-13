![Udacity Logo](./docs/img/udacity_logo.svg)

# Udacity Machine Learning Engineer Nanodegree Capstone Project
## Landmark Recognition

> ### Fady Morris Milad Ebeid  
> ### December 13, 2019

Computer vision algorithms include methods for acquiring, processing, analyzing and understanding digital images, and extraction of data from the real world. It is an interdisciplinary field that deals with how can computers gain a high-level understanding of digital images. It aims to mimic human vision.  
Convolutional neural networks are now capable of outperforming humans on some computer vision tasks,
such as classifying images.  
In this project, I provide a solution to the Landmark Recognition Problem. Given an input photo of a place anywhere around the world, the computer can recognize and label the landmark in which this image was taken.

# Libraries Used :
- [Python 3.x](https://www.python.org)
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Tensorflow](https://www.tensorflow.org)
- [Keras](https://keras.io)


# Directory Structure :

  
- [src/](./src/) : Contains the project source code. Jupyter notebooks, Python scripts, and exported HTML files of the project Jupyter notebooks.  
- [docs/](./docs/) : Contains the project [report](./docs/report.pdf) and [proposal](./docs/proposal.pdf).  
   
   
**Full project directory structure :**
```
.
├── README.md                                            - Project readme file.
├── src/
│   ├── data_exploration_and_preprocessing.ipynb         - Code for dataset download and preprocessing.
│   ├── image_downloader.py                              - Python helper script to download images.
│   └── Udacity_MLND_capstone_landmark-recognition.ipynb - Project implementation.
├── docs/                     - Project documentation directory.
│   ├── proposal.pdf          - Project proposal.
│   ├── report.pdf            - Project report.
│   ├── figures/              - Project output plots and graphs.
│   ├── stats/                - Project output statistics, metrics, and dataset summary.
│   └── img/                  - Project logos. 
├── data/                     - Project dataset.
│   ├── index_train.csv       
│   ├── index_validation.csv
│   ├── index_test.csv
│   ├── test/
│   ├── train/
│   ├── validation/
│   └── input_csv/            - CSV from Google Landmarks dataset.
│       ├── train.csv
│       └── train_label_to_category.csv
│
└── models/     - Project saved training best weights, training history and bottleneck features
```




# Data Preparation and Structure

The prepared data for this project can be downloaded from this [Google Drive link](https://drive.google.com/open?id=1k9zJ23fMfEBk1XzAsRYAJQjK9cpYSQTr). Download the dataset file `data.tar.gz` and extract it to the project root directory. This is a subset dataset that was extracted from from Common Visual Data Foundation [Google Landmarks Dataset v2](https://github.com/cvdfoundation/google-landmark). 
