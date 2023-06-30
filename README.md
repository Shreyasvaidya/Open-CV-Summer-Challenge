<h1 align="center">Summer Challenge | Writer Verfication</h1>
<h4 align="center">National Conference on Computer Vision, Pattern Recognition, Image Processing, and Graphics (NCVPRIPG'23)&nbsp;&nbsp;<a href="https://vl2g.github.io/challenges/wv2023/">Link</a></h4>
<hr>
<h3>Index</h3>
<ol>
  <li>Model Pipeline</li>
  <li>Installation & Requirements</li>
  <li>Repo Structure</li>
  <li>Usage</li>
  <li>Licence</li>
  <li>Authors</li>
  <li>Acknowledgment</li>     
</ol>
<hr>
<h3>Model Pipeline:</h3>
<ol>
  <li>Data cleaning:</li>
    <ul>
      <li>Detect the languages used in the dataset.</li>
      <li>Remove any digit text data.</li>
    </ul>
  <li>Data preprocessing:</li>
    <ul>
      <li>Segment the images using CRAFT algorithm.</li>
      <li>Binarize the images.</li>
      <li>Invert the images (black text on white background).</li>
    </ul>
  <li>Feature extraction: (*Phase-2 Modifications)</li>
    <ul>
      <li>Extract character-level features.</li>
      <li>Extract word-level features.</li>
      <li>Extract line-level features.</li>
      <li>Extract paragraph-level features.</li>
      <li>Extract stylistic features.</li>
      <li>Extract structural features.</li>
      <li>Extract statistical features.</li>
      <li>Extract Histogram of Oriented Gradients (HOG) features.</li>
      <li>Extract Scale-Invariant Feature Transform (SIFT) features.</li>
      <li>Extract Local Binary Patterns (LBP) features.</li>
    </ul>
  <li>Training a Siamese Neural Network:</li>
    The Siamese neural network will learn to compare two images and determine if they were written by the same person.
  <li>Plotting epoch vs accuracy and epoch vs loss:</li>
    Plot the epoch vs accuracy and epoch vs loss curves to track the progress of the training.
  <li>Evaluating the model based on ROC and AUC:</li>
    Evaluate the model using the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) metric.
</ol>

# Usage Instructions

<ol>
  <li> Place the training dataset in the dataset folder </li>
  <li>Download the CRAFT model from the official  repository  or from the 	[link]([URL](https://drive.google.com/file/d/1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ/view)) and  edit the model_path variable in the preprocess.py file.</li>
  <li>Run the script preprocess.py .This will create a new folder preprocessedTrain with binarised and cropped images inside the dataset folder</li>
</ol>



