Inspiration
Knowing that there are many classrooms across the world that have to settle for a sub-optimal ratio between educators and students, it is expected that there are many emotional and social needs of individual students that are often overlooked.

For example, this is especially critical for non verbal children with autism, who may react positively to certain aspects of the lesson plan but extremely negatively despite not being able to communicate their internal emotions verbally.

We recognized that there should be a tool that can accurately provide educators feedback on the social and emotional state of every child in their classroom so that they can restructure their lesson plan to uniquely accommodate the social and emotional growth of the class room through a personalized approach, which will ultimately lead to a more positive learning environment.

What it does
It allows the user to upload a video, which would then be analyzed using the deep learning image analysis platform AWS Rekognition to show the fluctuations of emotions in their students as time passes. Collecting this data, it will be neatly presented to the educator in order to improve their students classroom experience by focusing on lesson plans which had positive feedback and stepping away from lesson plans which had negative feedback.

How we built it
To be able to reflect on a student's emotional behavior throughout the classroom, we wanted to create a simple user interface where teachers can upload sample clips,

We started by trimming the video clip into a set of images separated by a one section to interval using OpenCV. Then, using AWS Rekognition API and its facial detection capabilities, we were able to detect what emotions a student was feeling for each image.

After scraping sentiment data and building a dataset, we used Python's data analysis stack to develop models of when the emotional behavior of the student changed throughout the clip. Based on these graphs, a teacher can decide the effectiveness of their lesson plan.

We built this app using Flask, HTML, CSS, BootStrap4, and Python. Flask controlled our backend development flow and provided data and graphical images to our front end.

What's next for Intelliment
Currently Intelliment only supports video upload, but the AWS Rekognition API we are using actually supports continuous livestreamed video input, allowing for future educators to receive real-time feedback on the emotional and social status of their classroom and each individual student.

Built With
python
html5
css3
javascript
bootstrap
flask
amazon-web-services
rekognition
