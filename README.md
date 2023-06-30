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
      We add a linear layer with 1352 nodes to the tail of the mobilenet arcitecture and train it as a classification problem.
      Then we throw away the tail and then use the distance between the 1000 dimensional features to classify on the val dataset 
  <li>Evaluating the model based on ROC and AUC:</li>
    Evaluate the model using the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) metric.
</ol>

## Usage Instructions

  1. Place the training dataset in the dataset folder
  2. Download the CRAFT model from the official  repository  or from the [link](www.google.com) and  edit the model_path variable in the preprocess.py file
  3. Run the script preprocess.py .This will create a new folder preprocessedTrain with binarised and cropped images inside the dataset folder.
  
  



