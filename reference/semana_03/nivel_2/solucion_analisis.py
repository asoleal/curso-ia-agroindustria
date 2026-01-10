# REFERENCE S03 - N2
import matplotlib.pyplot as plt
import pandas as pd
# ...
# RETO 1
plt.figure()
plt.scatter(df['Temperatura'], df['Rendimiento'], color='red')
plt.title('Temp vs Rendimiento')
plt.xlabel('Temp')
plt.ylabel('Rendimiento')
plt.savefig('relacion_temp_rendimiento.png')

# RETO 2
print("La variable clave es Humedad (corr positiva fuerte).")
