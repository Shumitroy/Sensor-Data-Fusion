from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from linkalman import LinKalman

if __name__ == "__main__":
	# create and parametrize Kalman filter here
	x0 = np.array([90.0, 0.0])
	A = np.array([[1.0, 1.0],
			  	[0.0, 1.0]])
	H = np.array([[1.0, 0.0]])
	R = np.array([[5.0]])
	Q = np.array([[1.0, 0.0],
			   [0.0, 10.0]])
	
	kalman = LinKalman(x0, A, H, R, Q)
	kalman.P = np.eye(2) * 10.0

	true_s = 100
	true_v = 1
	
	true_s_arr = []
	s_arr = []
	v_arr = []
	step_arr = range(50)
	for i in step_arr:
		print("Step ", i)
		print("  True measurement: ", true_s)
		print("  Predict State: ", kalman.predictState())
		print("  Predict Measurement: ", kalman.predictMeasurement())
		print("  K: ", kalman.computeKalmanGain())
		x, P = kalman.update(np.array([true_s]))
		print("  Update: ", x, P)
		s_arr.append(x[0])
		v_arr.append(x[1])
		true_s_arr.append(true_s)
		true_s = true_s + true_v
	
	fig, axs = plt.subplots(2)
	axs[0].plot(step_arr, s_arr)[0].set_label("pos")
	axs[0].plot(step_arr, true_s_arr, "rx")[0].set_label("meas")
	axs[0].legend()
	axs[1].plot(step_arr, v_arr)[0].set_label("vel")
	axs[1].legend()
	plt.show()

	
