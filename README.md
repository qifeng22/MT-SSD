# MT-SSD
The official code release of MT-SSD, a point-based single stage 3D detection model, is now available. Our code is based on OpenPCDet. To install it, please follow the command below.
## Installation
Requirements:
Linux (Ubuntu 18.04/20.04/21.04)

Python 3.9.0

PyTorch 1.7.1

CUDA 9.0 or higher (PyTorch 1.3+ needs CUDA 9.2+)
```
git clone https://github.com/qifeng22/MT-SSD.git && cd MT-SSD
pip install spconv-cuxxx ### replace cuxxx with your cuda version,such as cu102
python setup.py develop
```
## Prepare the datasets
For OpenPCDet, please refer to [here](https://github.com/open-mmlab/OpenPCDet/blob/master/docs/GETTING_STARTED.md) for the Dataset Preparation.

## Training
```
python train.py --cfg_file cfgs/kitti_models/MT-SSD.yaml --batch_size 8 --epoch 80 ## kitti

python train.py --cfg_file cfgs/waymo_models/MT-SSD.yaml --batch_size 12 --epoch 85 ## waymo single GPU

sh scripts/dist_train.sh 2 --cfg_file cfgs/waymo_models/MT-SSD.yaml --epoch 85   
## waymo multiple GPUs, you can change 2 to the number what you want.
```
For MT-SSD on waymo, we release the code in another repository, please refer to [MT-SSD(waymo)](https://github.com/qifeng22/MT-SSD-waymo).
## Evaluation
```
python test.py --cfg_file cfgs/kitti_models/IA-SSD.yaml  --batch_size ${BATCH_SIZE} --ckpt ${PTH_FILE}   
## PTH_FILE your_fold/MT-SSD/output/kitti_models/IA-SSD/default/ckpt/checkpoint_epoch_80.pth

python test.py --cfg_file cfgs/waymo_models/MT-SSD.yaml --batch_size ${BATCH_SIZE} --ckpt ${PTH_FILE} 
```
## Experimental results
### KITTI dataset
Quantitative results of different approaches on KITTI dataset (test set):
Here is the [ckpt](https://pan.baidu.com/s/1T34YnBAoF-uBbySxu7j27g?pwd=xwd8) .
![image](https://github.com/qifeng22/MT-SSD/assets/57132534/ae91d19a-30e4-4a80-98ae-d468664097bd)
Quantitative results of different approaches on KITTI dataset (val set):
Here is the [ckpt](https://pan.baidu.com/s/17gX0JqmvF36L7pVgmMncjQ?pwd=9l5x)
![image](https://github.com/qifeng22/MT-SSD/assets/57132534/d5533808-88c2-417a-bb6d-ca32d4d42542)
### Waymo val dataset
Here is the [ckpt](https://pan.baidu.com/s/1nMdQ7wtcR078uThnQu_Zcg?pwd=4y8f)
![image](https://github.com/qifeng22/MT-SSD/assets/57132534/361c4b84-fa9d-459a-9611-b967dfb50660)



