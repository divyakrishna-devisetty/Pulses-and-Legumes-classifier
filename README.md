# Pulses and Legumes classifier
This classifier is a custom image classification model built using transfer learning based on Googles Inception v3.

# Data Collection and preprocessing
The data collection is done in two ways. One way is by taking images from the mobile camera and the other images are collected from google by following the steps mentioned in this <a href="https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/" target="_blank">site</a> and using script file dload_images.py.

All the images are resized to 256*256 dimensions without losing aspect ratio. As part of data preprocessing images are placed in subfolders named after their category under the folder train. Data augmentation is used to increase the relevant data in the dataset.

# Training and testing

The model is trained on default train settings of inception v3 model. Data is split in a way such that 90% of images are used for training and 10% for testing.

# Required Libraries

<ul>
  <li>TensorFlow</li>
  <li>Keras</li>
  <li>PIL</li>
  <li>Flask</li>
  <li>python-resize-images</li>
  <li>imutils</li>
  <li>requests</li>
  <li>cv2</li>
  <li>numpy</li>
  <li>seaborn</li>
  <li>matplotlib</li>
  <li>pandas</li>
 </ul>

# Demo

![classify](https://github.com/divyakrishna-devisetty/Pulses-and-Legumes-classifier/blob/master/classify.gif)

# Further improvements
<ol>
  <li> Improve the dataset by adding more images.</li>
  <li> Try to implement the same using Tensorflow.js.</li>
  <li> Compare the model with other classification models.</li>
</ol>
