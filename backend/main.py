import time
import random
from clases import Agenda, BootMassivo

# --- CONFIGURACIÓN ---
# Ruta del archivo CSV con los contactos. Fijate de que este archivo exista.
# Debe tener las columnas: "First Name", "Last Name", "Phone 1 - Value"
CONTACTS_CSV_PATH = "contacts_example.csv" 

MENSAJE_TEXTO = "¡Hola {nombre}! Este es un mensaje de prueba enviado por nuestro bot. ¡Que tengas un excelente día!"

# Ruta de la imagen que quieres enviar (opcional, dejala en "" si no queres enviar imagen)
IMAGEN_PATH = "image_example.png"
IMAGEN_CAPTION = "Mira esta imagen de ejemplo." # Pie de foto para la imagen


def main():
    """
    Función principal que orquesta todo el proceso.
    """
    print("--- INICIANDO BOT DE WHATSAPP ---")

    # 1. Aqui gestiono la agenda de contactos
    print("\n[Paso 1: Cargando contactos]")
    agenda = Agenda()
    agenda.import_contacts(CONTACTS_CSV_PATH)
    
    if not agenda.contacts:
        print("No se cargaron contactos. Revisa el archivo CSV. Terminando el programa.")
        return

    print(f"Se han cargado {len(agenda.contacts)} contactos. Mostrando los primeros 5:")
    agenda.show(5)

    # 2. Iniciar el bot de Selenium
    print("\n[Paso 2: Iniciando el navegador]")
    bot = BootMassivo()
    bot.open_whatsapp()

    # 3. Enviar mensajes a cada contacto
    print("\n[Paso 3: Iniciando el envío masivo de mensajes]")
    total_contactos = len(agenda.contacts)
    enviados_ok = 0

    for i, (nombre, telefono) in enumerate(agenda.contacts.items()):
        print(f"\n--- Enviando a {i+1}/{total_contactos}: {nombre} ({telefono}) ---")
        
        
        numero_completo = f"591{telefono}" 

        if bot.open_chat(numero_completo, nombre):
            mensaje_personalizado = MENSAJE_TEXTO.format(nombre=nombre.split()[0]) # Usa solo el primer nombre
            bot.send_text(mensaje_personalizado)

            if IMAGEN_PATH:
                bot.send_picture(IMAGEN_PATH, IMAGEN_CAPTION)
            
            enviados_ok += 1
        
        # Pausa aleatoria entre contactos
        pausa = random.randint(10, 25)
        print(f"Pausa de {pausa} segundos antes del siguiente contacto.")
        time.sleep(pausa)

    # 4. Finishim
    print("\n--- PROCESO FINALIZADO ---")
    print(f"Resumen: Se intentó enviar a {total_contactos} contactos.")
    print(f"Envíos exitosos (chat abierto): {enviados_ok}")
    bot.quit()


if __name__ == "__main__":
    main()