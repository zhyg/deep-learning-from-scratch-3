if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dezero import Variable

x = Variable(np.array(2.0))
y = x ** 2
y.backward(create_graph=True) # 进行反向传播以求出导数，同时创建计算图
gx = x.grad
x.cleargrad()

z = gx ** 3 + y
z.backward() # 使用反向传播创建的计算图进行新的计算，再次进行反向传播
print(x.grad)