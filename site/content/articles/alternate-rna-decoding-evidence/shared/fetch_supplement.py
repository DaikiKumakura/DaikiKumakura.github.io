"""Download only selected XLSX members of the publisher's public ZIP.

Uses ordinary HTTP byte ranges, validates ZIP CRC/size, and never executes data.
Python 3.10+, standard library only. The complete archive is about 633 MB.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import binascii, hashlib, json, struct, zlib

URL='https://static-content.springer.com/esm/art%3A10.1038%2Fs41586-026-10678-2/MediaObjects/41586_2026_10678_MOESM3_ESM.zip'
ROOT=Path(__file__).resolve().parent

def byte_range(start,end):
    with urlopen(Request(URL,headers={'Range':f'bytes={start}-{end}'}),timeout=30) as r:
        if r.status!=206:raise RuntimeError('Server must support HTTP ranges; refusing full archive download')
        data=r.read(end-start+2)
        if len(data)!=end-start+1:raise RuntimeError('Unexpected range length')
        return data

def main():
    out=ROOT/'sources';out.mkdir(exist_ok=True)
    with urlopen(Request(URL,method='HEAD'),timeout=30) as r:total=int(r.headers['Content-Length'])
    start=max(0,total-65557);tail=byte_range(start,total-1)
    e=struct.unpack_from('<4s4H2LH',tail,tail.rfind(b'PK\x05\x06'))
    cd_size,cd_offset=e[5],e[6]
    directory=tail[cd_offset-start:cd_offset-start+cd_size] if cd_offset>=start else byte_range(cd_offset,cd_offset+cd_size-1)
    i=0;members=[]
    while directory[i:i+4]==b'PK\x01\x02':
        method=struct.unpack_from('<H',directory,i+10)[0]
        crc,compressed,size=struct.unpack_from('<III',directory,i+16)
        nl,xl,cl=struct.unpack_from('<HHH',directory,i+28)
        offset=struct.unpack_from('<I',directory,i+42)[0]
        name=directory[i+46:i+46+nl].decode('utf-8')
        if any(Path(name).name.startswith(s) for s in ('Supplementary_Data_2.','Supplementary_Data_3.','Supplementary_Data_8.')):
            if compressed>10_000_000 or size>20_000_000:raise RuntimeError('Selected file exceeds size limit')
            dest=out/Path(name).name
            if dest.exists():data=dest.read_bytes()
            else:
                header=byte_range(offset,offset+29)
                if header[:4]!=b'PK\x03\x04':raise RuntimeError('Missing local ZIP header')
                local_nl,local_xl=struct.unpack_from('<HH',header,26)
                data_offset=offset+30+local_nl+local_xl
                packed=byte_range(data_offset,data_offset+compressed-1)
                data=zlib.decompress(packed,-15) if method==8 else packed
            if len(data)!=size or binascii.crc32(data)&0xffffffff!=crc:raise RuntimeError('ZIP CRC or size mismatch')
            if dest.exists() and dest.read_bytes()!=data:raise RuntimeError('Existing source differs; do not overwrite')
            dest.write_bytes(data)
            members.append({'member':name,'file':dest.name,'bytes':size,'crc32':f'{crc:08x}','sha256':hashlib.sha256(data).hexdigest()})
        i+=46+nl+xl+cl
    if len(members)!=3:raise RuntimeError('Expected exactly three selected tables')
    record={'source':URL,'archive_bytes':total,'method':'HTTP byte ranges; individual ZIP member CRC and size verified','members':members}
    (out/'download-manifest.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
