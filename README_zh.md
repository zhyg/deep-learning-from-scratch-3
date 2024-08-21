<p>
<a href="https://www.amazon.co.jp/dp/4873119065/ref=cm_sw_r_tw_dp_U_x_KiA1Eb39SW14Q"><img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/deep-learning-from-scratch-3.png" height="250"></a>
</p>

## 本书概要

本书将创建一个名为"DeZero"的深度学习框架。DeZero是本书原创的框架。它用最少的代码实现了框架的现代功能。在本书中,我们将通过60个步骤完成这个小巧但功能强大的框架。通过这个过程,我们将培养对现代框架(如PyTorch、TensorFlow、Chainer等)的深入理解。


<p>
<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/dezero_logo.png" width="400px" </p>


<p>
  <a href="https://pypi.python.org/pypi/dezero"><img
		alt="pypi"
		src="https://img.shields.io/pypi/v/dezero.svg"></a>
  <a href="https://github.com/oreilly-japan/deep-learning-from-scratch-3/blob/master/LICENSE.md"><img
		alt="MIT License"
		src="http://img.shields.io/badge/license-MIT-blue.svg"></a>
  <a href="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3"><img
		alt="Build Status"
		src="https://travis-ci.org/oreilly-japan/deep-learning-from-scratch-3.svg?branch=master"></a>
</p>

## 新闻
<a href="https://koki0702.github.io/dezero-book/"><img src="https://raw.githubusercontent.com/koki0702/koki0702.github.io/master/dezero-book/images/summary_ja.png" height="150px"></a>

【试读】本书的部分内容已在线公开。
https://koki0702.github.io/dezero-book/


## 文件结构

|文件夹名 |说明         |
|:--        |:--                  |
|[dezero](/dezero)       |DeZero的源代码|
|[examples](/examples)     |使用DeZero的实现示例|
|[steps](/steps)|各步骤文件(step01.py ~ step60.py)|
|[tests](/tests)|DeZero的单元测试|


## 所需的外部库

本书使用的Python版本和外部库如下:

- [Python 3](https://docs.python.org/3/)
- [NumPy](https://numpy.org/)
- [Matplotlib](https://matplotlib.org/)

此外,我们还提供了可在NVIDIA GPU上运行的可选功能。在这种情况下,需要以下库:

- [CuPy](https://cupy.chainer.org/) （可选）


## 运行方法

本书中介绍的Python文件主要位于[steps](/steps)文件夹中。
要执行它们,请按以下方式运行Python命令(可以从任何目录执行):

```
$ python steps/step01.py
$ python steps/step02.py

$ cd steps
$ python step31.py
```

## 演示

DeZero的其他实现示例位于[examples](/examples)中。

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_tanh.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/tree/tanh)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_spiral.png" height="175"/>](/examples/spiral.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/example_gpu.png" height="175"/>](https://colab.research.google.com/github/oreilly-japan/deep-learning-from-scratch-3/blob/master/examples/mnist_colab_gpu.ipynb)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/gan.gif" height="175"/>](/examples/gan.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/vae.png" height="175"/>](/examples/vae.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/grad_cam.png" height="175"/>](/examples/grad_cam.py)

[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/style_transfer.png" height="175"/>](/examples/style_transfer.py)[<img src="https://raw.githubusercontent.com/oreilly-japan/deep-learning-from-scratch-3/images/pythonista.png" height="175"/>](https://github.com/oreilly-japan/deep-learning-from-scratch-3/wiki/DeZero%E3%82%92iPhone%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%99)

## 勘误表

本书的勘误信息发布在[:mag_right: 勘误表页面](../../wiki/Errata)上。

如果您发现勘误表页面上未列出的印刷错误或其他错误,请通知我们[:email: japan@oreilly.co.jp](<mailto:japan@oreilly.co.jp>)。
