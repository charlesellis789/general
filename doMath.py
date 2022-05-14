import numpy.polynomial.polynomial as poly
import numpy as np

def toOrdinal(n): # Returns a string variable that was a parameter n (int) converted to an ordinal value. (1 => 1st, 2 => 2nd, etc)
	return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

def performRegression(y_points,degrees):
	x_points = list(range(0,len(y_points)))
	coef = poly.polyfit(x_points,y_points,degrees)
	residual = 0
	sumOfSquares = 0
	mean = sum(y_points) / len(y_points)
	for i in range(0,len(x_points)):
		y = 0
		for j in range(0,degrees+1):
			y = y + coef[j]*x_points[i]**j
		residual = residual + (y-y_points[i])**2
		sumOfSquares = sumOfSquares + (mean-y_points[i])**2
	if sumOfSquares != 0:
		r_squared = 1 - residual / sumOfSquares
	else:
		r_squared = -1
	return [np.flip(coef),r_squared]

def interpolate(coefs,x_value):
	degree = len(coefs)
	interpolatedValue = 0
	for x in coefs:
		interpolatedValue = interpolatedValue + x * x_value**(degree-1)
		degree -= 1
	return interpolatedValue