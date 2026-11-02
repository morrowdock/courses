import hashlib, json, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate():
 with tempfile.TemporaryDirectory() as tmp:
  exe=Path(tmp)/'validate'
  subprocess.run(['swiftc',str(ROOT/'validator/CourseBundle.swift'),str(ROOT/'validator/main.swift'),'-o',str(exe)],check=True)
  for path in ROOT.glob('*/bundle.json'):
   p=json.loads((path.parent/'provenance.json').read_text())
   assert p['license']=='CC-BY-SA-4.0' and p['author'] and p['sources']
   assert {a['path'] for a in p['assets']} == {f.name for f in path.parent.iterdir() if f.name != 'provenance.json'}
   for asset in p['assets']:
    assert asset['path']=='bundle.json' and asset['origin'] and asset['rightsHolder'] and asset['license']=='CC-BY-SA-4.0'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==asset['sha256']
   subprocess.run([str(exe),str(path)],check=True)
if __name__=='__main__':validate()
