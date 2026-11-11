"""Рендерить кадри обертання сови для прелоадера (assets/img/owl-spin-N.webp).
   python3 _build/owl_frames.py   (джерело — оригінальний скан, шлях у SRC)"""
import sys, struct, json, io, math, os
from PIL import Image, ImageDraw, ImageFilter
SRC = sys.argv[1] if len(sys.argv) > 1 else 'assets/models/owl-figure.glb'
OUT = 'assets/img'; FRAMES = 12; FACE = -75; SS = 2; W = H = 360
d = open(SRC, 'rb').read(); jl = struct.unpack('<I', d[12:16])[0]; j = json.loads(d[20:20 + jl]); bo = 20 + jl + 8
def bv(i): v = j['bufferViews'][i]; o = bo + v.get('byteOffset', 0); return d[o:o + v['byteLength']]
def acc(i):
    a = j['accessors'][i]; raw = bv(a['bufferView'])[a.get('byteOffset', 0):]
    n = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3}[a['type']]; f = {5126: 'f', 5125: 'I', 5123: 'H'}[a['componentType']]; z = struct.calcsize(f)
    return [struct.unpack_from('<' + f * n, raw, k * z * n) for k in range(a['count'])]
pr = j['meshes'][0]['primitives'][0]
P = acc(pr['attributes']['POSITION']); UV = acc(pr['attributes']['TEXCOORD_0']); I = [x[0] for x in acc(pr['indices'])]
rot0 = 0
if j['nodes'][0].get('rotation'): rot0 = math.degrees(2 * math.asin(j['nodes'][0]['rotation'][1]))
else: rot0 = FACE
img_i = j['textures'][j['materials'][0]['pbrMetallicRoughness']['baseColorTexture']['index']]['source']
tex = Image.open(io.BytesIO(bv(j['images'][img_i]['bufferView']))).convert('RGB').resize((1024, 1024)); px = tex.load()
tris = []
for t in range(0, len(I), 3):
    vs = I[t:t + 3]; u = sum(UV[v][0] for v in vs) / 3; w = sum(UV[v][1] for v in vs) / 3
    (x1, y1, z1), (x2, y2, z2), (x3, y3, z3) = [P[v] for v in vs]
    n = ((y2 - y1) * (z3 - z1) - (z2 - z1) * (y3 - y1), (z2 - z1) * (x3 - x1) - (x2 - x1) * (z3 - z1), (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1))
    L = math.sqrt(sum(c * c for c in n)) or 1
    tris.append((vs, px[min(1023, int(u * 1024)), min(1023, int(w * 1024))], (n[0] / L, n[1] / L, n[2] / L)))
for k in range(FRAMES):
    a = math.radians(rot0 + 360 * k / FRAMES); ca, sa = math.cos(a), math.sin(a)
    img = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0)); dr = ImageDraw.Draw(img); buf = []
    for vs, col, nn in tris:
        pts = []
        for v in vs:
            x, y, z = P[v]; xr = x * ca + z * sa; zr = -x * sa + z * ca
            pts.append((W * SS / 2 + xr * 260 * SS, H * SS - 12 * SS - y * 275 * SS, zr))
        nz = -nn[0] * sa + nn[2] * ca; ny = nn[1]
        sh = 0.5 + 0.38 * abs(nz) + 0.18 * max(0, ny)
        buf.append((sum(q[2] for q in pts) / 3, [q[:2] for q in pts], tuple(min(255, int(c * sh)) for c in col) + (255,)))
    buf.sort(key=lambda q: q[0])
    for _, pp, c in buf: dr.polygon(pp, fill=c)
    img = img.resize((W, H), Image.LANCZOS)
    img.save(os.path.join(OUT, f'owl-spin-{k}.webp'), 'WEBP', quality=82, method=6)
    print('frame', k)
