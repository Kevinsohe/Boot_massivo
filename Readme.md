¡Excelente idea! Un buen archivo README.md es fundamental para que cualquier persona (incluido tu futuro "yo") entienda rápidamente el proyecto, cómo instalarlo y cómo usarlo.

He creado un README completo usando el formato Markdown. Este archivo está listo para ser copiado y pegado directamente en README.md en tu repositorio de GitHub.

🤖 WhatsApp Mass Messenger Bot

Este proyecto es un bot de automatización desarrollado en Python con Selenium, diseñado para enviar mensajes masivos de texto e imágenes a través de WhatsApp Web. Incluye técnicas para simular el comportamiento humano y evitar la detección, así como un sistema de gestión de contactos a partir de archivos CSV.

<!-- Reemplaza esto con un GIF de tu bot en acción si quieres -->

✨ Características Principales

Envío Masivo: Envía mensajes personalizados a una lista de contactos cargada desde un archivo CSV.

Soporte Multimedia: Capacidad para enviar imágenes con pies de foto.

Simulación Humana:

Tipeo realista con pausas y errores simulados.

Tiempos de espera aleatorios entre acciones para evitar patrones de bot.

Uso de User-Agent de navegadores reales.

Anti-Detección: Utiliza un perfil de Chrome persistente para no tener que escanear el código QR en cada ejecución.

Gestión de Contactos:

Importa contactos desde archivos CSV (compatible con el formato de exportación de Google Contacts).

Exporta la lista de contactos actual.

Crea backups automáticos de la lista de contactos.

Robustez: Utiliza selectores estables y esperas explícitas (WebDriverWait) para manejar la carga dinámica de WhatsApp Web.

🛠️ Tecnologías Utilizadas

Python 3

Selenium: Para la automatización y control del navegador.

Pandas: Para la manipulación de datos y gestión de archivos CSV.

WebDriver Manager: Para la gestión automática del chromedriver.

🚀 Instalación y Configuración

Sigue estos pasos para poner en marcha el bot en tu máquina local.

1. Prerrequisitos

Tener Python 3.8 o superior instalado.

Tener Google Chrome instalado.

Tener una cuenta de WhatsApp activa.

2. Clonar el Repositorio

Clona este repositorio en tu máquina local usando Git:

Generated bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio


(Reemplaza tu-usuario/tu-repositorio con la URL de tu repositorio real)

3. Instalar Dependencias

Instala todas las librerías necesarias ejecutando el siguiente comando en la raíz del proyecto:

Generated bash
pip install -r requirements.txt
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END
4. Preparar Archivos de Entrada

Antes de ejecutar el bot, necesitas preparar dos archivos:

contacts_example.csv: Un archivo CSV con tus contactos. Debe contener al menos las siguientes columnas:

First Name

Last Name (puede estar vacío)

Phone 1 - Value (el número de teléfono sin código de país)

image_example.png: La imagen que deseas enviar. Si no quieres enviar una imagen, simplemente deja la ruta vacía en la configuración del script main.py.

▶️ Cómo Ejecutar el Bot

Configura el Script: Abre el archivo main.py y modifica las variables en la sección de CONFIGURACIÓN según tus necesidades:

CONTACTS_CSV_PATH: La ruta a tu archivo de contactos.

MENSAJE_TEXTO: El mensaje que deseas enviar. Puedes usar {nombre} para personalizarlo con el primer nombre del contacto.

IMAGEN_PATH: La ruta a la imagen que deseas enviar.

IMAGEN_CAPTION: El pie de foto para la imagen.

Ejecuta el Script: Abre una terminal en la carpeta del proyecto y ejecuta:

Generated bash
python main.py
IGNORE_WHEN_COPYING_START
content_copy
download
Use code with caution.
Bash
IGNORE_WHEN_COPYING_END

Primer Uso - Escaneo de QR:

La primera vez que ejecutes el bot, se abrirá una ventana de Google Chrome con WhatsApp Web.

Deberás escanear el código QR con tu teléfono para iniciar sesión.

Tu sesión se guardará en una nueva carpeta llamada AutomationProfile. En las siguientes ejecuciones, el bot iniciará sesión automáticamente sin necesidad de escanear de nuevo.

Funcionamiento:

El bot cargará los contactos, abrirá WhatsApp y comenzará a enviar los mensajes uno por uno, con pausas entre cada envío. Podrás ver todo el proceso en la terminal.

⚠️ Advertencia y Descargo de Responsabilidad

El uso de bots para enviar mensajes masivos va en contra de los Términos de Servicio de WhatsApp.

El envío de spam o mensajes no solicitados puede llevar a la suspensión permanente de tu número de WhatsApp.

Este proyecto fue creado con fines educativos para demostrar las capacidades de la automatización web con Selenium.
