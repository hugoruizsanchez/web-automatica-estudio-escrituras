# Script de subida a página web
## -> Necesarion pandocs, pdftohtml y libreoffice
<<COMMENT 

Estructura que debe contener el directorio "web": 
---- SCRIPTS ----
exportar.sh  
compilar-web.py    
---- CARPETAS GENERADAS POR exportar.sh ----
web-devocionales
web-comparativas
web-estudios
---- ARCHIOS GENERADOS POR compilar_web.py ----
estudios.html
comparativas.html
devocionales.html
           
COMMENT

# -----------------------

# CONFIGURACIÓN DE VARIABLES

## Entrada
ubicacionDevocionales=/home/hugo/Drive/Teologia/Apuntes/devocionales-o-escritos-no-academicos
ubicacionComparativas=/home/hugo/Drive/Teologia/Apuntes/comparativas-y-concurrencias
ubicacionEstudios=/home/hugo/Drive/Teologia/Apuntes/estudios

## Salida --> ¡ES NECESARIO QUE LA CARPETA "web" ya ESTÉ CREADA!
ubicacionWeb=/home/hugo/Drive/Teologia/web

# -----------------------

# OPERAR EN LOS DIRECTORIOS

## Eliminar todos los archivos del directorio
cd $ubicacionWeb
rm -r web-estudios
rm -r web-devocionales
rm -r web-comparativas

## CREACIÓN DE CARPETAS 
notify-send "Creando carpetas"
mkdir -p web-estudios/pdf $ubicacionWeb/web-estudios/html
mkdir -p web-devocionales/pdf $ubicacionWeb/web-devocionales/html
mkdir -p web-comparativas/pdf $ubicacionWeb/web-comparativas/html

# -----------------------

# CONVERSIÓN A PDF

## Conversión de todos los archivos ODT a PDF, depositandolos en sus respectivas carpetas. 
notify-send "Convirtiendo a PDF los archivos ODT"
soffice --convert-to pdf --outdir web-estudios/pdf $ubicacionEstudios/*.odt
soffice --convert-to pdf --outdir web-comparativas/pdf $ubicacionComparativas/*.odt
soffice --convert-to pdf --outdir web-devocionales/pdf $ubicacionDevocionales/*.odt

## Conversión de todos los archivos TXT a PDF, depositandolos en sus respectivas carpetas. 
notify-send "Convirtiendo a PDF los archivos TXT"
for archivo in $ubicacionEstudios/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.pdf"
	mv "${archivo%.txt}.pdf" $ubicacionWeb/web-estudios/pdf
done

for archivo in $ubicacionDevocionales/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.pdf"
	mv "${archivo%.txt}.pdf" $ubicacionWeb/web-devocionales/pdf
done

for archivo in $ubicacionComparativas/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.pdf"
	mv "${archivo%.txt}.pdf" $ubicacionWeb/web-comparativas/pdf
done

## Los archivos que ya están en PDF, enviarlos directamente 
notify-send "Copiando los archivos PDF existentes"
cp $ubicacionEstudios/*.pdf web-estudios/pdf
cp $ubicacionComparativas/*.pdf web-comparativas/pdf
cp $ubicacionDevocionales/*.pdf web-devocionales/pdf

# -----------------------

# CONVERSIÓN  A HTML
cd $ubicacionWeb

## Conversión de todos los archivos ODT a HTML 
notify-send "Convirtiendo a HTML los archivos ODT"
soffice --convert-to xhtml --outdir $ubicacionWeb/web-estudios/html $ubicacionEstudios/*.odt
soffice --convert-to xhtml --outdir $ubicacionWeb/web-devocionales/html $ubicacionDevocionales/*.odt
soffice --convert-to xhtml --outdir $ubicacionWeb/web-comparativas/html $ubicacionComparativas/*.odt

### La salida será xhtml, que debe cambiarse a .html en todos los archivos
notify-send "Cambiando las extensiones XHTML a HTML"
for archivo in $ubicacionWeb/web-estudios/html/*.xhtml; do 
	mv "$archivo" "${archivo%xhtml}".html
done

for archivo in $ubicacionWeb/web-devocionales/html/*.xhtml; do 
	mv "$archivo" "${archivo%xhtml}".html
done

for archivo in $ubicacionWeb/web-comparativas/html/*.xhtml; do 
	mv "$archivo" "${archivo%xhtml}".html
done

## Conversión de todos los archivos TXT a HTML 
notify-send "Convirtiendo a HTML los archivos TXT"
for archivo in $ubicacionEstudios/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.html"
	mv "${archivo%.txt}.html" $ubicacionWeb/web-estudios/html
done

for archivo in $ubicacionDevocionales/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.html"
	mv "${archivo%.txt}.html" $ubicacionWeb/web-devocionales/html
done

for archivo in $ubicacionComparativas/*.txt; do 
	pandoc "$archivo" -o "${archivo%.txt}.html"
	mv "${archivo%.txt}.html" $ubicacionWeb/web-comparativas/html
done

## Conversión de todos los archivos PDF a HTML
notify-send "Convirtiendo a HTML los archivos PDF"

for archivo in $ubicacionEstudios/*.pdf; do 
	pdftohtml -noframes -i "$archivo" "${archivo%.pdf}.html"
	mv "${archivo%.pdf}.html" $ubicacionWeb/web-estudios/html
done

for archivo in $ubicacionDevocionales/*.pdf; do 
	pdftohtml -noframes -i "$archivo" "${archivo%.pdf}.html"
	mv "${archivo%.pdf}.html" $ubicacionWeb/web-devocionales/html
done

for archivo in $ubicacionComparativas/*.pdf; do 
	pdftohtml -noframes -i "$archivo" "${archivo%.pdf}.html"
	mv "${archivo%.pdf}.html" $ubicacionWeb/web-comparativas/html
done
notify-send "Trabajo de exportación finalizado"
## Procesar los archivos en python

notify-send "Procesando página web"
cd $ubicacionWeb
python3 compilar-web.py
rclone sync $ubicacionWeb web:htdocs
