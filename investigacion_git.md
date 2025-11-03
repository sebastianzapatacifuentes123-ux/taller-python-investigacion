# Investigacion sobre git basico
1. ¿Qué es el "staging area" o "índice" en Git y para qué sirve?
Explica la diferencia entre working directory, staging area y repository
¿Por qué es útil tener esta área intermedia?
DESARROLLO:
el staging area es una zona intermedia donde git guarda los archivos que estan listos para ser confirmados con un commit
working directory: donde trabajamos y editamos los archivos
staging area: donde se colocan los archivos con git add para preparar el commit
repository: donde se guardan de forma permanente los commits ya registrados
esta area intermedia permite revisar los cambios antes de hacer commit, evitando errores

2. ¿Qué hace el comando git status y por qué es importante usarlo frecuentemente?
Menciona al menos 3 tipos de información que proporciona
DESARROLLO:
el comado git status muestra el estado actual del repositorio
- si hay archivos nuevos no rastreados
- si hay archivos modificados que aun no estan en staging
- en que rama estamos trabajando
es importante usarlo para verificar que cambios se han hecho antes de hacer add o commit
 
3. Diferencia entre git fetch y git pull
¿Cuándo usarías uno u otro?
¿Cuál es más seguro y por qué?
DESARROLLO
git fetch: descarga los cambios del repositorio remoto, pero no los mezcla con el trabajo local
git pull: descarga y fusiona automaticamente los cambios del remoto con la rama local
git fetch es mas seguro, porque se puede revisar los cambios antes de fusionarlos manualmente

4. ¿Qué es un "merge conflict" y cómo se resuelve?
Da un ejemplo de cuándo podría ocurrir
Describe los pasos básicos para resolverlo
DESARROLLO
un merge conflict ocurre cunado dos personas modifican la misma parte de un archivo y git no sabe cual version mantener
ejemplo
- una persona cambia una linea en main.py
- otra persona cambia la misma linea en su rama 
cuando se hace git merge, git muestra un conflicto
para resolverlo: 
- abrir el archivo y decidir que parte conservar 
- eliminar los marcadores
- guardar el archivo
- ejecutar git add archivo_afectado. git commit -m "fix: resolver conflicto de merge en main.py"




