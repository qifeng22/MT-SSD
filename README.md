# MT-SSD
It is the official code release of MT-SSD. This is a point-based single stage 3D detection model. 
Our code based on the OpenPCDet. You can follow the below command to install it.

Requirements:
Linux (tested on Ubuntu 14.04/16.04/18.04/20.04/21.04)

Python 3.6+

PyTorch 1.1 or higher (tested on PyTorch 1.1, 1,3, 1,5~1.10)

CUDA 9.0 or higher (PyTorch 1.3+ needs CUDA 9.2+)
```
git clone https://github.com/open-mmlab/OpenPCDet.git
pip install spconv-cuxxx ### replace cuxxx with your cuda version,such as cu113
python setup.py develop
```
