import cv2
import numpy as np

if __name__ == "__main__":
	bg = cv2.imread('bg.png')
	bgg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
	f1 = cv2.imread('frame1.png')
	f1g = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
	cover = np.max(f1g) - np.min(f1g)

	# f2 = cv2.imread('frame2.png')
	iff = f1g - bgg
	co = []
	for i in range(len(iff)):
		for j in range(len(iff[0])):
			if np.abs(iff[i][j]) > 0.2 * cover:
				co.append([i, j])
	# pre = np.argwhere(np.abs(iff) > 0)
	res = np.zeros(shape = f1.shape)
	print(res.shape)
	print(iff.shape)
	for ele in co:
		res[ele[0]][ele[1]] = f1[ele[0]][ele[1]]
	# res[pre] = f1
	cv2.imwrite('imf1.png', res)