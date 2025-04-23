## Brain Tumor Segmentation using Fine-Tuned nnU-Netv2

This project aims to improve brain tumor segmentation using a fine-tuned version of the nnU-Netv2 architecture. By leveraging deep learning and medical imaging (MRI), we enhance the accuracy and reliability of tumor detection and segmentation. The system is trained and evaluated on the BraTS 2020 and BraTS 2021 datasets, using both standard and ResEnc nnU-Net configurations.  

We also introduce ensemble methods—Max Probability and Probability Averaging—to combine outputs from different models, achieving smoother and more precise segmentation results.  

A simple, user-friendly interface has been developed to make the model accessible to healthcare professionals, enabling quick MRI analysis and tumor visualization.

## Results 
Based on evaluation on the **BraTS 2021 dataset**, the segmentation model exhibits strong foreground segmentation performance, achieving a mean Dice score of **84.45%**, indicating substantial overlap between predicted and ground truth tumor regions.   
The mean Intersection over Union (IoU) further supports this, reaching **76.78%** and confirming high volumetric segmentation accuracy.  
In terms of tumor identification within the BraTS 2021 dataset, the model demonstrates a high Sensitivity of approximately **88.6%**,signifying its ability to correctly detect a large proportion of the actual tumor regions within the foreground