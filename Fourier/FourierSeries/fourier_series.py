import numpy as np 
import matplotlib.pyplot as plt
import time

figure = plt.figure(figsize=(8,4.125))
#manager = plt.get_current_fig_manager()
#manager.full_screen_toggle()

time.sleep(3)

l = np.pi

x = np.linspace(-l,l, 500)
y = np.cos(np.e**x) #f(x)

a_0 = 1/l * np.trapz(y, x, dx = 1/300)

y_fourier = np.zeros(len(x)) + a_0/2

for n in range(1, 300):

    figure.clear()
    axis = figure.subplots()
    axis.plot(x, y_fourier, color='black', label='Fourier Approximation')
    axis.plot(x,y, '--', color='red', label='Periodic Function')

    axis.set_title(f'Evaluation f(x) = cos(e^x) with fourier having {n} terms.')
    axis.set_xlabel('x')
    axis.set_ylabel('f(x) - Using Fourier')
   
    axis.plot(x, y_fourier)
    axis.grid()
    plt.xlim(1.2*min(x), 1.2*max(x))
    plt.ylim(1.2*min(y), 1.2*(max(y)))
    plt.draw()
    plt.pause(0.05)

    a_n = 1/l * np.trapz(y*np.cos(np.pi*n*x/l), x, dx = 1/100)
    b_n = 1/l * np.trapz(y*np.sin(np.pi*n*x/l), x, dx = 1/100)
    fourier_term = a_n*np.cos(np.pi*n*x/l) + b_n*np.sin(np.pi*n*x/l)
    y_fourier = np.add(fourier_term, y_fourier)

plt.show()

