import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication
 
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('EEG Readings')

data1 = np.random.normal(size=300)

p1 = win.addPlot()
curve1 = p1.plot(data1)
win.nextRow()
p2 = win.addPlot()
curve2 = p2.plot(data1)



p1.setLabel(axis='left', text='ADC-value',units='ADC value')
p1.setLabel(axis='bottom', text='time',units='ms')

p2.setLabel(axis='left', text='FFT', units='ADC value')
p2.setLabel(axis='bottom', text='Frequency',units='Hz')





ptr1 = 0
def update1():
    global data1, ptr1
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    data1[-1] = np.random.normal()
    curve1.setData(data1)
    ptr1 += 1
    curve1.setPos(ptr1, 0)


def update():
    update1()

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

 
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
