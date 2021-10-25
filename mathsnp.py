import numpy as np
import cv2
pic=cv2.imread("6484438.jpg")
pic_sin=np.sin(pic)
pic_sum=np.sum(pic)
pic_prod=np.prod(pic)
pic_mean=np.mean(pic)
pic_max=np.max(pic)
print(pic_max)
print(pic_mean)
print(pic_prod)
print(pic_sum)
print(pic_sin)
