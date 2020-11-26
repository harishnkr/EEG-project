from numpy.fft.helper import fftfreq
from numpy.fft import fft
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication
 
win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('EEG Readings')

data1 = np.random.normal(size=200)
data2=np.abs(np.fft.fft(data1)) **2
data=np.random.normal(size=2)

p1 = win.addPlot()
curve1 = p1.plot(data1)
win.nextRow()
p2 = win.addPlot()
curve2 = p2.plot()



p1.setLabel(axis='left', text='ADC-value',units='ADC value')
p1.setLabel(axis='bottom', text='time',units='s')

p2.setLabel(axis='left', text='FFT', units='ADC value')
p2.setLabel(axis='bottom', text='Frequency',units='Hz')





ptr1 = 0
def update():
    global data1, ptr1, data2
    data1[:-1] = data1[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
    #data2[:-1] = data2[1:]  # shift data in the array one sample left
                            # (see also: np.roll)
                            
    data1[-1] = np.random.normal()
    data2=np.random.normal(np.random.normal(15,.1),size=100)
    curve1.setData(data1)
    ptr1 += 1
    curve1.setPos(ptr1, 0)
    curve2.setData(data2)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)

 
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()