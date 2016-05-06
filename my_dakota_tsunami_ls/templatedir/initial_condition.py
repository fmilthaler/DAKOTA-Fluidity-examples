import math

# center of Gaussian:
x = 1e5
y = 5e5
# width and height
height = 2
width = {width} # in x-direction
length = {length} # in y-direction

def val(X):
    return height*math.exp(-(X[0]-x)**2/(2.*width**2)-(X[1]-y)**2/(2.*length)**2)
