from fileinput import filename
import cv2
import numpy as np
import os
test_original = cv2.imread("E:/FINGERPRINT/SOCOFing/Altered/Altered-Hard/155__M_Right_thumb_finger_Zcut.BMP")
filename=None
image=None
kp1,kp2,mp=None,None,None
best_score=0

for file in [file for file in os.listdir("E:\FINGERPRINT\SOCOFing\Real")]:
   
    fingerprint_database_image = cv2.imread("E:/FINGERPRINT/SOCOFing/Real/"+file)
   
    sift = cv2.SIFT_create()
   
    keypoints_1, descriptors_1 = sift.detectAndCompute(test_original, None)
    keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_database_image, None)
    matches = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
             dict()).knnMatch(descriptors_1, descriptors_2, k=2)
    match_points = []
   
    for p, q in matches:
      if p.distance < 0.1*q.distance:
         match_points.append(p)
    keypoints = 0
    if len(keypoints_1) <= len(keypoints_2):
      keypoints = len(keypoints_1)            
    else:
      keypoints = len(keypoints_2)
    if (len(match_points) / keypoints*100)>best_score:
      best_score=len(match_points) / keypoints*100
      filename=file
      image=fingerprint_database_image
      kp1,kp2,mp=keypoints_1,keypoints_2,match_points
      
print("% match: ", best_score)
print("Figerprint ID: " +filename)
result = cv2.drawMatches(test_original, kp1, image,
                          kp2, mp, None)
result = cv2.resize(result, None, fx=2.5, fy=2.5)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
      