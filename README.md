# Neural Networks and Deep Learning 2024/25

This repository contains two projects developed as part of a university course on Artificial Neural Networks and Deep Learning. Both projects achieved outstanding performance, with scores of 11 out of 10 points. The challenges, datasets, methods, and results are detailed below.

---

## Project 1: Image Classification of Blood Cells

The first task involved classifying 96x96 RGB images of blood cells into eight different classes using convolutional neural networks (CNNs). 

### Approach:
1. **Dataset Preparation**:
   - Removed 1800 outliers and 8 duplicates, reducing the dataset from 13,759 to 11,951 images.
   - Balanced class distributions using oversampling techniques.
   - Splitted dataset into 80% training and 20% validation sets.

2. **Methodology**:
   - Implemented multiple models including custom CNN, MobileNetV3Small, EfficientNetB7, and ConvNeXtBase.
   - Final solution was an ensemble of five ConvNeXtBase models with data augmentation and bagging, achieving 88% accuracy on unseen data.

3. **Key Innovations**:
   - Designed an augmentation pipeline using techniques like CutMix, MixUp, and RandAugment to increase dataset variability.
   - Fine-tuned pre-trained models and tested optimizers (AdamW provided the best results).

### Results:
The ensemble model achieved 88% test accuracy, improving significantly over initial attempts.

---

## Project 2: Semantic Segmentation of Mars Images

The second task was to predict pixel-wise class labels for 64x128 grayscale images of the Martian surface across five classes, including the background.

### Approach:
1. **Dataset Preparation**:
   - Identified and removed 110 outliers using DBSCAN on T-SNE-preprocessed data.
   - Handled class imbalance by applying class weighting in loss functions.
   - Augmented the dataset using transformations such as horizontal flipping and coarse dropout.

2. **Methodology**:
   - Built an ensemble of five Unet-based models. Variations included spatial attention layers, squeeze-excite blocks, and transformer layers in bottlenecks.
   - Experimented with multiple loss functions, including Focal Categorical Cross-Entropy and Dice Loss.

3. **Key Innovations**:
   - Introduced a dual Unet architecture to capture both coarse and fine-grained details.
   - Excluded the background class from loss calculations for better segmentation performance.

### Results:
The ensemble model achieved a mean intersection over union (mIoU) of 66.3%, demonstrating robust segmentation capabilities.

---

## Tools and Libraries
- **Frameworks**: TensorFlow and Keras
- **Visualization**: Matplotlib, Seaborn
- **Data Augmentation**: Albumentations
- **Others**: Scikit-learn for metrics and utility functions

---

## Acknowledgments

These projects were developed by the *Autobot* team:
- Gabriele Carminati
- Gabriele Carrino
- Matteo Briscini

Course: [Artificial Neural Networks and Deep Learning](http://chrome.ws.dei.polimi.it/index.php?title=Artificial_Neural_Networks_and_Deep_Learning), Politecnico di Milano, AY2024/25.
