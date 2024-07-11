import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Números Imaginarios")

st.markdown('''
Los números imaginarios son aquellos que pertenecen únicamente al conjunto de los *complejos*. Estos números son el resultado de un número real por una unidad imaginaria.

Esta unidad imaginaria es representada por la letra $i$, y se usa con las raíces pares negativas de la siguiente forma:
''')

st.latex("i=\\sqrt{-1}")

st.header("Los Números Complejos $\\mathbb{C}$:")


st.markdown('''
Los números complejos son aquellos que tienen una parte real y otra imaginaria. Esta forma permite representar a los elementos de este conjunto de distintas formas.

---
''')

st.subheader("La Forma Binómica:")

st.markdown('''
La forma binómica de un número complejo se representa de la siguiente forma:
$$
Z = a + bi 
$$

Donde $a$ es la parte real de Z y $b$ es la parte imaginaria de Z.

Así mismo, el conjunto de lo complejos cumple on las propiedades para suma y multiplicación con la que cumple el conjunto de los reales, $\\mathbb{R}$. Y es mediante la propiedad invertiva de la multiplicación.

Esta propiedad explica que: Para cualquier $Z = a + bi \\in \\mathbb{C}, Z \\neq 0, \\exists$ $Z^{-1}$
''')


st.markdown('''
Tal que $Z * Z^{-1} = 1$

La inversa de $Z$ se representa de la siguiente manera:

$Z^{-1} = \\frac{1}{a + bi} = \\frac{1}{a + bi} * \\frac{a - bi}{a - bi}$
''')

with st.container(border=True):
    st.markdown('''Terminando con la expresión: 
    $$
    Z^{-1} = \\frac{a}{a^2 + b^2} - \\frac{b}{a^2 + b^2}i
    $$
    ''')

st.markdown('''

De igual forma, existe otro término llamado *conjugada* representado como $\\bar{Z}$.

Si $Z = a + bi$ , entonces $\\bar{Z} = a - bi$ , donde el cambio reside en la parte Imaginaria, cambiando su signo.

Así $Z = \\bar{(\\bar{Z})}$

---
''')
st.subheader("La Forma Cartesiana")

st.markdown('''
La forma cartesiana de los números complejos utiliza el plano cartesiano de una forma diferente, el eje y pasa a ser el eje imaginario y el eje x el eje real, y la parte real y la parte imaginaria del número complejo son las coordenadas; de tal forma que, si $Z = a + bi$ , las coordenadas serán $(a,b)$.

''')

with st.container(border=True):
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        ini = float(st.number_input("Parte Real: ", value = 5.0))
        fin = float(st.number_input("Parte Imaginaria: ", value = 5.0))
        st.markdown(f'''
        El número complejo representado en esta gráfica es ${ini} + {fin}i$
        ''')
    with col2:
        x = ini
        y = fin
        fig, ax = plt.subplots()
        ax.plot([0,0],[ini*ini,fin*fin],"White")
        ax.plot([ini*ini, fin*fin],[0,0],"White")
        ax.scatter([x],[y])
        st.pyplot(fig)
st.markdown('''
---
''')

st.subheader("La Forma Polar: ")

st.markdown('''
La forma polar de los números complejos se representa de la siguiente forma:

Gracias al Teorema de Pitágoras, podemos definir la recta desde el punto de origen hasta el punto $(a,b)$ como $r$. Y con las razones trigonométricas tenemos que $a = r*\\cos{\\theta}$  y  $b = r*\\sin{\\theta}$.

Se tiene que la recta representada en azul es el *Módulo* de Z, representado como $|Z| = r$. Así mismo, existe el argumento de Z, siendo este el ángulo que tiene esta recta con respecto al eje x, representado como $Arg(Z) = \\theta$.

Sabiendo esto, la forma polar de cualquier número complejo es: $Z = r*e^{i*\\theta}$. A esta expresión se llega mediante las Razones Trigonométricas y la *Identidad de Euler* $(\\cos{\\theta} + \\sin{\\theta}*i)$.

De modo que, si $Z = a + bi = r*\\cos{\\theta} + r*\\sin{\\theta}*i = r*(\\cos{\\theta} + \\sin{\\theta}*i)$.
''')

with st.container(border=True):
    st.markdown('''
    De esta forma se llega por medio del Principio de Inducción Matemática a la expresión final:
    $$
    Z = r*e^{i*\\theta}
    $$
    ''')

with st.container(border=True):
    col1, col2 = st.columns([1, 2], gap="medium")
    with col1:
        r = float(st.number_input("Radio: ", value = 5.0))
        angle = float(st.number_input("Ángulo en grados: ", value = 5.0))
        a = r*np.cos(angle*np.pi/180)
        b = r*np.sin(angle*np.pi/180)
    with col2:
        fig, ax = plt.subplots()
        ax.plot([-10,-10],[10,10],"Black")
        ax.plot([10, 10],[-10,-10],"Black")
        ax.plot([0,a],[0,b], "Blue")
        ax.scatter([a],[b])
        st.pyplot(fig)

with st.container(border=True):
    st.markdown('''**Hecho por: Brayan Steven Valderrama Pabón - 2240660**''')
