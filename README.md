<h1 align="center">Summer Challenge | Writer Verfication</h1>
<h4 align="center">National Conference on Computer Vision, Pattern Recognition, Image Processing, and Graphics (NCVPRIPG'23)&nbsp;&nbsp;<a href="https://vl2g.github.io/challenges/wv2023/">Link</a></h4>
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
      <li>Segment the images using CRAFT algorithm.</li>
      <li>Binarize the images.</li>
      <li>Invert the images (black text on white background).</li>
    </ul>
  <li>Feature extraction: (*Phase-2 Modifications)</li>
    <ul>
      We add a linear layer with 1352 nodes to the tail of the mobilenet arcitecture and train it as a classification problem.
      Then we throw away the tail and then use the distances between the 1000 dimensional features to classify on the val dataset using nearest neighbor search. 
    </ul>
  <li>Evaluating the model based on ROC and AUC:</li>
    Evaluate the model using the Receiver Operating Characteristic (ROC) curve and the Area Under the Curve (AUC) metric.
</ol>
<h3> Imstallation </h3>
Python Libraries used:
<ul>
  <li>PIL</li>
  <li>CV2 (OpenCV)</li>
  <li>Pytorch and torchvision</li>
  <li>Matplotlib</li>
  <li>Sklearn</li>
  Other than that,we use the tesseract ocr engine. Installing the engine for the respective OS(with language support of Hindi) and python library pytesseract is required.
 <h3> Usage </h3>

  1. Place the training dataset in the dataset folder
  2. Download the CRAFT model from the official  repository  or from the [link](https://drive.google.com/file/d/1Jk4eGD7crsqCCg9C9VjCLkMN3ze8kutZ/view) and  edit the model_path variable in the preprocess.py file/
  3. Run the script preprocess.py .This will create a new folder preprocessedTrain with binarised and cropped images inside the dataset folder.
  4. Run All the cells in the train.ipynb file.Be sure to change the path of tessdata folder based on its location in the system.Also in windows the forward slashes have to be changed to 
     backslashes.
  5. The model pth file will be saved in the local directory
     **Model file** - [Model.pth](https://drive.google.com/file/d/1w8XV_rqawwvosHgY-M9yABVaN6HmmrE6/view?usp=sharing)
     
  6.The Eval script has to be run on colab.You can run all the cells ,or only calculate distances between test images and then predict using the saved knn file.
    **knn file** - [knn.pickle](https://drive.google.com/file/d/1bKv1ivylU_lS_MUac1prU1h8OiTxElpX/view?usp=sharing).
    
  7. Before running the colab script , the  dataset.zip file ,provided in the beginning of the competition has to be placed in the MyDrive folder.The pth file,semi-test.zip , and test.csv files are to be placed inside an ncv folder.



