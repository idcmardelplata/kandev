# Ventajas y desventajas de usar redis para la comunicacion entre distintos nodos

## Ventajas:
 - Abundante documentacion
 - Facil comunicacion con el resto de los nodos
 - Facil sincronizacion de la informacion
 - Sencillo de utilizar
 - Soporte de distintos mecanismos de persistencia (como postgresql)
 - Libreria en python madura y completa

## Desventajas
Es necesario que los kernels donde se ejecute tengan activados
los parametros del kernel `vm.overcommit_memory=1` y `net.core.somaxconn=512`.

El parametro `vm.overcommit_memory=1` permite que los procesos utilizen mas
memoria de la disponible fisicamente mediante el uso de una memoria swap o paginacion.

El parametro `net.core.somaxconn=512` se utiliza para establecer el numero maximo de
conexiones que se pueden encolar para un socket.

Ambos parametros necesitan permisos de superusuario para configurarse

> problemas y soluciones: [arch wiki](https://wiki.archlinux.org/title/redis) 

Para iniciar el shell de devbox se debe pasar el flag --pure ej:
`devbox shell --pure`. Esto aisla el entorno creado por devbox.
La posible causa de que redis no inicie junto a devbox suele ser
el firewall, esto se soluciona agregando el puerto de redis (6379)
a las reglas del firewall ej: `sudo ufw allow 6379` y reiniciando redis
con el comando `devbox services restart`.


### Posibles soluciones:
1) Crear un instalador que se ejecute como root y setee estos parametros
2) Crear documentacion explicandole al usuario como configurar estos parametros
3) Permitir la instalacion unicamente en sistemas que tengan esos parametros configurados
