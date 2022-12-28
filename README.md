# Zach's log

Latest code (3rd experiment) is in steve_webcam_detect_recog.py. This will do the face recognition. To run, in VSC terminal window, run python steve_webcam_detect_recog.py. You can easily do that by right-clicking on the file, and choose the Run Python File in Terminal option. Learned about this from this web page: https://pypi.org/project/face-recognition/

Prior to face recog, it was simply detecting faces using the webcam (2nd experiment). You can run the steve_webcam_detect.py script, similarly by right clicking on the file in VSC and Run Python File in Terminal option. Learned from this web page: https://realpython.com/face-detection-in-python-using-a-webcam/

The first experiment was to recognize faces from pictures. This can be cound on face_detect.py. To run, run this from terminal: python face_detect.py family3.jpg. Learned from this web page: https://realpython.com/face-recognition-with-python/#installing-opencv


Installation Requirements

#1 openCV
first try this: in a command terminal: pip install opencv-python
other tutorials
https://docs.opencv.org/4.x/d5/de5/tutorial_py_setup_in_windows.html

To check if it is correctly installed:
python

\>>>import cv2
\>>>print(cv2.__version__)


#2 face_recognition
pip install face_recognition

tutorial: https://pypi.org/project/face-recognition/


--------------

# Warning: DEPRECATED

Please use the repo for my book, available here: https://github.com/shantnu/PyEng


--------------

old readme


Run the code like this:

*python face_detect.py abba.png*

If you want to understand how the code works, the details are here:

https://realpython.com/blog/python/face-recognition-with-python/


Update: Now supports OpenCV3. This change has been made by furetosan ( https://github.com/furetosan) and tested on Linux.

To run the OpenCV3 version, run facedetect_cv3.py.
