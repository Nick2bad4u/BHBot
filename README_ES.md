#BHBot

Robot de cultivo de oro/XP para Brawlhalla

Muy inspirado en [BrawlhallaEZ](https://github.com/jamunano/BrawlhallaEZ)

### ----------------------------------------------- --------------------

### ¡BOT VUELVE A SER MANTENIDO ACTIVAMENTE!
###### ¡Únete a [Discord](https://discord.gg/2HDmuqqq9p) para ayudar a mantener el bot o agregar nuevas funciones!

### ----------------------------------------------- --------------------

**ADVERTENCIA:** El software se desarrolló originalmente para uso privado.
Si bien no está diseñado para ello, puede generar resultados imprevistos, incluida la ejecución de transacciones dentro de Mallhalla utilizando monedas del juego.

**Los desarrolladores renuncian a toda responsabilidad por los daños que puedan surgir del uso de este software. Se recomienda proceder con precaución y utilizar el software a su propia discreción.**

(El bot ha sido probado por varias personas durante más de 3000 horas sin problemas hasta el 18/04/2024)

# Instalación
La última versión siempre se puede descargar [aquí](https://github.com/Nick2bad4u/BHBot/releases)

# Características

- Funciona completamente en segundo plano.
- Envía entradas directamente a Brawlhalla para no molestarte
- Inicia automáticamente el juego.
- Crea/configura automáticamente el lobby
- Selecciona/cambia automáticamente el personaje y la duración del juego.
- Detecta y restablece automáticamente el límite de XP
- Admite modos personalizados
- Admite idiomas personalizados
- Incluso admite fuentes personalizadas
- ~~Te prepara café~~ (por ahora solo se admite té)

# Uso
- El proceso está diseñado para ser intuitivo. Simplemente elija la configuración requerida haciendo clic en el botón "Configuración"
- Una vez guardada la configuración, inicie el programa haciendo clic en el botón "Inicio"

# Limitaciones
- El bot requiere que "Contraer cruces" esté configurado en Sí. Si cree que debería configurarlo automáticamente, [abra un problema](https://github.com/nick2bad4u/bhbot/issues)
- El bot requiere que el idioma del juego esté configurado en inglés. Si cree que debería configurarlo automáticamente, [abra un problema](https://github.com/nick2bad4u/bhbot/issues)

# Resumen técnico
- El código subyacente siempre está disponible para que cualquiera pueda revisarlo.
- Básicamente, el bot emplea la API SendMessage de Windows para transmitir entradas directamente a la ventana de Brawlhalla. Utiliza detección de píxeles para discernir estados y determinar la acción apropiada en un momento dado.

- La clase BrawlhallaBot se puede utilizar directamente o se puede desarrollar un contenedor personalizado para ella. Está diseñado para funcionar de forma independiente, con gui.py sirviendo simplemente como un contenedor gráfico usando PySimpleGUI.
