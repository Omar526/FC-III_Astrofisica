# -*- coding: utf-8 -*-
"""
Created on 2024-04-18 18:00:29

@author: Omar Fernández
@mail: omar.fernandez.o@usach.cl

Description: To generate Newton-Rapson Animation
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def NR_animation():

    x = np.linspace(-15, 15, 50, True)

    def function(x):
        return 10*np.tanh(x) + x

    def d_function(x):
        return 10*(1-np.tanh(x)**2) + 1

    def newton_rapson(f, df, x0, delta=1e-10):
        x = [x0]
        n = 0
        while abs(f(x0)) >= delta: # delta tolerancia
            x0 = x0 - f(x0)/df(x0)
            n += 1
            x.append(x0)

            if n == 10:
                break
        return x, n

    # Configuración inicial para la animación
    fig, ax = plt.subplots()
    ax.plot(x, function(x), label=r"$f(x) = 10\tanh(x) + x$")
    ax.axhline(0, ls=":", color="k")
    ax.grid(ls="--")
    ax.legend()
    line, = ax.plot([], [], 'ro')

    # Línea de la tangente
    tangent_line, = ax.plot([], [], 'g--')

    # Línea vertical desde la intersección con el eje x
    vertical_line, = ax.plot([], [], 'b--')

    # Función de inicialización de la animación
    def init():
        line.set_data([], [])
        tangent_line.set_data([], [])
        vertical_line.set_data([], [])
        return line, tangent_line, vertical_line

    # Función de actualización de la animación
    def update(frame):
        if frame < len(x_values):
            x_val = x_values[frame]
            y_val = function(x_val)
            
            # Actualizar punto
            line.set_data(x_val, y_val)
            
            # Calcular la pendiente y el punto de la tangente
            slope = d_function(x_val)
            intercept = y_val - slope * x_val
            
            # Calcular la intersección de la tangente con el eje x
            x_intercept = -intercept / slope
            y_intercept = 0
            
            # Actualizar la línea de la tangente
            tangent_line.set_data([x_val, x_intercept], [y_val, y_intercept])
            
            # Actualizar la línea vertical desde la intersección con el eje x
            vertical_line.set_data([x_intercept, x_intercept], [-y_val, 0])
            
        return line, tangent_line, vertical_line

    # Realizar el método de Newton-Raphson
    x_values, _ = newton_rapson(function, d_function, x0=10, delta=1e-10)

    # Crear y mostrar la animación
    ani = FuncAnimation(fig, update, frames=len(x_values)+5, init_func=init, blit=True, interval=200)

    return ani


def BI_animation():
    # Definir la función
    def f(x):
        return 0.4*x**3 - 2*x - 5

    # Definir el intervalo inicial
    a = 1
    b = 7

    # Configuración inicial de la gráfica
    fig, ax = plt.subplots()
    ax.scatter(3.005, 0, marker="o", color="red")
    x_vals = np.linspace(0, 10, 100, True)
    y_vals = f(x_vals)
    ax.plot(x_vals, y_vals, label='$f(x) = 0.4x^3 - 2x - 5$')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')  # línea horizontal en y=0
    #line, = ax.plot([], [], 'r-', lw=2)
    root_point, = ax.plot([], [], 'rx')  # Marca 'x' para la raíz
    root_line = ax.axvline(x=0, color='g', linestyle='--')  # Línea vertical para la raíz
    ax.set_xlim(0,5)
    ax.set_ylim(-10,30)

    # Función de inicialización de la animación
    def init():
        #line.set_data([], [])
        root_point.set_data([], [])
        root_line.set_xdata(0)
        return root_point, root_line

    # Función de actualización de la animación
    def update(frame):
        global a, b
        c = (a + b) / 2
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        #line.set_data([a, b], [f(a), f(b)])
        
        # Mostrar la raíz
        root_x = (a + b) / 2
        root_point.set_data(root_x, f(root_x))
        root_line.set_xdata(root_x)
        
        # Resaltar el intervalo de convergencia
        ax.axvspan(a, b, alpha=0.3, color='gray')
        
        return root_point, root_line

    # Crear la animación
    ani = FuncAnimation(fig, update, frames=range(20), init_func=init, blit=True)

    # Mostrar la animación
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Método de Bisección')
    plt.legend()
    plt.grid(True)

    return ani