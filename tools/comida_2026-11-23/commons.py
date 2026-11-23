import json, re, sys, os, urllib.request, urllib.parse, html
UA={'User-Agent':'DatosYOciosidadesBot/1.0 (marcosabines@gmail.com)'}
OK=re.compile(r'^(CC BY(-SA)? ?[\d.]*|CC0|Public domain|PD.*|Dominio público)', re.I)
def get(url):
    return json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=40))
def clean(s): return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',s or ''))).strip()
def search(q, n=12):
    p={'action':'query','format':'json','generator':'search','gsrsearch':q+' filetype:bitmap','gsrnamespace':6,'gsrlimit':n,
       'prop':'imageinfo','iiprop':'url|extmetadata|size|mime','iiurlwidth':1600}
    r=get('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p))
    out=[]
    for pg in sorted(r.get('query',{}).get('pages',{}).values(), key=lambda x:x.get('index',0)):
        ii=pg['imageinfo'][0]; m=ii.get('extmetadata',{})
        lic=clean(m.get('LicenseShortName',{}).get('value'))
        if not OK.match(lic) or 'NC' in lic or 'ND' in lic: continue
        if ii['mime'] not in ('image/jpeg','image/png') or ii['width']<700: continue
        out.append({'file':pg['title'],'thumb':ii.get('thumburl') or ii['url'],'w':ii['width'],'h':ii['height'],
                    'artist':clean(m.get('Artist',{}).get('value'))[:120] or 'autor en Commons','lic':lic,'page':ii['descriptionurl']})
    return out
if __name__=='__main__':
    for x in search(sys.argv[1]): print(x['lic'],'|',x['w'],x['h'],'|',x['file'],'|',x['artist'][:50])
def by_title(t):
    p={'action':'query','format':'json','titles':t,'prop':'imageinfo','iiprop':'url|extmetadata|size|mime','iiurlwidth':1600}
    r=get('https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(p))
    pg=list(r['query']['pages'].values())[0]; ii=pg['imageinfo'][0]; m=ii.get('extmetadata',{})
    lic=clean(m.get('LicenseShortName',{}).get('value'))
    assert OK.match(lic) and 'NC' not in lic and 'ND' not in lic, (t,lic)
    return {'file':pg['title'],'thumb':ii.get('thumburl') or ii['url'],'w':ii['width'],'h':ii['height'],
            'artist':clean(m.get('Artist',{}).get('value'))[:120] or 'autor en Commons','lic':lic,'page':ii['descriptionurl']}
