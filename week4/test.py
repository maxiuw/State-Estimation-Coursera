from numpy import *

def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor
    frame. The values of epsilon and alpha are given in radians, while 
    r is in metres. Epsilon is the elevation angle and alpha is the
    azimuth angle (i.e., in the x,y plane).
    """
    p = zeros(3)  # Position vector 
    p[0] = (cos(epsilon) * r) * cos(alpha)  
    p[1] = (cos(epsilon) * r) * sin(alpha) 
    p[2] = sin(epsilon) * r 
    # Your here
  
    return p
  
def estimate_params(P):
    """
    Estimate parameters from sensor readings in the Cartesian frame.
    Each row in the P matrix contains a single 3D point measurement;
    the matrix P has size n x 3 (for n points). The format is:

    P = [[x1, y1, z1],
    [x2, x2, z2], ...]

    where all coordinate values are in metres. Three parameters are
    required to fit the plane, a, b, and c, according to the equation

    z = a + bx + cy

    The function should retrn the parameters as a NumPy array of size
    three, in the order [a, b, c].
    """
    param_est = zeros(3)
    inpt = zeros((P.shape[0],P.shape[1]))
    inpt[:,0] = ones((P.shape[0]))
    inpt[:,1:3] = P[:,:2]
    #  concatenate((P[:,:2],ones((P.shape[0],1))), axis = 1) 
    # param_est = (inpt**(-1)).T @  P[:,-1]  # [21.2        18.53496503  9.86551854]
    # inv(A.T @ A) @ A.T @ b inv(inpt.T@inpt) @ inpt.T @ P[:,-1]
    param_est = linalg.inv(inpt.T@inpt) @ inpt.T @ P[:,-1] # matmul(matmul(linalg.inv(matmul(inpt.T, inpt)), inpt.T), P[:,-1] )
    # Your code here

    return param_est
  
if __name__ == '__main__':
    inp = array([[1, 2, 5], [1.1, 2.1, 5.2], [1.2, 2.2, 5.4], [1.3, 2.3, 5.6]])
    param_est_result = estimate_params(inp)
    print(param_est_result)