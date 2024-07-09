# IMPORTANTE
Este prototipo necesita de una instancia de redis en correcto
funcionamiento para poder iniciar. Si el servidor de redis
no llega a conectarse correctamente siga estos pasos:

- asegurese de que el firewall no este bloqueando la conexion
   `sudo ufw status | grep 6379` debe mostar la linea **ALLOW Anywhere**.
   En caso de que no obtenga esa salida, debera permitir el servicio
   redis en el firewall, esto se hace con el comando `sudo ufw allow 6379`
   y luego reiniciando el servicio de redis con el comando `devbox services restart`  

- En caso de que lo anterior no funcione, simplemente inicie un shell   
   de **devbox** con el flag `pure` de esta manera `devbox shell --pure`
   tenga en cuenta de que esto no garantiza que redis pueda ver otras
   instancias dado que el firewall seguramente este bloqueando las conexiones.  

## Tareas

`devbox run it`: ejecuta el ejemplo
`devbox run test`: ejecuta las pruebas en caso de existir
