# Bowling-kata

## Objetivos

Este kata es uno de los primeros kata que hice para aprender programación orientada a objetos. Consistió en diseñar un programa en Python que calculara la puntuación final de una partida de bowling dada su tarjeta de puntuación.

- ❌No consistía en escribir un programa que calculara la puntuación precisa durante las tiradas del juego.
- ❌No checkea si las tiradas son válidas.
- ❌No valida el número correcto de tiradas y frames.
- ✔️Solo consistía en escribir un programa que fuera capaz de calcular correctamente la **puntuación final** de la partida al acabar.

## Experiencia
Tuve mis dificultades con este kata ya que no conseguía implementar correctamente el último frame. El problema era que no conseguía gestionar los contadores de manera adecuada para controlar cuándo empezaba el último frame. Empecé de nuevo el código a partir de un modelo DDD e intentando llevar un mejor control de los contadores (tarea en la que VictorPorlan me ayudó mucho) y finalmente conseguí que el programa pasara los casos test.

## Reglas del negocio

- Cada partida consta de 10 **frames**.
- Un frame (exceptuando el último frame, del que ya hablaré) consiste en dos intentos o tiradas para tirar todos los **pins**(bolos). Esto es, para cada frame normal (del primero al noveno) tienes dos tiradas, a menos que tires todos los pins (strike) en la primera, en ese caso la segunda tirada no se lleva a cabo. 
- En caso de no tirar todos los pins en un frame, la puntuación de ese frame (que se sumará a la puntuación total) será el número de pins tirados.
- En el caso de tirar todos los pins en la primera tirada del frame, eso se llama **strike**, y la puntuación de ese frame que será sumada a la puntuación total será de 10 (número de pins tirados) + el número de pins tirados en las **dos siguientes tiradas**.
- En el caso de tirar todos los pins haciendo uso de las dos tiradas del frame, la puntuación que se sumará será de 10 (número de pins tirados en el frame) + el número de pins tirados en la **siguiente tirada**.
- El último frame o **tenth** tiene una lógica distinta. 
  - Si se ejecuta un spare el jugador tendrá una tirada extra, y la puntuación del frame será de 10 + los pins tirados en la siguiente tirada. 
  - Si se ejecuta un strike el jugador tendrá dos tiradas extra y la puntuación del frame será de 10 + los pins tirados en las dos siguientes tiradas.
  - Este bonus solo puede ocurrir una vez (esto es, da igual que en la tirada extra vuelvas a hacer strike, no tendrás más tiradas extra, simplemente se sumará la puntuación de los 10 bolos tirados al frame.
- La puntuación total de la partida es la suma de las puntuaciones de los frames.
