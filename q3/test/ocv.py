import cv2, numpy as np, argparse

ap = argparse.ArgumentParser()
cap=cv2.VideoCapture(0)
while cap.isOpened()
    re,img=cap.read()
    #convert the image to grayscale
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #apply canny edge detection to the image
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    #show what the image looks like after the application of previous functions
    cv2.imshow("canny'd image", edges)
    cv2.waitKey(0)
    #perform HoughLines on the image
    lines = cv2.HoughLines(edges,1,np.pi/180,20)
    #create an array for each direction, where array[0] indicates one of the lines and array[1] indicates the other, which if both > 0 will tell us the orientation
    left = [0, 0]
    right = [0, 0]
    up = [0, 0]
    down = [0, 0]
    #iterate through the lines that the houghlines function returned
    for object in lines:
        theta = object[0][1]
        rho = object[0][0]
        print("the angle is ",theta)
        
    if cv2.waitKey(1)==ord('q'):
        break
    
