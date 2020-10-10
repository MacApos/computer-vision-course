import cv2
import imutils

img = cv2.imread(r'assets\view.jpg')
logo = cv2.imread(r'assets\python.png')
logo = imutils.resize(logo, height=150)

cv2.imshow('img', img)
cv2.imshow('logo', logo)
cv2.waitKey(25)

rows, cols, channels = logo.shape
roi = img[:rows, :cols]
cv2.imshow('roi', roi)
cv2.waitKey(25)

gray = cv2.cvtColor(src=logo, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.waitKey(25)

mask = cv2.threshold(src=gray, thresh=220, maxval=255, type=cv2.THRESH_BINARY)[1]
cv2.imshow('mask', mask)
cv2.waitKey(25)

# Odwrotna maska
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv', mask_inv)
cv2.waitKey(25)

# Drugi plan
img_bg = cv2.bitwise_and(src1=roi, src2=roi, mask=mask)
# Pierwszy plan
logo_fg = cv2.bitwise_and(src1=logo, src2=logo, mask= mask_inv)
cv2.imshow('img_bg', img_bg)
cv2.imshow('logo_fg', img_bg)
cv2.waitKey(25)

dst = cv2.add(src1=img_bg, src2=logo_fg)
img[:rows, :cols] = dst
cv2.imshow('out', img)
cv2.waitKey(0)