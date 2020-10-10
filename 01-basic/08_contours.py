import cv2 

img = cv2.imread(r'assets\python.png')
# cv2.imshow('img', original_img)

# konwersja do skali szarości
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

# Wydobycie maski
thresh = cv2.threshold(src=gray, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

# Detekcja konturów

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(len(contours))

for i in range(0,13):
    img_cnt = cv2.drawContours(image = img.copy(), contours=[contours[i]], contourIdx=-1, color=(0, 255, 0),
                               thickness=2)
    # cv2.imshow('img_cnt', img_cnt)
    # cv2.waitKey(250)

area = cv2.contourArea(contour=contours[4], oriented=True)
print(area)

max_area = 0

for idx, contour in enumerate(contours):
    area  = cv2.contourArea(contour=contour, oriented=True)
    if area > max_area:
        max_area = area
        idx_flag_area = idx

print(f'[INFO] Inedeks konturu o największym polu: {idx_flag_area}\nPole: {max_area}')

img_cnt_max_area = cv2.drawContours(image=img.copy(), contours=[contours[idx_flag_area]], contourIdx=-1,
                                        color=(0, 255, 0), thickness=2)
cv2.imshow('img_cnt_max_area', img_cnt_max_area)

cv2.waitKey(5000)

perimeter = cv2.arcLength(conturs[idx_flag_area], close=True)
print(perimeter)