import cv2  
import numpy as np
import pytesseract
import csv

def img_csv(img_path):
    
    th1 = 100
    th2 = 2000
    list1 = []  #lists required contours
    grid1 = []  #2-d array represents table data
    row = []    #lists texts converted from cropped images

    print(img_path)

    #reading an image from input
    img = cv2.imread(img_path)
    im = img.copy()

    #convertion on image to find contours
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,120,255,cv2.THRESH_BINARY)  
    image1, contours1, hierarchy1 = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    #Finding required contours
    for i in range(len(contours1)):
        perimeter=cv2.arcLength(contours1[i],True)
        if perimeter > th1 and perimeter < th2:
            # cv2.polylines(im,[contours1[i]],True,(0,255,0))
            list1.append(i)

    inv_list1 = list1[::-1] #inverse the list to start from top left

    for i in range(len(list1)):
        #To differentiate subsequent rows
        this = inv_list1[i]
        if i < len(inv_list1)-1:
            next = inv_list1[i+1]
        else:
            next = img.shape[0]
    
        #Get cropped image from original image
        cropped = img[contours1[inv_list1[i]][0][0][1]:max(contours1[inv_list1[i]][-2][0][1],contours1[inv_list1[i]][2][0][1]),contours1[inv_list1[i]][0][0][0]:contours1[inv_list1[i]][-2][0][0]]
    
        #Resize an cropped image before applying to tesseract
        res = cv2.resize(cropped,None,fx=2, fy=2, interpolation= cv2.INTER_LINEAR)
    
        #pytesseract is a python binding of tesseract
        text = pytesseract.image_to_string(res, lang = 'eng')
        # text.replace('"', "'")
        row.append(text)
        if(contours1[this][0][0][1] != contours1[next][0][0][1]):  #Compare y-cordinates of subsequent contours
            grid1.append(row) #Append row-wise to grid
            row = []  #Clear the list when switch to next row    

    #Write table data into csv file
    with open("data.csv", "w+", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(grid1)    
