# :sunny: Manejador de tipos de datos
Este es un manejador de tipos de datos en Python.

> Este manejador está en pañales, realmente tengo pocas cositas

## :computer: Requerimientos

Python3 and pip3.

Crear tu entorno virtual:

```shell
python3 -m venv env
```

Activar el entorno:

- Unix/macOS

```shell
source env/bin/activate
```

- Windows

```shell
./env\Script\activate
```

### Instalar requerimientos:

```shell
pip3 install -r requirements.txt
```

## :fire: Para correr

```shell
python3 main.py
```

## :bulb: Cómo usar

i. ATOMICO \<nombre> \<representacion> \<alineacion>

Define un nuevo tipo atómico de nombre \<nombre>, cuya representación ocupa
\<representación> bytes y debe estar alineado a \<alineación> bytes.

ii. STRUCT \<nombre> \[\<tipo>]

Define un nuevo registro de nombre \<nombre>. La definición de los campos del registro viene dada por la lista en \[\<tipo>].


iii. UNION \<nombre> \[\<tipo>]

Define un nuevo registro de nombre \<nombre>. La definición de los campos del registro viene dada por la lista en \[\<tipo>].


iV. DESCRIBIR \<nombre>

Debe dar la información correspondiente al tipo con nombre \<nombre>.

v. SALIR

Para salir del simulador.

## :mag: For run the tests

```shell
cd tests
coverage3 run --source=type_manager -m unittest test_type_manager.py
```

#### Coverage of the tests

```shell
coverage3 report -m
```

| Module | Coverage |
|:----:|:--:|
| -| - |