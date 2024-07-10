# Documentacion de problemas

## Redis

Escenario: Dentro de la shell de devbox, se intenta acceder a redis-cli
Error: Could not connect to Redis at 127.0.0.1:6379: Connection refused
Solucion exitosa: 
  1. Asegurarse de que la shell de devbox se ejecuta como pura
  2. Iniciar, usando el comando de abajo, el servicio de redis.
    `devbox services start redis`
