Install dependency

`pip install -qr requirements.txt`



## File Structure

```
yolov5/		...
SIXray/		images/
		labels/
```

`images/` includes all images from 20.zip of SIXray. `labels` is unzipped from `label.zip`.

## Train

`python train.py --img 640 --batch 16 --epochs 10 --data SIXray.yaml --weights yolov5s.pt --nosave`

add `--resume` if needed.



## Inference

`python detect.py --weights best.pt --img 640 --conf 0.25 --source ../SIXray/images/`

Results are in `./runs/detect/exp/`.



# 测试说明

```bash
git clone https://github.com/yushuz/yolov5.git
cd yolov5

# 若使用conda ---------------------
conda create --name SIXray
conda activate SIXray
# --------------------------------
pip install -r requirements.txt
```

将待检测图片文件放入`data/images`，运行`python detect.py`即可测试。

- 也可以指定测试图片文件路径，如下所示，运行

  `python detect.py --source /your_file_path`

- 如果想要在测试过程中即时预览测试结果，添加`--view-image`。

- 要了解其他命令行选项，运行`python detect.py --help`。



测试结果保存在`runs/detect/exp`中，如果进行多次测试，会依次序生成`exp1` `exp2`...等多个路径。



#### 生成模拟视频

运行`python makeVideo.py`。

默认用于生成视频的输入图片路径为`runs/detect/exp`，可添加`--source your_file_path`更改；默认视频保存路径为`./saveVideo.avi`，可添加`--save_name your_name`更改。其他命令行选项参见`--help`。