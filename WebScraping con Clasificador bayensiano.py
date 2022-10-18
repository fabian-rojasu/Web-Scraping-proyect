from ast import arg
from os import link
from bs4 import BeautifulSoup
import requests 
import re
import time
import multiprocessing as mp
import os
import numpy as np
import matplotlib.pyplot as plt





totalPolitica = 108
totalDeporte = 139
totalVideoJuegos =123
totalRopa= 43
totalLenguajes =98
totalTecnologia =144
totalMobiliario =96
Total = 750




etiquetas = ['Politica', 'Deporte', 'Videojuegos', 'Ropa', 'Lenguajes de Programacion', 'Tecnologia', 'Mobilario', 'Sin funcionar']
diccionarioPalabras = {'Politica' : ['Presidente', 'votar', 'voto', 'democracia','alcalde','anarquismo','aristocracia','asamblea','autarquía','autonomía',
                       'burocracia','caciquismo', 'califa','canciller','censura','ciencia','coercitivo','concejal','consenso','conservadurismo','corrupción',
                       'decisión','demagogia','democracia','derecha','descentralización','desgobierno','despotismo','dictadura','dignatario','dinastía',
                       'diplomacia','diputado','dirigente','emir','emperador','ética','facción','familia','faraón','federalismo','fuerza','gabinete',
                       'gerontocracia','gobernador', 'Gobierno','gobierno','ideología','imperialismo','impunidad','influir','izquierda','junta','legitimidad',
                       'ley', 'política','liberalismo','líder','matriarcado','mayoría', 'sufragio','ministro','minoría','mitin','monarquía','moral','nacionalismo',
                       'oligarquía','oposición','oratoria','parlamento','partido','patriarcado','plebiscito','pluralismo','plutocracia','poder','prevaricación',
                       'propaganda','príncipe','rajá','rector','referéndum', 'Politica','regente','república','régimen','senado','sistema','soberano','soberanía',
                       'soborno','socialismo','sociedad','solución','status','sufragio','teoría','tirano','tiranía','totalitarismo','tutela','valido','violencia','visir',
                       'voluntad','voto', 'negociar','nepotismo', 'Política', 'congreso', 'civil', 'estado', 'elecciones', 'electoral', 'república', 'República'], 

                       'Deporte' : ['Football', 'Soccer', 'LaLiga', 'Saprissa', 'Messi','alero','animador','antorcha','árbitro','arco','atleta','atletismo','balón',
                       'baloncesto','bandera','banquillo','base','bicicleta','bota','boxeador','boxeo','caballo','calambre','calle','canasta','canoa','casco',
                       'césped','ciclista','contrarreloj','corredor','correr','cronómetro','decatlón','deportista','desfile','desmayo','diana','disco','distancia',
                       'doping','dorsal','entrega','entrenador','escalar','escolta','esfuerzo','esgrima','espectador','esquiador','estadio','éxito','flecha','fútbol',
                       'futbolista','gimnasia','gimnasta','gol','golf','golfista','grada','impulso','jinete','judo','jugador','kárate','lanzamiento','larguero','lesión',
                       'listón','maillot','Maratón','marcador','marcha','martillo','medalla','medallista','meta','nadar','obstáculo','olimpiada','oxígeno','partido',
                       'patinador','pelota','pelotón','penalti','Deporte', 'deporte', 'deportivo','pértiga','pesa','pista','pívot','polo','portería','portero','prórroga',
                       'raqueta','récord','red','reglas', 'Basketball', 'relajación','relevo','remar','respeto','revés','ría','rival','saltador','saltar','saque','sudor',
                       'táctica','tanto','tenista','testigo','tirador','valla','victoria','volea','zapatilla', 'FIFA', 'NBA', 'Premier', 'League', 'league',
                       'Bundesliga', 'bundesliga', 'serie a', 'Seria A', 'Ligue 1', 'Real Madrid', 'MLB', 'NFL', 'técnica','temporada',], 

                        'Videojuegos' : ['GTA V', 'Fortnite', 'FIFA 23','3D','abandonware','acción','adicción','alpha','altavoces','arcade','arte','auriculares','avatar',
                        'aventura','banear','beta','bonus','boss','bot','botón','bug','campaña','campear','cartucho','casete','casual','CD','cheat','checkpoint','cinemática',
                        'clan','clipping','combo','computadora','consumidor','conversacional','craftear','crash','demo','deportes','desarrollo','descarga','discos',
                        'distribuidor','DVD','e-sports','easter egg','electrónico','emulador','energía','entretenimiento','estrategia','expansión','fail','farmear','fase',
                        'feria','fps','freeware','game over','gamepad','género','hardware','hype','imagen','indie','industria', 'gaming', 'asus', 'msi','instrucciones',
                        'inteligencia artificial','interacción','joystick','juego en línea','kick','lag','lúdico','maná','mando','mapa','MMORPG','mod','moneda','motor', 
                        'multijugador','nivel','noob', 'eSports','ordenador','palanca','parche','periférico','personaje','perspectiva','plataforma','primera persona',
                        'pro gamer','ratón','realidad virtual', 'recreativo','respawn','retro','review','revista','rol','scroll','sdk','shareware','shooter','simulador',
                        'skin','software','sonido', 'RPG','speedrun','tarjeta gráfica','teclado','tecnología','tester','update','vida extra','walkthrough','youtuber', 'Steam',
                        'aplicación', 'juegos', 'juego', 'consola', 'plataforma', 'app'], 

                        'Ropa' : ['Boxer', 'pantalón', 'camisa','anillo','arete','pendiente','cinturón','gorro','guante','sombrero','sostén','brasier','sujetador',
                        'suéter','jersey','traje','vestido','billetera','blusa','boina','camiseta','chaqueta','corbata','falda','gorra','piyama','pijama','botas','bota',
                        'gafas','pantuflas','calcetines','calcetin','calzoncillos','calzoncillo','zapatos','zapato','pantalones', 'colección', 'Ropa', 'ropa', 'moda', 
                        'calzado'],

                        'Lenguajes de Programacion' : ['HTML', 'JavaScript', 'Python', 'Java','C++','C', 'C#', 'framework', 'programación', 'TI', 'código', 'desarrollador', 
                        'programador', 'programadores', 'lenguajes','librería', 'bug', 'dominio', 'software', 'Front-End', 'front-end', 'Back-End', 'back-end', 'Full-Stack', 
                        'full--stack', 'móvil', 'UI/UX', 'tester', 'ingeniero', 'database', 'bases', 'datos', 'ciberseguridad', 'proyecto', 'project', 'manager', 
                        'Visual Basic', '.NET', 'PHP', 'php', 'Perl', 'perl', 'c++', 'c', 'c#', 'java', 'python', 'ruby', 'Ruby', 'Swift', 'swift', 'go', 'Go', 'SQL',
                        'Android', 'android', 'interfaz', 'interface', 'user', 'CSS', 'css', 'diagrama', 'algoritmo', 'abstracción', 'array', 'list', 'binario', 'clase', 
                        'bool', 'int', 'string', 'String', 'class', 'clase','abstract', 'abstracta', 'compiler', 'compilación', 'compilar', 'compilador', 'declaration', 
                        'declaración', 'encapsulamiento', 'encapsulation', 'integer', 'boolean', 'herencia', 'inheritance','IDE', 'GUI', 'JDK', 'OOP', 'POO', 'UML', 
                        'diagrama', 'object', 'programming', 'developers', 'developer'],
                        
                        'Tecnologia' : ['antivirus', 'aplicación', 'CD-ROM', 'computadora', 'configuración', 'correo electrónico', 'digitalizar', 'editar', 'emoticon', 
                        'emoticono', 'emoji', 'equipo tecnologico', 'hipertexto', 'ícono', 'icono', 'inteligencia artifical', 'internet', 'ordenador', 'ratón', 
                        'ventan emergente', 'virus', 'web', 'respaldo', 'backup', 'byte', 'caché', 'cookies', 'bit', 'fibra óptica', 'FAQ', 'Gigabyte', 'GB', 'gb', 
                        'gigabyte', 'followers', 'hardware', 'hashtag', 'HTTP', 'RAM', 'metadatos', 'periféricos', 'IP', 'ip', 'sistema operativo', 'spam', 'software', 
                        'troll', 'URL', 'widget', 'copia de seguridad', 'batería', 'navegador', 'click', 'clic', 'portapapeles', 'código', 'Panel de control', 
                        'informática', 'conectar', 'copy', 'paste', 'copiar', 'pegar', 'cursor', 'ciberespacio', 'datos', 'base de datos', 'borrar', 'escritorio', 
                        'desarrolador', 'digital', 'disco duro', 'descargar', 'e-mail', 'gmail', 'hotmail', 'ejecutar', 'USB', 'memoria USB', 'pirata informático', 
                        'hacker', 'piratear', 'auriculares', 'audífonos', 'página de inicio', 'bandeja de entrada', 'instalar', 'tecla', 'teclas', 'teclado','portátil', 
                        'link', 'enlace', 'buzón de voz', 'memoria', 'menú', 'mensaje de voz', 'módem', 'router', 'red', 'bandeja de salida', 'contraseña', 'imprimir', 
                        'impresora', 'privacidad', 'procesador','reiniciar', 'resetear', 'guardar', 'escáner', 'escanear', 'pantalla', 'screenshot', 'captura de pantalla', 
                        'captura', 'electrónico', 'correo', 'servidor', 'programa', 'teléfono', 'celular', 'smartphone', 'redes', 'sociales', 'pestanaña', 'etiquetar', 
                        'encender', 'apagar', 'actualizar', 'cargar', 'subir', 'usuario', 'sitio', 'web', 'wifi', 'WiFi', 'Wi-Fi', 'Wifi', 'inalámbrico','laptops', 'laptops', 
                        'carpeta', 'asus', 'msi', 'electrónicos', 'correos'],
                        
                        'Mobiliario' : ['muebles', 'mueble', 'utensilio', 'mobiliario', 'menaje', 'vestíbulo', 'sala', 'salón', 'biblioteca', 'dormitorio', 'tocador', 'baño', 
                        'sanitario', 'comedor', 'cocina', 'silla', 'mecedora', 'sofá', 'butaca', 'reclinatorio', 'banqueta', 'armario', 'ropero', 'guardarropa', 'cómoda', 
                        'alacena', 'estantería', 'librería', 'casillero', 'repisa', 'estante', 'gaveta','despensa', 'mesa', 'pupitre', 'catre', 'lámpara', 'candelabro', 
                        'cuadro', 'marco', 'macetero', 'alfombra', 'tapiz', 'cortinas', 'cortina', 'madera', 'caoba', 'roble', 'castaño', 'abedul', 'latón', 'pino', 'metal', 
                        'bronce', 'cobre', 'acero', 'cuero', 'plástico', 'tela', 'seda', 'barniz', 'cerradura', 'puerta', 'ensambladura', 'rodapié', 'bisagra', 'visagra', 
                        'tapicería', 'ebanistería', 'carpintería', 'pintura', 'pulido', 'acabado', 'pulido', 'lijado', 'clavado', 'barnizado', 'tallado', 'decoración', 
                        'ebanista', 'carpintero', 'fabricante', 'artesano', 'decorador', 'pintor', 'amueblar', 'piso', 'atornillar', 'clavar','hogar', 'Hogar', 'remodelacion', 
                        'Remodelación', 'decoración', 'Decoración',]}
links=['https://www.w3schools.com/python/python_conditions.asp', 'https://www.nba.com/', 'https://elcaminantecr.com/tienda/', 'https://www.tse.go.cr/', 
       'https://www.msi.com/index.php', 'https://cr.epaenlinea.com/', 'https://www.google.com/intl/es/gmail/about/', 'https://www.ikea.com/es/es/', 
       'https://shop.lineuprewards.com/collections/forever-21','https://www.garpercr.com/', 'https://www.artelec.cr/', 'https://www.intelec.co.cr/', 
       'https://stackoverflow.com/', 'https://www.geeksforgeeks.org/', 'https://cnnespanol.cnn.com/category/politica/', 'http://www.cne.gob.ve/', 
       'https://www.onpe.gob.pe/elecciones/2022/elecciones-regionales-municipales/','https://semanariouniversidad.com/elecciones/', 
       'https://www.bbc.com/mundo/topics/ckgy9w45qxvt', 'https://www.ine.mx/voto-y-elecciones/elecciones-2022/','https://www.elmundo.cr/elecciones-2022/',
       'https://es.wikipedia.org/wiki/Elecciones_generales_de_Costa_Rica_de_2022', 'http://ucrelectoral.ucr.ac.cr/', 'https://www.nacion.com/etiqueta/elecciones%202022/',
       'https://www.cse.gob.ni/', 'https://delfino.cr/2022/02/elecciones-2022-figueres-y-alvarado-encabezan-resultados-al-primer-corte-con-13-5-de-las-mesas-escrutadas',
       'https://www.corteelectoral.gub.uy/elecciones-universitarias-2022', 'https://www.parlamentomercosur.org/innovaportal/v/19962/1/parlasur/calendario-electoral-2022.html',
       'https://wapp.registraduria.gov.co/electoral/Elecciones-2022/', 'https://idehpucp.pucp.edu.pe/analisis1/elecciones-regionales-y-municipales-2022-se-confirmaron-las-tendencias/', 
       'https://www.gob.pe/12516-consultar-tu-local-de-votacion-y-si-eres-miembro-de-mesa-en-las-elecciones-regionales-y-municipales-2022', 'https://www.ica.org/es/elecciones-del-ica-2022',
       'https://www.moe.org.co/calendario-electoral-conozca-las-fechas-clave-para-las-elecciones-presidenciales-del-2022/', 'https://www.unlpam.edu.ar/elecciones-2022', 
       'https://www.exteriores.gob.es/Consulados/saopaulo/es/Comunicacion/Noticias/Paginas/Articulos/Elecciones-al-Parlamento-de-Andaluc%C3%ADa-2022.aspx', 
       'https://www.fundacioncarolina.es/ac-05-2022/', 'https://www.tribunal-electoral.gob.pa/eventos-electorales/plan-general-elecciones-plagel/', 'https://www.unafut.com/', 
       'https://es-la.facebook.com/UnafutOficial/', 'https://www.instagram.com/unafutoficial/?hl=es', 'https://es.wikipedia.org/wiki/Primera_Divisi%C3%B3n_de_Costa_Rica', 
       'https://play.google.com/store/apps/details?id=io.pixeles.genius.costarica&hl=es_CR&gl=US', 'https://www.sensaciondeportiva.com/tag/unafut/', 'https://www.fedefutbol.com/ligas-asociadas/unafut-2/',
       'https://amprensa.com/2022/09/unafut-cierra-periodo-de-inscripciones-con-cuatro-movimientos-de-ultima-hora/', 'https://www.laliga.com/', 'https://es-la.facebook.com/LaLiga/', 
       'https://www.lateja.cr/deportes/video-unafut-marca-la-cancha-sobre-criterios-de/OL3QE4W6EBHD3MKRPZTAJ2YSKI/story/', 'https://en.wikipedia.org/wiki/La_Liga', 
       'https://futbolcentroamerica.com/costarica/Costa-Rica-Unafut-ya-definio-el-calendario-para-el-Apertura-2022-20220708-0013.html', 'https://fantasyunafut.com/', 
       'https://www.inamu.go.cr/unafut', 'https://semanariouniversidad.com/deportes/unafut-quita-la-obligacion-de-emplear-mascarillas-para-los-partidos/', 'https://www.teletica.com/tag/unafut',
       'https://observador.cr/pensando-en-el-repechaje-unafut-y-federacion-acordaron-suspender-un-mes-el-torneo-nacional/', 'https://elguardian.cr/unafut-definio-las-fechas-del-clausura-2023/',
       'https://be.linkedin.com/company/unafut?trk=public_profile_volunteering-position_profile-section-card_full-click', 'https://www.skysports.com/la-liga-table',
       'https://www.presidencia.go.cr/comunicados/tag/union-de-clubes-de-futbol-de-la-primera-division-unafut/', 'https://www.crhoy.com/noticias-sobre/unafut', 'https://laquinielaunafut.com/',
       'https://www.larepublica.net/noticia/unafut-suspende-campeonato-nacional-de-futbol-indefinidamente', 'https://www.espn.co.cr/futbol/costa-rica/nota/_/id/8715187/justicia-reglamentos-unafut-descenso',
       'https://www.elmundo.cr/deportes/unafut-premio-a-lo-mejor-del-futbol-costarricense/', 'https://www.transfermarkt.co.uk/laliga/startseite/wettbewerb/ES1', 'https://www.nacion.com/etiqueta/unafut/',
       'https://www.promerica.fi.cr/quienes-somos/liga-promerica/unafut/', 'https://apps.apple.com/cr/app/liga-promerica/id1577203757', 'https://es.trustpilot.com/review/g2a.com',
       'https://www.vidaextra.com/android/valve-ha-mejorado-app-steam-que-parece-nueva-puedes-descargar-juegos-tu-movil', 'https://store.steampowered.com/app/1549250/UNDECEMBER/',
       'https://play.google.com/store/apps/details?id=com.valvesoftware.android.steam.community&hl=es&gl=US', 'https://es.wikipedia.org/wiki/Steam', 'https://juegosadn.es/sites/steam/', 
       'https://store.steampowered.com/?l=spanish', 'https://apps.apple.com/pe/app/g2a/id895515193', 'https://es-es.facebook.com/G2AcomSpain/', 'https://help.steampowered.com/es/', 
       'https://es.wikipedia.org/wiki/G2A', 'https://www.g2a.co/', 'https://www.venca.es/','https://m.aboutyou.es/c/hombre/ropa-20290', 'https://www.amazon.es/clothing-accessories/b?ie=UTF8&node=2846220031', 
       'https://www.thedesireshop.es/es/12-ropa', 'https://www.kiabi.es/','https://www.next.es/es/men', 'https://www.studio16.es/c408296-ropa.html', 'https://www.c-and-a.com/es/es/shop/mujer-categorias',
       'https://www.laredoute.es/pplp/100/157878/cat-201.aspx', 'https://es.wikipedia.org/wiki/Ropa', 'https://www.parfois.com/es/es/ropa/', 'https://www.only.com/es-es/moda-de-mujer', 
       'https://inside-shops.com/es/', 'https://es.wikipedia.org/wiki/Mobiliario', 'https://www.archiproducts.com/es/productos/mobiliario', 'https://www.sklum.com/es/524-comprar-mobiliario', 
       'https://kavehome.com/es/es/mobiliario', 'https://www.vidaxl.es/g/436/mobiliario','https://www.bruneau.es/catalog/mobiliario/3448594o-jmbpr', 'https://www.billin.net/glosario/definicion-mobiliario/',
       'https://www.retif.es/c-559-mobilBiario-tiendas/', 'https://www.maisonsdumonde.com/ES/es/c/muebles-0efb00bec42f8fb7b942b4b76ad5c077', 'https://es.grosfillex.com/4-mobiliario-de-jardin', 
       'https://www.actiu.com/es/muebles/','https://materialesdefabrica.com/mobiliario-de-interior/', 'https://www.noirrac.com/que-mobiliario-no-puede-faltar-en-una-tienda/', 'https://www.boconcept.com/es-es/',
       'https://www.rderoom.es/shop/12-mobiliario', 'https://www.architonic.com/es/products/mobiliario/0/3210002/1', 'https://kendomobiliario.com/', 'https://www.makro.es/marketplace/c/mobiliario?offset=80&limit=20',
       'https://www.kalamazoo.es/mobiliario-de-oficina_C03.html' 'https://es.wikipedia.org/wiki/Programaci%C3%B3n', 'https://concepto.de/programacion/', 'https://www.netec.com/que-es-programacion',
       'https://www.edx.org/es/aprende/programacion-informatica', 'https://platzi.com/cursos/programacion-basica/', 'https://es.khanacademy.org/computing/computer-programming',
       'https://learndigital.withgoogle.com/activate/course/basics-code', 'https://www.linguee.com/spanish-english/translation/programaci%C3%B3n.html','https://programacion.net/',
       'https://es.wikipedia.org/wiki/Software', 'https://concepto.de/software/', 'https://www.areatecnologia.com/informatica/que-es-software.html','https://definicion.de/software/',
       'https://www.significados.com/software/', 'https://edu.gcfglobal.org/es/informatica-basica/que-es-hardware-y-software/1/', 'https://www.profesionalreview.com/software/',
       'https://www.euroinnova.edu.es/blog/que-es-el-software-y-sus-componentes-basicos', 'https://www.wolterskluwer.com/es-es/expert-insights/que-tipos-de-software-hay', 
       'https://vegagestion.es/los-tres-grandes-tipos-software/', 'https://www.nextu.com/blog/hardware-y-software-rc22/', 'https://www.sdelsol.com/', 
       'https://www.amazon.es/Software/b?ie=UTF8&node=599376031', 'https://www.sede.fnmt.gob.es/descargas/descarga-software', 'https://www.dnielectronico.es/portaldnie/PRF1_Cons02.action?pag=REF_1101', 
       'https://www.europapress.es/portaltic/software/', 'https://www.ejemplos.co/20-ejemplos-de-software/', 'https://dle.rae.es/software', 'https://www.assoftware.es/', 
       'https://www.yeeply.com/blog/lenguajes-de-programacion-mas-usados/', 'https://www.universia.net/es/actualidad/empleo/lenguajes-programacion-mas-usados-actualidad-1136443.html', 
       'https://es.wikipedia.org/wiki/Lenguaje_de_programaci%C3%B3n', 'https://www.epitech-it.es/cuantos-lenguajes-existen/', 
       'https://keepcoding.io/blog/5-lenguajes-de-programacion-mas-usados-2022/','https://kodigo.org/cuales-son-los-10-lenguajes-de-programacion-mas-usados-en-la-actualidad/',
       'https://blog.centrodeelearning.com/2021/12/15/lenguajes-de-programacion-mas-utilizados/', 'https://www.edix.com/es/instituto/lenguajes-de-programacion/', 
       'https://www.marketingandweb.es/marketing/lenguajes-de-programacion-mas-usados/', 'https://www.areatecnologia.com/informatica/lenguajes-de-programacion.html',
       'https://programas.cuaed.unam.mx/repositorio/moodle/pluginfile.php/1023/mod_resource/content/1/contenido/index.html', 'https://concepto.de/lenguaje-de-programacion/',
       'https://dinahosting.com/blog/los-10-lenguajes-de-programacion-mas-usados/', 'https://blogthinkbig.com/lenguajes-programacion-usados', 
       'https://www.wildcodeschool.com/es-ES/blog/tipos-de-lenguajes-de-programacion', 'https://lenguajesdeprogramacion.net/', 
       'https://hipertextual.com/2022/07/lenguajes-programacion-mas-demandados-2022', 'https://rockcontent.com/es/blog/tipos-de-lenguaje-de-programacion/',
       'https://axarnet.es/blog/lenguajes-de-programacion-mas-usados', 'https://jdelectricos.com.co/aparatos-electricos-y-electronicos/', 
       'https://www.bbc.com/mundo/noticias/2016/05/160504_tecnologia_aparatos_mas_influyentes_historia_yv', 'https://es.wikipedia.org/wiki/Aparato_electr%C3%B3nico', 
       'https://www.endesa.com/es/blog/blog-de-endesa/electrodomesticos/aparato-electronico-electrico', 
       'https://www.miteco.gob.es/es/calidad-y-evaluacion-ambiental/temas/prevencion-y-gestion-residuos/flujos/aparatos-electr/electricos-y-electronicos-materiales-y-componentes.aspx',
       'https://ecoinstaladores.com/asociaciones/que-son-los-aparatos-electricos-y-electronicos/', 'https://limpiezademalaga.es/categorias-aparatos-electricos-electronicos/', 
       'https://www.nrdc.org/es/experts/noah-horowitz/guia-aparatos-electronicos-menor-consumo-energia-nrdc-2013', 'https://www.areatecnologia.com/electronica/aparatos-electronicos.html',
       'https://es.wikipedia.org/wiki/Tecnolog%C3%ADa', 'https://concepto.de/tecnologia/', 'https://economipedia.com/definiciones/tecnologia.html', 'http://www.unl.edu.ar/ingreso/cursos/cac/21ot/',
       'https://www.edu.xunta.gal/espazoAbalar/sites/espazoAbalar/files/datos/1464945204/contido/1_la_tecnologa.html', 'https://conceptodefinicion.de/tecnologia/','https://elpais.com/tecnologia/', 
       'https://www.bbc.com/mundo/topics/cyx5krnw38vt', 'https://www.significados.com/tecnologia/', 'https://es.wikipedia.org/wiki/Internet', 'https://en.wikipedia.org/wiki/Internet', 
       'https://www.att.com/internet/', 'https://www.speedtest.net/es', 'https://www.t-mobile.com/home-internet', 'https://www.internetsociety.org/es/', 'https://www.internetessentials.com/', 
       'https://archive.org/', 'https://es.wikipedia.org/wiki/Inform%C3%A1tica', 'https://www.informatica.us.es/index.php/conoce-tu-futura-escuela/la-informatica', 'https://concepto.de/informatica/', 
       'https://conceptodefinicion.de/informatica/', 'https://www.informatica.com/', 'https://definicion.de/informatica/', 'https://www.ingles.com/traductor/inform%C3%A1tica', 
       'https://www.tecnologia-informatica.com/que-es-informatica/', 'https://www.bbvaopenmind.com/articulos/historia-de-la-informatica/','https://www.significados.com/informatica/',
       'https://www.pirlotv.fr/', 'https://www.pacaloca.com/'       
    ]
linksProceso1 = links[:49]
linksProceso2 = links[49:98]
linksProceso3 = links[98:147]
linksProceso4 = links[147:]

class VincularLinksPalabras:
    def __init__(self, link, palabras) :
        self.link = link
        self.palabras = palabras

def webScrapping(urls,urles):

 
    for url in urls:
        try:
            page = requests.get(url)
        except: 
            print("El siguiente URL presenta fallas:", url)

        soup = BeautifulSoup(page.content, 'html.parser')

        meta = soup.find_all('meta')

        cont = 0

        descripcion = ''
        keywords = ''

        for tag in meta:
            if 'name' in tag.attrs.keys() and tag.attrs['name'].strip().lower() in ['description', 'keywords']:
                if (cont == 0):
                    descripcion = tag.attrs['content']
                    cont += 1
                elif(cont == 1):
                    keywords = tag.attrs['content']

        listaPalabrasDescripcion = []
        listaPalabrasKeywords = []
        patron = '[^-¡!.¿?, ]+'
        listaPalabrasDescripcion = re.findall(patron, descripcion)
        listaPalabrasKeywords = re.findall(patron, keywords)

        diccionarioIncidencia={'Politica':0,
                                'Deporte':0,
                                'Videojuegos':0,
                                'Ropa':0,
                                'Lenguajes de Programacion':0,
                                'Tecnologia' : 0,
                                'Mobiliario' : 0}
        
        palabrasCoincididas = []

        for i in listaPalabrasDescripcion:
            cont2 = 0
            while (cont2 < len(diccionarioPalabras)):
                for key, values in diccionarioPalabras.items():
                    if(i in values):
                        if i not in palabrasCoincididas:
                            diccionarioIncidencia[key]+=1
                            palabrasCoincididas.append(i)
                        elif(i in palabrasCoincididas):
                            pass
                    cont2 += 1

        for i in listaPalabrasKeywords:
            cont2 = 0
            while (cont2 < len(diccionarioPalabras)):
                for key, values in diccionarioPalabras.items():
                    if(i in values):
                        if i not in palabrasCoincididas:
                            diccionarioIncidencia[key]+=1
                            palabrasCoincididas.append(i)
                        elif(i in palabrasCoincididas):
                            pass
                cont2 += 1
        
        res=clasificador(diccionarioIncidencia)

        for i, j in res.items():
            if(i == 'Politica'):
                urles[0].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Deporte'):
                urles[1].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Videojuegos'):
                urles[2].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Ropa'):
                urles[3].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Lenguajes de Programacion'):
                urles[4].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Tecnologia'):
                urles[5].append(VincularLinksPalabras(url, palabrasCoincididas))
            if(i == 'Mobiliario'):
                urles[6].append(VincularLinksPalabras(url, palabrasCoincididas))
    
   

def clasificador(diccionario):

    resultados={}

    diccionarioClasificador={'Politica':0,
                            'Deporte':0,
                            'Videojuegos':0,
                            'Ropa':0,
                            'Lenguajes de Programacion':0,
                            'Tecnologia' : 0,
                            'Mobiliario' : 0}
    result=0
    for i, j in diccionario.items():
        if i == "Politica":
            diccionarioClasificador[i] = (j/totalPolitica)*(totalPolitica/Total)
        if i == "Deporte":
            diccionarioClasificador[i] = (j/totalDeporte)*(totalDeporte/Total)
        if i == "Videojuegos":
            diccionarioClasificador[i] = (j/totalVideoJuegos)*(totalVideoJuegos/Total)
        if i == "Ropa":
            diccionarioClasificador[i] = (j/totalRopa)*(totalRopa/Total)
        if i == "Lenguajes de Programacion":
            diccionarioClasificador[i] = (j/totalLenguajes)*(totalLenguajes/Total)
        if i == "Tecnologia":
            diccionarioClasificador[i] = (j/totalTecnologia)*(totalTecnologia/Total)
        if i == "Mobiliario":
            diccionarioClasificador[i] = (j/totalMobiliario)*(totalMobiliario/Total)
    for i, j in diccionarioClasificador.items():
        if resultados!={}:  
            for llave, value in resultados.items():
                if value < j:
                    if j > (value) :
                        resultados={}
                        resultados[i]=j
        else:
            resultados[i]=j

    for llave, value in resultados.items():
        if(value==0.0):
            resultados={}
        
    return resultados






opt = 0

if __name__ == '__main__':

    while(opt != 3):

      

        print('1. Multiproceso')
        print('2. Normal')
        print('3. Salir')
        opt = input('\nDigite una opcion: ')

        if(opt == '1'):
            with mp.Manager() as manager:
                urlPolitica=manager.list()  
                urlDeporte=manager.list()  
                urlVideoJuegos=manager.list()  
                urlRopa=manager.list()  
                urlLenguajeProgrmacion=manager.list()  
                urlMobiliario = manager.list()  
                urlTecnologia = manager.list()  
                x = manager.list()  
                x.append(urlPolitica)
                x.append(urlDeporte)
                x.append(urlVideoJuegos)
                x.append(urlRopa)
                x.append(urlLenguajeProgrmacion)
                x.append(urlMobiliario)
                x.append(urlTecnologia)

                pr1 = mp.Process(target=webScrapping, args=(linksProceso1,x))
                pr2 = mp.Process(target=webScrapping, args=(linksProceso2,x))
                pr3 = mp.Process(target=webScrapping, args=(linksProceso3,x))
                pr4 = mp.Process(target=webScrapping, args=(linksProceso4,x))
                
                start = time.time()

                pr1.start()
                pr2.start()
                pr3.start()
                pr4.start()

                pr1.join()
                pr2.join()
                pr3.join()
                pr4.join()

                end = time.time()

                urles=[]
                for a in x:
                    urles.append(list(a))

            os.system('cls')
            print("\t\t-------MULTIPROCESO-------")
            print('\nDuracion del proceso: ', end - start, 'segundos')
            print("Politica: {0}, Deporte: {1}, Video Juegos: {2}, Ropa: {3}, Lenguajes de progrmacion: {4}, Tecnología: {5}, Mobiliario: {6}".format(len(urles[0]),len(urles[1]),len(urles[2]),len(urles[3]),len(urles[4]),len(urles[5]),len(urles[6])))
            print("\nPOLITICA")
            for i in urles[0]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nDEPORTE")
            for i in urles[1]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nVIDEOJUEGOS")
            for i in urles[2]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nROPA")
            for i in urles[3]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nLENGUAJES DE PROGRAMACION")
            for i in urles[4]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)        
            print("\nTECNOLOGIA")
            for i in urles[5]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nMOBILIARIO")
            for i in urles[6]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            sinFuncionar = int(len(links)) - (int(len(urles[0])) + int(len(urles[1])) + int(len(urles[2])) + int(len(urles[3])) + int(len(urles[4])) + int(len(urles[5])) + int(len(urles[6])))
            resultadosEtiquetas = [len(urles[0]), len(urles[1]), len(urles[2]), len(urles[3]), len(urles[4]), len(urles[5]), len(urles[6]), sinFuncionar]
            plt.title("Porcentaje de links asignados a cada tematica")
            plt.pie(x=resultadosEtiquetas, labels = etiquetas, autopct=lambda p:f'{p:.2f}% ({p*sum(resultadosEtiquetas)/100 :.0f})')
            plt.axis('equal')
            circle = plt.Circle(xy=(0,0), radius =.75, facecolor = 'white')
            plt.gca().add_artist(circle)
            plt.show()

        elif(opt == '2'):

            start = time.time()
            urlPolitica=[]
            urlDeporte=[]
            urlVideoJuegos=[]
            urlRopa=[]
            urlLenguajeProgrmacion=[]
            urlMobiliario = []
            urlTecnologia = []

            urles = [urlPolitica,urlDeporte,urlVideoJuegos,urlRopa,urlLenguajeProgrmacion,urlMobiliario,urlTecnologia]

            webScrapping(links,urles)

            end = time.time()

            print('cls')
            print('\nDuracion del proceso: ', end - start, 'segundos')
            print("Politica: {0}, Deporte: {1}, Video Juegos: {2}, Ropa: {3}, Lenguajes de progrmacion: {4}, Tecnología: {5}, Mobiliario: {6}".format(len(urles[0]),len(urles[1]),len(urles[2]),len(urles[3]),len(urles[4]),len(urles[5]),len(urles[6])))
            print("\nPOLITICA")
            for i in urles[0]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nDEPORTE")
            for i in urles[1]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nVIDEOJUEGOS")
            for i in urles[2]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nROPA")
            for i in urles[3]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nLENGUAJES DE PROGRAMACION")
            for i in urles[4]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)        
            print("\nTECNOLOGIA")
            for i in urles[5]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            print("\nMOBILIARIO")
            for i in urles[6]:
                print("\nURL: ", i.link)
                print("Palabras Coincidentes: ")
                for j in i.palabras:
                    print("\t\t->", j)
            sinFuncionar = int(len(links)) - (int(len(urles[0])) + int(len(urles[1])) + int(len(urles[2])) + int(len(urles[3])) + int(len(urles[4])) + int(len(urles[5])) + int(len(urles[6])))
            resultadosEtiquetas = [len(urles[0]), len(urles[1]), len(urles[2]), len(urles[3]), len(urles[4]), len(urles[5]), len(urles[6]), sinFuncionar]
            plt.title("Porcentaje de links asignados a cada tematica")
            plt.pie(x=resultadosEtiquetas, labels = etiquetas, autopct=lambda p:f'{p:.2f}% ({p*sum(resultadosEtiquetas)/100 :.0f})')
            plt.axis('equal')
            circle = plt.Circle(xy=(0,0), radius =.75, facecolor = 'white')
            plt.gca().add_artist(circle)
            plt.show()

        elif(opt == '3'):
            break
        
        else:
            os.system('cls')