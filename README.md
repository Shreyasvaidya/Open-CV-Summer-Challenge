<center><b> Code for the summer challenge on writer verification </b></center>

<h3>Model Pipeline:</h3>
<ol>
  <li>Data cleaning:</li>
    <ul>
      <li>Detect the languages used in the dataset.</li>
      <li>Remove any digit text data.</li>
    </ul>
  <li>Data preprocessing:</li>
    <ul>
      <li>Segment the images using CRAFT algorithms.</li>
      <li>Binarize the images.</li>
      <li>Invert the images (black text on white background).</li>
    </ul>
  <li>Feature extraction: *(Phase-2 Modifications)</li>
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
