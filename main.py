import cv2
iron_man = cv2.imread("iron man.jpeg")
lightning = cv2.imread("lightning.jpeg")
y, x, ch = iron_man.shape
lightning_resize = cv2.resize(lightning, (x, y))
lightning_rot = cv2.rotate(lightning_resize, cv2.ROTATE_180)
add = cv2.addWeighted(iron_man, 0.50,lightning_rot, 0.50, 0)
cv2.imshow("add", add)
cv2.imwrite("iron man lightning.jpeg", add)
cv2.waitKey(0)
cv2.destroyAllWindows()