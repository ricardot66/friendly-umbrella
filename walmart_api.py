import requests
import csv
from scraper_api import ScraperAPIClient

client = ScraperAPIClient('c009f1737b5837fa675ade72875c175b')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
categories = ['https://www.walmart.com.mx/electrodomesticos/licuadoras-y-batidoras/licuadoras',
              'https://www.walmart.com.mx/electrodomesticos/licuadoras-y-batidoras/batidoras',
              'https://www.walmart.com.mx/electrodomesticos/licuadoras-y-batidoras/procesador-de-alimentos'
              'https://www.walmart.com.mx/electrodomesticos/cafeteras-y-extractores/cafeteras',
              'https://www.walmart.com.mx/electrodomesticos/cafeteras-y-extractores/extractores',
              'https://www.walmart.com.mx/electrodomesticos/cafeteras-y-extractores/teteras-y-hervidoras',
              'https://www.walmart.com.mx/electrodomesticos/electrodomesticos-especializados/postres-y-reposteria',
              'https://www.walmart.com.mx/electrodomesticos/electrodomesticos-especializados/utensilios-y-accesorios-electricos',
              'https://www.walmart.com.mx/electrodomesticos/destacados-electrodomesticos/electrodomesticos-destacados',
              'https://www.walmart.com.mx/electrodomesticos/hornos-electricos-y-sandwicheras/sandwicheras-y-waffleras',
              'https://www.walmart.com.mx/electrodomesticos/hornos-electricos-y-sandwicheras/tostadores',
              'https://www.walmart.com.mx/electrodomesticos/hornos-electricos-y-sandwicheras/hornos-electricos',
              'https://www.walmart.com.mx/electrodomesticos/purificadores-y-dispensadores-de-agua/purificador-de-agua',
              'https://www.walmart.com.mx/electrodomesticos/purificadores-y-dispensadores-de-agua/dispensador-de-agua',
              'https://www.walmart.com.mx/electrodomesticos/vaporeras-y-parrillas-electricas/parrilas-electricas-y-grill',
              'https://www.walmart.com.mx/electrodomesticos/vaporeras-y-parrillas-electricas/freidoras-y-sartenes-electricos',
              'https://www.walmart.com.mx/electrodomesticos/vaporeras-y-parrillas-electricas/vaporeras-y-arroceras',
              'https://www.walmart.com.mx/electrodomesticos/maquinas-de-coser-y-planchas-de-vapor/centrales-de-vapor',
              'https://www.walmart.com.mx/electrodomesticos/maquinas-de-coser-y-planchas-de-vapor/planchas-de-vapor',
              'https://www.walmart.com.mx/electrodomesticos/maquinas-de-coser-y-planchas-de-vapor/maquinas-de-coser',
              'https://www.walmart.com.mx/electrodomesticos/aspiradoras/aspiradoras',
              'https://www.walmart.com.mx/electrodomesticos/aspiradoras/limpiadores-de-vapor',
              # LINEA BLANCA
              'https://www.walmart.com.mx/linea-blanca/destacados-linea-blanca/linea-blanca-destacados',
              #Refrigeradores y Congeladores
              'https://www.walmart.com.mx/linea-blanca/refrigeradores-y-congeladores/frigobares',
              'https://www.walmart.com.mx/linea-blanca/refrigeradores-y-congeladores/refrigeradores',
              'https://www.walmart.com.mx/linea-blanca/refrigeradores-y-congeladores/congeladores',
              'https://www.walmart.com.mx/linea-blanca/refrigeradores-y-congeladores/cavas',
              # Lavadoras y Secadoras
              'https://www.walmart.com.mx/linea-blanca/lavadoras-y-secadoras/lavadoras',
              'https://www.walmart.com.mx/linea-blanca/lavadoras-y-secadoras/secadoras',
              'https://www.walmart.com.mx/linea-blanca/lavadoras-y-secadoras/centros-de-lavado',
              'https://www.walmart.com.mx/linea-blanca/lavadoras-y-secadoras/lavasecadora'
              # Estufas y Hornos
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/microondas',
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/estufas',
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/campanas',
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/parrillas',
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/hornos-empotrables',
              'https://www.walmart.com.mx/linea-blanca/estufas-y-hornos/lavavajillas'
              # Aire acondicionado y Calentadores
              'https://www.walmart.com.mx/linea-blanca/aire-acondicionado-y-calentadores/calefactores',
              'https://www.walmart.com.mx/linea-blanca/aire-acondicionado-y-calentadores/ventiladores',
              'https://www.walmart.com.mx/linea-blanca/aire-acondicionado-y-calentadores/aire-acondicionado',
              'https://www.walmart.com.mx/linea-blanca/aire-acondicionado-y-calentadores/calentadores-de-agua',

              #CELULARES
              'https://www.walmart.com.mx/celulares/destacados-celulares/destacados-celulares',
              # Smartphones
              'https://www.walmart.com.mx/celulares/smartphones/celulares-desbloqueados',
              'https://www.walmart.com.mx/celulares/smartphones/at-t',
              'https://www.walmart.com.mx/celulares/smartphones/movistar',
              'https://www.walmart.com.mx/celulares/smartphones/telcel',
              # Accesorios Celulares
              'https://www.walmart.com.mx/celulares/accesorios-celulares/accesorios-smartphones',
              'https://www.walmart.com.mx/celulares/accesorios-celulares/memorias-para-celular',
              'https://www.walmart.com.mx/celulares/accesorios-celulares/micas-para-pantalla',
              # Telefonia Fija
              'https://www.walmart.com.mx/celulares/telefonia-fija/telefonos-alambricos',
              'https://www.walmart.com.mx/celulares/telefonia-fija/telefonos-inalambricos',
              # Smartwatch y Wearables
              'https://www.walmart.com.mx/celulares/smartwatch-y-wearables/smartwatch',
              'https://www.walmart.com.mx/celulares/smartwatch-y-wearables/wearables',
              # Fundas Micas y Accesorios
              'https://www.walmart.com.mx/celulares/fundas-micas-y-accesorios/otros-accesorios-para-celular',
              'https://www.walmart.com.mx/celulares/fundas-micas-y-accesorios/fundas-para-celulares',
              'https://www.walmart.com.mx/celulares/fundas-micas-y-accesorios/protectores-micas-y-soportes',
              # Cargadores y Baterias Portatiles
              'https://www.walmart.com.mx/celulares/cargadores-y-baterias-portatiles/cargadores-portatiles',
              'https://www.walmart.com.mx/celulares/cargadores-y-baterias-portatiles/baterias-internas',
              'https://www.walmart.com.mx/celulares/cargadores-y-baterias-portatiles/cables-y-cargadores',

              #FOTOGRAFIA
              'https://www.walmart.com.mx/fotografia/destacados-fotografia/destacados-fotografia',
              # Cámaras
              'https://www.walmart.com.mx/fotografia/camaras/camaras-acuaticas',
              'https://www.walmart.com.mx/fotografia/camaras/camaras-instantaneas',
              'https://www.walmart.com.mx/fotografia/camaras/camaras-digitales',
              'https://www.walmart.com.mx/fotografia/camaras/camaras-reflex',
              'https://www.walmart.com.mx/fotografia/camaras/camaras-deportivas',
              'https://www.walmart.com.mx/fotografia/camaras/camaras-profesionales',
              # Cámaras de Video
              'https://www.walmart.com.mx/fotografia/camaras-de-video/videocamaras-deportivas',
              'https://www.walmart.com.mx/fotografia/camaras-de-video/videocamaras-digitales',
              'https://www.walmart.com.mx/fotografia/camaras-de-video/videocamaras-profesionales',
              # Accesorios para Cámaras
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/estuches-maletines-y-limpieza',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/tripies-y-estabilizadores',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/lentes',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/flash-e-iluminacion',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/microfonos-para-camara',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/filtros-y-accesorios-para-estudio',
              'https://www.walmart.com.mx/fotografia/accesorios-para-camaras/accesorios-camaras-deportivas',
              # Drones
              'https://www.walmart.com.mx/fotografia/drones/modelismo-naval',
              'https://www.walmart.com.mx/fotografia/drones/drones',
              'https://www.walmart.com.mx/fotografia/drones/controles-helices-y-soportes',
              'https://www.walmart.com.mx/fotografia/drones/automodelismo',
              # Memorias Baterias y Cargadores
              'https://www.walmart.com.mx/fotografia/memorias-baterias-y-cargadores/monitores-cables-y-otros',
              'https://www.walmart.com.mx/fotografia/memorias-baterias-y-cargadores/baterias-y-cargadores',
              'https://www.walmart.com.mx/fotografia/memorias-baterias-y-cargadores/memorias-micro-sd',
              'https://www.walmart.com.mx/fotografia/memorias-baterias-y-cargadores/memorias-sd',
              # Lentes
              'https://www.walmart.com.mx/lp-fotografia/marcas-lentes',

              # TV Y VIDEO
              'https://www.walmart.com.mx/tv-y-video/destacados-tv-y-video',
              # Pantallas
              'https://www.walmart.com.mx/tv-y-video/pantallas/65-o-mas-pulgadas',
              'https://www.walmart.com.mx/tv-y-video/pantallas/55-a-64-pulgadas',
              'https://www.walmart.com.mx/tv-y-video/pantallas/47-a-54-pulgadas',
              'https://www.walmart.com.mx/tv-y-video/pantallas/37-a-46-pulgadas',
              'https://www.walmart.com.mx/tv-y-video/pantallas/28-a-36-pulgadas',
              'https://www.walmart.com.mx/tv-y-video/pantallas/27-pulgadas-o-menos',
              'https://www.walmart.com.mx/tv-y-video/pantallas/4k-ultra-hd',
              'https://www.walmart.com.mx/tv-y-video/pantallas/smart-tv',
              'https://www.walmart.com.mx/tv-y-video/pantallas/tv-digital'
              'https://www.walmart.com.mx/tv-y-video/pantallas/todas',
              # DVD Y BluRay
              'https://www.walmart.com.mx/tv-y-video/dvd-y-bluray/dvd',
              'https://www.walmart.com.mx/tv-y-video/dvd-y-bluray/bluray'
              # Audio para TV
              'https://www.walmart.com.mx/tv-y-video/audio-para-tv/barras-de-sonido',
              'https://www.walmart.com.mx/tv-y-video/audio-para-tv/teatros-en-casa',
              # Muebles y Soportes para TV
              'https://www.walmart.com.mx/tv-y-video/muebles-y-soportes-para-tv/soportes',
              'https://www.walmart.com.mx/tv-y-video/muebles-y-soportes-para-tv/centros-de-entretenimiento',
              # Accesorios TV y Video
              'https://www.walmart.com.mx/tv-y-video/accesorios-tv-y-video/cables',
              'https://www.walmart.com.mx/tv-y-video/accesorios-tv-y-video/control-remoto',
              'https://www.walmart.com.mx/tv-y-video/accesorios-tv-y-video/antenas',
              'https://www.walmart.com.mx/tv-y-video/accesorios-tv-y-video/soportes',

              # AUDIO
              'https://www.walmart.com.mx/audio/destacados-audio',
              # Bocinas y Bafles
              'https://www.walmart.com.mx/audio/bocinas-y-bafles/bocinas-portatiles',
              'https://www.walmart.com.mx/audio/bocinas-y-bafles/bafles',
              'https://www.walmart.com.mx/audio/bocinas-y-bafles/bocinas-para-exterior',
              'https://www.walmart.com.mx/audio/bocinas-y-bafles/bocinas',
              # Barras de Sonido y Teatros en Casa
              'https://www.walmart.com.mx/audio/barras-de-sonido-y-teatros-en-casa/teatros-en-casa',
              'https://www.walmart.com.mx/audio/barras-de-sonido-y-teatros-en-casa/barras-de-sonido',
              'https://www.walmart.com.mx/audio/barras-de-sonido-y-teatros-en-casa/accesorios-de-audio',
              'https://www.walmart.com.mx/audio/barras-de-sonido-y-teatros-en-casa/receptores'
              # Audio para Autos
              'https://www.walmart.com.mx/audio/audio-para-autos/autoestereos'
              'https://www.walmart.com.mx/audio/audio-para-autos/subwoofers-para-autos'
              'https://www.walmart.com.mx/audio/audio-para-autos/amplificadores-y-fuentes-de-poder'
              'https://www.walmart.com.mx/audio/audio-para-autos/ecualizadores-y-accesorios',
              'https://www.walmart.com.mx/audio/audio-para-autos/bocinas-para-autos-y-set-de-medios',
              'https://www.walmart.com.mx/audio/audio-para-autos/gps-y-dispositivos-electronicos',
              # Audífonos
              'https://www.walmart.com.mx/audio/audifonos/audifonos-dj',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-in-ear',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-diadema',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-in-ear-bluetooth',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-diadema-bluetooth',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-deportivos-bluetooth',
              'https://www.walmart.com.mx/audio/audifonos/audifonos-deportivos'
              # Minicomponentes y Grabadoras
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/bafles',
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/radiograbadoras-y-radiorelojes',
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/micro-y-minicomponentes',
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/grabadoras-de-voz',
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/microfonos',
              'https://www.walmart.com.mx/audio/minicomponentes-y-grabadoras/karaoke',
              # DJ
              'https://www.walmart.com.mx/audio/dj/controladores-y-mixers',
              'https://www.walmart.com.mx/audio/dj/tornamesas-y-cd-players',
              'https://www.walmart.com.mx/audio/dj/bocinas-y-monitores'
              'https://www.walmart.com.mx/audio/dj/luces-de-discoteca',
              # Reproductores MP3 y Ipod
              'https://www.walmart.com.mx/audio/reproductores-mp3-y-ipod/accesorios-ipod-y-mp3',
              'https://www.walmart.com.mx/audio/reproductores-mp3-y-ipod/mp3-y-ipod',

              # INSTRUMENTOS MUSICALES
              'https://www.walmart.com.mx/instrumentos-musicales/destacados-instrumentos',
              # Cuerdas
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/guitarras-acusticas',
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/guitarras-electroacusticas',
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/bajos',
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/afinadores-cuerdas-y-mas',
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/violines-ukuleles-y-mas',
              'https://www.walmart.com.mx/instrumentos-musicales/cuerdas/guitarras-electricas',
              # Teclados
              'https://www.walmart.com.mx/instrumentos-musicales/teclados/teclados',
              'https://www.walmart.com.mx/instrumentos-musicales/teclados/pianos',
              'https://www.walmart.com.mx/instrumentos-musicales/teclados/bancos-fundas-y-mas',
              # Percusión
              'https://www.walmart.com.mx/instrumentos-musicales/percusion/baterias',
              'https://www.walmart.com.mx/instrumentos-musicales/percusion/tambores-percusiones-y-mas',
              'https://www.walmart.com.mx/instrumentos-musicales/percusion/platillos-baquetas-y-mas',
              # Viento y Acordeones
              'https://www.walmart.com.mx/instrumentos-musicales/viento-y-acordeones/acordeones-y-armonicas',
              'https://www.walmart.com.mx/instrumentos-musicales/viento-y-acordeones/saxofones-trompetas-y-mas',
              'https://www.walmart.com.mx/instrumentos-musicales/viento-y-acordeones/boquillas-canas-y-mas',
              # Amplificadores y Microfonos
              'https://www.walmart.com.mx/instrumentos-musicales/amplificadores-y-microfonos/atriles-cables-y-mas',
              'https://www.walmart.com.mx/instrumentos-musicales/amplificadores-y-microfonos/amplificadores',
              'https://www.walmart.com.mx/instrumentos-musicales/amplificadores-y-microfonos/microfonos',
              # DJ
              'https://www.walmart.com.mx/instrumentos-musicales/dj/controladores-y-mixers',
              'https://www.walmart.com.mx/instrumentos-musicales/dj/tornamesas-y-cd-players',
              'https://www.walmart.com.mx/instrumentos-musicales/dj/bocinas-y-monitores',
              'https://www.walmart.com.mx/instrumentos-musicales/dj/luces-de-discoteca',
              'https://www.walmart.com.mx/instrumentos-musicales/dj/software-y-accesorios',
              'https://www.walmart.com.mx/instrumentos-musicales/dj/audifonos-dj',

              # COMPUTADORAS
              'https://www.walmart.com.mx/computadoras/destacados-computadoras/destacados-computadoras',
              # Laptops
              'https://www.walmart.com.mx/computadoras/laptops/todas-las-laptops',
              'https://www.walmart.com.mx/computadoras/laptops/macbooks',
              'https://www.walmart.com.mx/computadoras/laptops/chromebooks',
              'https://www.walmart.com.mx/computadoras/laptops/notebooks',
              'https://www.walmart.com.mx/computadoras/laptops/ultrabooks',
              'https://www.walmart.com.mx/computadoras/laptops/2-en-1-y-touchscreen',
              # Computadoras de Escritorio
              'https://www.walmart.com.mx/computadoras/computadoras-de-escritorio/todas-las-computadoras-de-escritorio',
              'https://www.walmart.com.mx/computadoras/computadoras-de-escritorio/all-in-one',
              'https://www.walmart.com.mx/computadoras/computadoras-de-escritorio/desktops',
              'https://www.walmart.com.mx/computadoras/computadoras-de-escritorio/cpu',
              # Tablets
              'https://www.walmart.com.mx/computadoras/tablets/todas-las-tablets',
              'https://www.walmart.com.mx/computadoras/tablets/ipad',
              'https://www.walmart.com.mx/computadoras/tablets/tablets-android',
              'https://www.walmart.com.mx/computadoras/tablets/accesorios-para-tablets',
              # PC Gamer
              'https://www.walmart.com.mx/computadoras/pc-gamer/laptops-y-pc-gamer',
              'https://www.walmart.com.mx/computadoras/pc-gamer/juegos-para-pc',
              'https://www.walmart.com.mx/computadoras/pc-gamer/accesorios-gamer',
              # Impresoras y Scanners
              'https://www.walmart.com.mx/computadoras/impresoras-y-scanners/cartuchos',
              'https://www.walmart.com.mx/computadoras/impresoras-y-scanners/multifuncionales',
              'https://www.walmart.com.mx/computadoras/impresoras-y-scanners/scanner',
              'https://www.walmart.com.mx/computadoras/impresoras-y-scanners/impresoras',
              'https://www.walmart.com.mx/computadoras/impresoras-y-scanners/plotter',
              # Proyectores y Monitores
              'https://www.walmart.com.mx/computadoras/proyectores-y-monitores/proyectores',
              'https://www.walmart.com.mx/computadoras/proyectores-y-monitores/lamparas-pantallas-y-accesorios',
              'https://www.walmart.com.mx/computadoras/proyectores-y-monitores/monitores',
              # Accesorios para Computadoras
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/memorias-usb-y-sd',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/mouse-teclados-y-webcams',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/bocinas-audifonos-y-microfonos',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/otros-accesorios-pc',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/fundas-y-maletines',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/reguladores-y-no-breaks',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/discos-duros',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/cargadores-y-baterias-portatiles',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/mochilas-para-laptops',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/cables-y-adaptadores',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/accesorios-mac',
              'https://www.walmart.com.mx/computadoras/accesorios-para-computadoras/accesorios-de-red',
              # Software
              'https://www.walmart.com.mx/computadoras/software/antivirus',
              'https://www.walmart.com.mx/computadoras/software/office',
              'https://www.walmart.com.mx/computadoras/software/productividad',
              # Componentes de Computadoras
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/tarjetas-de-video',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/servidores',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/hub',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/routers',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/enfriadores-y-ventiladores',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/fuentes-de-poder',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/lectores-de-cd-y-dvd',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/memoria-ram',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/modems',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/procesadores',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/tarjetas-de-sonido',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/tarjetas-madre',
              'https://www.walmart.com.mx/computadoras/componentes-de-computadoras/torres-y-gabinetes-de-pc',
              # OFICINA Y PAPELERIA
              'https://www.walmart.com.mx/oficina-y-papeleria/destacados-oficina-y-papeleria/destacados-oficina-y-papeleria',
              # Papeleria
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/mochilas-loncheras-y-lapiceras',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/calculadoras',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/papel',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/libretas-y-agendas',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/papeleria-basica',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/escritura',
              'https://www.walmart.com.mx/oficina-y-papeleria/papeleria/pizarrones-rotafolios-y-tripies',
              # Oficina y Negocio
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/mochilas-y-maletines',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/negocio-y-punto-de-venta',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/enmicadoras-trituradoras-y-mas',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/seguridad',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/archiveros',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/organizacion-y-articulos-de-oficina',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/plumas-fuente',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/libretas-y-agendas',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/mantenimiento-y-senalizacion',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/embalaje',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/escritorios',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/sillas-de-oficina',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/multifuncionales',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/todas-las-laptops',
              'https://www.walmart.com.mx/oficina-y-papeleria/oficina-y-negocio/impresoras',
              # Arte y Diseño
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/estuches-de-arte',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/pinturas-y-pinceles',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/colores-y-plumines',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/estilografos',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/caballetes-y-bastidores',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/blocks-y-papel',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/corte',
              'https://www.walmart.com.mx/oficina-y-papeleria/arte-y-diseno/manualidades-para-ninos',
              # Artículos de Fiesta y Disfraces
              'https://www.walmart.com.mx/oficina-y-papeleria/articulos-de-fiesta-y-disfraces/fiesta-y-decoracion',
              'https://www.walmart.com.mx/oficina-y-papeleria/articulos-de-fiesta-y-disfraces/disfraces-para-adulto',
              'https://www.walmart.com.mx/oficina-y-papeleria/articulos-de-fiesta-y-disfraces/disfraces-para-nino',
              'https://www.walmart.com.mx/oficina-y-papeleria/articulos-de-fiesta-y-disfraces/mascaras',
              'https://www.walmart.com.mx/oficina-y-papeleria/articulos-de-fiesta-y-disfraces/accesorios-para-disfraces',
              # Videojuegos
              'https://www.walmart.com.mx/videojuegos/destacados-videojuegos/destacados-videojuegos',
              # Xbox One
              'https://www.walmart.com.mx/videojuegos/xbox-one/consolas',
              'https://www.walmart.com.mx/videojuegos/xbox-one/juegos',
              'https://www.walmart.com.mx/videojuegos/xbox-one/accesorios',
              'https://www.walmart.com.mx/videojuegos/xbox-one/juegos-digitales',
              # PlayStation 4
              'https://www.walmart.com.mx/videojuegos/playstation-4/consolas-consola-ps4',
              'https://www.walmart.com.mx/videojuegos/playstation-4/accesorios',
              'https://www.walmart.com.mx/videojuegos/playstation-4/playstation-vr',
              'https://www.walmart.com.mx/videojuegos/playstation-4/juegos-ps4'
              # Nintendo Switch
              'https://www.walmart.com.mx/videojuegos/nintendo-switch/accesorios',
              'https://www.walmart.com.mx/videojuegos/nintendo-switch/consolas'
              'https://www.walmart.com.mx/videojuegos/nintendo-switch/juegos',
              'https://www.walmart.com.mx/videojuegos/nintendo-switch/juegos-digitales',
              # Lanzamientos y Preventas
              'https://www.walmart.com.mx/videojuegos/lanzamientos-y-preventas/lanzamientos',
              # Coleccionables y Retro Games
              'https://www.walmart.com.mx/videojuegos/coleccionables-y-retro-games/amiibo',
              'https://www.walmart.com.mx/videojuegos/coleccionables-y-retro-games/consolas-retro',
              'https://www.walmart.com.mx/videojuegos/coleccionables-y-retro-games/figuras-interactivas',
              'https://www.walmart.com.mx/videojuegos/coleccionables-y-retro-games/tarjetas-de-coleccion',
              'https://www.walmart.com.mx/videojuegos/coleccionables-y-retro-games/articulos-de-coleccion',
              # Xbox 360
              'https://www.walmart.com.mx/videojuegos/xbox-360/juegos',
              'https://www.walmart.com.mx/videojuegos/xbox-360/accesorios',
              # PlayStation 3
              'https://www.walmart.com.mx/videojuegos/playstation-3/juegos',
              'https://www.walmart.com.mx/videojuegos/playstation-3/accesorios'
              # PC Gamer
              'https://www.walmart.com.mx/videojuegos/pc-gamer/laptops-y-pc-gamer',
              'https://www.walmart.com.mx/videojuegos/pc-gamer/juegos-para-pc',
              'https://www.walmart.com.mx/videojuegos/pc-gamer/accesorios-gamer',
              # Nintendo
              'https://www.walmart.com.mx/videojuegos/nintendo/accesorios',
              'https://www.walmart.com.mx/videojuegos/nintendo/juegos-wii-u',
              'https://www.walmart.com.mx/videojuegos/nintendo/juegos-3ds',
              'https://www.walmart.com.mx/videojuegos/nintendo/juegos',

              # JUGUETES
              'https://www.walmart.com.mx/juguetes/destacados-juguetes/destacados-juguetes',
              # Muñecas y Peluches
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/munecas-bebe',
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/munecas-de-moda',
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/accesorios-para-munecas',
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/peluches',
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/animalitos-y-ponys',
              'https://www.walmart.com.mx/juguetes/munecas-y-peluches/munecas-de-porcelana',
              # Montables
              'https://www.walmart.com.mx/juguetes/montables/correpasillos',
              'https://www.walmart.com.mx/juguetes/montables/montables-electricos',
              # Figuras de Acción y Coleccionables
              'https://www.walmart.com.mx/juguetes/figuras-de-accion-y-coleccionables/figuras-de-accion',
              'https://www.walmart.com.mx/juguetes/figuras-de-accion-y-coleccionables/funko',
              'https://www.walmart.com.mx/juguetes/figuras-de-accion-y-coleccionables/juguetes-de-coleccion',
              # Casitas y Juegos de Jardín
              'https://www.walmart.com.mx/juguetes/casitas-y-juegos-de-jardin/casitas-y-cocinas-para-ninos',
              'https://www.walmart.com.mx/juguetes/casitas-y-juegos-de-jardin/juegos-al-aire-libre',
              'https://www.walmart.com.mx/juguetes/casitas-y-juegos-de-jardin/alberca-y-juguetes-acuaticos',
              # Juegos de Construcción
              'https://www.walmart.com.mx/juguetes/juegos-de-construccion/mas-bloques-de-construccion',
              'https://www.walmart.com.mx/juguetes/juegos-de-construccion/lego',
              'https://www.walmart.com.mx/juguetes/juegos-de-construccion/megablocks',
              'https://www.walmart.com.mx/juguetes/juegos-de-construccion/playmobil',
              # Bicicletas, Patines y Scooters
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/bicicletas',
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/patinetas-de-balance-y-triciclos',
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/patines-y-patinetas',
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/scooters',
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/bicicletas-de-montana',
              'https://www.walmart.com.mx/juguetes/bicicletas-patines-y-scooters/bicicletas-urbanas',
              # Juegos de Mesa
              'https://www.walmart.com.mx/juguetes/juegos-de-mesa/juegos-de-mesa',
              'https://www.walmart.com.mx/juguetes/juegos-de-mesa/rompecabezas',
              # Juguetes Preescolar
              'https://www.walmart.com.mx/juguetes/juguetes-preescolar/juguetes-de-bebe',
              'https://www.walmart.com.mx/juguetes/juguetes-preescolar/preescolar',
              # Manualidades y Juguetes Didácticos
              'https://www.walmart.com.mx/juguetes/manualidades-y-juguetes-didacticos/juegos-de-dibujo-y-manualidades',
              'https://www.walmart.com.mx/juguetes/manualidades-y-juguetes-didacticos/modelado-y-plastilina',
              'https://www.walmart.com.mx/juguetes/manualidades-y-juguetes-didacticos/pizarrones-y-mesas-de-dibujo',
              'https://www.walmart.com.mx/juguetes/manualidades-y-juguetes-didacticos/juguetes-didacticos-y-escolares',
              # Lanzadores
              'https://www.walmart.com.mx/juguetes/lanzadores/lanzadores-de-agua',
              'https://www.walmart.com.mx/juguetes/lanzadores/lanzadores',
              # Carritos y Radiocontrol
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/autos-de-control-remoto',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/carritos',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/pistas',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/autos-de-coleccion',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/aviones-y-helicopteros-de-control-remoto',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/barcos-y-lanchas-de-control-remoto',
              'https://www.walmart.com.mx/juguetes/carritos-y-radiocontrol/trenes-de-control-remoto'
              # Mascotas y Juguetes Electrónicos
              'https://www.walmart.com.mx/juguetes/mascotas-y-juguetes-electronicos/juguetes-electronicos',
              'https://www.walmart.com.mx/juguetes/mascotas-y-juguetes-electronicos/mascotas-electronicos',
              'https://www.walmart.com.mx/juguetes/mascotas-y-juguetes-electronicos/juguetes-interactivos',
              # Drones
              'https://www.walmart.com.mx/juguetes/drones/drones',
              'https://www.walmart.com.mx/juguetes/drones/accesorios-para-drones',

              # DEPORTES
              'https://www.walmart.com.mx/deportes/destacados-deportes/deportes-destacados',
              # Juegos Recreativos
              'https://www.walmart.com.mx/deportes/juegos-recreativos/trampolines-y-bouncers',
              'https://www.walmart.com.mx/deportes/juegos-recreativos/mesas-de-juego',
              'https://www.walmart.com.mx/deportes/juegos-recreativos/scooters',
              # Entrenamiento y Fitness
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/elipticas-y-escaladoras',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/bicicletas-fijas',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/gimnasios-y-aparatos-de-ejercicio',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/mancuernas-pesas-y-barras',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/yoga-y-pilates',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/crossfit',
              'https://www.walmart.com.mx/deportes/entrenamiento-y-fitness/monitores-cardiacos',
              # Ciclismo
              'https://www.walmart.com.mx/deportes/ciclismo/bicicletas',
              'https://www.walmart.com.mx/deportes/ciclismo/bicicletas-electricas',
              'https://www.walmart.com.mx/deportes/ciclismo/bicicletas-de-montana',
              'https://www.walmart.com.mx/deportes/ciclismo/accesorios-y-refacciones',
              'https://www.walmart.com.mx/deportes/ciclismo/bicicletas-urbanas',
              'https://www.walmart.com.mx/deportes/ciclismo/bicicletas-de-ruta',
              'https://www.walmart.com.mx/deportes/ciclismo/cascos-y-proteccion',
              # Camping
              'https://www.walmart.com.mx/deportes/camping/casas-de-campana',
              'https://www.walmart.com.mx/deportes/camping/sleeping-bags',
              'https://www.walmart.com.mx/deportes/camping/colchones-inflables',
              'https://www.walmart.com.mx/deportes/camping/mochilas-de-camping',
              'https://www.walmart.com.mx/deportes/camping/kits-de-supervivencia-y-accesorios',
              'https://www.walmart.com.mx/deportes/camping/muebles-de-campismo',
              'https://www.walmart.com.mx/deportes/camping/hieleras-y-termos',
              # Deportes Acuáticos
              'https://www.walmart.com.mx/deportes/deportes-acuaticos/accesorios-deportes-acuaticos',
              'https://www.walmart.com.mx/deportes/deportes-acuaticos/natacion',
              'https://www.walmart.com.mx/deportes/deportes-acuaticos/albercas-e-inflables',
              'https://www.walmart.com.mx/deportes/deportes-acuaticos/kayac-y-canotaje',
              # Deportes en Equipo
              'https://www.walmart.com.mx/deportes/deportes-en-equipo/futbol-soccer',
              'https://www.walmart.com.mx/deportes/deportes-en-equipo/basquetbol',
              'https://www.walmart.com.mx/deportes/deportes-en-equipo/futbol-americano',
              'https://www.walmart.com.mx/deportes/deportes-en-equipo/voleibol',
              'https://www.walmart.com.mx/deportes/deportes-en-equipo/baseball',
              # Deportes Individuales y de Contacto
              'https://www.walmart.com.mx/deportes/deportes-individuales-y-de-contacto/tenis',
              'https://www.walmart.com.mx/deportes/deportes-individuales-y-de-contacto/squash-badminton-y-padel',
              'https://www.walmart.com.mx/deportes/deportes-individuales-y-de-contacto/box',
              'https://www.walmart.com.mx/deportes/deportes-individuales-y-de-contacto/artes-marciales',
              'https://www.walmart.com.mx/deportes/deportes-individuales-y-de-contacto/skate-y-patines',
              # Accesorios Deportivos
              'https://www.walmart.com.mx/deportes/accesorios-deportivos/guantes-y-accesorios',
              'https://www.walmart.com.mx/deportes/accesorios-deportivos/ligas-y-cuerdas-para-saltar',
              'https://www.walmart.com.mx/deportes/accesorios-deportivos/hidratacion-deportiva',
              'https://www.walmart.com.mx/deportes/accesorios-deportivos/mochilas-y-maletas-deportivas',
              # Bicicletas, Patines y Scooters
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/bicicletas',
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/patinetas-de-balance-y-triciclos',
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/patines-y-patinetas',
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/scooters',
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/bicicletas-de-montana',
              'https://www.walmart.com.mx/deportes/bicicletas-patines-y-scooters/bicicletas-urbanas'
              # Motos
              'https://www.walmart.com.mx/deportes/motos/destacados-motos',
              'https://www.walmart.com.mx/deportes/motos/motos-de-trabajo',
              'https://www.walmart.com.mx/deportes/motos/motonetas-y-scooters',
              'https://www.walmart.com.mx/deportes/motos/motos-doble-proposito',
              'https://www.walmart.com.mx/deportes/motos/motos-para-ciudad',
              'https://www.walmart.com.mx/deportes/motos/cuatrimotos',
              'https://www.walmart.com.mx/deportes/motos/motos-deportivas',
              'https://www.walmart.com.mx/deportes/motos/chopper',
              'https://www.walmart.com.mx/deportes/motos/cascos-guantes-y-ropa',
              # Fan Shop
              'https://www.walmart.com.mx/deportes/fan-shop/fan-shop-soccer',
              # Nutrición y Medicina Deportiva
              'https://www.walmart.com.mx/deportes/nutricion-y-medicina-deportiva/vitaminas',
              'https://www.walmart.com.mx/deportes/nutricion-y-medicina-deportiva/cintas-kinesiologicas-y-soportes',
              'https://www.walmart.com.mx/deportes/nutricion-y-medicina-deportiva/proteinas-y-suplementos',
              # Ropa y Calzado Deportivo
              'https://www.walmart.com.mx/deportes/ropa-y-calzado-deportivo/licras-y-mallas',
              'https://www.walmart.com.mx/deportes/ropa-y-calzado-deportivo/playeras-y-tops-deportivos',
              'https://www.walmart.com.mx/deportes/ropa-y-calzado-deportivo/ropa-interior-deportiva',
              'https://www.walmart.com.mx/deportes/ropa-y-calzado-deportivo/sudaderas-y-chamarras',
              # Ropa Deportiva Hombre
              'https://www.walmart.com.mx/deportes/ropa-deportiva-hombre/polos-y-playeras-deportivas',

              # AUTOS Y LLANTAS
              'https://www.walmart.com.mx/autos-y-llantas/destacados-autos/destacados-autos',
              # Llantas y Rines
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-para-moto',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-13',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-14',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-15',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-16',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-17',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-18',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-19',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-20',
              'https://www.walmart.com.mx/autos-y-llantas/llantas-y-rines/llantas-rin-21'
              # Limpieza y Estética Automotriz
              'https://www.walmart.com.mx/autos-y-llantas/limpieza-y-estetica-automotriz/accesorios-de-limpieza',
              'https://www.walmart.com.mx/autos-y-llantas/limpieza-y-estetica-automotriz/aspiradoras-para-auto',
              'https://www.walmart.com.mx/autos-y-llantas/limpieza-y-estetica-automotriz/pulido-limpieza-y-cuidado',
              'https://www.walmart.com.mx/autos-y-llantas/limpieza-y-estetica-automotriz/hidrolavadoras',
              # Accesorios para Moto
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-para-moto/llantas-para-motocicleta',
              # Accesorios y Herramientas
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/gps-y-dispositivos-electronicos',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/accesorios-interiores',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/accesorios-exteriores',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/limpiaparabrisas-y-antenas',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/portaequipaje-carga-y-racks',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/alarmas-y-seguridad',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/herramientas-electricas',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/herramientas-manuales',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/dados-y-llaves',
              'https://www.walmart.com.mx/autos-y-llantas/accesorios-y-herramientas/accesorios-para-moto'
              # Refacciones y Autopartes
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/baterias-para-auto-y-moto',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/aire-acondicionado-y-ventilacion',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/espejos-retrovisores',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/parrillas-y-defensas',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/salpicaderas-y-tolvas',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/radiadores-y-marcos',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/piezas-de-motor',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/amortiguadores-y-suspension',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/tuning',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/frenos',
              'https://www.walmart.com.mx/autos-y-llantas/refacciones-y-autopartes/puertas-y-manijas'
              # Iluminación Automotriz
              'https://www.walmart.com.mx/autos-y-llantas/iluminacion-automotriz/calaveras',
              'https://www.walmart.com.mx/autos-y-llantas/iluminacion-automotriz/cuartos',
              'https://www.walmart.com.mx/autos-y-llantas/iluminacion-automotriz/faros',
              # Aceites, Lubricantes y Aditivos
              'https://www.walmart.com.mx/autos-y-llantas/aceites-lubricantes-y-aditivos/aditivos-y-lubricantes'
              'https://www.walmart.com.mx/autos-y-llantas/aceites-lubricantes-y-aditivos/filtros-y-accesorios',
              'https://www.walmart.com.mx/autos-y-llantas/aceites-lubricantes-y-aditivos/anticongelantes',
              'https://www.walmart.com.mx/autos-y-llantas/aceites-lubricantes-y-aditivos/aceites-para-motor',
              # Audio para Autos
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/autoestereos',
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/subwoofers-para-autos',
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/amplificadores-y-fuentes-de-poder',
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/ecualizadores-y-accesorios',
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/bocinas-para-autos-y-set-de-medios',
              'https://www.walmart.com.mx/autos-y-llantas/audio-para-autos/gps-y-dispositivos-electronicos'
              # Motos
              'https://www.walmart.com.mx/autos-y-llantas/motos/destacados-motos',
              'https://www.walmart.com.mx/autos-y-llantas/motos/motos-de-trabajo',
              'https://www.walmart.com.mx/autos-y-llantas/motos/motonetas-y-scooters',
              'https://www.walmart.com.mx/autos-y-llantas/motos/motos-doble-proposito',
              'https://www.walmart.com.mx/autos-y-llantas/motos/motos-para-ciudad',
              'https://www.walmart.com.mx/autos-y-llantas/motos/cuatrimotos',
              'https://www.walmart.com.mx/autos-y-llantas/motos/motos-deportivas',
              'https://www.walmart.com.mx/autos-y-llantas/motos/chopper',
              'https://www.walmart.com.mx/autos-y-llantas/motos/cascos-guantes-y-ropa',

              # COLCHONES Y BLANCOS
              'https://www.walmart.com.mx/colchones-y-blancos/destacados-colchones-y-blancos/destacados-colchones-y-blancos',
              # Colchones
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/matrimoniales',
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/individuales',
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/queen-size',
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/king-size',
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/bases-para-cama-y-box',
              'https://www.walmart.com.mx/colchones-y-blancos/colchones/colchones-de-cuna',
              # Blancos
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/colchas-edredones-y-coordinados',
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/almohadas-y-cojines',
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/sabanas',
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/cubre-colchon-y-colchonetas',
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/cobertores-y-cobijas',
              'https://www.walmart.com.mx/colchones-y-blancos/blancos/toallas-y-batas',

              # MUEBLES
              'https://www.walmart.com.mx/muebles/destacados-muebles/muebles-destacados',
              # Salas y centros de entretenimiento
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/salas',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/centros-de-entretenimiento',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/sofa-cama',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/sillones-y-reclinables',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/libreros',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/mesas-y-espejos',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/bancas-y-baules',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/puffs',
              'https://www.walmart.com.mx/muebles/salas-y-centros-de-entretenimiento/muebles-para-bar',
              # Comedores y Muebles de Cocina
              'https://www.walmart.com.mx/muebles/comedores-y-muebles-de-cocina/cocinas-integrales',
              'https://www.walmart.com.mx/muebles/comedores-y-muebles-de-cocina/comedores',
              'https://www.walmart.com.mx/muebles/comedores-y-muebles-de-cocina/gabinetes-alacenas-y-estantes',
              'https://www.walmart.com.mx/muebles/comedores-y-muebles-de-cocina/mesas',
              'https://www.walmart.com.mx/muebles/comedores-y-muebles-de-cocina/sillas',
              # Recámaras y Clósets
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/recamaras',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/literas',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/closets-y-armarios',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/cajoneras-y-espejos',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/buros'
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/cabeceras'
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/bases-para-cama-y-box',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/tocadores-y-mesas-de-noche',
              'https://www.walmart.com.mx/muebles/recamaras-y-closets/bancas-y-baules',
              # Muebles Infantiles
              'https://www.walmart.com.mx/muebles/muebles-infantiles/camas-y-literas',
              'https://www.walmart.com.mx/muebles/muebles-infantiles/muebles-para-ninos',
              'https://www.walmart.com.mx/muebles/muebles-infantiles/cunas',
              'https://www.walmart.com.mx/muebles/muebles-infantiles/mecedoras',
              'https://www.walmart.com.mx/muebles/muebles-infantiles/muebles',
              # Escritorios y Muebles de Oficina
              'https://www.walmart.com.mx/muebles/escritorios-y-muebles-de-oficina/escritorios',
              'https://www.walmart.com.mx/muebles/escritorios-y-muebles-de-oficina/libreros',
              'https://www.walmart.com.mx/muebles/escritorios-y-muebles-de-oficina/sillas-de-oficina',
              # Muebles y Accesorios de Baño
              'https://www.walmart.com.mx/muebles/muebles-y-accesorios-de-bano/muebles',
              'https://www.walmart.com.mx/muebles/muebles-y-accesorios-de-bano/accesorios-de-bano',
              'https://www.walmart.com.mx/muebles/muebles-y-accesorios-de-bano/toallas-y-batas',
              'https://www.walmart.com.mx/muebles/muebles-y-accesorios-de-bano/tapetes-para-bano',
              # Persianas y cortinas
              'https://www.walmart.com.mx/muebles/persianas-y-cortinas/cortinas',
              'https://www.walmart.com.mx/muebles/persianas-y-cortinas/persianas',
              # Decoración, Tapetes y Cojines
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/cojines-decorativos',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/cuadros-y-relojes-de-pared',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/figuras-decorativas-y-floreros',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/espejos-y-percheros',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/portarretratos',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/tapetes-y-alfombras',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/tapices-y-posters',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/lamparas-de-mesa-y-piso',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/velas-y-candelabros',
              'https://www.walmart.com.mx/muebles/decoracion-tapetes-y-cojines/chimeneas-decorativas',

              # PATIO Y JARDIN
              'https://www.walmart.com.mx/patio-y-jardin/destacados-patio-y-jardin/patio-jardin-destacados',
              # Calentadores y Chimeneas
              'https://www.walmart.com.mx/patio-y-jardin/calentadores-y-chimeneas/calentadores',
              'https://www.walmart.com.mx/patio-y-jardin/calentadores-y-chimeneas/chimeneas',
              # Toldos y Sombrillas
              'https://www.walmart.com.mx/patio-y-jardin/toldos-y-sombrillas/sombrillas-y-bases',
              'https://www.walmart.com.mx/patio-y-jardin/toldos-y-sombrillas/carpas-y-toldos',
              # Muebles de Jardín
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/bistro-y-chat-set',
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/camastros',
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/comedores-y-desayunadores',
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/salas-para-jardin',
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/hamacas-y-columpios',
              'https://www.walmart.com.mx/patio-y-jardin/muebles-de-jardin/muebles-plegables-y-de-plastico',
              # Asadores y Accesorios
              'https://www.walmart.com.mx/patio-y-jardin/asadores-y-accesorios/asadores-de-carbon',
              'https://www.walmart.com.mx/patio-y-jardin/asadores-y-accesorios/accesorios-para-asar'
              # Decoración
              'https://www.walmart.com.mx/patio-y-jardin/decoracion/macetas',
              'https://www.walmart.com.mx/patio-y-jardin/decoracion/lamparas-de-patio',
              'https://www.walmart.com.mx/patio-y-jardin/decoracion/fuentes',
              'https://www.walmart.com.mx/patio-y-jardin/decoracion/cojines',
              # Herramientas
              'https://www.walmart.com.mx/patio-y-jardin/herramientas/herramientas-electricas',
              'https://www.walmart.com.mx/patio-y-jardin/herramientas/herramientas-manuales',
              'https://www.walmart.com.mx/patio-y-jardin/herramientas/mangueras-y-riego',
              'https://www.walmart.com.mx/patio-y-jardin/herramientas/almacenamiento-y-cobertizos',

              # FERRETERIA
              'https://www.walmart.com.mx/ferreteria/destacados-ferreteria/destacados-ferreteria',
              # Herramientas Electricas
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/taladros-y-atornilladores',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/rotomartillos',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/pulidoras-y-lijadoras',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/sierras-y-esmeriladoras',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/pistolas-de-calor-y-neumaticas',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/compresores',
              'https://www.walmart.com.mx/ferreteria/herramientas-electricas/generadores',
              # Herramientas Manuales
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/juegos-de-herramientas',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/llaves-y-pinzas',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/matracas-brocas-y-desarmadores',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/nivelacion-y-medicion',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/remaches-sujetadores-y-mas',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/cajas-de-herramienta',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/cucharas-cepillos-y-llanas',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/carretillas-carga-y-mantenimiento',
              'https://www.walmart.com.mx/ferreteria/herramientas-manuales/seguetas-serruchos-y-corte'
              # Seguridad Industrial
              'https://www.walmart.com.mx/ferreteria/seguridad-industrial/cascos-y-caretas-de-seguridad',
              'https://www.walmart.com.mx/ferreteria/seguridad-industrial/lentes-de-seguridad-fajas-y-arneses',
              'https://www.walmart.com.mx/ferreteria/seguridad-industrial/senalizacion',
              'https://www.walmart.com.mx/ferreteria/seguridad-industrial/chalecos-reflejantes',
              'https://www.walmart.com.mx/ferreteria/seguridad-industrial/botas-y-guantes',
              # Ferretería para el Hogar
              'https://www.walmart.com.mx/ferreteria/ferreteria-para-el-hogar/cadenas-y-candados',
              'https://www.walmart.com.mx/ferreteria/ferreteria-para-el-hogar/cerraduras',
              'https://www.walmart.com.mx/ferreteria/ferreteria-para-el-hogar/pilas',
              'https://www.walmart.com.mx/ferreteria/ferreteria-para-el-hogar/timbres',
              # Iluminación
              'https://www.walmart.com.mx/ferreteria/iluminacion/focos',
              'https://www.walmart.com.mx/ferreteria/iluminacion/lamparas-de-pared',
              'https://www.walmart.com.mx/ferreteria/iluminacion/lamparas-de-techo',
              'https://www.walmart.com.mx/ferreteria/iluminacion/lamparas-y-focos-vintage',
              'https://www.walmart.com.mx/ferreteria/iluminacion/ventiladores-de-techo',
              'https://www.walmart.com.mx/ferreteria/iluminacion/linternas-luminarios-y-reflectores',
              # Organización y Almacenaje
              'https://www.walmart.com.mx/ferreteria/organizacion-y-almacenaje/almacenamiento-y-cobertizos',
              'https://www.walmart.com.mx/ferreteria/organizacion-y-almacenaje/organizadores-de-herramientas',
              'https://www.walmart.com.mx/ferreteria/organizacion-y-almacenaje/cajas-de-herramientas',
              # Electricidad
              'https://www.walmart.com.mx/ferreteria/electricidad/extensiones-multicontactos-y-supresores',
              'https://www.walmart.com.mx/ferreteria/electricidad/accesorios-electricos-y-electronicos',
              'https://www.walmart.com.mx/ferreteria/electricidad/cables-electricos-y-tubo-conduit',
              'https://www.walmart.com.mx/ferreteria/electricidad/matainsectos',
              'https://www.walmart.com.mx/ferreteria/electricidad/contactos-y-apagadores',
              # Plomería y Baño
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/bombas-e-hidroneumaticos',
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/llaves-grifos-y-regaderas',
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/rejillas-tapas-y-tapones',
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/accesorios-de-plomeria',
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/mangueras-valvulas-y-conectores',
              'https://www.walmart.com.mx/ferreteria/plomeria-y-bano/flotadores-y-sapos',
              # Impermeabilizantes y Pinturas
              'https://www.walmart.com.mx/ferreteria/impermeabilizantes-y-pinturas/accesorios-para-pintar',
              'https://www.walmart.com.mx/ferreteria/impermeabilizantes-y-pinturas/lonas-y-cuerdas',
              'https://www.walmart.com.mx/ferreteria/impermeabilizantes-y-pinturas/taburetes-y-escaleras',
              # Maquinaria y Equipo
              'https://www.walmart.com.mx/ferreteria/maquinaria-y-equipo/equipo-para-soldar',

              # COCINA Y HOGAR
              'https://www.walmart.com.mx/cocina-y-hogar/destacados-hogar/cocina-y-hogar-destacados',
              # Artículos de Cocina
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/baterias-de-cocina',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/sartenes',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/ollas-y-cacerolas',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/linea-profesional',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/utensilios-de-cocina',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/hermeticos-y-refractarios',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/utensilios-de-horneado-y-reposteria',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/parrilla-y-utensilios',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/articulos-para-cafe-y-te',
              'https://www.walmart.com.mx/cocina-y-hogar/articulos-de-cocina/termos-e-hidratacion',
              # Mesa
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/vajillas-y-platos',
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/servicio-de-mesa',
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/vasos-y-copas',
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/cubiertos',
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/cuchillos',
              'https://www.walmart.com.mx/cocina-y-hogar/mesa/bar-y-cocteleria',
              # Organización del Hogar
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/organizadores-para-closet',
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/zapateras',
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/cajas-organizadoras',
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/organizadores-de-cocina-y-alacenas',
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/limpieza-y-botes-de-basura',
              'https://www.walmart.com.mx/cocina-y-hogar/organizacion-del-hogar/ganchos',
              # Cuarto de Lavado
              'https://www.walmart.com.mx/cocina-y-hogar/cuarto-de-lavado/cestos-de-ropa',
              'https://www.walmart.com.mx/cocina-y-hogar/cuarto-de-lavado/accesorios-de-lavanderia-y-planchado',
              'https://www.walmart.com.mx/cocina-y-hogar/cuarto-de-lavado/estantes-y-gabinetes',
              # Casa Inteligente
              'https://www.walmart.com.mx/cocina-y-hogar/casa-inteligente/destacados-casa-inteligente',
              'https://www.walmart.com.mx/cocina-y-hogar/casa-inteligente/iluminacion-inteligente',
              'https://www.walmart.com.mx/cocina-y-hogar/casa-inteligente/cerraduras-electronicas',
              'https://www.walmart.com.mx/cocina-y-hogar/casa-inteligente/seguridad',
              'https://www.walmart.com.mx/cocina-y-hogar/casa-inteligente/automatizacion-del-hogar',
              # Iluminación
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/focos',
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/lamparas-de-pared',
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/lamparas-de-techo',
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/lamparas-y-focos-vintage',
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/ventiladores-de-techo',
              'https://www.walmart.com.mx/cocina-y-hogar/iluminacion/linternas-luminarios-y-reflectores',
              # Decoración, Tapetes y Cojines
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/cojines-decorativos',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/cuadros-y-relojes-de-pared',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/figuras-decorativas-y-floreros',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/espejos-y-percheros',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/portarretratos',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/tapetes-y-alfombras',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/tapices-y-posters',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/lamparas-de-mesa-y-piso',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/velas-y-candelabros',
              'https://www.walmart.com.mx/cocina-y-hogar/decoracion-tapetes-y-cojines/chimeneas-decorativas',
              # Persianas y Cortinas
              'https://www.walmart.com.mx/cocina-y-hogar/persianas-y-cortinas/cortinas',
              'https://www.walmart.com.mx/cocina-y-hogar/persianas-y-cortinas/persianas',

              # BELLEZA Y CUIDADO
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/destacados-belleza-y-cuidado-personal/destacados-belleza-y-cuidado-personal',
              # Perfumes y Lociones
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/perfumes-y-lociones/perfumes-para-mujer',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/perfumes-y-lociones/perfumes-para-hombre',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/perfumes-y-lociones/sets-de-hombre',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/perfumes-y-lociones/sets-de-mujer',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/perfumes-y-lociones/perfumes-para-ninos',
              # Cuidado del Cabello
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/planchas-para-cabello',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/secadoras-de-cabello',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/cepillos-alaciadores-y-rizadoras',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/cepillos-y-accesorios',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/gel-mousse-y-spray',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/ceras-y-cremas',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/shampoo-y-acondicionador-profesional',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-del-cabello/tratamientos-profesionales',
              # Depilación y Afeitado
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/barba-y-bigote',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/recortadoras-y-detalladoras',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/rasuradoras-electricas',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/depiladoras',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/kits-de-corte',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/rastrillos-y-navajas-para-afeitar',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/geles-y-espumas',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/depilacion-y-afeitado/depilacion-profesional',
              # Maquillaje
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/cara',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/ojos',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/labios',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/unas',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/brochas-y-accesorios',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/maquillaje/sets-de-maquillaje',
              # Cuidado Corporal
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-corporal/jabones-y-limpieza-personal',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-corporal/cuidado-de-las-manos-y-pies',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-corporal/exfoliantes-y-cremas-corporales',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-corporal/productos-dermatologicos',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/cuidado-corporal/tratamientos-corporales',
              # Spa y Masaje
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/spa-y-masaje/masajeadores',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/spa-y-masaje/productos-para-spa',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/spa-y-masaje/camas-y-sillas-para-masajes',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/spa-y-masaje/aromaterapia',
              # Higiene Personal
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/higiene-personal/desodorantes-y-antitranspirantes',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/higiene-personal/bloqueadores-y-bronceadores',
              'https://www.walmart.com.mx/belleza-y-cuidado-personal/higiene-personal/talco',

              # ACCESORIOS DE MODA
              'https://www.walmart.com.mx/accesorios-de-moda/destacados-accesorios-de-moda/accesorios-de-moda-destacados',
              # Accesorios para Mujer
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-mujer/bolsas-para-mujer',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-mujer/carteras-mujer',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-mujer/mochilas-de-moda',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-mujer/otros-accesorios-de-moda',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-mujer/monos-y-diademas-infantiles',
              # Accesorios para Hombre
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/carteras-para-hombre',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/corbatas-y-monos',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/mancuernillas',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/otros-accesorios-hombre',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/gorras-y-gorros',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/cinturones-y-tirantes',
              'https://www.walmart.com.mx/accesorios-de-moda/accesorios-para-hombre/mariconeras-y-bolsos-para-hombres',
              # Relojes
              'https://www.walmart.com.mx/accesorios-de-moda/relojes/relojes-para-hombre',
              'https://www.walmart.com.mx/accesorios-de-moda/relojes/relojes-para-mujer',
              'https://www.walmart.com.mx/accesorios-de-moda/relojes/relojes-para-nino',
              # Lentes
              'https://www.walmart.com.mx/accesorios-de-moda/lentes/lentes-de-sol-hombre',
              'https://www.walmart.com.mx/accesorios-de-moda/lentes/lentes-de-sol-mujer',
              'https://www.walmart.com.mx/accesorios-de-moda/lentes/lentes-oftalmicos-mujer',
              'https://www.walmart.com.mx/accesorios-de-moda/lentes/lentes-oftalmicos-hombre',
              # Joyería y Bisutería
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/juegos-de-joyas',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/pulseras',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/collares',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/anillos',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/aretes',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/joyeros',
              'https://www.walmart.com.mx/accesorios-de-moda/joyeria-y-bisuteria/joyeria-religiosa',
              # Maletas
              'https://www.walmart.com.mx/accesorios-de-moda/maletas/mochilas-y-maletas-deportivas',
              'https://www.walmart.com.mx/accesorios-de-moda/maletas/maletas-de-viaje',
              'https://www.walmart.com.mx/accesorios-de-moda/maletas/accesorios-de-viaje',
              'https://www.walmart.com.mx/accesorios-de-moda/maletas/sets-de-maletas',
              # Lencería y Pijamas
              'https://www.walmart.com.mx/accesorios-de-moda/lenceria-y-pijamas/sandalias-dama',
              'https://www.walmart.com.mx/accesorios-de-moda/lenceria-y-pijamas/brasieres',

              # SALUD Y BIENESTAR
              'https://www.walmart.com.mx/salud-y-bienestar/destacados-salud-y-bienestar/destacados-salud-y-bienestar',
              # Spa y Masaje
              'https://www.walmart.com.mx/salud-y-bienestar/spa-y-masaje/masajeadores',
              'https://www.walmart.com.mx/salud-y-bienestar/spa-y-masaje/productos-para-spa',
              'https://www.walmart.com.mx/salud-y-bienestar/spa-y-masaje/camas-y-sillas-para-masajes',
              'https://www.walmart.com.mx/salud-y-bienestar/spa-y-masaje/aromaterapia',
              # Fajas y Control de Peso
              'https://www.walmart.com.mx/salud-y-bienestar/fajas-y-control-de-peso/basculas-y-medidores-de-grasa',
              'https://www.walmart.com.mx/salud-y-bienestar/fajas-y-control-de-peso/fajas',
              'https://www.walmart.com.mx/salud-y-bienestar/fajas-y-control-de-peso/productos-terapeuticos',
              # Equipo Ortopédico
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-ortopedico/movilidad',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-ortopedico/ortopedia-y-rehabilitacion',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-ortopedico/sillas-de-ruedas',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-ortopedico/aseo-y-cuidado-del-paciente',
              # Equipo Médico
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/termometros',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/humidificadores-y-nebulizadores',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/oxigenoterapia-y-oximetro',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/camas-de-hospital-y-colchones',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/glucometros-y-tiras-reactivas',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/baumanometros-y-pulsometros',
              'https://www.walmart.com.mx/salud-y-bienestar/equipo-medico/instrumental-medico',
              # Lentes Oftalmicos
              'https://www.walmart.com.mx/salud-y-bienestar/lentes-oftalmicos/lentes-oftalmicos-hombre',
              'https://www.walmart.com.mx/salud-y-bienestar/lentes-oftalmicos/lentes-oftalmicos-mujer',
              # Higiene Bucal y Dental
              'https://www.walmart.com.mx/salud-y-bienestar/higiene-bucal-y-dental/higiene-bucal',
              'https://www.walmart.com.mx/salud-y-bienestar/higiene-bucal-y-dental/cepillos-dentales-electricos',
              # Vitaminas y Suplementos
              'https://www.walmart.com.mx/salud-y-bienestar/vitaminas-y-suplementos/proteinas-y-suplementos',
              'https://www.walmart.com.mx/salud-y-bienestar/vitaminas-y-suplementos/adelgazantes',
              'https://www.walmart.com.mx/salud-y-bienestar/vitaminas-y-suplementos/vitaminas',
              # Salud Sexual
              'https://www.walmart.com.mx/salud-y-bienestar/salud-sexual/lubricantes-y-humectantes',
              'https://www.walmart.com.mx/salud-y-bienestar/salud-sexual/condones-y-anticonceptivos',
              # Dermocosméticos
              'https://www.walmart.com.mx/salud-y-bienestar/dermocosmeticos/piel-sensible',

              # BEBES
              'https://www.walmart.com.mx/bebes/destacados-bebes/bebes-destacados',
              # Cambio de pañales
              'https://www.walmart.com.mx/bebes/cambio-de-panales/bano-y-cuidado-de-la-piel',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/panales',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/panales-de-tela',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/toallitas',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/panaleras',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/botes-y-accesorios',
              'https://www.walmart.com.mx/bebes/cambio-de-panales/cambiadores',
              # Carriolas
              'https://www.walmart.com.mx/bebes/carriolas/sistemas-de-viaje',
              'https://www.walmart.com.mx/bebes/carriolas/ligeras',
              'https://www.walmart.com.mx/bebes/carriolas/dobles',
              'https://www.walmart.com.mx/bebes/carriolas/estandar',
              'https://www.walmart.com.mx/bebes/carriolas/accesorios-para-carriolas',
              # Autoasientos
              'https://www.walmart.com.mx/bebes/autoasientos/convertibles',
              'https://www.walmart.com.mx/bebes/autoasientos/infantiles',
              'https://www.walmart.com.mx/bebes/autoasientos/boosters',
              'https://www.walmart.com.mx/bebes/autoasientos/sistemas-de-viaje',
              # Cuarto del Bebé
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/cunas',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/cunas-de-viaje-y-corrales',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/colchones-de-cuna',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/muebles',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/mecedoras',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/monitores',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/ropa-de-cama',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/bambinetos-y-moises',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/cobijas-y-frazadas',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/organizacion',
              'https://www.walmart.com.mx/bebes/cuarto-del-bebe/decoracion',
              # Juguetes y Estimulación Temprana
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/preescolar',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/gimnasios-y-tapetes',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/columpios-y-bouncers',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/centro-de-actividades-y-andaderas',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/juguetes-de-bebe',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/moviles',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/accesorios-y-juguetes-de-bano',
              'https://www.walmart.com.mx/bebes/juguetes-y-estimulacion-temprana/mordederas-y-chupones',
              # Alimentación y Lactancia
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/biberones',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/sillas-altas-y-boosters',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/esterilizadores-y-calentadores',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/lactancia',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/platos-y-cubiertos',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/vasos-entrenadores',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/baberos',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/accesorios-y-limpieza',
              'https://www.walmart.com.mx/bebes/alimentacion-y-lactancia/mordederas-y-chupones',
              # Monitores y Seguridad
              'https://www.walmart.com.mx/bebes/monitores-y-seguridad/seguridad-del-bebe',
              'https://www.walmart.com.mx/bebes/monitores-y-seguridad/monitores',
              'https://www.walmart.com.mx/bebes/monitores-y-seguridad/puertas-de-seguridad'
              # Baño e Higiene del Bebé
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/baneras',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/toallitas',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/salud-del-bebe',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/banos-entrenadores',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/bano-y-cuidado-de-la-piel',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/accesorios-y-juguetes-de-bano',
              'https://www.walmart.com.mx/bebes/bano-e-higiene-del-bebe/batas-y-toallas',
              # Mamá
              'https://www.walmart.com.mx/bebes/mama/panaleras',
              'https://www.walmart.com.mx/bebes/mama/lactancia',
              'https://www.walmart.com.mx/bebes/mama/cangureras-y-rebozos',
              'https://www.walmart.com.mx/bebes/mama/almohadas-de-maternidad',
              'https://www.walmart.com.mx/bebes/mama/fajas-de-maternidad',
              'https://www.walmart.com.mx/bebes/mama/cubre-lactancia',
              # Cuarto para Niños
              'https://www.walmart.com.mx/bebes/cuarto-para-ninos/organizacion',
              'https://www.walmart.com.mx/bebes/cuarto-para-ninos/accesorios-para-ninos',
              'https://www.walmart.com.mx/bebes/cuarto-para-ninos/decoracion',
              # Ropa de Bebé
              'https://www.walmart.com.mx/bebes/ropa-de-bebe/interiores-y-pijamas',
              'https://www.walmart.com.mx/bebes/ropa-de-bebe/conjuntos-y-mamelucos',
              # Zapatos para Bebé
              'https://www.walmart.com.mx/bebes/zapatos-para-bebe/zapatos',
              'https://www.walmart.com.mx/bebes/zapatos-para-bebe/sandalias',
              # Ropa Interior y Pijamas
              'https://www.walmart.com.mx/bebes/ropa-interior-y-pijamas/interiores-y-pijamas',
              # Guantes, Gorros y Más
              'https://www.walmart.com.mx/bebes/guantes-gorros-y-mas/guantes-y-gorros-para-bebes',

              # MASCOTAS
              'https://www.walmart.com.mx/mascotas/destacados-mascotas/mascotas-destacados',
              # Perros
              'https://www.walmart.com.mx/mascotas/perros/alimento-para-perros',
              'https://www.walmart.com.mx/mascotas/perros/alimento-premium-para-perros',
              'https://www.walmart.com.mx/mascotas/perros/camas-y-tapetes-para-perro',
              'https://www.walmart.com.mx/mascotas/perros/casas-y-muebles-para-perro',
              'https://www.walmart.com.mx/mascotas/perros/ropa-y-accesorios',
              'https://www.walmart.com.mx/mascotas/perros/premios-y-carnazas',
              'https://www.walmart.com.mx/mascotas/perros/platos-y-bebederos-para-perros',
              'https://www.walmart.com.mx/mascotas/perros/juguetes-para-perros',
              'https://www.walmart.com.mx/mascotas/perros/collares-correas-y-placas',
              'https://www.walmart.com.mx/mascotas/perros/seguridad-y-tecnologia',
              'https://www.walmart.com.mx/mascotas/perros/jaulas-transportadoras-y-mas',
              'https://www.walmart.com.mx/mascotas/perros/salud-e-higiene',
              'https://www.walmart.com.mx/mascotas/perros/limpieza-y-cuidado-del-hogar',
              # Gatos
              'https://www.walmart.com.mx/mascotas/gatos/alimento-para-gatos',
              'https://www.walmart.com.mx/mascotas/gatos/arena-y-areneros',
              'https://www.walmart.com.mx/mascotas/gatos/rascaderos-muebles-y-rampas',
              'https://www.walmart.com.mx/mascotas/gatos/casas-camas-y-transportadoras',
              'https://www.walmart.com.mx/mascotas/gatos/platos-y-bebederos-para-gatos',
              'https://www.walmart.com.mx/mascotas/gatos/juguetes-para-gatos',
              'https://www.walmart.com.mx/mascotas/gatos/limpieza-del-hogar',
              'https://www.walmart.com.mx/mascotas/gatos/salud-y-belleza-gatos',
              # Reptiles
              'https://www.walmart.com.mx/mascotas/reptiles/alimento-para-reptiles',
              'https://www.walmart.com.mx/mascotas/reptiles/terrarios-y-decoracion',
              'https://www.walmart.com.mx/mascotas/reptiles/habitats-e-iluminacion',
              'https://www.walmart.com.mx/mascotas/reptiles/limpieza-y-salud-reptiles',
              # Peces
              'https://www.walmart.com.mx/mascotas/peces/alimento-para-peces',
              'https://www.walmart.com.mx/mascotas/peces/acuarios-y-peceras',
              'https://www.walmart.com.mx/mascotas/peces/decoracion-peceras',
              'https://www.walmart.com.mx/mascotas/peces/funcionamiento-e-iluminacion',
              'https://www.walmart.com.mx/mascotas/peces/limpieza-y-salud-peces',
              # Aves
              'https://www.walmart.com.mx/mascotas/aves/alimento-para-aves',
              'https://www.walmart.com.mx/mascotas/aves/jaulas-y-nidos',
              'https://www.walmart.com.mx/mascotas/aves/comederos-y-bebederos',
              'https://www.walmart.com.mx/mascotas/aves/juguetes-para-aves',
              # Roedores
              'https://www.walmart.com.mx/mascotas/roedores/habitats-y-jaulas',
              'https://www.walmart.com.mx/mascotas/roedores/juguetes-para-roedores',
              'https://www.walmart.com.mx/mascotas/roedores/accesorios-para-roedores',

              # LIBROS Y REVISTAS
              'https://www.walmart.com.mx/libros-y-revistas/destacados-libros-y-revistas/libros-destacados',
              # e-Readers y Accesorios
              'https://www.walmart.com.mx/libros-y-revistas/e-readers-y-accesorios/albumes-y-estampas',
              'https://www.walmart.com.mx/libros-y-revistas/e-readers-y-accesorios/agendas-y-calendarios',
              'https://www.walmart.com.mx/libros-y-revistas/e-readers-y-accesorios/lectores-electronicos',
              # Escolares y Arte
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/decoracion-y-diseno',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/diseno-y-dibujo',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/libros-de-moda',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/musica',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/idiomas',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/diccionarios-y-enciclopedias',
              'https://www.walmart.com.mx/libros-y-revistas/escolares-y-arte/computo',
              # Infantil y Juvenil
              'https://www.walmart.com.mx/libros-y-revistas/infantil-y-juvenil/comics-e-historietas',
              'https://www.walmart.com.mx/libros-y-revistas/infantil-y-juvenil/literatura-juvenil',
              'https://www.walmart.com.mx/libros-y-revistas/infantil-y-juvenil/actividades-y-didacticos',
              'https://www.walmart.com.mx/libros-y-revistas/infantil-y-juvenil/cuentos-y-fabulas',
              # Literatura y Novelas
              'https://www.walmart.com.mx/libros-y-revistas/literatura-y-novelas/ficcion-y-fantasia',
              'https://www.walmart.com.mx/libros-y-revistas/literatura-y-novelas/clasicos',
              'https://www.walmart.com.mx/libros-y-revistas/literatura-y-novelas/novelas',
              'https://www.walmart.com.mx/libros-y-revistas/literatura-y-novelas/terror-y-suspenso',
              # Recreación y Estilo de Vida
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/auto-ayuda-y-desarrollo-personal',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/paternidad',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/pasatiempos',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/deportes-y-fitness',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/cocina-y-gourmet',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/nutricion-y-dietas',
              'https://www.walmart.com.mx/libros-y-revistas/recreacion-y-estilo-de-vida/mascotas',

              # PELICULAS
              # DVD
              'https://www.walmart.com.mx/peliculas/dvd/accion',
              'https://www.walmart.com.mx/peliculas/dvd/infantil',
              'https://www.walmart.com.mx/peliculas/dvd/familiar',
              'https://www.walmart.com.mx/peliculas/dvd/musical',
              'https://www.walmart.com.mx/peliculas/dvd/aventura',
              'https://www.walmart.com.mx/peliculas/dvd/comedia',
              'https://www.walmart.com.mx/peliculas/dvd/crimen',
              'https://www.walmart.com.mx/peliculas/dvd/documental',
              'https://www.walmart.com.mx/peliculas/dvd/drama',
              'https://www.walmart.com.mx/peliculas/dvd/romantica',
              'https://www.walmart.com.mx/peliculas/dvd/sci-fi',
              'https://www.walmart.com.mx/peliculas/dvd/suspenso',
              'https://www.walmart.com.mx/peliculas/dvd/terror',
              'https://www.walmart.com.mx/peliculas/dvd/anime',
              # Blu-ray 3D
              'https://www.walmart.com.mx/peliculas/blu-ray-3d/blu-ray-3d',
              # Blu-ray
              'https://www.walmart.com.mx/peliculas/blu-ray/anime',
              'https://www.walmart.com.mx/peliculas/blu-ray/infantil',
              'https://www.walmart.com.mx/peliculas/blu-ray/musical',
              'https://www.walmart.com.mx/peliculas/blu-ray/accion',
              'https://www.walmart.com.mx/peliculas/blu-ray/aventura',
              'https://www.walmart.com.mx/peliculas/blu-ray/comedia',
              'https://www.walmart.com.mx/peliculas/blu-ray/documental',
              'https://www.walmart.com.mx/peliculas/blu-ray/drama',
              'https://www.walmart.com.mx/peliculas/blu-ray/familiar',
              'https://www.walmart.com.mx/peliculas/blu-ray/romantica',
              'https://www.walmart.com.mx/peliculas/blu-ray/sci-fi',
              'https://www.walmart.com.mx/peliculas/blu-ray/suspenso',
              'https://www.walmart.com.mx/peliculas/blu-ray/terror',
              # Series de TV
              'https://www.walmart.com.mx/peliculas/series-de-tv/dvd',
              'https://www.walmart.com.mx/peliculas/series-de-tv/blu-ray',
              # 4k
              'https://www.walmart.com.mx/peliculas/4k/peliculas-4k'

              # ALIMENTOS
              # Cafe y Te
              'https://www.walmart.com.mx/alimentos/cafe-y-te/cafe-de-grano-y-molido',
              'https://www.walmart.com.mx/alimentos/cafe-y-te/infusiones-y-te',

              # CERVEZA, VINOS Y LICORES
              # Licores Destilados
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/cognacs',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/ginebras',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/mezcales',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/ron',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/tequilas',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/vodkas',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/whiskys',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/licores-y-destilados/licores',

              # Vinos y Espumosos
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/vinos-y-espumosos/vinos',
              'https://www.walmart.com.mx/cervezas-vinos-y-licores/vinos-y-espumosos/vinos-espumosos',

              ]

'https://www.walmart.com.mx/api/rest/model/atg/commerce/catalog/ProductCatalogActor/getPriceAndPromotions?skuIds='
'https://www.walmart.com.mx/api/v2/page/browse/peliculas/blu-ray/anime?size=24&page=0'
with open('walmart_sku_scrape.csv', 'a') as sku_csv:
    sku_csv_writer = csv.writer(sku_csv)
    for url in categories:
        api_url = url[:26] + '/api/v2/page/browse' + url[26:]
        api_request = requests.get(api_url, headers)
        r = api_request.json()

        for n in range(len(r['appendix']['SearchResults']['content'])):
            walmartId = r['appendix']['SearchResults']['content'][n]['id']
            productId = r['appendix']['SearchResults']['content'][n]['productId']
            skuDisplayName = r['appendix']['SearchResults']['content'][n]['skuDisplayName']
            productSeoUrl = r['appendix']['SearchResults']['content'][n]['productSeoUrl']
            productRatings = r['appendix']['SearchResults']['content'][n]['productRatings']
            freeShippingItem = r['appendix']['SearchResults']['content'][n]['freeShippingItem']
            skuPrice = r['appendix']['SearchResults']['content'][n]['skuPrice']
            brandName = r['appendix']['SearchResults']['content'][n]['brandName']
            bundle = r['appendix']['SearchResults']['content'][n]['bundle']

            sku_csv_writer([walmartId, productId, skuDisplayName, productSeoUrl, productRatings, freeShippingItem,
                            skuPrice, brandName, bundle])
