# Proyecto Campus

Proyecto Campus es una aplicación para el seguimiento académico de estudiantes (campers). Facilita la inscripción de estudiantes, la gestión de cursos y el seguimiento del rendimiento en diversas disciplinas de programación y sistemas de gestión de bases de datos.

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Uso](#uso)
3. [Seguimiento Académico](#seguimiento-académico)
4. [Rutas de Entrenamiento](#rutas-de-entrenamiento)
5. [Tipos de Usuarios](#tipos-de-usuarios)
6. [Módulo de Reportes](#módulo-de-reportes)
7. [Estructura de Archivos JSON](#estructura-de-archivos-json)
8. [Contribución](#contribución)
9. [Licencia](#licencia)
10. [Contacto](#contacto)

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/ErikSneyPlata/Proyecto_campus.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd Proyecto_campus
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python main.py
    ```
2. Sigue las instrucciones en pantalla para navegar por las funcionalidades de la aplicación.

## Seguimiento Académico

### Inscripción Estudiantes
- Nombres
- Apellidos
- Dirección
- Acudiente
- Teléfonos de contacto (# de celular y # fijo)
- Estado (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado)
- Riesgo

### Cursos
- Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)
- Programación Web (HTML, CSS y Bootstrap)
- Programación formal (Java, JavaScript, C#)
- Bases de datos (MySQL, MongoDB y PostgreSQL)
- Backend (NetCore, Spring Boot, NodeJS y Express)

## Rutas de Entrenamiento
- Ruta NodeJS
- Ruta Java
- Ruta NetCore

Los estudiantes inscritos y aprobados deben ser asignados a una ruta sin superar los 33 estudiantes por salón.

## Tipos de Usuarios

### Camper
### Trainer
### Coordinador
- Registrar la nota de los campers (nota teórica y nota práctica > 60)
- Cambiar su estado

La prueba teórica tiene un peso del 30% y la prueba práctica del 60%. Los quizes y trabajos tienen un peso del 10%.

### CampusLands
- 3 salones (4 horas)
- Capacidad para 33 estudiantes por salón

## Módulo de Reportes

El módulo de reportes debe tener las siguientes funcionalidades:
- Listar los campers que se encuentren en estado de inscrito.
- Listar los campers que aprobaron el examen inicial.
- Listar los entrenadores que se encuentran trabajando con CampusLands.
- Listar los campers que cuentan con bajo rendimiento.
- Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento.
- Mostrar cuántos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.

## Estructura de Archivos JSON

```json
{
    "estudiantes": [
        {
            "id": 1,
            "nombre": "Juan Perez",
            "cursos": ["Python", "JavaScript"],
            "rendimiento": {
                "Python": "A",
                "JavaScript": "B"
            }
        }
    ],
    "cursos": [
        {
            "id": 101,
            "nombre": "Python",
            "descripcion": "Curso de programación en Python"
        }
    ],
    "usuarios": [
        {
            "id": 1001,
            "nombre": "Ana Lopez",
            "rol": "Entrenador"
        }
    ]
}```
