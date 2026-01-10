# REFERENCE S03 - N1
import pandas as pd
# ... (Carga y limpieza previa) ...
# df = ... (asumiendo df limpio)

# RETO 1
print(df[df['Rendimiento_Ton'] > 4.0])

# RETO 2
# df.to_csv('../datos/cosecha_limpia.csv', index=False)
