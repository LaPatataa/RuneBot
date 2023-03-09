from webbrowser import Chrome
import os
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
import time

options = ChromeOptions()
options.headless = True
driver = Chrome(executable_path='/Users/manue/Desktop/pyton/chromedriver',options=options)

fecha = "13/12/2022"
campeon = ["morgana", "lulu", "vayne", "warwick", "ashe", "malzahar", "ekko", "thresh", "kaisa", "ahri", "akshan", "khazix", "jinx", "xinzhao", "zeri", "aatrox"
  , "trundle", "yone", "lucian", "ezreal", "maokai", "jhin", "skarner", "fizz", "singed", "drmundo", "rell", "soraka", "camille", "jarvaniv", "jayce", "zoe", "swain"
  , "elise", "hecarim", "irelia", "tristana", "volibear", "leona", "amumu", "katarina", "sona", "velkoz", "twistedfate", "yuumi", "akali", "nidalee", "qiyana"
  , "kogmaw", "sivir", "kled", "rengar", "ziggs", "kassadin", "senna", "masteryi", "leesin", "vex", "karthus", "varus", "nautilus", "renata", "rumble", "veigar"
  , "teemo", "annie", "alistar", "blitzcrank", "nami", "orianna", "rakan", "talon", "sejuani", "yasuo", "karma", "vi", "sett", "udyr", "leblanc", "syndra", "zed"
  , "ryze", "gangplank", "viego", "kindred", "twitch", "diana", "draven", "kayn", "pantheon", "illaoi", "xayah", "lillia", "monkeyking", "galio", "gwen", "tahmkench"
  , "viktor", "aphelios", "olaf", "taric", "zyra", "evelynn", "lissandra", "gragas", "poppy", "azir", "darius", "vladimir", "samira", "shen", "seraphine", "lux"
  , "braum", "riven", "chogath", "neeko", "taliyah", "jax", "heimerdinger", "shaco", "fiora", "yorick", "sion", "brand", "quinn", "kennen", "gnar", "zac", "nocturne"
  , "fiddlesticks", "rammus", "tryndamere", "kalista", "bard", "missfortune", "caitlyn", "janna", "mordekaiser", "renekton", "anivia", "nasus", "shyvana", "pyke"
  , "ornn", "malphite", "graves", "garen", "aurelionsol", "kayle", "urgot", "xerath", "corki", "zilean", "ivern", "nunu", "reksai", "sylas", "cassiopeia","belveth","nilah"
  ,"ksante"]

#lista respaldo 
#campeon = ["morgana", "lulu", "vayne", "warwick", "ashe", "malzahar", "ekko", "thresh", "kaisa", "ahri", "akshan", "khazix", "jinx", "xinzhao", "zeri", "aatrox"
#  , "trundle", "yone", "lucian", "ezreal", "maokai", "jhin", "skarner", "fizz", "singed", "drmundo", "rell", "soraka", "camille", "jarvaniv", "jayce", "zoe", "swain"
#  , "elise", "hecarim", "irelia", "tristana", "volibear", "leona", "amumu", "katarina", "sona", "velkoz", "twistedfate", "yuumi", "akali", "nidalee", "qiyana"
#  , "kogmaw", "sivir", "kled", "rengar", "ziggs", "kassadin", "senna", "masteryi", "leesin", "vex", "karthus", "varus", "nautilus", "renata", "rumble", "veigar"
#  , "teemo", "annie", "alistar", "blitzcrank", "nami", "orianna", "rakan", "talon", "sejuani", "yasuo", "karma", "vi", "sett", "udyr", "leblanc", "syndra", "zed"
#  , "ryze", "gangplank", "viego", "kindred", "twitch", "diana", "draven", "kayn", "pantheon", "illaoi", "xayah", "lillia", "monkeyking", "galio", "gwen", "tahmkench"
#  , "viktor", "aphelios", "olaf", "taric", "zyra", "evelynn", "lissandra", "gragas", "poppy", "azir", "darius", "vladimir", "samira", "shen", "seraphine", "lux"
#  , "braum", "riven", "chogath", "neeko", "taliyah", "jax", "heimerdinger", "shaco", "fiora", "yorick", "sion", "brand", "quinn", "kennen", "gnar", "zac", "nocturne"
#  , "fiddlesticks", "rammus", "tryndamere", "kalista", "bard", "missfortune", "caitlyn", "janna", "mordekaiser", "renekton", "anivia", "nasus", "shyvana", "pyke"
#  , "ornn", "malphite", "graves", "garen", "aurelionsol", "kayle", "urgot", "xerath", "corki", "zilean", "ivern", "nunu", "reksai", "sylas", "cassiopeia","belveth"]

for champ in campeon:

  nombre=champ
  print(champ)
  driver.get(f"https://www.leagueofgraphs.com/es/champions/builds/{champ}")
  if champ == "bard":
    nombre = "bardo"

  if champ == "monkeyking":
    nombre = "wukong"

  if champ == "leesin":
    nombre = "lee sin"
  
  if champ == "twistedfate":
    nombre = "twisted fate"
  
  if champ == "aurelionsol":
    nombre = "aurelion sol"

  if champ == "xinzhao":
    nombre = "xin zhao"

  if champ == "drmundo":
    nombre = "Dr.mundo"

  if champ == "jarvaniv":
    nombre = "jarvan iv"

  if champ == "masteryi":
    nombre = "maestro yi"
  
  if champ == "tahmkench":
    nombre = "tahm kench"
  
  if champ == "missfortune":
    nombre = "miss fortune"

  if champ == "kaisa":
    nombre = "kai'sa" 

  if champ == "kogmaw":
    nombre = "kog'maw" 

  if champ == "belveth":
    nombre = "Bel'Veth"
  
  if champ == "ksante":
    nombre == "K'Sante"


  soup = BeautifulSoup(driver.page_source,"lxml")
  
  #Rol

  rol = soup.find("div",class_="rolesEntries").find("img") 
  rol = rol.get("alt")

  #Porcentajes

  porcentajes = soup.find('div', "pie-chart small",id="graphDD2").contents[0]
  porcentajes = "".join(porcentajes).strip()
  
  #Orden de habilidades

  ordenHabilidaddesAux = soup.find_all("div",class_="championSpellLetter requireTooltip")
  ordenHabilidaddes = []

  for habilidades in ordenHabilidaddesAux:
    orden = (habilidades.get_text()).strip()
    ordenHabilidaddes.append(orden)
   

  #Runas Principales
  runaPrincipalAux = soup.find("table",class_="perksTableOverview")
  runaPrincipalAux = runaPrincipalAux.find_all("div",attrs={"style":""})

  runasPrincipales = []

  for runas in runaPrincipalAux:
    runas = runas.find("div",attrs={"style":""})
    if runas != None:
      aux = runas.find("img")
      runasPrincipales.append(aux.get("alt"))

  #Runas Secundarias y runas pequeñas  

  runaSecundariasAux = soup.find("table",class_="perksTableOverview secondary")
  runaSecundariasAux = runaSecundariasAux.find_all("div",attrs={"style":""})


  runaSecundarias = []

  for runes in runaSecundariasAux:
    runes = runes.find("div",attrs={"style":""})
    if runes != None:
      aux2 = runes.find("img")
      runaSecundarias.append(aux2.get("alt"))

  itemsAux = soup.find_all("div",class_="championSpell")

  #botas

  botasaux = ["Botas de mercurio","Botas de movilidad","Botas de rapidez","Botas de hechicero","Botas jonias de la lucidez","Grebas de berserker","Botas blindadas"]


  for itemsv in itemsAux:
    aux3 = itemsv.find("img").get("alt")
    if aux3 in botasaux: 
      botas = aux3
  
  #Items

  principales = soup.find_all('div', "championSpell")
  objs = []
  for obj in range(len(principales)):
    imgprincipales = principales[obj].find('img', alt=True)
    principalts = imgprincipales.get('alt')
    if principalts in botasaux: 
      principalts = ""
    objs.append(principalts)
  objpr = objs[6:10]
  objpr = " | ".join(objpr)

  objetos = soup.find_all('div', "championSpell small-margin")
  objinfin = []
  for obj in range(len(objetos)):
            imginfin = objetos[obj].find('img', alt=True)
            alts = imginfin.get('alt')
            objinfin.append(alts)
  x = len(objinfin) - 3
  objin = objinfin[:x]
  objin = " | ".join(objin)
  objfin = objinfin[-3:]
  objfin = " | ".join(objfin)

#Convertir las runas en emojis de discord
#Runas primarias 

#Presicion

  if 'Ataque intensificado' in runasPrincipales or 'Compás letal' in runasPrincipales or 'Pies veloces' in runasPrincipales or 'Conquistador' in runasPrincipales:
    principal = "<:Precision:962120531384082493>"

    if "Ataque intensificado" in runasPrincipales:
      runa1 = "<:ataqueintensificado:961354506338189332>:cd::cd::cd:"

    elif "Compás letal" in runasPrincipales:
      runa1 = ":cd:<:cadencialetal:961354507923640451>:cd::cd:"

    elif "Pies veloces" in runasPrincipales:
      runa1 = ":cd::cd:<:piesveloces:961354508133355580>:cd:"

    elif "Conquistador" in runasPrincipales:
      runa1 = ":cd::cd::cd:<:conquistador:961354508338864149>"

  #Linea1

    if "Supercuración" in runasPrincipales:
      runa2 = "<:sobrecuracion:961354507688763505>:cd::cd:"
    
    elif "Triunfo" in runasPrincipales:
      runa2 = ":cd:<:triunfo:961354507965587496>:cd:"

    elif "Claridad mental" in runasPrincipales:
      runa2 = ":cd::cd:<:claridadmental:961354506803744768>"

  #Linea2

    if "Leyenda: Presteza" in runasPrincipales:
      runa3 = "<:leyendaceleridad:961354507441299517>:cd::cd:"
    
    elif "Leyenda: Tenacidad" in runasPrincipales:
      runa3 = ":cd:<:tenacidad:961354507932028928>:cd:"

    elif "Leyenda: Linaje" in runasPrincipales:
      runa3 = ":cd::cd:<:linage:961354507554549760>"

  #Linea3

    if "Golpe de gracia" in runasPrincipales:
      runa4 = "<:golpedegracia:961354507403550781>:cd::cd:"
    
    elif "Derribado" in runasPrincipales:
      runa4 = ":cd:<:corte:961354507403546624>:cd:"

    elif "Último esfuerzo" in runasPrincipales:
      runa4 = ":cd::cd:<:utimabatalla:961354507973984266>"


  #Dominacion

  elif 'Electrocutar' in runasPrincipales or 'Depredador' in runasPrincipales or 'Cosecha oscura' in runasPrincipales or 'Lluvia de cuchillas' in runasPrincipales:
    principal = "<:Dominacion:962120416699236442>"

    if "Electrocutar" in runasPrincipales:
      runa1 = "<:electrocutar:961346841436364910>:cd::cd::cd:"

    elif "Depredador" in runasPrincipales:
      runa1 = ":cd:<:depredador:961346841465745508>:cd::cd:"

    elif "Cosecha oscura" in runasPrincipales:
      runa1 = ":cd::cd:<:cosecha:961346841369256007>:cd:"

    elif "Lluvia de cuchillas" in runasPrincipales:
      runa1 = ":cd::cd::cd:<:lluviadeespadas:961346841935495228>"

  #Linea1

    if "Golpe bajo" in runasPrincipales:
      runa2 = "<:golpebajo:961346841419608064>:cd::cd:"
    
    elif "Sabor a sangre" in runasPrincipales:
      runa2 = ":cd:<:saborasangre:961346842069704774>:cd:"

    elif "Impacto repentino" in runasPrincipales:
      runa2 = ":cd::cd:<:impactorepentino:961346841079849001>"

  #Linea2

    if "Guardián zombi" in runasPrincipales:
      runa3 = "<:centinelazombie:961346841293766696>:cd::cd:"
    
    elif "Poro fantasmal" in runasPrincipales:
      runa3 = ":cd:<:porofantasma:961346842073903104>:cd:"

    elif "Colección de globos oculares" in runasPrincipales:
      runa3 = ":cd::cd:<:colecciondeojos:961346841478303774>"

  #Linea3

    if "Cazador de tesoros" in runasPrincipales:
      runa4 = "<:cazadordetesoros:961346841281196062>:cd::cd::cd:"
    
    elif "Cazador ingenioso" in runasPrincipales:
      runa4 = ":cd:<:cazadoringenioso:961346841281200188>:cd::cd:"

    elif "Cazador incesante" in runasPrincipales:
      runa4 = ":cd::cd:<:cazadorimplacable:961346841318920243>:cd:"

    elif "Cazador definitivo" in runasPrincipales:
      runa4 = ":cd::cd::cd:<:cazadordefinitivo:961346841281179688>"

  #brujeria

  elif 'Invocar a Aery' in runasPrincipales or 'Cometa arcano' in runasPrincipales or 'Irrupción de fase' in runasPrincipales:
    principal = "<:brujeria:962120391885729822>"

    if "Invocar a Aery" in runasPrincipales:
      runa1 = "<:aery:961363642345979934>:cd::cd:"

    elif "Cometa arcano" in runasPrincipales:
      runa1 = ":cd:<:cometaarcano:961363642132090910>:cd:"

    elif "Irrupción de fase" in runasPrincipales:
      runa1 = ":cd::cd:<:faseveloz:961363642245316708>"


  #Linea1

    if "Orbe anulador" in runasPrincipales:
      runa2 = "<:orbedeanulacion:961363642375344238>:cd::cd:"
    
    elif "Banda de maná" in runasPrincipales:
      runa2 = ":cd:<:anillodeflujodemana:961363642186608650>:cd:"

    elif "Capa del nimbo" in runasPrincipales:
      runa2 = ":cd::cd:<:cadadenimbo:961363642316619836>"

  #Linea2

    if "Trascendencia" in runasPrincipales:
      runa3 = "<:trascendencia:961363642404724796>:cd::cd:"
    
    elif "Celeridad" in runasPrincipales:
      runa3 = ":cd:<:celeridad:961363642048208956>:cd:"

    elif "Concentración absoluta" in runasPrincipales:
      runa3 = ":cd::cd:<:concentracionabsoluta:961363642325008474>"

  #Linea3

    if "Piroláser" in runasPrincipales:
      runa4 = "<:pirolazer:961363642421510194>:cd::cd:"
    
    elif "Caminar sobre agua" in runasPrincipales:
      runa4 = ":cd:<:caminatasobreagua:961363642203381881>:cd:"

    elif "Se avecina tormenta" in runasPrincipales:
      runa4 = ":cd::cd:<:tormentacreciente:961363642123698197>"

  #Valor

  elif 'Garras del inmortal' in runasPrincipales or 'Reverberacción' in runasPrincipales or 'Protector' in runasPrincipales:
    principal = "<:valor:962120572303716392>"

    if "Garras del inmortal" in runasPrincipales:
      runa1 = "<:agarreperpetuo:961365783710142574>:cd::cd:"

    elif "Reverberacción" in runasPrincipales:
      runa1 = ":cd:<:replica:961365784234438726>:cd:"

    elif "Protector" in runasPrincipales:
      runa1 = ":cd::cd:<:guardian:961365784536444988>"


  #Linea1

    if "Demoler" in runasPrincipales:
      runa2 = "<:demolicion:961365781885628466>:cd::cd:"
    
    elif "Fuente de vida" in runasPrincipales:
      runa2 = ":cd:<:fuentedevida:961365782162444350>:cd:"

    elif "Golpe de escudo" in runasPrincipales:
      runa2 = ":cd::cd:<:golpedeescudo:961365782237954048>"

  #Linea2

    if "Condicionamiento" in runasPrincipales:
      runa3 = "<:acondicionamiento:961365780866400276>:cd::cd:"
    
    elif "Fuerzas renovadas" in runasPrincipales:
      runa3 = ":cd:<:segundoaire:961365783324262440>:cd:"

    elif "Revestimiento de huesos" in runasPrincipales:
      runa3 = ":cd::cd:<:corazaosea:961365781243899925>"

  #Linea3

    if "Sobrecrecimiento" in runasPrincipales:
      runa4 = "<:crecimientoexesivo:961365781910806538>:cd::cd:"
    
    elif "Revitalizar" in runasPrincipales:
      runa4 = ":cd:<:revitalizar:961365783378800670>:cd:"

    elif "Inquebrantable" in runasPrincipales:
      runa4 = ":cd::cd:<:inquebrantable:961365782854529075>"


  #Inpiración

  elif 'Mejora glacial' in runasPrincipales or 'Libro de hechizos' in runasPrincipales or 'Primer golpe' in runasPrincipales:
    principal = "<:inspiracion:962120501369647164>"

    if "Mejora glacial" in runasPrincipales:
      runa1 = "<:aumentoglaciar:961367112247558225>:cd::cd:"

    elif "Libro de hechizos" in runasPrincipales:
      runa1 = ":cd:<:librodehechizos:961367112704733234>:cd:"

    elif "Primer golpe" in runasPrincipales:
      runa1 = ":cd::cd:<:primergolpe:961367114365665331>"


  #Linea1

    if "Destello hextech" in runasPrincipales:
      runa2 = "<:hextechdestello:961367110917980210>:cd::cd:"
    
    elif "Calzado mágico" in runasPrincipales:
      runa2 = ":cd:<:calzadomagico:961367109940690995>:cd:"

    elif "Momento oportuno" in runasPrincipales:
      runa2 = ":cd::cd:<:cronometro:961367110070718495>"

  #Linea2

    if "Mercado del futuro" in runasPrincipales:
      runa3 = "<:mercadodefuturos:961367111404503050>:cd::cd:"
    
    elif "Desmaterializador de súbditos" in runasPrincipales:
      runa3 = ":cd:<:desmaterializador:961367112373370880>:cd:"

    elif "Entrega de galletas" in runasPrincipales:
      runa3 = ":cd: :cd: <:entregadegalletas:961367110746009611>"

  #Linea3

    if "Perspicacia cósmica" in runasPrincipales:
      runa4 = "<:prespicacia:961367111526133870>:cd::cd:"
    
    elif "Velocidad de acercamiento" in runasPrincipales:
      runa4 = ":cd:<:velocidaddeaproimacion:961367112109146122>:cd:"

    elif "Tónico de distorsión temporal" in runasPrincipales:
      runa4 = ":cd::cd:<:tonicodedistorsion:961367112004296724>"

#Runas segundarias

#Presicion

  if 'Supercuración' in runaSecundarias or 'Triunfo' in runaSecundarias or 'Claridad mental' in runaSecundarias or 'Leyenda: Presteza' in runaSecundarias or 'Leyenda: Tenacidad' in runaSecundarias or 'Leyenda: Linaje' in runaSecundarias:
    segundaria="<:Precision:962120531384082493>"

#Linea1
    
    if "Supercuración" in runaSecundarias:
      runa2sec = "<:sobrecuracion:961354507688763505>:cd::cd:"
    
    elif "Triunfo" in runaSecundarias:
      runa2sec = ":cd:<:triunfo:961354507965587496>:cd:"

    elif "Claridad mental" in runaSecundarias:
      runa2sec = ":cd::cd:<:claridadmental:961354506803744768>"
    
    else:
      runa2sec = ":cd::cd::cd:"

  #Linea2

    if "Leyenda: Presteza" in runaSecundarias:
      runa3sec = "<:leyendaceleridad:961354507441299517>:cd::cd:"
    
    elif "Leyenda: Tenacidad" in runaSecundarias:
      runa3sec = ":cd:<:tenacidad:961354507932028928>:cd: "

    elif "Leyenda: Linaje" in runaSecundarias:
      runa3sec = ":cd::cd:<:linage:961354507554549760>"

    else:
      runa3sec = ":cd::cd::cd:"

  #Linea3

    if "Golpe de gracia" in runaSecundarias:
      runa4sec = "<:golpedegracia:961354507403550781>:cd::cd:"
    
    elif "Derribado" in runaSecundarias:
      runa4sec = ":cd:<:corte:961354507403546624>:cd:"

    elif "Último esfuerzo" in runaSecundarias:
      runa4sec = ":cd: :cd: <:utimabatalla:961354507973984266>"

    else:
      runa4sec = ":cd::cd::cd:"

  #Dominacion

  elif 'Golpe bajo' in runaSecundarias or 'Sabor a sangre' in runaSecundarias or 'Impacto repentino' in runaSecundarias or 'Guardián zombi' in runaSecundarias or 'Poro fantasmal' in runaSecundarias or 'Colección de globos oculares' in runaSecundarias:
    segundaria="<:Dominacion:962120416699236442>"

  #Linea1
    if "Golpe bajo" in runaSecundarias:
      runa2sec = "<:golpebajo:961346841419608064>:cd::cd:"
    
    elif "Sabor a sangre" in runaSecundarias:
      runa2sec = ":cd:<:saborasangre:961346842069704774>:cd:"

    elif "Impacto repentino" in runaSecundarias:
      runa2sec = ":cd::cd:<:impactorepentino:961346841079849001>"

    else:
      runa2sec = ":cd::cd::cd:"

  #Linea2

    if "Guardián zombi" in runaSecundarias:
      runa3sec = "<:centinelazombie:961346841293766696>:cd::cd:"
    
    elif "Poro fantasmal" in runaSecundarias:
      runa3sec = ":cd:<:porofantasma:961346842073903104>:cd:"

    elif "Colección de globos oculares" in runaSecundarias:
      runa3sec = ":cd::cd:<:colecciondeojos:961346841478303774>"

    else:
      runa3sec = ":cd::cd::cd:"

  #Linea3

    if "Cazador de tesoros" in runaSecundarias:
      runa4sec = "<:cazadordetesoros:961346841281196062>:cd::cd::cd:"
    
    elif "Cazador ingenioso" in runaSecundarias:
      runa4sec = ":cd:<:cazadoringenioso:961346841281200188>:cd::cd:"

    elif "Cazador incesante" in runaSecundarias:
      runa4sec = ":cd::cd:<:cazadorimplacable:961346841318920243>:cd:"

    elif "Cazador definitivo" in runaSecundarias:
      runa4sec = ":cd::cd::cd:<:cazadordefinitivo:961346841281179688>"

    else:
      runa4sec = ":cd::cd::cd::cd:"

  #brujeria

  elif 'Orbe anulador' in runaSecundarias or 'Banda de maná' in runaSecundarias or 'Capa del nimbo' in runaSecundarias or 'Trascendencia' in runaSecundarias or 'Celeridad' in runaSecundarias or 'Concentración absoluta' in runaSecundarias:
    segundaria="<:brujeria:962120391885729822>"

  #Linea1

    if "Orbe anulador" in runaSecundarias:
      runa2sec = "<:orbedeanulacion:961363642375344238>:cd::cd:"
    
    elif "Banda de maná" in runaSecundarias:
      runa2sec = ":cd:<:anillodeflujodemana:961363642186608650>:cd:"

    elif "Capa del nimbo" in runaSecundarias:
      runa2sec = ":cd::cd:<:cadadenimbo:961363642316619836>"

    else:
      runa2sec = ":cd::cd::cd:"

  #Linea2

    if "Trascendencia" in runaSecundarias:
      runa3sec = "<:trascendencia:961363642404724796>:cd::cd:"
    
    elif "Celeridad" in runaSecundarias:
      runa3sec = ":cd:<:celeridad:961363642048208956>:cd:"

    elif "Concentración absoluta" in runaSecundarias:
      runa3sec = ":cd::cd:<:concentracionabsoluta:961363642325008474>"

    else:
      runa3sec = ":cd::cd::cd:"

  #Linea3

    if "Piroláser" in runaSecundarias:
      runa4sec = "<:pirolazer:961363642421510194>:cd::cd:"
    
    elif "Caminar sobre agua" in runaSecundarias:
      runa4sec = ":cd:<:caminatasobreagua:961363642203381881>:cd:"

    elif "Se avecina tormenta" in runaSecundarias:
      runa4sec = ":cd::cd:<:tormentacreciente:961363642123698197>"

    else:
      runa4sec = ":cd::cd::cd:"

  #Valor

  elif 'Demoler' in runaSecundarias or 'Fuente de vida' in runaSecundarias or 'Golpe de escudo' in runaSecundarias or 'Condicionamiento' in runaSecundarias or 'Fuerzas renovadas' in runaSecundarias or 'Revestimiento de huesos' in runaSecundarias:
    segundaria="<:valor:962120572303716392>"
  #Linea1

    if "Demoler" in runaSecundarias:
      runa2sec = "<:demolicion:961365781885628466>:cd::cd:"
    
    elif "Fuente de vida" in runaSecundarias:
      runa2sec = ":cd:<:fuentedevida:961365782162444350>:cd:"

    elif "Golpe de escudo" in runaSecundarias:
      runa2sec = ":cd::cd:<:golpedeescudo:961365782237954048>"

    else:
      runa2sec = ":cd::cd::cd:"

  #Linea2

    if "Condicionamiento" in runaSecundarias:
      runa3sec = "<:acondicionamiento:961365780866400276>:cd::cd:"
    
    elif "Fuerzas renovadas" in runaSecundarias:
      runa3sec = ":cd:<:segundoaire:961365783324262440>:cd:"

    elif "Revestimiento de huesos" in runaSecundarias:
      runa3sec = ":cd::cd:<:corazaosea:961365781243899925>" 
    else:
      runa3sec = ":cd::cd::cd:"

  #Linea3

    if "Sobrecrecimiento" in runaSecundarias:
      runa4sec = "<:crecimientoexesivo:961365781910806538>:cd::cd:"
    
    elif "Revitalizar" in runaSecundarias:
      runa4sec = ":cd:<:revitalizar:961365783378800670>:cd:"

    elif "Inquebrantable" in runaSecundarias:
      runa4sec = ":cd::cd:<:inquebrantable:961365782854529075>"

    else:
      runa4sec = ":cd::cd::cd:"

  #Inpiración

  elif 'Destello hextech' in runaSecundarias or 'Calzado mágico' in runaSecundarias or 'Momento oportuno' in runaSecundarias or 'Mercado del futuro' in runaSecundarias or 'Desmaterializador de súbditos' in runaSecundarias or 'Entrega de galletas' in runaSecundarias:
    segundaria="<:inspiracion:962120501369647164>"
  #Linea1

    if "Destello hextech" in runaSecundarias:
      runa2sec = "<:hextechdestello:961367110917980210>:cd::cd:"
    
    elif "Calzado mágico" in runaSecundarias:
      runa2sec = ":cd:<:calzadomagico:961367109940690995>:cd:"

    elif "Momento oportuno" in runaSecundarias:
      runa2sec = ":cd::cd:<:cronometro:961367110070718495>"

    else:
      runa2sec = ":cd::cd::cd:"

  #Linea2

    if "Mercado del futuro" in runaSecundarias:
      runa3sec = "<:mercadodefuturos:961367111404503050>:cd::cd:"
    
    elif "Desmaterializador de súbditos" in runaSecundarias:
      runa3sec = ":cd:<:desmaterializador:961367112373370880>:cd:"

    elif "Entrega de galletas" in runaSecundarias:
      runa3sec = ":cd::cd:<:entregadegalletas:961367110746009611>"

    else:
      runa3sec = ":cd::cd::cd:"

  #Linea3

    if "Perspicacia cósmica" in runaSecundarias:
      runa4sec = "<:prespicacia:961367111526133870>:cd::cd:"
    
    elif "Velocidad de acercamiento" in runaSecundarias:
      runa4sec = ":cd:<:velocidaddeaproimacion:961367112109146122>:cd:"

    elif "Tónico de distorsión temporal" in runaSecundarias:
      runa4sec = ":cd::cd:<:tonicodedistorsion:961367112004296724>"

    else:
      runa4sec = ":cd::cd::cd:"

  if "+9 de fuerza adaptable" in runaSecundarias[2]:
    runa1pequena = "<:fuerza:961452164423770142>"
  elif "+10% "+ "de velocidad de ataque" in runaSecundarias[2]:
    runa1pequena = "<:velocidad:961452164511838259>"
  elif "+8 de velocidad de habilidades" in runaSecundarias[2]:
    runa1pequena = "<:reduccion:961452164331495434>"

  if "+9 de fuerza adaptable" in runaSecundarias[3]:
    runa2pequena = "<:fuerza:961452164423770142>"
  elif "+6 armadura" in runaSecundarias[3]:
    runa2pequena = "<:defesa:961452164394393630>"
  elif "+8 de resistencia mágica" in runaSecundarias[3]:
    runa2pequena = "<:magica:961452164381802566>"

  if "+15-90 de vida (según el nivel)" in runaSecundarias[4]:
    runa3pequena = "<:vida:961452164419555368>"
  elif "+6 armadura" in runaSecundarias[4]:
    runa3pequena = "<:defesa:961452164394393630>"
  elif "+8 de resistencia mágica" in runaSecundarias[4]:
    runa3pequena = "<:magica:961452164381802566>"

  if principal == "<:Dominacion:962120416699236442>":
    texto = (f"Última vez actualizado {fecha} \n**{nombre}** : _{rol}_\n**Porcentaje de victorias : {porcentajes}**\n        {principal}                        {segundaria}\n{runa1}         {runa2sec}\n{runa2}               {runa3sec}\n{runa3}               {runa4sec}\n{runa4}         {runa1pequena}{runa2pequena}{runa3pequena}")
    texto = (texto+f"\n\n**Orden Habilidades : {ordenHabilidaddes[0]} > {ordenHabilidaddes[1]} > {ordenHabilidaddes[2]}**")
    texto = (texto+f"\n\n**items iniciales :** {objin} \n**items principales :** {objpr} \n**Botas :** {botas} \n**items finales :** {objfin}")

  elif principal == "<:Precision:962120531384082493>":
    texto = (f"Última vez actualizado {fecha} \n**{nombre}** : _{rol}_\n**Porcentaje de victorias : {porcentajes}**\n        {principal}                        {segundaria}\n{runa1}         {runa2sec}\n{runa2}               {runa3sec}\n{runa3}               {runa4sec}\n{runa4}               {runa1pequena}{runa2pequena}{runa3pequena}")
    texto = (texto+f"\n\n**Orden Habilidades : {ordenHabilidaddes[0]} > {ordenHabilidaddes[1]} > {ordenHabilidaddes[2]}**")
    texto = (texto+f"\n\n**items iniciales :** {objin} \n**items principales :** {objpr} \n**Botas :** {botas} \n**items finales :** {objfin}")

  elif principal == "<:valor:962120572303716392>" or principal == "<:inspiracion:962120501369647164>" or principal == "<:brujeria:962120391885729822>":
    texto = (f"Última vez actualizado {fecha} \n**{nombre}** : _{rol}_\n**Porcentaje de victorias : {porcentajes}**\n        {principal}                        {segundaria}\n{runa1}               {runa2sec}\n{runa2}               {runa3sec}\n{runa3}               {runa4sec}\n{runa4}               {runa1pequena}{runa2pequena}{runa3pequena}")
    texto = (texto+f"\n\n**Orden Habilidades : {ordenHabilidaddes[0]} > {ordenHabilidaddes[1]} > {ordenHabilidaddes[2]}**")
    texto = (texto+f"\n\n**items iniciales :** {objin} \n**items principales :** {objpr} \n**Botas :** {botas} \n**items finales :** {objfin}")

  f = open(os.path.join(r"/Users/manue/Desktop/BotRune/runas/"+champ+".txt"), 'w+',encoding="utf-8")
  f.write(texto)
  f.close()

driver.quit()