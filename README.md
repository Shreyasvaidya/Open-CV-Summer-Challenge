<h1 align="center">Summer Challenge | Writer Verfication</h1>
<h4 align="center">National Conference on Computer Vision, Pattern Recognition, Image Processing, and Graphics (NCVPRIPG'23) &nbsp;&nbsp;
<a href="https://vl2g.github.io/challenges/wv2023/">Link</a></h4>
<hr>

<h3>Index</h3>
<ol>
  <li>Model Pipeline</li>
  <li>Installation & Requirements</li>
  <li>Usage</li>
  <li>Authors</li>
  <li>Acknowledgment</li>     
</ol>

<hr>

<h3>Model Pipeline:</h3>
<ol>
  <li>Data preprocessing:</li>
    <ul>
      <li>Segment the images using the CRAFT algorithm.</li>
      <li>Binarize the images.</li>
      <li>Invert the images (black text on white background).</li>
    </ul>
  <li>Feature extraction & Model Training</li>
    <ul>
      We add a linear layer with 1352 nodes to the tail of the Mobilenet architecture and train it as a classification problem.
      Then we throw away the tail and then use the distances between the 1000-dimensional features to classify the validation dataset using the nearest neighbour search. 
    </ul>
  <li>Evaluating the model based on ROC and AUC:</li>
    Evaluate the model using the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) metric.
</ol>

<h3> Installation </h3>
Python Libraries used:
<ul>
  <li>PIL</li>
  <li>CV2 (OpenCV)</li>
  <li>Pytorch and torchvision</li>
  <li>Matplotlib</li>
  <li>Sklearn</li>
  <li>Other than that, we use the Tesseract OCR engine. Installing the engine for the respective OS(with language support of Hindi) and Python library Pytesseract is required.</li>
</ul>
  * You can download all the required libraries using the below phython code:
  
    !pip install -r dependencies.json

<h3> Usage </h3>
<ol>
  <li> Place the training dataset in the dataset folder. </li>
  <li> Download the CRAFT model from the official  repository  or from the <a href="https://drive.google.com/file/d/1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ/view">[CRAFT Link]</a> and  edit the model_path variable in the preprocess.py file.</li>
  <li> Run the script preprocess.py . This will create a new folder preprocessedTrain with binarised and cropped images inside the dataset folder.</li>
  <li> Run all the cells in the train.ipynb file. Be sure to change the path of testdata folder based on its location in the system. Also in windows the forward slashes have to be changed to backslashes.</li>
  <li> The model pth file will be saved in the local directory. </li>
  <li> The Eval script has to be run on colab. You can run all the cells, or only calculate distances between test images and then predict using the saved knn file.</li>
  <li>  Before running the colab script, download the dataset.zip file in your DRIVE folder.The pth file, semi-test.zip and test.csv files are to be placed inside an ncv folder.</li>
      **Model file** - [Model.pth]<a href="https://drive.google.com/file/d/1w8XV_rqawwvosHgY-M9yABVaN6HmmrE6/view?usp=sharing"> Link </a><br>
      &nbsp; **KNN file** - [knn.pickle]<a href="https://drive.google.com/file/d/1bKv1ivylU_lS_MUac1prU1h8OiTxElpX/view?usp=sharing"> Link </a>
</ol>

<h3>Authors</h3>
  1. Anushkaa Ambuj
  2. Anupama Birman  
  3. Shreyas Vaidya

<h3>Acknowledgemnets</h3>
<ol>
  <li>Hafemann et.al, Learning Features for Offline Handwritten Signature Verification using Deep Convolutional Neural Networks.</li>
  <li> [Official implementation of Character Region Awareness for Text Detection (CRAFT)](https://github.com/clovaai/CRAFT-pytorch)</li>
</ol>

