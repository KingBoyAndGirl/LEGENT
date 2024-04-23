#!/bin/bash

# source deactivate
#
## 创建名为 LEGENT 的 Conda 环境，并安装 Python 3.10.14
# conda create -n LEGENT python=3.10.14 -y
#
## 激活 LEGENT 环境
# source activate LEGENT

# 安装torch
pip install torchvision==0.17.2+cu121 torch==2.2.2+cu121 -f https://download.pytorch.org/whl/torch_stable.html

# 安装项目根目录下的 Python 包
pip install -e .

# 安装项目根目录下的 Python 包以及 llava 额外依赖
pip install -e ".[llava]"

