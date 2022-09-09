# Optimal-Image compression
<h3>Get optimal Image Quality of an Image</h3>

<p>To get the right amount by how much an image should be compressed, we use Linear Regresssion. </p>

<p>How can we use it ? The answer would be by mapping bits per pixel to the image quality.

<p>In this <a href="https://github.com/contentstack/optimal_image_score/blob/main/training_and_testing_scripts/LinearRegressionModel.ipynb">file</a>, we can see that there are cetain quality numbers attached to every image file. The following numbers are obtained by testing 1000s of images with different bpp values to see how long we can compress them so that the difference is negligible. </p>

<p> What is bpp ? They are the number of bits persent in a single pixel</p>
<p>To calculate bpp ( bits per pixel ), we need three things : </p>
<ul>Height of the Image</ul>
<ul>Width of an Image </ul>
<ul>Size of an image (in bits ) </ul>

<p>bpp of an image = Size of an Image ( in bits )/ ( height * width )</p>
<p>When the bpp is calculated and found to be lesser than 0.5, we could see that the compression that can be achieved is less, thereby implying the quality value should be higher. Hence, the bpp value is indirectly proportional to the quality of an image. </p>

<p>To test the following hypothesis, let us take an example and consider this image.</p>
<img width="492" src="https://user-images.githubusercontent.com/87975235/178252465-f9ecdff2-3950-47b5-bf75-f2e325569e34.png">
<p>BPP of the following image = 0.3698</p>
<p>Now, let us compress it to a value of 60 and 85 and visualize the results. </p>
<img width="1057" alt="Screenshot 2022-07-11 at 4 29 51 PM" src="https://user-images.githubusercontent.com/87975235/178250212-01966fc0-79df-4390-8170-582b438d3983.png">
<p>On the left, we have zoomed the nose area of the woman and the quality is set to 60, whereas on the right, the quality is 85. A simpler distinction can be seen on either side. Therefore, we can conclude that lower bpp is indirectly proportional to the quality value</p>

<p>Thus, fitting a linear regression model deems beneficial for this usecase, as the scatter plot for the same is as shown below</p>
<img width="675" alt="Screenshot 2022-07-11 at 4 48 00 PM" src="https://user-images.githubusercontent.com/87975235/178252973-f8931a23-75fe-4002-b9ac-b90bd230d6da.png">
<p>Since, a recommendation lower than 50 will greatly erase the metadata for the image, we don't perform recommendation below that value. Furthermore, we can also discard the bpp values above 4.15, as any value greater than that would not contribute in our recommendation.</p>
<p>After fitting the Linear Regression Curve, we obtain the following curve whose accuracy is ~98%</p>

<img width="701" alt="Screenshot 2022-07-11 at 4 51 58 PM" src="https://user-images.githubusercontent.com/87975235/178253558-de821fd7-fbcb-44e0-8581-aac80c398217.png">


PROS :
<li>Faster computation </li>
<li>Meets the need</li>
<li>Space efficient</li>
<li>Can be retrained</li>
Model is saved : <a href='https://github.com/contentstack/optimal_image_score/tree/main/models'>here</a>



