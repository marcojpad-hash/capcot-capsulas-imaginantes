# -*- coding: utf-8 -*-
# Grupo A comida (Mj t596u/t597u, 23-nov-2026). Narración ES = guiones verificados de Mj TAL CUAL
# (pendientes/abiertos/2026-11-22_guiones-semana-30nov-6dic.md, cargados en guiones_mj.json). EN = traducción fiel.
import json, os
G = {int(k): v for k, v in json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guiones_mj.json'))).items()}
def src(n):
    out=[]
    for i,f in enumerate(G[n]['fuentes']):
        cita,url=f.rsplit(': ',1)
        if url.endswith('the-medieval-beverage-of-choice-'): url+='alcohol-or-water'  # URL truncada en el archivo; ésta es la página real
        out.append(dict(id=f'SRC-{i+1:03d}',cita_corta=cita,url=url))
    return out
def S(n, slug, cama, bpm, title_en, ht_es, ht_en, en, ost_es, ost_en, imgs, sfx, capas):
    es=G[n]['esc']; assert len(es)==6==len(en)
    return dict(n=n, slug=slug, cama=cama, bpm=bpm, title_es=G[n]['title'], title_en=title_en, ht_es=ht_es, ht_en=ht_en, sources=src(n),
        scenes=[dict(es=es[i], en=en[i], ost_es=ost_es[i], ost_en=ost_en[i], img=imgs[i], sfx=[sfx[i]], **({'capa':capas[i]} if capas.get(i) else {})) for i in range(6)])
VP=[dict(nombre='Viena', nombre_en='Vienna', lon=16.37, lat=48.21), dict(nombre='París', nombre_en='Paris', lon=2.35, lat=48.86)]
SPECS={}
SPECS['antonieta']=S(15,'antonieta-pastel','marimba',96,"Did Marie Antoinette say 'let them eat cake'?",
 ['#historia','#MariaAntonieta','#mitos','#curiosidades','#sabiasque'],['#history','#MarieAntoinette','#myths','#facts','#didyouknow'],
 ['It is one of the most famous lines in history: "Let them eat cake." It is attributed to Marie Antoinette, queen of France, when she was told the people had no bread.',
  'The line is used to stand for the monarchy\'s indifference to the suffering of the people. But did Marie Antoinette really say it?',
  'There is no evidence that Marie Antoinette ever spoke those words. The expression appears in texts written before she arrived in France.',
  'A similar version appears in the Confessions of Jean-Jacques Rousseau, published in the 18th century. Rousseau attributed the line to a "great princess," without naming Marie Antoinette.',
  'The line became linked to the queen during the French Revolution, when people sought to discredit the monarchy. It became a symbol of her supposed indifference.',
  'So no: there is no evidence that Marie Antoinette said "let them eat cake." It is a line that was pinned on her to criticize the monarchy.'],
 ['','Indiferencia de la monarquía','Sin pruebas','Rousseau: «una gran princesa»','Revolución francesa','No hay evidencia'],
 ['','The monarchy\'s indifference','No evidence','Rousseau: "a great princess"','French Revolution','No evidence'],
 ['File:Vigée Le Brun, Élisabeth - Marie-Antoinette en gaulle, 1783.JPG','File:Marie Antoinette and her Children by Élisabeth Vigée-Lebrun.jpg',
  'File:Reinsperger - Carolina, Josepha and Antonia of Austria - Hofburg.png','File:Maurice Quentin de La Tour - Portrait de Jean-Jacques Rousseau (1712-1778), écrivain et philosophe - P210 - Musée Carnavalet.jpg',
  'File:Exécution de Marie Antoinette le 16 octobre 1793.jpg','File:Brioche aux pépites de chocolat.jpg'],
 ['pluma','madera','campanas','pluma','tormenta','madera'],
 {2:dict(tipo='mapa',region=[-5,25,40,55],puntos=VP,flechas=[[16.37,48.21,2.35,48.86,'']],titulo='De Viena a Francia',titulo_en='From Vienna to France',fuente='Britannica · Natural Earth'),
  5:dict(tipo='dato',valor='0 pruebas',valor_en='0 evidence',etiqueta='de que ella lo dijera',etiqueta_en='that she said it',fuente='Britannica · History.com')})
SPECS['fortuna']=S(31,'galletas-fortuna','arpegio',94,'Are fortune cookies really Chinese?',
 ['#comida','#galletasdelafortuna','#japon','#curiosidades','#sabiasque'],['#food','#fortunecookie','#japan','#facts','#didyouknow'],
 ['In many Chinese restaurants in the United States, the meal ends with a cookie that holds a message. But are they really Chinese?',
  'Modern fortune cookies have a history tied to Japan and the United States. There are several theories about their exact origin.',
  'A Japanese tradition known as tsujiura senbei used rice crackers with messages. Depictions of this kind of sweet have been found in 19th-century prints.',
  'In the early 20th century, fortune cookies began to catch on in San Francisco. Makoto Hagiwara, a Japanese immigrant, is one of the figures linked to their spread.',
  'During World War Two, many Japanese Americans were sent to internment camps. The cookies passed into the hands of Chinese American companies, which made them popular.',
  'That is why, although today they are linked to Chinese restaurants, fortune cookies have Japanese roots and an American history.'],
 ['','Japón y Estados Unidos','Tsujiura senbei','Makoto Hagiwara, San Francisco','Campos de internamiento','Raíces japonesas'],
 ['','Japan and the United States','Tsujiura senbei','Makoto Hagiwara, San Francisco','Internment camps','Japanese roots'],
 ['File:Fortune cookie broken 20040628 223252 1.jpg','File:Torii path with lantern at Fushimi Inari Taisha Shrine, Kyoto, Japan.jpg','File:Fortune Cookie 1878.jpg',
  'File:Original Hagiwara fortune cookie press 01.jpg','File:Dorothea Lange, Japanese-American boarding up store front before relocation, San Francisco, 1942.jpg','File:Tsujiura senbei.jpg'],
 ['madera','campanas','madera','madera','viento','madera'],
 {1:dict(tipo='mapa',region=[125,250,15,55],puntos=[dict(nombre='Japón',nombre_en='Japan',lon=135.77,lat=34.97),dict(nombre='San Francisco',lon=237.58,lat=37.77)],flechas=[[135.77,34.97,237.58,37.77,'']],titulo='Japón → Estados Unidos',titulo_en='Japan → United States',fuente='Smithsonian · Natural Earth'),
  2:dict(tipo='dato',valor='Siglo XIX',valor_en='19th century',etiqueta='grabados de tsujiura senbei',etiqueta_en='prints of tsujiura senbei',fuente='Smithsonian Magazine')})
SPECS['croissant']=S(32,'croissant-otomano','pizzicato',100,'Was the croissant born to celebrate an Ottoman defeat?',
 ['#comida','#croissant','#historia','#mitos','#sabiasque'],['#food','#croissant','#history','#myths','#didyouknow'],
 ['A widely repeated story claims the croissant was invented to celebrate the Ottoman defeat during the siege of Vienna in 1683.',
  'The legend says Viennese bakers, working before dawn, discovered an attack and raised the alarm. To celebrate, they created a bread shaped like a crescent moon, an Ottoman symbol.',
  'The problem is that there are no reliable documents confirming that story. It is an appealing tale, but not documented history.',
  'What we do know is that Austria had breads called kipferl, shaped like a crescent, long before the modern croissant became popular in France.',
  'In the 19th century, the Austrian businessman August Zang opened a Viennese bakery in Paris. His products helped spread the crescent-shaped bread.',
  'The modern croissant developed in France from Central European traditions. The story of the siege of Vienna is a legend without solid evidence.'],
 ['','La leyenda de los panaderos','Sin documentos fiables','Kipferl austriaco','August Zang en París','Leyenda sin pruebas'],
 ['','The bakers\' legend','No reliable documents','Austrian kipferl','August Zang in Paris','A legend without evidence'],
 ['File:Croissants au beurre (18953292873).jpg','File:Martin Battle of Vienna.jpg','File:Vienna assediata dalle Armi Ottomane gli 12 Lugliio 1683.jpg',
  'File:Topfenkolatsche und Wiener Kipferl IMG 7585.JPG','File:Boulangerie de Paris, XIXe siècle, NJ9828(3).jpg','File:Croissant 3.jpg'],
 ['madera','tormenta','campanas','madera','madera','madera'],
 {0:dict(tipo='dato',valor='1683',valor_en='1683',etiqueta='asedio de Viena',etiqueta_en='siege of Vienna',fuente='Europeana'),
  4:dict(tipo='mapa',region=[-5,25,40,55],puntos=VP,flechas=[[16.37,48.21,2.35,48.86,'']],titulo='De Viena a París',titulo_en='From Vienna to Paris',fuente='Europeana · Natural Earth')})
SPECS['agua']=S(42,'agua-cerveza-medieval','tambor',90,'In the Middle Ages, did nobody drink water because everyone drank beer?',
 ['#historia','#edadmedia','#mitos','#curiosidades','#sabiasque'],['#history','#medieval','#myths','#facts','#didyouknow'],
 ['In many medieval movies, everyone seems to drink beer or wine because water was supposedly too dangerous.',
  'It is true that some water sources could be contaminated and that quality varied a lot between places and periods.',
  'But that does not mean people avoided water altogether. Medieval documents show that water was consumed in many contexts.',
  'In places like Ypres, in present-day Belgium, there were networks of reservoirs, pipes and cisterns. The authorities regulated access to water.',
  'Beer and wine were common drinks in many regions, but they were not the only option. Access to water depended on the city and the period.',
  'So no: medieval Europeans did not live on beer alone. They drank water when they could get it from sources considered safe, and they also had fermented drinks.'],
 ['','Fuentes contaminadas','El agua sí se bebía','Ypres: depósitos y tuberías','Cerveza y vino, no la única opción','Agua de fuentes seguras'],
 ['','Contaminated sources','Water was drunk','Ypres: reservoirs and pipes','Beer and wine, not the only option','Water from safe sources'],
 ['File:Sir Geoffrey Luttrell at table - Luttrell Psalter (c.1325-1335), f.208 - BL Add MS 42130.jpg','File:Woman drawing water from a well, from the manuscript De Universo or "De rerum naturis", Monte Cassino MS Casin 132.jpg',
  'File:Paulus Aegineta – Opera, 1542 – BEIC IE9020308.jpg','File:Vol II (22) Hypra (Ypres). (IA dr vol-ii-22-hypra-ypres-12126169).jpg',
  'File:Herttel Pyrprew, Mendel Band I (1425), Seite 20v.jpg','File:A north east view of Cheapside with the cross and conduit ... LCCN2004667974.jpg'],
 ['madera','lluvia','pluma','lluvia','madera','lluvia'],
 {3:dict(tipo='mapa',region=[-6,14,44,56],puntos=[dict(nombre='Ypres',lon=2.88,lat=50.85)],titulo='Ypres, actual Bélgica',titulo_en='Ypres, present-day Belgium',fuente='Wellcome Collection · Natural Earth'),
  2:dict(tipo='dato',valor='Agua',valor_en='Water',etiqueta='consumida en muchos contextos',etiqueta_en='consumed in many contexts',fuente='Wellcome Collection · New Histories (Sheffield)')})
SPECS['agua']['pad']=0.7; SPECS['agua']['cortinilla_s']=6  # sin añadir texto: pausa entre escenas 0.7 s y cortinilla de 6 s (máx. permitido) para no quedar <60 s
SPECS['croissant']['cama']='pulso'  # la última cápsula del registro de rotación usó pizzicato
