import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X=np.array(X)
	y=np.array(y).reshape(-1,1)
	Xt=np.transpose(X)
	XtX=Xt @ X
	inv=np.linalg.inv(XtX)
	theta=inv @ Xt @ y
	return [round(float(val),1) for val in theta.flatten()]