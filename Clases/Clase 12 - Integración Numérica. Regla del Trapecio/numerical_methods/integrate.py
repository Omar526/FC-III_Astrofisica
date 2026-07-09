import numpy as np

def riemann_rule(f, a, b, n):
    pass

def trapezoid_rule(f, a, b, n):
    """ metodo para resolver integrales
    f:
     a:
      b:
       n:
         """

    dx = (b-a) / n # ancho de trapecio
    xi = np.arange(a, b + dx, dx) # puntos del dominio
    omega_i = dx * np.ones(len(xi))

    # seleccionamos el primer elemento del array
    omega_i[0] = dx/2

    # seleccionamos el último elemento del array
    omega_i[-1] = dx/2

    Ai = omega_i * f(xi)
    I = np.sum(Ai)

    return I