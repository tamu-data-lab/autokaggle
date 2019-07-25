import numpy as np
import sys
sys.path.append("../autokaggle/")
from autokaggle import *

if __name__ == '__main__':
    ntime, nnum, ncat = 4, 10, 8
    nsample = 10000
    x_num = np.random.random([nsample, nnum])
    x_time = np.random.random([nsample, ntime])
    x_cat = np.random.randint(0, 10, [nsample, ncat])

    x_all = np.concatenate([x_num, x_time, x_cat], axis=1)
    x_train = x_all[:int(nsample * 0.8), :]
    x_test = x_all[int(nsample * 0.8):, :]

    y_all = np.random.randint(0, 3, nsample)
    y_train = y_all[:int(nsample * 0.8)]
    y_test = y_all[int(nsample * 0.8):]

    clf = AutoKaggle()
    datainfo = np.array(['TIME'] * ntime + ['NUM'] * nnum + ['CAT'] * ncat)
    clf.fit(x_train, y_train, time_limit=12 * 60 * 60, data_info=datainfo)

    F1_score = clf.evaluate(x_test, y_test)
    print(F1_score)