import cv2
import numpy as np

img = cv2.imread(r'assets\checkbox.png')
# cv2.imshow('img', img)

img = cv2.copyMakeBorder(
    src=img,
    top=20,
    bottom=20,
    left=20,
    right=20,
    borderType=cv2.BORDER_CONSTANT,
    value=(255, 255, 255))

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)
# print(gray.shape)

blured = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=0)
# cv2.imshow('blured', blured)

thresh = cv2.threshold(src=blured, thresh=75, maxval=200, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST,
                            method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wszystkich konturów: {len(contours)}')

img = cv2.drawContours(image=img, contours=[contours[2]], contourIdx=-1,
                       color=(0, 255, 0), thickness=2)
# cv2.imshow('contours', img)

for idx in [1, 2]:
    mask = np.ones(shape=gray.shape, dtype='uint8')
    cv2.drawContours(mask, [contours[idx]], contourIdx=-1, color=255, thickness=-1)
    # cv2.imshow(f'mask{idx}', mask)

    mask_inv = cv2.bitwise_not(mask)
    # cv2.imshow(f'mask_inv{idx}', mask_inv)

    added_img = cv2.add(gray, mask_inv)
    # cv2.imshow(f'added_img{idx}', added_img)

    added_img_inv = cv2.bitwise_not(added_img)
    # cv2.imshow(f'added_img_inv{idx}', added_img_inv)

    cnt = cv2.countNonZero(added_img_inv)
    if cnt > 0:
        checked_idx = idx

print(checked_idx)

img = cv2.drawContours(image=img, contours=[contours[checked_idx]], contourIdx=-1,
                       color=(0, 255, 0), thickness=2)
cv2.imshow('checked_contour', img)

cv2.waitKey(0)
