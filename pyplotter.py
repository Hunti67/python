import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def click_event(event):
    print('x: {0} & y: {1}'.format(event.xdata, event.ydata))


def find_index(name, arr):
    i = 0
    for items in arr:
        i += 1
        #print(items)
        if items == name:
            #print(i)
            break

    print('{0} index {1}'.format(name, i))
    return i

#data = np.zeros((70, 5000))


filename = filedialog.askopenfilename()
#filename = "/home/hunti/datalogs/2022-09-26-vibration_testing/log02/vibration_testing02src_01_ev_20_evTA_BSM_MOTOR_DATA.csv"
numlines = 0


pd_data = pd.read_csv(filename, low_memory=False)

data = pd_data.to_numpy()




numlines = len(pd_data)
print('Number of lines = {0}'.format(numlines))

headers = data[0, :]
time = data[1:, 0]
time = time.astype(np.float)

index = find_index(' m1EncoderFiltered', headers)
be_el_encoder = data[1:, index]

index = find_index(' m2EncoderFiltered', headers)
be_az_encoder = data[1:, index]
be_az_encoder = be_az_encoder.astype(np.uint32)

#print(type(time[0]))

fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', click_event)

plt.plot(time, be_az_encoder, color='green')
plt.show()







'''
with open(filename, newline='') as logfile:
    reader = csv.reader(logfile)
    print('Number of lines = {0}'.format(numlines))
    for lines in reader:
        np.append(data,lines)
        numlines += 1
        #print('line {0}'.format(numlines))
'''




