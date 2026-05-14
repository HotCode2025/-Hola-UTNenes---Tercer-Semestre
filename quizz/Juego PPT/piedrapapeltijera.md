# Piedra, Papel y Tijera — Documentación del código

## Estructura general

El juego vive en un único archivo HTML. Los estilos están separados en un archivo externo que se vincula en el `<head>`:

```html
<link rel="stylesheet" href="piedrapapeltijera.css">
```

Toda la lógica está en un bloque `<script>` al final del `<body>`. Poniéndolo al final se garantiza que el HTML ya esté cargado cuando el JS intente buscar elementos por ID.

---

## Datos del juego

Antes de cualquier función, se definen dos constantes globales que el resto del código usa:

```js
const emojis  = { 1: '✊', 2: '✋', 3: '✌️' }
const palabras = ['Piedra', 'Papel', 'Tijera', '1', '2', '3']
```

**`emojis`** es un objeto que actúa como diccionario: dado un número de jugada devuelve el emoji correspondiente. Se accede con `emojis[1]` → `'✊'`, `emojis[2]` → `'✋'`, etc.

**`palabras`** es un array (lista ordenada) con el texto del conteo. Se recorre con un índice que empieza en 0: `palabras[0]` → `'Piedra'`, `palabras[5]` → `'3'`. Su longitud es `palabras.length` = 6.

Son `const` porque sus valores no cambian en ningún momento durante la ejecución.

---

## Función `aleatorio(min, max)`

```js
function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}
```

Devuelve un número entero aleatorio entre `min` y `max`, ambos inclusive.

- `Math.random()` genera un decimal entre 0 y 1 (ej: `0.734`).
- Multiplicarlo por `(max - min + 1)` escala ese decimal al tamaño del rango. Con min=1 y max=3, el resultado queda entre 0 y 2.999...
- Sumar `min` desplaza ese resultado para que empiece en 1: queda entre 1 y 3.999...
- `Math.floor()` descarta los decimales, dejando 1, 2 o 3.

Se llama una sola vez al inicio de `jugar()` para fijar la jugada de la PC antes de la animación:

```js
const pc = aleatorio(1, 3)
```

---

## Botones de elección

```html
<div class="opciones" id="opciones">
    <button class="btn" onclick="jugar(1)" title="Piedra">✊</button>
    <button class="btn" onclick="jugar(2)" title="Papel">✋</button>
    <button class="btn" onclick="jugar(3)" title="Tijera">✌️</button>
</div>
```

El `div.opciones` (CSS) alinea los botones en fila con flexbox. Su `id="opciones"` permite que JS lo encuentre para deshabilitar todos sus botones a la vez.

Cada botón tiene `onclick="jugar(n)"` que llama a la función principal pasando 1, 2 o 3. Ese número es la clave con la que más adelante se busca el emoji en el objeto `emojis`:

```js
emojis[1]  // → '✊'
emojis[2]  // → '✋'
emojis[3]  // → '✌️'
```

Al hacer clic, JS deshabilita los tres botones para que no se pueda interrumpir la animación:

```js
opcionesEl.querySelectorAll('.btn').forEach(b => b.disabled = true)
```

- **`querySelectorAll('.btn')`** devuelve una lista con todos los elementos que tengan la clase `btn` dentro de `opcionesEl`.
- **`.forEach(b => b.disabled = true)`** recorre esa lista y deshabilita cada uno. La `=>` es una **arrow function**, una forma corta de escribir una función anónima. `b` representa cada botón en la iteración.

El estilo `.btn:disabled` en CSS (opacidad reducida, cursor bloqueado) se activa automáticamente cuando un botón está deshabilitado. Al terminar la animación, JS los rehabilita con `b.disabled = false`.

---

## Sección de conteo y animación

```html
<div class="conteo oculto" id="conteo">
    <div class="palabra" id="palabra"></div>
    <div class="punos">
        <span class="puno" id="puno-jugador">🤜</span>
        <span class="puno" id="puno-pc">🤛</span>
    </div>
    <div class="mensaje" id="mensaje"></div>
</div>
```

Este bloque contiene todo lo que ocurre después de elegir. Arranca invisible con la clase `oculto` (CSS: `display: none`). JS lo muestra quitando esa clase al inicio de `jugar()`:

```js
conteoEl.classList.remove('oculto')
```

### Texto del conteo — `div.palabra`    

```html
<div class="palabra" id="palabra"></div>
```

Empieza vacío. JS va escribiendo las palabras del array `palabras` una por una, cada 400ms, usando `setInterval`:

```js
let i = 0
const intervalo = setInterval(() => {
    i++
    if (i < palabras.length) {
        palabraEl.textContent = palabras[i]
        // dispara animación zoom...
    } else {
        clearInterval(intervalo)  // detiene el intervalo
        // inicia la revelación del resultado...
    }
}, 400)
```

**`setInterval(función, ms)`** ejecuta la función repetidamente cada `ms` milisegundos. **`clearInterval`** lo detiene cuando `i` llega al final del array.

Cada vez que cambia la palabra, JS dispara la animación de zoom (CSS: `@keyframes zoomOut`) alternando la clase `zoom`:

```js
palabraEl.classList.remove('zoom')
void palabraEl.offsetWidth   // fuerza al navegador a recalcular el layout antes de continuar
palabraEl.classList.add('zoom')
```

Las animaciones CSS solo se reinician cuando la clase se *agrega*, no cuando ya estaba presente. El `void offsetWidth` obliga al navegador a aplicar el estado sin la clase antes de volver a agregarla, garantizando que la animación arranque desde cero. Este mismo truco se repite en varios lugares del código.

Al terminar el conteo, la palabra hace fade out antes de desaparecer (CSS: `transition: opacity 0.2s`):

```js
setTimeout(() => palabraEl.classList.add('fadeout'), 400)
setTimeout(() => {
    palabraEl.textContent = ''
    palabraEl.classList.remove('zoom', 'fadeout')
    // revelar resultado...
}, 620)
```

Los dos `setTimeout` están separados: el primero (400ms) agrega `fadeout` para iniciar el fade, el segundo (620ms = 400 + 220) espera que termine y luego limpia el texto.

### Los puños — `span.puno`

```html
<span class="puno" id="puno-jugador">🤜</span>
<span class="puno" id="puno-pc">🤛</span>
```

Durante el conteo rebotan gracias a la animación CSS. Para activarla, JS agrega la clase `animando` al div padre:

```js
conteoEl.classList.remove('animando')
void conteoEl.offsetWidth      // reflow para reiniciar si ya estaba animando
conteoEl.classList.add('animando')
```

El CSS detecta el selector `.conteo.animando .puno` y aplica la animación de rebote (`@keyframes sacudir`) a ambos puños.

Al terminar el conteo, los puños cambian al emoji de la jugada elegida. También usan zoom (clase `revelar`, que reutiliza el mismo `@keyframes zoomOut`) para que el cambio no sea abrupto:

```js
punoJ.classList.remove('revelar')
void punoJ.offsetWidth
punoJ.textContent = emojis[jugador]   // ej: emojis[1] → '✊'
punoJ.classList.add('revelar')

punoPC.classList.remove('revelar')
void punoPC.offsetWidth
punoPC.textContent = emojis[pc]
punoPC.classList.add('revelar')
```

---

## Función `mostrarResultado(jugador, pc)` y el cartel

```html
<div class="mensaje" id="mensaje"></div>
```

El cartel de resultado vive dentro del mismo `div.conteo`. Empieza invisible con `opacity: 0` y `transform: scale(0.85)` definidos en CSS (no usa `display: none`, así siempre ocupa su espacio y el marco blanco no salta de tamaño).

La función recibe los dos números de jugada, determina el ganador y actualiza el cartel:

```js
function mostrarResultado(jugador, pc) {
    const msgEl = document.getElementById('mensaje')
    msgEl.classList.remove('visible', 'ganaste', 'perdiste', 'empate')

    if (pc === jugador) {
        msgEl.textContent = 'Empate'
        msgEl.classList.add('empate')
    } else if (
        (jugador === 1 && pc === 3) ||   // Piedra gana a Tijera
        (jugador === 2 && pc === 1) ||   // Papel gana a Piedra
        (jugador === 3 && pc === 2)      // Tijera gana a Papel
    ) {
        msgEl.textContent = 'Ganaste!'
        msgEl.classList.add('ganaste')
    } else {
        msgEl.textContent = 'Perdiste'
        msgEl.classList.add('perdiste')
    }

    void msgEl.offsetWidth
    msgEl.classList.add('visible')
}
```

**`msgEl.classList.remove('visible', 'ganaste', 'perdiste', 'empate')`**  
Resetea todas las clases de resultado a la vez antes de agregar la nueva. Sin esto, las clases de rondas anteriores se acumularían.

Se usa `===` (igualdad estricta) en lugar de `==` porque compara valor *y* tipo de dato, evitando comparaciones inesperadas entre números y strings.

Según el resultado, se agrega una clase que en CSS cambia el color de fondo:

| Clase | Color |
|---|---|
| `ganaste` | Verde pastel |
| `perdiste` | Rosa pastel |
| `empate` | Celeste pastel |

Finalmente, el `void offsetWidth` + `classList.add('visible')` dispara la transición CSS (`opacity` de 0 a 1, `scale` de 0.85 a 1), haciendo que el cartel aparezca suavemente en lugar de un corte abrupto.

---

## Diagrama del flujo completo

```
clic en botón (jugar(n))
        │
        ▼
genera pc = aleatorio(1,3)
deshabilita botones
resetea estado visual anterior
muestra div.conteo
        │
        ▼
activa animación de rebote en puños (clase "animando")
        │
        ▼
muestra "Piedra" con zoom
        │
  setInterval cada 400ms
        ├── "Papel"
        ├── "Tijera"
        ├── "1"
        ├── "2"
        └── "3"
        │
  clearInterval
        │
  setTimeout 400ms → fadeout de la palabra
  setTimeout 620ms →
        ├── limpia texto de palabra
        ├── puños cambian a emojis elegidos (zoom)
        ├── mostrarResultado() → cartel con fade
        └── habilita botones
```
