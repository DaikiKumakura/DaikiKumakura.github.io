"""Link unambiguous numbered citations to an article's numbered references."""
import re
from html.parser import HTMLParser

HEADING = re.compile(r'<h2\b[^>]*>\s*[^<]*(?:文献|参考資料|出典|References|Reference list|Sources)[^<]*</h2>', re.I)
NEXT = re.compile(r'<h[12]\b', re.I)
MARKER = re.compile(r'(?<!\[)\[\s*(\d+(?:\s*[,，–-]\s*\d+)*)\s*\]|［\s*(\d+(?:\s*[,，–-]\s*\d+)*)\s*］')

class CitationText(HTMLParser):
    def __init__(self, valid):
        super().__init__(convert_charrefs=False);self.valid=valid;self.stack=[];self.output=[]
    def handle_starttag(self,tag,attrs):
        self.output.append(self.get_starttag_text())
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append((tag,dict(attrs)))
    def handle_startendtag(self,tag,attrs):self.output.append(self.get_starttag_text())
    def handle_endtag(self,tag):
        self.output.append('</'+tag+'>')
        if self.stack and self.stack[-1][0]==tag:self.stack.pop()
    def handle_data(self,data):
        if any(t in {'a','code','pre','script','style','h1','h2','h3','h4','h5','h6'} or (t=='span' and 'math' in a.get('class','').split()) for t,a in self.stack):
            self.output.append(data);return
        def link(m):
            text=m.group(1) or m.group(2)
            numbers=re.findall(r'\d+',text)
            if not all(int(n) in self.valid for n in numbers):return m.group(0)
            text=re.sub(r'\s*[,，]\s*',', ',text)
            return '('+re.sub(r'\d+',lambda n:'<a class="reference-link" href="#ref-'+n[0]+'">'+n[0]+'</a>',text)+')'
        data=MARKER.sub(link,data)
        def located(m):
            if int(m[1]) not in self.valid:return m[0]
            return '(<a class="reference-link" href="#ref-'+m[1]+'">'+m[1]+'</a>, '+m[2]+')'
        data=re.sub(r'[\[［](\d+),\s*((?:印字|印刷|PDF|printed|Table|Fig|pp?\.)[^\]］]+)[\]］]',located,data)
        self.output.append(data)
    def handle_entityref(self,name):self.output.append('&'+name+';')
    def handle_charref(self,name):self.output.append('&#'+name+';')
    def handle_comment(self,data):self.output.append('<!--'+data+'-->')
    def handle_decl(self,decl):self.output.append('<!'+decl+'>')

def link_numbered_references(body):
    headings=list(HEADING.finditer(body))
    if len(headings)!=1:return body
    heading=headings[0];endmatch=NEXT.search(body,heading.end());end=endmatch.start() if endmatch else len(body)
    section=body[heading.end():end]
    lists=list(re.finditer(r'<ol>\s*([\s\S]*?)</ol>',section,re.I))
    if len(lists)!=1:return body
    listing=lists[0]
    if '<ol' in listing[1] or '<ul' in listing[1]:return body
    entries=list(re.finditer(r'<li(?:\s[^>]*)?>[\s\S]*?</li>',listing[1],re.I))
    if not entries:return body
    if re.search(r'\bid="ref-\d+"',body):return body
    count=0
    def add_id(m):
        nonlocal count
        count+=1
        return '<li id="ref-'+str(count)+'">'
    updated=re.sub(r'<li>',add_id,listing[1],flags=re.I)
    if count!=len(entries):return body
    newsection=section[:listing.start(1)]+updated+section[listing.end(1):]
    parser=CitationText(set(range(1,count+1)));parser.feed(body[:heading.start()]);parser.close()
    return ''.join(parser.output)+body[heading.start():heading.end()]+newsection+body[end:]
