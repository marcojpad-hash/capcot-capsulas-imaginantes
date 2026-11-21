# Lote 23-28 nov 2026 (+2 reservas). Reutiliza guiones del lote 14-nov no publicados (render fallido por TTS) con cierres reescritos; tardigrado nuevo.
import sys,copy
sys.path.insert(0,'/workspace/capcot_prod_20261114')
from contenido import C as C0
C={}
PLAN=[('nudillos','2026-11-23','07:00'),('pollo','2026-11-24','17:00'),('medusa','2026-11-25','07:00'),
      ('platano','2026-11-26','17:00'),('microondas','2026-11-27','07:00'),('mareo','2026-11-28','17:00'),
      ('huevo',None,None),('tardigrado',None,None)]
CIERRE={
 'nudillos':'No es un ejercicio recomendado; si duele o se hincha, consulta a un médico. Y si el crac nace de un hueco y no de una burbuja, ¿qué otros ruidos de tu cuerpo seguirán mal explicados? Esto fue Datos y ociosidades.',
 'pollo':'Las bacterias del pollo se eliminan al cocinarlo bien, no con el chorro de agua. Entonces, ¿qué otro hábito de limpieza en tu cocina estará regando justo lo que querías quitar? Esto fue Datos y ociosidades.',
 'mareo':'Así que ese mareo no es debilidad: es tu cerebro tratando de resolver una contradicción. Mira lejos y respira. ¿Qué otras peleas entre tus sentidos estará arreglando tu cerebro sin avisarte? Esto fue Datos y ociosidades.',
 'huevo':'Luego guárdalo con cáscara en el refri; así dura hasta una semana. Un huevo perfecto no es suerte: es tiempo y frío. ¿Qué otro color raro de tu cocina será pura química? Esto fue Datos y ociosidades.',
}
COVER={'nudillos':'¿QUÉ PASA\nCUANDO\nTRUENAS\nLOS DEDOS?','pollo':'¿LAVAS EL\nPOLLO\nCRUDO?\nMEJOR NO'}
for k,f,h in PLAN:
  if k in C0:
    v=copy.deepcopy(C0[k]); v['fecha'],v['hora']=f,h
    if k in CIERRE: v['narr'][-1]=CIERRE[k]
    if k in COVER: v['cover']=COVER[k]
    C[k]=v
C['tardigrado']=dict(fecha=None,hora=None,nicho='#animales',estilo='carta_tarot',musica='menor_calma',
 title='Revivió tras 30 años congelado: el tardígrado',cover='REVIVIÓ\nTRAS 30 AÑOS\nCONGELADO',titulo_corto='30 años congelado',
 encuadres=['general','detalle','macro','general','contrapicado','macro','detalle','general','general'],
 narr=[
 'Un musgo de la Antártida pasó treinta años en un congelador. Le pusieron agua, esperaron… y algo empezó a caminar.',
 'Y esto te toca más de lo que crees: ese bicho diminuto podría enseñarnos a proteger nuestras propias células.',
 'Era un tardígrado, también llamado oso de agua: un animal microscópico con ocho patitas que vive en musgos y charcos.',
 'El musgo se recogió en mil novecientos ochenta y tres y se guardó a veinte grados bajo cero durante treinta años y medio.',
 'Revivieron dos tardígrados y de un huevo nació otro. Uno de ellos y la cría tuvieron descendencia varias veces.',
 '¿Cómo aguantan sin agua? Al secarse, sus proteínas únicas se vuelven una especie de vidrio. Eso es vitrificar: endurecerse sin formar cristales.',
 'Sin esas proteínas no sobrevive al secado; y puestas en levaduras, las vuelven más resistentes.',
 'Otra proteína suya, Dsup, en células humanas de laboratorio redujo cerca de cuarenta por ciento el daño de los rayos X al ADN.',
 'Ojo: no es indestructible, y unas células en un plato no son una persona. Pero si un animal de musgo pausa su vida tres décadas, ¿qué más sabrá hacer que aún no entendemos? Esto fue Datos y ociosidades.'],
 sources=[
  dict(id='SRC-001',cita_corta='Tsujimoto M., Imura S., Kanda H. (2016). Recovery and reproduction of an Antarctic tardigrade retrieved from a moss sample frozen for over 30 years. Cryobiology 72(1): 78-81.',url='https://pubmed.ncbi.nlm.nih.gov/26724522/',doi='10.1016/j.cryobiol.2015.12.003',
       supports=['Musgo recogido en la Antártida en 1983, guardado a -20 °C durante 30.5 años','Revivieron dos individuos y se desarrolló un huevo','Uno de los revividos y la cría se reprodujeron repetidamente','Récord más largo de supervivencia registrado para tardígrados']),
  dict(id='SRC-002',cita_corta='Boothby T. C. et al. (2017). Tardigrades Use Intrinsically Disordered Proteins to Survive Desiccation. Molecular Cell 65(6): 975-984.',url='https://pubmed.ncbi.nlm.nih.gov/28306513/',doi='10.1016/j.molcel.2017.02.018',
       supports=['Tardígrados: animales microscópicos que sobreviven la desecación','Proteínas exclusivas de tardígrados necesarias para tolerar el secado','Al expresarse en otros sistemas (levadura, bacterias) aumentan su tolerancia','Las proteínas vitrifican (sólido amorfo no cristalino) al secarse']),
  dict(id='SRC-003',cita_corta='Hashimoto T. et al. (2016). Extremotolerant tardigrade genome and improved radiotolerance of human cultured cells by tardigrade-unique protein. Nature Communications 7: 12808.',url='https://www.nature.com/articles/ncomms12808',doi='10.1038/ncomms12808',
       supports=['También llamados osos de agua','Proteína Dsup en células humanas cultivadas suprime ~40% el daño al ADN por rayos X']),
 ])
P_TARDI=[
 "wide establishing shot of a frozen green moss clump inside an antique laboratory freezer, frost crystals, a single drop of water falling onto it, mystical glow",
 "close detail of a human hand holding a glass petri dish with a tiny glowing creature, cells drawn like stars around it",
 "macro view of a cute chubby eight-legged water bear tardigrade walking on a moss leaf, round body, tiny claws",
 "wide view of a snowy Antarctic landscape with a researcher in a red coat collecting moss into a small bag",
 "low-angle view of two small tardigrades waking up beside a hatching round egg, warm light, gentle celebration",
 "macro view of a dried curled-up tardigrade turning into translucent glass, amber light passing through it",
 "detail of yeast cells and bacteria drawn as small round and rod shapes glowing with protective shields",
 "wide view of a stylized DNA double helix shielded by a glowing tardigrade-shaped guardian from incoming x-ray beams",
 "wide calm view of a tardigrade standing on a moss hill under a starry night sky, contemplative mood"]
