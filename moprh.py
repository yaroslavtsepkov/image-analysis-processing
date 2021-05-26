def erosion(img, kernel):
		kern_center = (kernel.shape[0]//2,kernel.shape[1]//2)
		kernel_ones_count = kernel.sum()
		eroded_img = np.zeros((img.shape[0]+kernel.shape[0]-1, img.shape[1]+kernel.shape[1]-1))
		img_shape = img.shape

		x_append = np.zeros((img.shape[0],kernel.shape[1]-1))
		img = np.append(img, x_append, axis=1)
		y_append = np.zeros((kernel.shape[0]-1,img.shape[1]))
		img = np.append(img, y_append, axis=0)
		
		for i in range(img_shape[0]):
			for j in range(img_shape[1]):
				i_ = i+kernel.shape[0]
				j_ = j+kernel.shape[1]
				if kernel_ones_count == (kernel*img[i:i_,j:j_]).sum()/255:
					eroded_img[i+kern_center[0],j+kern_center[1]] = 255

		return(eroded_img[:img_shape[0],:img_shape[1]])

def dilation(img, kernel):
		kern_center = (kernel.shape[0]//2,kernel.shape[1]//2)
		kernel_ones_count = kernel.sum()
		dilated_img = np.zeros((img.shape[0]+kernel.shape[0]-1, img.shape[1]+kernel.shape[1]-1))
		img_shape = img.shape
		

		x_append = np.zeros((img.shape[0],kernel.shape[1]-1))
		img = np.append(img, x_append, axis=1)
		y_append = np.zeros((kernel.shape[0]-1,img.shape[1]))
		img = np.append(img, y_append, axis=0)
		
		for i in range(img_shape[0]):
			for j in range(img_shape[1]):
				i_ = i+kernel.shape[0]
				j_ = j+kernel.shape[1]
				if (kernel*img[i:i_,j:j_]).sum() != 0:
					dilated_img[i+kern_center[0],j+kern_center[1]] = 255

		return(dilated_img[:img_shape[0],:img_shape[1]])

def opening(img, kernel):
		opened_img = erosion(img, kernel)
		opened_img = dilation(opened_img, kernel)

		return opened_img

def closing(img, kernel):
		closed_img = dilation(img, kernel)
		closed_img = erosion(closed_img, kernel)

		return closed_img
