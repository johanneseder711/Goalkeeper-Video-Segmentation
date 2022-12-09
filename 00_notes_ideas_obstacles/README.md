# Project-LOG
## 20221208 - Project Start
I am not sure where to start this project, yet. I guess it makes sense to clearly define the objectives first. As I am a stakeholder and interested in the solution myself I will start framing the target solution through the eyes of a goalkeeper coach. 
### Defining the objective - viewpoint: stakeholder
As a goalkeeper coach I am interested in improving a goalkeepers performance. I do this by regularly and properly training. Each goalkeeper training has certain focus topics, where I try to work on 
specific attributes of a goalkeeper, e.g. safety of catch, feetwork, jumping power or reaction. 

As a coach my work on the pitch focuses mainly on leading the goalkeepers through the exercises and to make sure that the exercises have the right intensity and difficulty and correct exercise execution to prevent injuries and improve skills.

This is not an easy task. Watching intensity and execution while having to shoot balls and managing the other goalkeepers is intense and requires high attention all the time. Especially when learning new techniques where it is required to watch the execuiton of the exercise closely while shooting or throwing balls for the goalkeeper. For this reason, it is essential for any goalkeeper coach to film and create videos of the training sessions. The videos provide detailed insights, which could never be gathered during training because the execution speed of the exercises is much too high to see the needed details.

Then after each goalkeeper training session it requires a huge amount of time to cut and edit the videos and then sending them to the goalkeepers to give them tips on how to improve based on the insights provided by the videos. Therefore, it would be nice to have this process automated. 

#### The detailed idea is the following: 
* A video is provided, which contains one or more exercises performed by the goalkeepers
* In one exercise, usually one goalkeeper performs the exercise and the others watch or help during exercise execution (they might also shoot or throw balls) but there might also be multiple goalkeepers executing at the same time
* For each goalkeeper in the video I want clips from the video provided where he (the goalkeeper) is actively executing an exercise, but not the clips where he is watching or part of the execution for other goalkeepers
    * When the exercise stays the same but he is doing multiple repetitions I would expect multiple clips for each repetition
    * cut out waiting or recovery times
    * clips should start and end about 2 seconds before the exercise start and end (or repetition start and end if multiple)

## 20221209 - Technical implementation and pose estimation

### Defining the objective - viewpoint: Engineer
From the engineering point of view I see two open tasks: 
1. Classify if in the current frame an exercise is performed or not
    * First idea would be to do pose estimation for a frame, label frame if action or not, train RNN with pose estimation keypoints to classify if currently an exercise is performed or pause
2. Determine the active goalkeeper performing the current exercise and assign it to him

#### Pose estimation - First thoughts: 
I know hardly anything about pose estimation. I am going with the hands on approach and will try to use some pretrained model on a frame and see if I can get this running first. Then I will try to understand what is happening behind the scenes inside the model. 

My first thought on the key point extraction of the pose estimation is that the coordinates depend on the current camera height, position and angle. The coordinates have to be independent of the camera positions, etc. Not sure how to do this, yet, but I guess there is for sure some mathematical operation we can perform on the coordinates to translate them into a different coordinate system. 

#### Pose estimation - Hands On: 

Found a nice article on [StackAbuse](https://stackabuse.com/pose-estimation-and-keypoint-detection-with-yolov7-in-python/) using a model called YOLO (check out the [paper](https://arxiv.org/abs/2207.02696) on arxiv and this [blog post](https://viso.ai/deep-learning/yolov7-guide/) later), meaning You Only Look Once, to do pose estimation. I will try to follow the article and document the most important lessons for me below: 
* Pose estimation is a special case of keypoint detection
