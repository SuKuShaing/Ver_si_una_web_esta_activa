from selenium import webdriver
import time
import playsound

def verificar_web(url):
    try:
        driver = webdriver.Chrome()  # O usa el controlador específico de tu navegador
        driver.get(url)
        driver.implicitly_wait(10)
        print("La página está activa.")
        playsound.playsound('success.mp3')  # Emite un sonido cuando la página está activa
        return True
    except Exception as e:
        print("Error al acceder a la página:", e)
        return False
    finally:
        driver.quit()

if __name__ == "__main__":
    url = "https://ecdm.cl/"  # Reemplaza esto con la URL de la página que deseas verificar
    activa = False
    while True:
        if activa:
            activa = verificar_web(url)  # Verificar cada 1 minuto si está activa
        else:
            activa = verificar_web(url)  # Verificar cada 10 minutos si no está activa
        time.sleep(60 if activa else 900)  # Esperar el tiempo de intervalo apropiado
