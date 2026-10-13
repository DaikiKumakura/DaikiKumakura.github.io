import zipfile,re,sys
from xml.etree import ElementTree as ET
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def read(path):
    z=zipfile.ZipFile(path)
    ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('m:si',ns):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%ns['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml')); rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rid={r.get('Id'):r.get('Target') for r in rels}
    sheets={}
    for s in wb.find('m:sheets',ns):
        tgt=rid[s.get('{%s}id'%ns['r'])]; tgt=tgt.lstrip('/'); tgt=tgt if tgt.startswith('xl/') else 'xl/'+tgt
        rows=[]
        for row in ET.fromstring(z.read(tgt)).iter('{%s}row'%ns['m']):
            cells={}
            for c in row.findall('m:c',ns):
                col=re.match(r'[A-Z]+',c.get('r')).group(0); v=c.find('m:v',ns); t=c.get('t')
                if v is None: 
                    isel=c.find('m:is',ns); val=''.join(x.text or '' for x in isel.iter('{%s}t'%ns['m'])) if isel is not None else None
                else: val=ss[int(v.text)] if t=='s' else v.text
                cells[col]=val
            rows.append(cells)
        sheets[s.get('name')]=rows
    return sheets
if __name__=='__main__':
    for p in sys.argv[1:]:
        sh=read(p); print(p)
        for k,v in sh.items(): print('  ',k,len(v),'rows')
