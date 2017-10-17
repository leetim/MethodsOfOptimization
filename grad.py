import numpy as np
import scipy as sp

A = np.array
M = np.matrix
T = np.transpose

a = (0.5 - np.random.rand(8, 8)) + 40*np.identity(8)*(np.random.rand(8, 8))
b = 20.0*(0.5 - np.random.rand(8, 1))
print a

def f(x):
    return A((T(x).dot(M(a)).dot(x) + T(b).dot(x)))[0][0]#[0][0]
def grad_f(x):
    return (M(a) + T(M(a))).dot(x) + b
def grad2_f(x):
    return (M(a) + T(M(a)))
print "=================solve====================="
solve_x = np.linalg.solve(a + T(a), -b)
print solve_x
print f(solve_x)
print grad_f(solve_x)
print "=================det======================="
# print (a + T(a))
if not len(filter(lambda i: np.linalg.det((a + T(a))[0:i+1:, 0:i+1:]) > 0, range(8))) in [0, 8]:
    print "maximum or minimum does not exist!"
    exit()


def grad_going(f, g, x0):
    x = x0
    while True:
        grad = g(x)
        h = 1.0
        f0 = f(x)
        f1 = f0
        while h > 0.0001:
            if f1 > f(x - h*grad):
                x -= h*grad
                f1 = f(x)
            else:
                h /= 2
        # print np.abs(f0 - f1)
        if np.abs(f0 - f1) < 0.000000001:
            break
    return x


def newton(f, g, g2, x0):
    check = lambda x1, x2: np.abs(f(x1) - f(x2)) < 0.000000001
    while True:
        x = x0 - np.linalg.inv(g2(x0))*g(x0)
        if check(x, x0):
            return x
        x0 = x


grad_solve = grad_going(f, grad_f, 100*np.ones((8, 1)))
newton_solve = newton(f, grad_f, grad2_f, np.zeros((8, 1)))
print "==============grad_solve==================="
print grad_solve
print "==============newton_solv=================="
print newton_solve
print "==============diff========================="
print np.abs(grad_solve - newton_solve)
print (np.abs(solve_x - newton_solve))
print (np.abs(grad_solve - solve_x))
print f(grad_solve)
