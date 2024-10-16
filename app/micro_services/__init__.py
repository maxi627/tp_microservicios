import subprocess
import os

def run_compose(file_path, action="up", detach=True):
    """Ejecuta docker-compose con el archivo dado y la acción especificada (up, down, etc.)"""
    cmd = ["docker-compose", "-f", file_path, action]
    
    if action == "up" and detach:
        cmd.append("-d")
    
    try:
        # Ejecuta el comando de docker-compose
        subprocess.run(cmd, check=True)
        print(f"Ejecutado {action} en {file_path} con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar {file_path}: {e}")

def manage_services(action="up"):
    """Gestiona todos los servicios de microservicios."""
    # Lista de nombres de servicios, según los archivos docker-compose
    services = ["pago", "compra","producto","stock"]
    
    # Recorrer cada archivo docker-compose directamente en el mismo directorio
    for service in services:
        file_name = f"docker-compose.{service}.yml"
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        
        if os.path.exists(file_path):
            run_compose(file_path, action=action)
        else:
            print(f"El archivo {file_path} no existe.")

if __name__ == "__main__":
    # Ejecuta la gestión de servicios (levantar o apagar)
    manage_services(action="up")  # Para levantar los servicios
    # manage_services(action="down")  # Para apagarlos
