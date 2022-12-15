import cv2
img = cv2.imread("solar-system.jpg")

img[0:340,600:600] 
text = "Sun"
text1 = "Mercury"
text2 = "Venus"
text3 = "Earth"
text4 = "Mars"
text5 = "Jupiter"
text6 = "Saturn"
text7 = "Uranus"
text8 = "Neptune"
cv2.putText(img,text,(0,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1.5, color=(255,0,0))
cv2.putText(img,text1,(110,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text2,(200,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text3,(290,290),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text4,(380,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text5,(580,400),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text6,(750,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text7,(970,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.putText(img,text8,(1110,350),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(255,0,0))
cv2.imshow("solar-system",img)

cv2.waitKey(0)