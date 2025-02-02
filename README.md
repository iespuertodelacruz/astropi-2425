# astropi-matraka

Participación del [IES Puerto de la Cruz - Telesforo Bravo](https://www3.gobiernodecanarias.org/medusa/edublog/iespuertodelacruztelesforobravo/) en el desafío [Astro Pi Mission Space Lab](https://astro-pi.org/mission-space-lab).

> IES Puerto de la Cruz - Telesforo Bravo  
> C/Las Cabezas, 7. Puerto de la Cruz, CP 38400  
> 922380112

Esta iniciativa se engloba dentro del proyecto [Pensamiento Computacional y Ciencias del Espacio](docs/presentacion-pcce.pdf) de la [Consejería de Educación, Formación Profesional, Actividad Física y Deporte](https://www.gobiernodecanarias.org/educacion/web/programas-redes-educativas/redes-educativas/red-canarias-innovas/steam/convocatorias/proyecto-pensamiento-computacional-y-ciencias-del-espacio/index.html) del Gobierno de Canarias.

![Pensamiento Computacional y Ciencias del Espacio](images/cartel-pcce.jpg)

## El equipo

El equipo se llama **Matraka** y está compuesto por **Carla, Daniele y Aarón** de primer curso del CFGS de **Desarrollo de Aplicaciones Web**.

![Matraca](images/matraca.png)

## Enlaces de interés

- [Descubre dónde está ahora mismo la ISS](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/International_Space_Station/Where_is_the_International_Space_Station)
- [Conoce la Raspberry Pi de la ISS](https://www.youtube.com/watch?v=Dyn4kYYJbIY)
- [Mi primer programa en RPi de la ISS](https://www.youtube.com/watch?v=pyhjdBbbrQw)
- [Comandos básicos de la RPi](https://view.genially.com/5ea5af9f63183e0d9437b732/horizontal-infographic-timeline-astropi-mision-zero)
- [Primeros pasos con Sense HAT](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat/0)
- [Sensores AstroPi](https://astro-pi.org/about/the-sensors)
- [Simulador de Python + Sense HAT](https://trinket.io/sense-hat)

## Paquetes necesarios

Para el desarrollo del código necesitaremos ciertos paquetes/librerías que nos ofrecen funcionalidades de distinta naturaleza.

Algunos paquetes están en la librería estándar ([stdlib](https://docs.python.org/es/3.13/library/index.html)) mientras que otros hay que instalarlos aparte:

- [datetime](https://docs.python.org/es/3.13/library/datetime.html) (stdlib)
- [time](https://docs.python.org/es/3.13/library/time.html) (stdlib)
- [orbit](https://github.com/0Pyonier1/G-_in_Space_Astro_Pi/issues/1)
- [picamera](https://picamera.readthedocs.io/en/release-1.13/)
- [pillow](https://pillow.readthedocs.io/en/stable/)
- [sense-hat](https://pythonhosted.org/sense-hat/)
- [skyfield](https://rhodesmill.org/skyfield/)

⭐ El paquete `orbit` está incluido en el sistema operativo **Flight OS** de la RPi que se encuentra en la ISS.

## Sense HAT

Utilizar el **Sense HAT** es super sencillo con Python:

```python
from sense_hat import SenseHat
sense = SenseHat()
```

### Sensores de entorno

| Función                   | Descripción                                                                                                |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `sense.get_temperature()` | Devuelve la temperatura en grados Celsius ([ºC](https://www.convertworld.com/es/temperatura/celsius.html)) |
| `sense.get_humidity()`    | Devuelve la humedad relativa en porcentaje (%)                                                             |
| `sense.get_pressure()`    | Devuelve la presión atmosférica ([hPa](https://www.convertworld.com/es/presion/hectopascal.html))          |

### Sensores IMU

La **IMU** (Unidad de medida inercial) es una combinación de tres sensores (magnetómetro, giroscopio y acelerómetro).

Cada uno de los sensores devuelve un diccionario con las medidas en los 3 ejes del espacio, con claves `x` `y` `z`.

### Magnetómetro

Intensidad del campo magnético ([µT](https://www.convertworld.com/es/induccion-magnetica/microtesla.html)):

```python
sense.set_imu_config(compass_enabled=True, gyro_enabled=False, accel_enabled=False)
sense.get_compass_raw()
```

### Giroscopio

Rotación ([rad/s](https://www.convertworld.com/es/frecuencia/radianes-por-segundo.html)):

```python
sense.set_imu_config(compass_enabled=False, gyro_enabled=True, accel_enabled=False)
sense.get_gyroscope_raw()
```

### Acelerómetro

Aceleración ([G](https://www.convertworld.com/es/aceleracion/fuerza-g.html)):

```python
sense.set_imu_config(compass_enabled=False, gyro_enabled=False, accel_enabled=True)
sense.get_accelerometer_raw()
```

## Posición de la ISS

Se proporciona la siguiente función que devuelve el posicionamiento de la ISS:

```python
get_ISS_position()
```

El diccionario devuelto tiene las siguientes claves:

- `latitude` (º)
- `longitude` (º)
- `altitude` ([km](https://www.convertworld.com/es/longitud/kilometro.html))

## Puesta en marcha

Desde una máquina **Linux** lleva a cabo los siguientes comandos:

**⚠️ EJECUTA LOS COMANDOS UNO POR UNO COMPROBANDO QUE NO HAYA ERRORES**

```bash
sudo apt-get install -y git curl
curl -LsSf https://astral.sh/uv/install.sh | sh
curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to ~/.local/bin
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
echo alias j=just >> ~/.bashrc
source ~/.bashrc
```

Para **clonar el repositorio** debes haberte autenticado previamente en la máquina que estés usando con tu cuenta de GitHub:

```bash
cd $HOME
git clone git@github.com:iespuertodelacruz/astropi-matraka.git
```

Para **ejecutar el programa** principal debes hacer lo siguiente:

```bash
cd astropi-matraka/src
uv run main.py  # vale con ejecutar → j
```

## Manos a la obra

El trabajo del equipo es completar el código del fichero [`main.py`](src/main.py) para obtener un fichero `iss.csv` de salida con los siguientes datos:

- **Fecha y hora** (UTC).
- **Latitud**.
- **Longitud**.
- **Altura**.
- **Temperatura**.
- **Humedad**.
- **Presión**.
- **Campo magnético** en el eje X.
- **Campo magnético** en el eje Y.
- **Campo magnético** en el eje Z.
- **Aceleración** en el eje X.
- **Aceleración** en el eje Y.
- **Aceleración** en el eje Z.
- **Rotación** en el eje X.
- **Rotación** en el eje Y.
- **Rotación** en el eje Z.

### Observaciones

- Recuerda que el fichero `.csv` debe tener una **cabecera** con los nombres de las columnas.
- Usa **nombres en inglés con minúsculas y sin espacios** para la cabecera del fichero.
- Toma un registro de todos estos datos cada **5 segundos**.
