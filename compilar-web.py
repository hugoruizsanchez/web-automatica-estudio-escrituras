import glob # Acceso a los archivos
import numpy; # Para ordenar arrays
import datetime; 

##
# limpiarinfo: limpia la información inútil de los archivos, los convierte en ubicaciones dinámicas
##
def limpiarInfo (archivos):
	salida = []
	for archivo in archivos:
		separacion = archivo.split("/"); # Convertir en un array siendo cada directorio un elemento
		if ".html" in separacion[len (separacion)-1] or ".pdf" in separacion[len (separacion)-1]: # Solo nos interesan los archivos .pdf y .html DENTRO del directorio deseado (*)
			salida.append (separacion[len (separacion)-3]+"/"+separacion [len (separacion)-2]+"/"+separacion [len (separacion)-1]) # Necesitamos los 3 últimos directorios para tener toda la información para el index
	return salida; 

# Recoger los archivos

archivosPdfDevocionales = glob.glob ("/home/hugo/Drive/Teologia/web/web-devocionales/pdf/*");
archivosPdfComparativas = glob.glob ("/home/hugo/Drive/Teologia/web/web-comparativas/pdf/*");
archivosPdfEstudios = glob.glob ("/home/hugo/Drive/Teologia/web/web-estudios/pdf/*");

archivosHtmlDevocionales = glob.glob ("/home/hugo/Drive/Teologia/web/web-devocionales/html/*");
archivosHtmlComparativas = glob.glob ("/home/hugo/Drive/Teologia/web/web-comparativas/html/*");
archivosHtmlEstudios = glob.glob ("/home/hugo/Drive/Teologia/web/web-estudios/html/*");

# Limpiarlos

archivosPdfDevocionales = limpiarInfo (archivosPdfDevocionales);
archivosPdfComparativas = limpiarInfo (archivosPdfComparativas);
archivosPdfEstudios = limpiarInfo (archivosPdfEstudios);

archivosHtmlDevocionales = limpiarInfo (archivosHtmlDevocionales);
archivosHtmlComparativas = limpiarInfo (archivosHtmlComparativas);
archivosHtmlEstudios = limpiarInfo (archivosHtmlEstudios);

# Verificación de integridad 

if len(archivosPdfDevocionales) == len (archivosHtmlDevocionales):
	print ("Integridad de los archivos de Devocionales: Correcta"); 
	if len(archivosPdfComparativas) == len (archivosHtmlComparativas):
		print ("Integridad de los archivos de Comparativas: Correcta"); 
		if len(archivosPdfEstudios) == len (archivosHtmlEstudios):
			print ("Integridad de los archivos de Estudios: Correcta");
		else:
			print ("Integridad de los archivos de Estudios: Incorrecta"); exit ();
	else:
		print ("Integridad de los archivos de Comparativas: Incorrecta"); exit ();
else:
	print ("Integridad de los archivos de Devocionales: Incorrecta"); exit ();
	
# Ordenar HTML y PDF para que su posicion en el array sea la misma. 

archivosPdfDevocionales.sort()
archivosPdfComparativas.sort()
archivosPdfEstudios.sort()

archivosHtmlDevocionales.sort()
archivosHtmlComparativas.sort()
archivosHtmlEstudios.sort()

# Creación del documento 

paginaEstudios = open("estudios.html", "w"); 
paginaComparativas = open("comparativas.html", "w"); 
paginaDevocionales =  open("devocionales.html", "w"); 

# Introducir encabezado

paginaEstudios.write ("<html> <head> <link rel='stylesheet' href='estilo-pagina-docs.css'> <title> Estudios </title> </head> <body> <header> <img src='https://upload.wikimedia.org/wikipedia/commons/8/87/Christian_cross.svg' />  <h1> <a href='index.html'> Estudio de la Escritura </a> </h1> <nav> <a href='estudios.html' class='resaltado'> Estudios </a> <a href='comparativas.html'> Comparativas</a> <a href='devocionales.html'> Devocionales</a> </nav> </header> <main> <div class='cuadro-advertencia'> <div class='titulo-advertencia'> ¡Atención! </div> <p class='mensaje-advertencia'> Por defectos de compatibilidad, se recomienda ver los documentos en formato PDF en vez de visionarlos directamente en la web.</p> </div> <h2> Estudios </h2> <p> Publicaciones pragmáticas, cuyo objeto es compendiar información, sea al respecto de un concepto concreto, áreas de la Biblia, conjuntos de pasajes, etcétera.</p>");
paginaComparativas.write ("<html> <head> <link rel='stylesheet' href='estilo-pagina-docs.css'> <title> Comparativas </title> </head> <body> <header> <img src='https://upload.wikimedia.org/wikipedia/commons/8/87/Christian_cross.svg' /> <h1> <a href='index.html'> Estudio de la Escritura </a> </h1> <nav> <a href='estudios.html'> Estudios </a> <a href='comparativas.html' class='resaltado'> Comparativas</a> <a href='devocionales.html' > Devocionales</a> </nav> </header> <main> <div class='cuadro-advertencia'> <div class='titulo-advertencia'> ¡Atención! </div> <p class='mensaje-advertencia'> Por defectos de compatibilidad, se recomienda ver los documentos en formato PDF en vez de visionarlos directamente en la web.</p> </div> <h2> Comparativas </h2> <p> Comparación de pasajes, en búsqueda de concurrencias. Incluyen comentarios marginales.</p>");
paginaDevocionales.write ("<html> <head> <link rel='stylesheet' href='estilo-pagina-docs.css'> <title> Devocionales </title> </head> <body> <header> <img src='https://upload.wikimedia.org/wikipedia/commons/8/87/Christian_cross.svg' />  <h1> <a href='index.html'> Estudio de la Escritura </a> </h1> <nav> <a href='estudios.html' > Estudios </a> <a href='comparativas.html'> Comparativas</a> <a href='devocionales.html' class='resaltado'> Devocionales</a> </nav> </header> <main> <div class='cuadro-advertencia'> <div class='titulo-advertencia'> ¡Atención! </div> <p class='mensaje-advertencia'> Por defectos de compatibilidad, se recomienda ver los documentos en formato PDF en vez de visionarlos directamente en la web.</p> </div> <h2> Devocionales </h2> <p> Redacciones breves presentadas para inspirar la devoción al Señor; esta sección también la empleo para artículos de opinión relacionados con la fe. </p>");

# Introducir los divs 

def introducirDivDocumento (documento, rutaArchivoPdf, rutaArchivoHtml):
	nombre = rutaArchivoPdf [rutaArchivoPdf.rindex("/")+1:rutaArchivoPdf.index(".")]
	documento.write ("<div class ='documento'>");
	documento.write ("<div class='nombre-documento'>"+nombre+"</div>");
	documento.write ("<div class='descarga-documento'>");
	documento.write ("<a href='"+rutaArchivoPdf+"' target='_blank' class='opcion-descarga descarga-pdf'>Ver en PDF</a>");
	documento.write ("<a href='"+rutaArchivoHtml+"' target='_blank' class='opcion-descarga descarga-web'>Ver en la web</a>");
	documento.write ("</div> </div>");

for i in range(len(archivosHtmlEstudios)):
	introducirDivDocumento (paginaEstudios, archivosPdfEstudios[i], archivosHtmlEstudios[i]);
	
for i in range(len(archivosHtmlDevocionales)):
	introducirDivDocumento (paginaDevocionales, archivosPdfDevocionales[i], archivosHtmlDevocionales[i]);
	
for i in range(len(archivosHtmlComparativas)):
	introducirDivDocumento (paginaComparativas, archivosPdfComparativas[i], archivosHtmlComparativas[i]);

# Introducir footer 

paginaEstudios.write ("</main> <footer> Hugo Ruiz Sánchez. Documentos de libre difusión. Última edición: "+ str(datetime.date.today())+"</footer></body> </html>");
paginaDevocionales.write ("</main> <footer> Hugo Ruiz Sánchez. Documentos de libre difusión. Última edición: "+str(datetime.date.today())+"</footer></body> </html>");
paginaComparativas.write ("</main> <footer> Hugo Ruiz Sánchez. Documentos de libre difusión. Última edición: "+str(datetime.date.today())+"</footer></body> </html>");

# FIN: Cerrar archivos

paginaEstudios.close()
paginaComparativas.close()
paginaDevocionales.close()

""" DOCUMENTO HTML GENERADO. 
<html> 
	<head> 
		<title> Devocionales </title> 
		<link rel="stylesheet" href="estilo-pagina-docs.css">
	</head> 
	
	<body> 
		<header> 
			<img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Christian_cross.svg" />
			<h1> <a href='index.html'> Estudio de la Escritura </a> </h1>
			
			<nav>
				<a href='estudios.html' > Estudios </a>
				<a href='comparativas.html'> Comparativas</a>
				<a href='devocionales.html' class='resaltado'> Devocionales</a>
			</nav>
		</header>
		<main> 
			<div class="cuadro-advertencia"> 
				<div class="titulo-advertencia"> ¡Atención! </div>
				<p class="mensaje-advertencia"> Por defectos de compatibilidad, recomiendo ver los documentos en formato PDF en vez de visionarlos directamente en la web.</p>
			</div>
			
			<h2> Devocionales </h2>
			
			<p> Redacciones breves presentadas para inspirar la devoción al Señor; esta sección también la empleo para artículos de opinión relacionados con la fe. </p>
		
			<!-- Generación automática --> 
			
			<div class ='documento'> 
				<div class='nombre-documento'> VARIABLE AQUI </div>
				<div class='descarga-documento'>
					<a href='VARIABLE AQUI' class='opcion-descarga'>Ver en PDF</a>
					<a href='VARIABLE AQUI' class='opcion-descarga'>Ver en la web</a>
				</div>
			</div>
		</main>
		<footer> Hugo Ruiz Sánchez. Última edición:  </footer>
		
		
	</body>
</html> 
"""

