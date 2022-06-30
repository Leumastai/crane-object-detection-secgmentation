## Crane Object Detection and Crane Handle Segmentation
This repo includes codes for crane object detection and segmentation. The goal of this project is to improve my ML skill. This project is best executed in a Google Colaboratory environment

## Data Sourcing, Processing, and Training

Crane images was scraped from google images. After scraping the images, I labeled the images using LabelImg library to get image annotations. These annotaions (XML) were then converted to CSV file. The CSV files were then converted to tf.records file, so as to enable a seamless data processing.

## Files
- crane_handle_instance_segmentation(inference).ipynb
- crane_handle_instance_segmentation(Training).ipynb
- crane_object_detection(Training).ipynb
- crane_object_detection(inference).ipynb
- crane_scraper.py
