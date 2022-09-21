# Evident_Auditing_System
The purpose of developing this system is to computerize the traditional way of searching a particular person from the CCTV video footage in less time. 
We will use computer vision library and AI to detect a person in a video footage using the sketch of that person. 
This system will help to cut down the efforts done by police authorities during analysing the huge video footages. 
![wwww](https://user-images.githubusercontent.com/73888467/191596541-8960927d-7cf0-43e4-818d-53853fee399b.png)


Hardware:
 
Minimum RAM:-8GB
 
Hard Disk:-500 GB
 
Processor:-Intel core i5
 
Software:
 
Language: - Python 3
 
Libraries: - OpenCV, pyQT
 
Operating System: - Windows 10
![image](https://user-images.githubusercontent.com/73888467/191596895-f38037a3-056a-4e31-8267-f25a27a72e23.png)
We will take CCTV footage and a sketch as an input from the user. The sketch will show the person whom we have to find out in the Video footage. This sketch will also show the colours of the cloths that the person is wearing.
We will use Pattern Matching for searching and finding the location of the input sketch in each frame of the video footage. Then After that we will try to find the best possible frame which matches with our input image.
![image](https://user-images.githubusercontent.com/73888467/191597100-afac43f0-977b-4220-b51b-7d25b404a80f.png)
Using pattern matching, we can find out how much the neighbourhood of each pixel of a particular frame matches with the Input image.
We will use different methods during pattern matching and analyse the results obtained using each method.
After that, we will trim down the Input video footage to provide the initial video frames in which the person the Input Image was detected. 
![image](https://user-images.githubusercontent.com/73888467/191597159-5df9ac62-aa05-44c8-b43b-1411c9eba461.png)
Implementation detail:

Step:1 Take the video footage and the drawing of the person from
            the user. 
Step:2 Reading and Resizing the video.
Step:3 while(true) {
a. Find min value and max value for each frame of the video footage.
b. If max value > thresholding value then;
	1.  Note down the timestamp of the video
	2.  Break
}
Step:4 Crop the video according to the timestamp found in the
           Previous step.
Step:5 show the output in the video player to the user using GUI![image](https://user-images.githubusercontent.com/73888467/191597225-526d932c-bed9-4b29-945c-d6bac2a68fd6.png)

Summary and Conclusions:
![image](https://user-images.githubusercontent.com/73888467/191597349-62f0e35b-abc1-41a5-840a-088f3344515b.png)
We had developed a system that can successfully detect the person with 60% - 65% accuracy.
We are hoping to make the system more faster by using parallel processing.

Limitation:
     	The system can’t have a very high accuracy as the CCTV footage is not very         	clear and we will have to just depend on the colours of the cloths and 	contour of the body of the person.
 
Major Difficulties encountered:
The outcome depends of the quality of the CCTV footage and input drawing provided. 
The system doesn’t recognize properly in poor light so may give false results.
OpenCV's template matching doesn't let you to check for rotations and scaling. You could, however, write code for it. A brute force algorithm would be to generate all possible rotations and scales before matching them. That, however, would be incredibly slow. 

![image](https://user-images.githubusercontent.com/73888467/191597404-f42168d3-59f3-4690-9587-58465105e731.png)


