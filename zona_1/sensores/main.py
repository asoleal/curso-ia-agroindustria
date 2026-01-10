import random

def leer_sensor():
    temperatura = random.uniform(20, 35)
    humedad = random.uniform(40, 80)
    print(f"📡 ZONA 1 reportando: Temp={temperatura:.1f}°C, Hum={humedad:.1f}%")

if __name__ == "__main__":
    leer_sensor()
