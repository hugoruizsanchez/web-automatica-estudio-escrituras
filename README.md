# Web automática para la gestión de la web "Estudio Escrituras"
## Tratamiento de archivos ODT, TXT, PDF para ser convertidos a formatos legibles por el navegador (HTML, PDF)

> Atención: se trata de un proyecto personal, que se adecúa a las necesidades particulares de mi objetivo concreto - la integración automática de contenido a mi web teológica "Estudio Escrituras" -, cuya estructura difiere a la de otro tipo de webs. No es un software de gestión automática de páginas webs, sino mi solución particular aplicada a un único contexto, publicado para ser utilizado como mera referencia y apoyo.

1. Casi todos mis archivos se encuentran en formatos .odt - el formato en que exporta LibreOffice - ; o en su defecto, ficheros de texto plano .txt o ya exportados .pdf
2. Cada archivo está organizado en su correspondiente carpeta, bien sea una `comparativa`, un `devocional` o un `estudio`.
3. Un script escrito en bash, `exportar.sh` crea una nueva estructura de carpetas y opera sobre los directorios de mi área de trabajo, convirtiendo automáticamente cada archivo en su interior en formatos .pdf y .html, que son los que presento en esta página. Este procedimiento usa las utilidades que brinda LibreOffice para la consola de comandos, denominadas soffice. Las exportaciones en PDF siempre funcionan bien, pero cuando hago el mismo proceso con HTML, el formato tiende a desconfigurarse.
4. Finalmente, un programa escrito en Python, `compilar-web.py` inspecciona la estructura de carpetas creada por el script anterior, creando los archivos .html necesarios para enlazar todos los documentos en una página web completa y funcional. 
