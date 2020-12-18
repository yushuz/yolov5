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