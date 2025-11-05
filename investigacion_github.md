# Investigacion sobre GitHub y colaboracion
1. ¿Qué es un Pull Request (PR) y cuál es su propósito?
¿En qué se diferencia de un merge directo?
¿Cuáles son las ventajas de usar PRs en proyectos colaborativos?
DESAROOLLO
un pull request (PR) es una solicitud que un colaborador hace para que sus cambios sean revisados e integrados en la rama principal de un repositorio en github
 DIFERENCIA CON MERGE DIRECTO: con un merge directo, los cambios se integran sin revision. en cambio un PR permite revisar el codigo, comentar y aprobar antes de unirlo
 VENTAJAS: 
 - permite revision de codigo por otros niembros del equipo
 - evita errores o conflictos antes de integrar 
 - documenta el historial de cambios y discusiones tecnicas

 2. ¿Qué es un fork en GitHub y cuándo se usa?
Diferencia entre fork y clone
¿Cómo contribuirías a un proyecto open source usando fork?
DESARROLLO
un fork es una copia de un repositorio en una cuenta de github, que permite modificarlo sin afectar el original
DIFERENCIA
fork crea una copia en github
clone descarga una copia local del repositorio
CONTRIBUCION OPEN SOURCE
- haces un fork del reporsitorio
- clonas tu fork
- creas una rama, haces cambios y los subes
- envias un pull request al repositorio original
 
 3. ¿Qué es el archivo .gitignore y por qué es importante?
Menciona al menos 5 tipos de archivos que NO deberían subirse a un repositorio Python
¿Qué problemas podrían ocurrir si no usas .gitignore?
DESARROLLO 
el archivo gitignore le indica a git que archivos o carpetas debe ignorar para no subirlos al repertorio
- venv/ (entornos virtuales)
_pycache_/(archivos temporales de python)
-*. pyc (archivos compilados)
.env (variable sensibles)
*long(archivos de registros)
POBLEMAS SI NO SE USA
- se suben archivos innecesarios o poesados
- riesgos de exponer contraseñas o configuraciones privadas

4. ¿Qué son los issues en GitHub y para qué sirven?
¿Qué información debería contener un buen issue?
¿Cómo se pueden relacionar issues con commits?
DESARROLLO
los issues son reportes o tareas que permiten registrar errores, mejoras o pendientes dentro del proyecto
- titulo claro
- descripcion del problema
- pasos para reproducirlo
- archivos o capturas relacionadas
COMO SE PUEDE RELACIONAR ISSUES CON COMITS
un commit puede cerrar un issue automaticamente usando palabras claves 

5. Investiga qué es GitHub Actions
¿Para qué se utiliza?
Menciona 2 ejemplos de tareas que podrías automatizar 
DESARROLLO
es una herramienta de aumatizacion integrada de github permite ejecutar flujos de traabajo (workflows) automath unicamente cada vez que ocurre un evento (como un pus o PR)
- ejecutar pruebas unitarias cuando alguien sube codigo
- despeglar una aplicion a un servidor o a un servicio en la nube
- analizar el codigo con linters o revisores automatico
