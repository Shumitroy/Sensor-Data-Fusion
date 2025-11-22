from random import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# IMPLEMENT THE FOLLOWING CLASS.
class LinKalman:
	def __init__(self, x, A, H, R, Q):
		self.x = x
		self.A = A
		self.H = H
		self.R = R
		self.Q = Q

		self.P = np.array([[1]])
		pass

	# return state prediction as tuple (x_{t|t-1}, P_{t|t-1})
	def predictState(self):
		# x_pred = A x
		self.x = self.A @ self.x
		# P_pred = A P A^T + Q
		self.P = self.A @ self.P @ self.A.T + self.Q
		return self.x, self.P

	# return measurement prediction (\hat z_{t|t-1})
	def predictMeasurement(self):
		#z_pred = H x_pred
		z_pred = self.H @ self.x 
		return z_pred
		
	# return matrix K
	def computeKalmanGain(self):
		# K = P H^T (H P H^T + R)^-1
		K = self.P @ self.H.T @ np.linalg.inv(self.H @ self.P @ self.H.T + self.R)
		return K

	# Update self.x and self.P, return tuple (x_{t|t}, P_{t_t})
	def update(self, z):
		K= self.computeKalmanGain()

		self.x = self.x + K @ (z - self.H @ self.x)
		I = np.eye(self.P.shape[0])
		self.P = (I - K @ self.H) @ self.P



		return self.x, self.P

if __name__ == "__main__":
	x = np.array([0])
	A = np.array([[1]])
	H = np.array([[1]])
	R = np.array([[1]])
	Q = np.array([[0.01]])
	z_mean = np.array([[20]])

	print("x:", x)
	print("A:", A)
	print("H:", H)
	print("R:", R)
	print("Q:", Q)

	kalman = LinKalman(x, A, H, R, Q)
	
	x_arr = [] # to collect data for plots
	P_arr = []
	z_arr = []
	step_arr = []
	
	for step in range(100):
		print("Step ", step)
		print("  Predict State: ", kalman.predictState())
		print("  Predict Measurement: ", kalman.predictMeasurement())
		print("  K: ", kalman.computeKalmanGain())
		z = np.array(np.random.normal(z_mean, R))
		x, P = kalman.update(z)
		print("  Update: ", x, P)

		step_arr.append(step)
		x_arr.append(x[0])
		P_arr.append(P[0][0])
		z_arr.append(z[0])

	fig, axs = plt.subplots(2)
	axs[0].plot(step_arr, x_arr)
	axs[0].plot(step_arr, z_arr, "rx")
	axs[1].plot(step_arr, P_arr)
	plt.show()
