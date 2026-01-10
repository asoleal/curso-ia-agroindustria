import sys
import os

print("------------------------------------------------")
print("🛠️  DIAGNÓSTICO DE ENTORNO - SEMANA 01")
print("------------------------------------------------")

# 1. Verificar versión de Python
version = sys.version.split()[0]
print(f"✅ Python detectado: Versión {version}")

if int(sys.version_info.major) < 3:
    print("❌ ERROR: Necesitas Python 3 para este curso.")
else:
    print("   Estado: CORRECTO")

# 2. Verificar directorio de trabajo
current_dir = os.getcwd()
print(f"✅ Directorio actual: {current_dir}")
print("   Consejo: Asegúrate de estar ejecutando esto desde la carpeta correcta.")

# 3. Mensaje de bienvenida
print("\n------------------------------------------------")
print("🎉 ¡Todo listo! Tu entorno funciona correctamente.")
print("👉 Siguiente paso: Abre el archivo 'README.md' y comienza el TALLER.")
print("------------------------------------------------")
