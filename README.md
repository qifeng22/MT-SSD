# MT-SSD
The official code release of MT-SSD, a point-based single stage 3D detection model, is now available. Our code is based on OpenPCDet. To install it, please follow the command below.
## Installation
Requirements:
Linux (tested on Ubuntu 14.04/16.04/18.04/20.04/21.04)

Python 3.9.0

PyTorch 1.7.1

CUDA 9.0 or higher (PyTorch 1.3+ needs CUDA 9.2+)
```
git clone https://github.com/open-mmlab/OpenPCDet.git
pip install spconv-cuxxx ### replace cuxxx with your cuda version,such as cu113
python setup.py develop
```
