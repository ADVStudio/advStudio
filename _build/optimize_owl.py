"""Оптимізує 3D-скан сови для сайту.
   python3 _build/optimize_owl.py <вхідний.glb> assets/models/owl-figure.glb
   - повертає модель обличчям до камери (кут FACE_DEG навколо осі Y)
   - зменшує текстури до TEX px (JPEG)
   - додає згладжені нормалі
"""
import sys, struct, json, io, math
from PIL import Image

FACE_DEG = -75
TEX = 2048
src, dst = sys.argv[1], sys.argv[2]
d = open(src, 'rb').read()
jl = struct.unpack('<I', d[12:16])[0]; j = json.loads(d[20:20 + jl]); bo = 20 + jl + 8

def bv(i):
    v = j['bufferViews'][i]; o = bo + v.get('byteOffset', 0); return d[o:o + v['byteLength']]

def acc(i):
    a = j['accessors'][i]; raw = bv(a['bufferView'])[a.get('byteOffset', 0):]
    n = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3}[a['type']]; fmt = {5126: 'f', 5125: 'I', 5123: 'H'}[a['componentType']]
    sz = struct.calcsize(fmt); return [struct.unpack_from('<' + fmt * n, raw, k * sz * n) for k in range(a['count'])]

pr = j['meshes'][0]['primitives'][0]
P = acc(pr['attributes']['POSITION']); UV = acc(pr['attributes']['TEXCOORD_0']); I = [x[0] for x in acc(pr['indices'])]

# smooth normals
N = [[0.0, 0.0, 0.0] for _ in P]
for t in range(0, len(I), 3):
    a, b, c = I[t:t + 3]; (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = P[a], P[b], P[c]
    ux, uy, uz = x2 - x1, y2 - y1, z2 - z1; vx, vy, vz = x3 - x1, y3 - y1, z3 - z1
    n = (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)
    for v in (a, b, c):
        N[v][0] += n[0]; N[v][1] += n[1]; N[v][2] += n[2]
for n in N:
    l = math.sqrt(n[0] ** 2 + n[1] ** 2 + n[2] ** 2) or 1; n[0] /= l; n[1] /= l; n[2] /= l

out = bytearray(); views = []; accs = []
def add_view(data, target=None):
    while len(out) % 4: out.append(0)
    off = len(out); out.extend(data); v = {'buffer': 0, 'byteOffset': off, 'byteLength': len(data)}
    if target: v['target'] = target
    views.append(v); return len(views) - 1
def add_acc(view, ctype, count, typ, mn=None, mx=None):
    a = {'bufferView': view, 'componentType': ctype, 'count': count, 'type': typ}
    if mn is not None: a['min'] = mn; a['max'] = mx
    accs.append(a); return len(accs) - 1

pv = add_view(b''.join(struct.pack('<3f', *p) for p in P), 34962)
pa = add_acc(pv, 5126, len(P), 'VEC3', [min(p[i] for p in P) for i in range(3)], [max(p[i] for p in P) for i in range(3)])
nv = add_view(b''.join(struct.pack('<3f', *n) for n in N), 34962); na = add_acc(nv, 5126, len(N), 'VEC3')
uv = add_view(b''.join(struct.pack('<2f', *u) for u in UV), 34962); ua = add_acc(uv, 5126, len(UV), 'VEC2')
iv = add_view(b''.join(struct.pack('<I', i) for i in I), 34963); ia = add_acc(iv, 5125, len(I), 'SCALAR')

images = []
for k, im in enumerate(j['images']):
    img = Image.open(io.BytesIO(bv(im['bufferView'])))
    img = img.resize((TEX, TEX), Image.LANCZOS)
    buf = io.BytesIO(); img.save(buf, 'JPEG', quality=88 if k == 0 else 84, optimize=True)
    images.append({'bufferView': add_view(buf.getvalue()), 'mimeType': 'image/jpeg'})

h = math.radians(FACE_DEG) / 2
nj = {
    'asset': {'version': '2.0', 'generator': 'ADV optimize_owl.py'}, 'scene': 0, 'scenes': [{'nodes': [0]}],
    'nodes': [{'mesh': 0, 'name': 'ADV_Owl', 'rotation': [0, math.sin(h), 0, math.cos(h)]}],
    'meshes': [{'primitives': [{'attributes': {'POSITION': pa, 'NORMAL': na, 'TEXCOORD_0': ua}, 'indices': ia, 'material': 0}]}],
    'materials': [{'name': 'owl', 'normalTexture': {'index': 0}, 'occlusionTexture': {'index': 1},
                   'pbrMetallicRoughness': {'metallicFactor': 0.0, 'roughnessFactor': 0.62, 'baseColorTexture': {'index': 2}}}],
    'textures': [{'sampler': 0, 'source': i} for i in range(len(images))], 'samplers': j.get('samplers', [{}]),
    'images': images, 'accessors': accs, 'bufferViews': views, 'buffers': [{'byteLength': len(out)}],
}
js = json.dumps(nj, separators=(',', ':')).encode(); js += b' ' * ((4 - len(js) % 4) % 4)
while len(out) % 4: out.append(0)
with open(dst, 'wb') as f:
    f.write(struct.pack('<III', 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(out)))
    f.write(struct.pack('<II', len(js), 0x4E4F534A) + js); f.write(struct.pack('<II', len(out), 0x004E4942) + out)
print('written', dst, round((12 + 16 + len(js) + len(out)) / 1048576, 2), 'MB', len(P), 'verts', len(I) // 3, 'tris')
