# IIC2133 - Estructuras de Datos y Algoritmos

## 2023-1

Bienvenido al sitio web del curso de Estructuras de Datos y Algoritmos. En esta página podrás encontrar la información administrativa del curso. En el repositorio podrás encontrar código ya preparado por tus ayudantes, junto con los eventuales enunciados de las tareas y las diapositivas de clases.

## Tabla de contenidos

- [IIC2133 - Estructuras de Datos y Algoritmos](#iic2133---estructuras-de-datos-y-algoritmos)
  - [2023-1](#2023-1)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Material Complementario](#material-complementario)
    - [Talleres fundamentos de C](#talleres-fundamentos-de-c)
    - [Capsulas de EDD y Algoritmos en C](#capsulas-de-edd-y-algoritmos-en-c)
    - [Material catedra extra](#material-catedra-extra)
  - [Material Tareas](#material-tareas)
  - [Clases](#clases)
  - [Ayudantías](#ayudantías)
  - [Equipo](#equipo)
    - [Profesores](#profesores)
    - [Ayudantes](#ayudantes)
  - [Evaluación](#evaluación)
    - [Evaluaciones Escritas](#evaluaciones-escritas)
    - [Tareas](#tareas)
  - [Política de Atrasos](#política-de-atrasos)
  - [Política de integridad académica](#política-de-integridad-académica)

## Material Complementario
### Talleres fundamentos de C

- [Intro a C por Vicente Errázuriz y Raúl Álvarez](https://github.com/DCCentral-de-Apuntes/intro-C)
- [Capsula de Debugging en GDB](https://youtu.be/RNfVQQEUoMQ)

### Capsulas de EDD y Algoritmos en C
- [Capsula DFS](https://youtu.be/tJV3CV0edl0)
- [Capsula BST en C](https://youtu.be/j9W1qKCvFRE)
- [Capsula Tablas de Hash en C](https://youtu.be/P1DOE8W_RD4)
- [Capsula MinHeap en C](https://youtu.be/LYe67zvL9vY)

### Material catedra extra
- [Lista de reproducción 2021-2](https://www.youtube.com/playlist?list=PLgIrOsyBCImpDQu30UKrMVSRHf3gW2gKb).
- [Explicación BVH y KdTree](https://youtu.be/_mSVK0OaaYw)

## Material Tareas

- T0
- T1
- T2
- T3

## Clases

|   Tipo    | Número | Tema | Fecha | Sección 1  | Sección 2 |
| :-------: | :----: | :------------------------------------------: | :---: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------: |

  ## Ayudantías

|   Tipo    | Número | Tema | | Material   |
| :--- | :--- | :--- | :--- | :--- |

## Equipo

### Profesores
| Nombre  | Sección | Email |
| :-------------- | :------ | :---------------- |
| Sebastián Bugedo | 1  | bugedo@uc.cl |
| Mario Droguett | 2  | mario@uc.cl |

### Ayudantes

| Nombre    | Email    | Github |
| :----------------------- | :---------------------- | :------------------------------------------------------- |

## Evaluación

El curso consta de una parte teórica, evaluada mediante evaluaciones escritas (interrogaciones), y una parte práctica, evaluada mediante tareas de programación en C.

### Evaluaciones Escritas

Habrá 3 interrogaciones, donde se evaluarán los aspectos más teóricos del contenido.

| Evaluación | Fecha |
| :-------------- | :--------- |
### Tareas

Habrá 4 tareas de programación en C, donde deberán resolver un problema complejo y analizarlo en un informe escrito.

| Evaluación | Fecha Publicacion  | Fecha Entrega      |
| :--------- | :----------------- | :----------------- |
| Tarea 0    | AA AAA AAA     | AA AAA AAA     |
| Tarea 1    | AA AAA AAA     | AA AAA AAA     |
| Tarea 2    | AA AAA AAA     | AA AAA AAA     |
| Tarea 3    | AA AAA AAA     | AA AAA AAA     |

La nota final del curso se calcula de la siguiente manera:

```c++
double nota_final() {
  /* La nota de cada tarea */
  double T0, T1, T2, T3;
  /* La nota de cada interrogación*/
  double I1, I2, I3;

  /* Promedio de tareas */
  double NT = min(0.20 * T0 + 0.30 * T1 + 0.25 * T2 + 0.25 * T3, 7.0);
  /* Promedio de interrogaciones */
  double NI = min(0.25 * I1 + 0.30 * I2 + 0.45 * I3, 7.0);

  /* Nota final */
  double NF = (NT + NI) / 2;

  /* Es necesario tener sobre 3.7 en las evaluaciones escritas y las tareas por separado para aprobar el curso */
  if (NI < 3.7 || NT < 3.7) {
    return min(3.9, NF);
  } else {
    return min(NF, 7);
  }
}
```

## Política de Atrasos

La formula de atrasos es la siguiente:

```c++
  double nota_con_atraso(double nota, int dias_de_atraso){
    if (dias_de_atraso > 4) { return 1.0; }

    return max(1.0, nota - 0.7 * dias_de_atraso);
  }
```

## Política de integridad académica

Este curso se adscribe a la política de integridad académica de la Escuela de Ingeniería y el Departamento de Computación.

---

Los alumnos de la Escuela de Ingeniería de la Pontificia Universidad Católica de Chile deben mantener un comportamiento acorde a la Declaración de Principios de la Universidad. En particular, se espera que **mantengan altos estándares de honestidad académica**. Cualquier acto deshonesto o fraude académico está prohibido; los alumnos que incurran en este tipo de acciones se exponen a un Procedimiento Sumario. Es responsabilidad de cada alumno conocer y respetar el documento sobre Integridad Académica publicado por la Dirección de Docencia de la Escuela de Ingeniería (disponible en SIDING).

Específicamente, para los cursos del Departamento de Ciencia de la Computación, rige obligatoriamente la siguiente política de integridad académica. Todo trabajo presentado por un alumno para los efectos de la evaluación de un curso debe ser hecho individualmente por el alumno, sin apoyo en material de terceros. Por “trabajo” se entiende en general las interrogaciones escritas, las tareas de programación u otras, los trabajos de laboratorio, los proyectos, el examen, entre otros.

**En particular, si un alumno copia un trabajo, o si a un alumno se le prueba que compró o intentó comprar un trabajo, obtendrá nota final 1.1 en el curso y se solicitará a la Dirección de Docencia de la Escuela de Ingeniería que no le permita retirar el curso de la carga académica semestral.**

Por “copia” se entiende incluir en el trabajo presentado como propio, partes hechas por otra persona. **En caso que corresponda a “copia” a otros alumnos, la sanción anterior se aplicará a todos los involucrados**. En todos los casos, se informará a la Dirección de Docencia de la Escuela de Ingeniería para que tome sanciones adicionales si lo estima conveniente. Obviamente, está permitido usar material disponible públicamente, por ejemplo, libros o contenidos tomados de Internet, siempre y cuando se incluya la referencia correspondiente y sea autorizado por los ayudantes.

Lo anterior se entiende como complemento al Reglamento del Alumno de la Pontificia Universidad Católica de
Chile<sup><a name="pucCLBack">[1](#pucCL)</a></sup>. Por ello, es posible pedir a la Universidad la aplicación de sanciones adicionales especificadas en dicho reglamento.

<sub>**<a name="pucCL">[1](#pucCL)</a>**: Reglamento del Alumno de la Pontificia Universidad Católica de Chile disponible en: http://admisionyregistros.uc.cl/alumnos/informacion-academica/reglamentos-estudiantiles [&#8593;](#pucCLBack)</sub>
