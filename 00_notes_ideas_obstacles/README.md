# Project-LOG
# 20221208 - Project Start
I am not sure where to start this project, yet. I guess it makes sense to clearly define the objectives first. As I am a stakeholder and interested in the solution myself I will start framing the target solution through the eyes of a goalkeeper coach. 
## Defining the objective - viewpoint: stakeholder
As a goalkeeper coach I am interested in improving a goalkeepers performance. I do this by regularly and properly training. Each goalkeeper training has certain focus topics, where I try to work on 
specific attributes of a goalkeeper, e.g. safety of catch, feetwork, jumping power or reaction. 

As a coach my work on the pitch focuses mainly on leading the goalkeepers through the exercises and to make sure that the exercises have the right intensity and difficulty and correct exercise execution to prevent injuries and improve skills.

This is not an easy task. Watching intensity and execution while having to shoot balls and managing the other goalkeepers is intense and requires high attention all the time. Especially when learning new techniques where it is required to watch the execuiton of the exercise closely while shooting or throwing balls for the goalkeeper. For this reason, it is essential for any goalkeeper coach to film and create videos of the training sessions. The videos provide detailed insights, which could never be gathered during training because the execution speed of the exercises is much too high to see the needed details.

Then after each goalkeeper training session it requires a huge amount of time to cut and edit the videos and then sending them to the goalkeepers to give them tips on how to improve based on the insights provided by the videos. Therefore, it would be nice to have this process automated. 

## The detailed idea is the following: 
* A video is provided, which contains one or more exercises performed by the goalkeepers
* In one exercise, usually one goalkeeper performs the exercise and the others watch or help during exercise execution (they might also shoot or throw balls) but there might also be multiple goalkeepers executing at the same time
* For each goalkeeper in the video I want clips from the video provided where he (the goalkeeper) is actively executing an exercise, but not the clips where he is watching or part of the execution for other goalkeepers
    * When the exercise stays the same but he is doing multiple repetitions I would expect multiple clips for each repetition
    * cut out waiting or recovery times
    * clips should start and end about 2 seconds before the exercise start and end (or repetition start and end if multiple)

# 20221209 - Technical implementation and pose estimation

## Defining the objective - viewpoint: Engineer
From the engineering point of view I see two open tasks: 
1. Classify if in the current frame an exercise is performed or not
    * First idea would be to do pose estimation for a frame, label frame if action or not, train RNN with pose estimation keypoints to classify if currently an exercise is performed or pause
2. Determine the active goalkeeper performing the current exercise and assign it to him

## Pose estimation - First thoughts: 
I know hardly anything about pose estimation. I am going with the hands on approach and will try to use some pretrained model on a frame and see if I can get this running first. Then I will try to understand what is happening behind the scenes inside the model. 

My first thought on the key point extraction of the pose estimation is that the coordinates depend on the current camera height, position and angle. The coordinates have to be independent of the camera positions, etc. Not sure how to do this, yet, but I guess there is for sure some mathematical operation we can perform on the coordinates to translate them into a different coordinate system. 

## Pose estimation - Hands On: 

Found a nice article on [StackAbuse](https://stackabuse.com/pose-estimation-and-keypoint-detection-with-yolov7-in-python/) using a model called YOLO (check out the [paper](https://arxiv.org/abs/2207.02696) on arxiv and this [blog post](https://viso.ai/deep-learning/yolov7-guide/) later), meaning You Only Look Once, to do pose estimation. I will try to follow the article and document the most important lessons for me below: 
* Pose estimation is a special case of keypoint detection
* YOLO (You Only Look Once) is a methodology, as well as family of models built for object detection
* There are different versions of Yolo models, Yolov7 is the newest version
* YOLOv5 is the first large-scale implementation of YOLO in PyTorch

# 221211 - Further implementation and documentation

## Object detection vs instance segmentation
 
After trying to make this work I found a lot of talking about object detection and instance segmentation. Didn't know the difference in detail so i quickly googled what the difference is. Check out this [Article on Roboflow](https://blog.roboflow.com/instance-segmentation-roboflow/) 

In simple words: 
* Object Detection: Helps detecting an object in an image. Usually this is done by bounding boxes surrounding the object that is identified. 
* Instance Segementation: Is a more detailed and complex task and can be seen as an extension to object detection. This really identifies an object and its associated shape in an image and classifies each occurance as a seperate instance.

Example: Object detection detects people in an image by surrounding them with bounding boxes. Instance segmentation then helps to identifiy seperat

## [curl command](https://everything.curl.dev/usingcurl)

The curl command stands for Client-URL. Meaning its a client side programm that uploads or downloads data with a URL. That also pretty much explains basically what it does, although it is capabale of a lot more things using flags. 
In the StackAbuse article they used -L (which i could not find what it means, guess its just downloading form the URL after the flag) and -o. -o Flag lets you specify where to put the downloaded content and additionally rename it. 

Especially useful might also be the -O flag if you want the downloaded stuff to be in the current directoy and use the rightmost part of the url as the name. Check out also the [Link](https://everything.curl.dev/usingcurl/downloads/url-named) for more details on that. 

## [Github Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases)

In the Github Release of Yolov7 the Releases are used to store the trained models weight files. 

## .pt file extension

.pt (or sometimes also .pth) is a Pytorch specific extension to save models, weights or checkpoints of a model. This is in contrast to the Tensorflow way of saving models as .pb files. 
Check out this [stackoverflow](https://stackoverflow.com/questions/59095824/what-is-the-difference-between-pt-pth-and-pwf-extentions-in-pytorch) post on the differncen between .pt and .pth (and why you might rather use .pt) or this [reddit](https://www.reddit.com/r/MLQuestions/comments/g16snd/deep_learning_model_formats_pt_format/) post on the differnce of .pb vs .pt. 

## [Command Line Arguments for Your Python Script](https://machinelearningmastery.com/command-line-arguments-for-your-python-script/)

It is possible to run python scripts from the command line with command line arguments. Pyhton provides a library called argparse to read or define the supported arguments and then use this for variables or do sth. with it. Very nice - didn't know that was possibel. 😎 