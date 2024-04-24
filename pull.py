import os
import subprocess



# Obtiene el nombre del servicio desde el archivo .env
service_name = 'front_woocommerce.service'


def run_command(command):
    """ Ejecuta un comando en el shell y retorna su salida. """
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout + result.stderr
    except subprocess.CalledProcessError as e: 
        return e.output + e.stderr

def main():
    # Ejecuta git pull
    print("Ejecutando git pull...")
    print(run_command("git pull"))

    # Detiene el servicio
    print(f"Deteniendo el servicio {service_name}...")
    print(run_command(f"sudo systemctl stop {service_name}"))

    # Inicia el servicio
    print(f"Iniciando el servicio {service_name}...")
    print(run_command(f"sudo systemctl start {service_name}"))

    # Obtiene el estado del servicio
    print(f"Estado del servicio {service_name}:")
    print(run_command(f"sudo systemctl status {service_name}"))

if __name__ == "__main__":
    main()
