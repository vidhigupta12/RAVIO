# RAVIO

## Features
### (1) Video Application
This application facilitates data upload & retrieval from the database with various other features. Following are the key features of this module:
● It consists of 3 database tables.<br>
● There is a separate table for video data, likes & comments.<br>
● The user's dashboard has also been made where they can view their uploaded videos arranged by their category.<br>
● A user can also edit/ delete uploaded videos.<br>
● Users can also view videos uploaded by other users.<br>
● Users can delete their accounts.<br>
● Users can subscribe to other channels.<br>
● Users can set their profile pictures.<br>
● Users can comment on videos uploaded by other users.<br>
● Users can also like videos uploaded by other users.<br>
● Users can also use the search bar to search for videos.<br>
● The app has login/ signup functionality as well.<br>

### (2) Sentiment Analysis
When the user comments on a video, the comments are processed through the ML model & the model gives a positive or negative score depending upon the words used. If it's a negative comment, its counter is increased & it is displayed in red color. Similarly if its positive comment, its counter is increased & it is displayed in green color. The overall count of each type of sentiment is displayed on our video dashboard so that the user can know how many positive or negative comments there are on his/her video. We used naive bayes classification technique for this purpose. NLTK library of python was used inorder to import twitter tweets data. The data was cleaned by removing stopwords from the nltk library. Further naive bayes theorem was implemented to calculate probabilities of both positive & negative classes. Finally the comment was classified.

## Images
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/flow.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/homepage.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/login.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/login_home.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/search.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/profile.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/dashboard.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/upload.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/video.png?raw=true)
![alt text](https://github.com/Abhinav2207/RAVIO/blob/main/Images/comment.png?raw=true)
