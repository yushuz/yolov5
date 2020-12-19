import cv2 as cv
import glob
import numpy as np
from matplotlib import pyplot as plt
import argparse


# fps = 18    # 保存视频的FPS，可以适当调整
# step = 6    # 图片每帧移动step个像素

# # img_height应该于video_height一致
# #img_width = 720
# img_height = 560
# #img_dim = (img_width, img_height)

# # video的窗口的大小
# video_width = 960
# video_height = 560


mov_pic_start = -400
mov_pic_end = 400


# 固定图片，移动采样窗口形成视频

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--fps', type=int, default=18, help='保存视频的FPS，可以适当调整')
	parser.add_argument('--step', type=int, default=6, help='图片每帧移动step个像素')
	parser.add_argument('--img_height', type=int, default=560, help='img_height应该于video_height一致')
	parser.add_argument('--video_width', type=int, default=960, help='video_width')
	parser.add_argument('--video_height', type=int, default=560, help='video_height')
	parser.add_argument('--source', type=str, default='runs/detect/exp', help='source')
	parser.add_argument('--save_name', type=str, default='saveVideo.avi', help='specify the name of the video that would be saved')
	opt = parser.parse_args()
	print(opt)

	video_dim = (opt.video_width, opt.video_height)
	dim = (20, opt.video_height)

	pure_black_big = np.zeros((video_dim[1], video_dim[0], 3)) # 一个大的纯黑色图片。放在视频的开头 也可以改成白色或者别的颜色
	pure_black_small = np.zeros((dim[1], dim[0], 3)) # 一个窄的纯黑色图片。放在视频中两张图片之间

	fourcc = cv.VideoWriter_fourcc(*'MJPG') # Specify video codec
	videoWriter = cv.VideoWriter(opt.save_name, fourcc, opt.fps, video_dim) # 最后一个是保存视频的尺寸
	imgs=glob.glob(opt.source + '/*.jpg')

	pic = pure_black_big.copy()
	frame = pic.copy()
	n = 0
	while n<len(imgs):
	    img = cv.imread(imgs[n])
	    #img = cv.resize(img, img_dim)
	    img_width = int(img.shape[1] * opt.img_height / img.shape[0]) # resize img
	    img = cv.resize(img, (img_width, opt.img_height)) # resize img
	    pic = np.concatenate([img, pic], axis = 1) # 把img连接到现在的画卷（pic）前面
	    frame_start = pic.shape[1] - video_dim[0] # 视频窗口的leftbound在画卷上的横坐标
	    for i in range(frame_start, 0, -opt.step): #视频窗口一直滚动到画卷的另一端
	        frame = pic[:,i:i+video_dim[0],:].astype(np.uint8) #截取一个长度为 i:i+video_dim[0] 的窗口成为一个frame
	        if frame.shape != (560, 960, 3):
	            print(frame.shape)
	            break
	        videoWriter.write(frame)
	    pic = frame # 令最后的frame成为新的画卷
	    pic = np.concatenate([pure_black_small, pic], axis = 1) #在画卷上衔接一个小的黑色快
	    n += 1
	videoWriter.release()