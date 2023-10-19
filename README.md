# particiones

random_split

Descripción: El primer metodo realiza una partición aleatoria simple del conjunto de datos. Reorganiza las instancias de forma aleatoria y luego selecciona un porcentaje para entrenamiento y el complemento para pruebas.
Razón:Para mi la razon que elije esta es que en la elección aleatoria es útil cuando no hay ninguna estructura específica en los datos que sugiera una división más compleja. Es una forma básica y común de crear conjuntos de entrenamiento y prueba.

fixed_size_split

Descripción: El segundo metodo divide el conjunto de datos tomando un porcentaje fijo de instancias para entrenamiento y el resto para pruebas, independientemente de la cantidad total de datos.
Razón: Que puede ser útil cuando deseas una proporción específica de datos para entrenamiento y pruebas, sin importar el tamaño total del conjunto de datos.

class_split

Descripción: El tercer metodo separa el conjunto de datos por clases, tomando un porcentaje de instancias de cada clase para el entrenamiento y el complemento para las pruebas.
Razón: En esta es que si las clases en tu conjunto de datos tienen cantidades desiguales de instancias, este método ayuda a garantizar que todas las clases estén representadas tanto en el conjunto de entrenamiento como en el de prueba.

stratified_split

Descripción: El cuarto metodo realiza una partición estratificada manteniendo la proporción de clases en ambos conjuntos (entrenamiento y prueba).
Razón: Es que es muy util cuando las clases están desequilibradas. Asegura que la distribución de clases sea similar en ambas particiones, lo que puede ser crucial para el aprendizaje del modelo.

feature_ratio_split

Descripción: Este ultimo metodo divide el conjunto de datos basándose en la proporción de una característica específica. Toma un porcentaje de instancias cuyo valor de la característica es menor o igual a un umbral determinado.
Razón: Por ultimo elegi esta por que util si hay una característica específica que deseas que guíe la partición, por ejemplo, si se sospecha que esa característica es crucial para la predicción y deseas mantener una proporción específica en ambas particiones.
