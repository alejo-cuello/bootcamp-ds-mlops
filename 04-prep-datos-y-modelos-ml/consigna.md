# Ejercicio 🏡

## 📍 Objetivo
<br>Realizar la preparación de datos de la Encuesta anual de hogares realizada en todo el territorio de la Ciudad de Buenos Aires, Argentina en el 2019.
<br>Prácticamente vas a acondicionar el dataset para que te quede listo para buscar correlaciones o entrenar algún modelo de Machine Learning.

El dataset proviene del Open Data del Gobierno de Buenos Aires: [Encuesta anual de hogares 2019](https://data.buenosaires.gob.ar/dataset/encuesta-anual-hogares)

---
## 📍 Consigna 1

**_1) Cargamos los datos_**
- Carguen el dataset:
```
  data = pd.read_csv("encuesta-anual-hogares-2019.csv", sep=',') 
```
**_2) Inspección inicial_**
- Eliminen las columnas `id` y `hijos_nacidos_vivos`

**_3) Discretización_**
- Para las siguientes columnas discreticen por igual frecuencia e igual rango.
    <br>`ingresos_familiares` con q=8
    <br>`ingreso_per_capita_familiar` con q=10

- En algunas situaciones hay ciertos elementos que se repiten al momento de discretizar, una forma de eliminar duplicados es con el argumento `duplicates='drop'`.
    <br><br>Para las siguientes columnas `ingreso_total_lab` y `ingreso_total_no_lab` consideren:
    ```
    data['ingreso_total_lab'] = pd.qcut(data['ingreso_total_lab'], q=10, duplicates='drop')
    data['ingreso_total_no_lab'] = pd.qcut(data['ingreso_total_no_lab'], q=4, duplicates='drop')
    ```

- Para la columna `edad` discreticen usando igual distancia (rango) con `bins=5`.

**_4) Preparación de datos_**
- Cambien el tipo de dato a `str` de las siguientes columnas: `comuna` y `nhogar`.
  <br>_¿Por qué hacemos esto?_ Para estas columnas el número es simplemente una connotación, para representar una comuna por ejemplo pero no hay una relación numérica entre ellos.

- _¿Qué esperas como valor en la columna `años_escolaridad`?_ Número enteros pero no siempre es así, cada entidad o empresa tiene diferentes formas de rellenar una encuesta.
    <br>Evalua lo siguiente: `data['años_escolaridad'].unique()`, vas a poder ver los valores únicos en la columna. Donde destacamos que todos son `object/string`.

- Reemplazar `Ningun año de escolaridad aprobado` por un '0'. 
<br>Efectivamente por '0' y no 0, porque esta columna maneja datos tipo `object/string`.
    ```
    data['años_escolaridad'] = data['años_escolaridad'].replace('Ningun año de escolaridad aprobado', '0')
    ```

- Vamos a convertir los tipos de datos de la columna anterior `años_escolaridad` a enteros.
    <br>De manera intuitiva podríamos hacer:
    ```
    data['años_escolaridad'] = data['años_escolaridad'].astype("Int32")
    ```
    PEROOOOOOO marca un error, ¿cierto?
    
    Posiblemente muchas veces les pase que cuando hagan una _cast_ (conversión de un tipo de dato a otro) pueden llegar a tener conflictos si esa columna tienen _NaN_. Para este caso si queremos convertir los valores de la columna `años_escolaridad` de _string_ a _int_, hay que hacer un paso intermedio que es pasarlo a _float_.
    ```
    data['años_escolaridad'] = data['años_escolaridad'].astype(float).astype("Int32")
    ```

- Discreticen para la columna `años_escolaridad` por igual frecuencia e igual rango con un `q=5`

- No necesariamente siempre hay que rellenar los `NaN` en todas las columnas, porque quizás esa cantidad de `NaN` no es tan representativa para nuestro análisis. Así que podes eliminarlo para todo el dataframe o para ciertas columnas.
    ```
    # Eliminar filas que contengan NaN
    data = data.dropna(subset=['situacion_conyugal', 'sector_educativo', 'lugar_nacimiento', 'afiliacion_salud'])
    ```
- Después de eliminar filas, podes resetear el índice para que mantenga la secuencia:
    ```
    data = data.reset_index(drop=True)
    ```

- Rellenar los datos faltantes para la columna `años_escolaridad`. Primero añadan la categoría `desconocido` y luego hacen un rellenado de los datos faltantes con `desconocido`.

- Rellenar los datos faltantes para la columna `nivel_max_educativo` con `value=desconocido`

## 📍 Respuesta esperada 1

Si hacen `status(data)` deberían obtener lo siguiente :

---

respuesta_1 = pd.read_csv("tarea_respuesta1.csv", sep=',') 

respuesta_1

## 📍 Consigna 2

---

**_5) One hot encoding_**

- Hagan `data_ohe = pd.get_dummies(data)`
- Guardar `data_ohe` en un archivo pickle como vimos en clase con el nombre `categories_ohe.pickle`.
- Carguen el dataset `new_data = pd.read_csv("new_data.csv", sep=',')`
- A `new_data` hagan un reindex con las columnas que guardaron el archivo pickle y para los valores `NaN` rellenenlos con un `0`.

## 📍 Respuesta esperada 2

---

respuesta_2 = pd.read_csv("tarea_respuesta2.csv", sep=',') 

respuesta_2

## 📍 Consigna 3

Cargar su notebook y datasets a un repositorio público personal y compartirlo por Discord.
<br>Consideren usar git lfs para los dataset con extensión csv.