# Física Computacional III

Una de las competencias esenciales de un/a profesional de la astrofísica es la capacidad de traducir modelos físicos y ecuaciones matemáticas en algoritmos y simulaciones que permitan analizar sistemas reales. Esta habilidad es clave cuando la complejidad de los modelos impide obtener soluciones analíticas exactas, haciendo necesario el uso de aproximaciones numéricas.

A medida que los sistemas físicos que estudiamos se vuelven más realistas, las ecuaciones que los describen aumentan en complejidad. En muchos casos, estas no poseen soluciones analíticas o resultan difíciles de obtener en la práctica, lo que hace necesario recurrir a métodos de aproximación numérica.

Por ejemplo, incluso un problema aparentemente simple como el movimiento de un planeta alrededor de una estrella se vuelve intratable analíticamente al considerar más de dos cuerpos (problema de los *N-cuerpos*), requiriendo resolver ecuaciones diferenciales acopladas de forma aproximada para estudiar su evolución temporal.

De manera similar, en mecánica clásica, sistemas tan comunes como un péndulo real (con fricción) o la caída de un objeto considerando resistencia del aire conducen a ecuaciones diferenciales que no admiten soluciones simples. En electromagnetismo, situaciones como calcular el campo eléctrico generado por múltiples cargas en geometrías no triviales (por ejemplo, conductores reales) también requieren una implementación computacional para ser abordadas.

En este curso, el foco estará en desarrollar esta capacidad: formular problemas físicos, comprender su base matemática e implementar soluciones computacionales desde cero. Esto incluye no solo el uso de herramientas, sino también la comprensión de sus fundamentos, limitaciones y fuentes de error.

A lo largo del curso, construiremos e implementaremos métodos numéricos fundamentales —como la resolución de ecuaciones no lineales, interpolación, diferenciación, integración numérica y solución de ecuaciones diferenciales ordinarias— evaluando su desempeño en problemas de física y astrofísica y comparando con librerías científicas como `scipy`.

Estas herramientas constituyen la base para modelar y simular una amplia variedad de fenómenos físicos, y preparan el camino para cursos más avanzados en física computacional.

---

## Habilidades por Desarrollar

- Traducir modelos físicos y ecuaciones matemáticas en algoritmos y simulaciones computacionales.  
- Implementar métodos numéricos fundamentales en Python.  
- Analizar la precisión, estabilidad y limitaciones de distintos métodos numéricos.  
- Interpretar resultados computacionales en el contexto de problemas físicos y astrofísicos.  
- Desarrollar pensamiento algorítmico aplicado a la resolución de problemas científicos.  
- Utilizar herramientas de computación científica (como `numpy`, `matplotlib` y `scipy`).  
- Comunicar resultados mediante visualizaciones y explicaciones claras.  

---

## Relación con Física Computacional IV

Este curso sienta las bases para Física Computacional IV, donde se abordan problemas de mayor complejidad, tales como:

- Ecuaciones diferenciales ordinarias de segundo orden y sistemas vectoriales.  
- Simulación de sistemas de *N-cuerpos* bajo interacción gravitacional.
- Ecuaciones diferenciales en derivadas parciales.  
- Transformada de Fourier y análisis espectral.

El dominio de los fundamentos adquiridos en Física Computacional III será clave para abordar con éxito estos contenidos, donde los modelos serán más exigentes tanto en términos físicos como computacionales.

---

## Bibliografía Básica

- **R. Landau** – *A Survey of Computational Physics: Introductory Computational Science*. Princeton University Press. [Leer en línea](https://www.dsf.unica.it/~fiore/survey.pdf)
- **M. Zingale** – *Tutorial on Computational Astrophysics*. [Leer en línea](https://zingale.github.io/comp_astro_tutorial/intro.html)
- **Q. Kong** – *Python Programming and Numerical Methods: A Guide for Engineers and Scientists*. Elsevier. [Leer en línea](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html)