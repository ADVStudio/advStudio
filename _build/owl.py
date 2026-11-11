"""Генератор low-poly 3D-сови ADV у форматі GLB (без зовнішніх бібліотек).

    python3 _build/owl.py

Створює assets/models/owl.glb (маскот) та owl-business/landing/ecom.glb (для вкладок послуг).
"""
import json
import math
import os
import random
import struct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "models")


def hexc(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


# ---------- геометрія ----------
def ellipsoid(c, r, seg=8, rings=6, jitter=0.0, seed=1, rot=(0, 0, 0)):
    rnd = random.Random(seed)
    verts = []
    for i in range(rings + 1):
        th = math.pi * i / rings
        row = []
        for j in range(seg):
            ph = 2 * math.pi * j / seg + (math.pi / seg if i % 2 else 0)
            x, y, z = math.sin(th) * math.cos(ph), math.cos(th), math.sin(th) * math.sin(ph)
            if 0 < i < rings and jitter:
                k = 1 + rnd.uniform(-jitter, jitter)
                x, y, z = x * k, y * k, z * k
            row.append((x * r[0], y * r[1], z * r[2]))
        verts.append(row)
    tris = []
    for i in range(rings):
        for j in range(seg):
            a, b = verts[i][j], verts[i][(j + 1) % seg]
            c2, d = verts[i + 1][j], verts[i + 1][(j + 1) % seg]
            if i == 0:
                tris.append((a, d, c2))
            elif i == rings - 1:
                tris.append((a, b, c2))
            else:
                tris += [(a, b, d), (a, d, c2)]
    return xform(tris, c, rot)


def cone(c, r, h, seg=5, rot=(0, 0, 0)):
    tip = (0, h, 0)
    ring = [(r * math.cos(2 * math.pi * k / seg), 0, r * math.sin(2 * math.pi * k / seg)) for k in range(seg)]
    tris = []
    for k in range(seg):
        a, b = ring[k], ring[(k + 1) % seg]
        tris += [(a, tip, b), (a, b, (0, 0, 0))]
    return xform(tris, c, rot)


def box(c, s, rot=(0, 0, 0)):
    x, y, z = (v / 2 for v in s)
    p = [(-x, -y, -z), (x, -y, -z), (x, y, -z), (-x, y, -z), (-x, -y, z), (x, -y, z), (x, y, z), (-x, y, z)]
    f = [(0, 2, 1), (0, 3, 2), (4, 5, 6), (4, 6, 7), (0, 1, 5), (0, 5, 4), (3, 6, 2), (3, 7, 6), (0, 4, 7), (0, 7, 3), (1, 2, 6), (1, 6, 5)]
    return xform([(p[a], p[b], p[d]) for a, b, d in f], c, rot)


def xform(tris, c, rot):
    rx, ry, rz = (math.radians(a) for a in rot)

    def t(v):
        x, y, z = v
        y, z = y * math.cos(rx) - z * math.sin(rx), y * math.sin(rx) + z * math.cos(rx)
        x, z = x * math.cos(ry) + z * math.sin(ry), -x * math.sin(ry) + z * math.cos(ry)
        x, y = x * math.cos(rz) - y * math.sin(rz), x * math.sin(rz) + y * math.cos(rz)
        return (x + c[0], y + c[1], z + c[2])
    return [tuple(t(v) for v in tri) for tri in tris]


def mirror(tris):
    return [tuple((-v[0], v[1], v[2]) for v in (tri[0], tri[2], tri[1])) for tri in tris]


# ---------- сова ----------
def owl(accent="#8b3dff", accent2="#b6ff3b", prop=None):
    P = {}  # material -> tris

    def add(mat, tris):
        P.setdefault(mat, []).extend(tris)

    add("body", ellipsoid((0, 0.72, 0), (0.56, 0.68, 0.5), 9, 7, 0.06, 3))
    add("belly", ellipsoid((0, 0.64, 0.27), (0.38, 0.48, 0.3), 8, 6, 0.03, 5))
    add("body", ellipsoid((0, 1.42, 0.02), (0.5, 0.42, 0.44), 9, 6, 0.05, 7))
    # лицьовий диск
    for s in (1, -1):
        add("face", ellipsoid((0.17 * s, 1.42, 0.32), (0.2, 0.21, 0.1), 7, 5, 0.04, 11))
        add("eye", ellipsoid((0.17 * s, 1.44, 0.4), (0.105, 0.105, 0.06), 8, 5, 0, 13))
        add("pupil", ellipsoid((0.17 * s, 1.44, 0.455), (0.05, 0.05, 0.02), 6, 4, 0, 17))
    # брова-«штрих» як у логотипі
    add("accent", box((-0.15, 1.6, 0.37), (0.18, 0.045, 0.06), (0, 0, 14)))
    add("accent", box((0.15, 1.6, 0.37), (0.18, 0.045, 0.06), (0, 0, -14)))
    # дзьоб
    add("beak", cone((0, 1.37, 0.43), 0.06, 0.14, 4, (115, 0, 0)))
    # вушка-пір'я
    add("tuft", cone((0.3, 1.68, -0.02), 0.12, 0.2, 4, (-10, 0, -42)))
    add("tuft", cone((-0.3, 1.68, -0.02), 0.12, 0.2, 4, (-10, 0, 42)))
    # крила
    w = ellipsoid((0.52, 0.8, -0.02), (0.13, 0.5, 0.36), 7, 6, 0.06, 19, (0, 0, -10))
    add("wing", w)
    add("wing", mirror(w))
    # хвіст і лапки
    add("wing", cone((0, 0.22, -0.4), 0.16, 0.36, 4, (-120, 0, 0)))
    for s in (1, -1):
        for k in (-1, 0, 1):
            add("beak", cone((0.16 * s + 0.05 * k, 0.05, 0.36), 0.035, 0.16, 4, (90, 0, 0)))
    # підставка
    add("stand", ellipsoid((0, -0.02, 0), (0.75, 0.06, 0.75), 12, 2, 0, 23))
    add("glow", ellipsoid((0, -0.035, 0), (0.78, 0.035, 0.78), 12, 2, 0, 29))

    if prop == "laptop":
        add("prop", box((0, 0.66, 0.62), (0.62, 0.035, 0.38), (-12, 0, 0)))
        add("prop", box((0, 0.86, 0.46), (0.62, 0.4, 0.03), (-25, 0, 0)))
        add("screen", box((0, 0.86, 0.48), (0.54, 0.32, 0.01), (-25, 0, 0)))
    elif prop == "rocket":
        add("prop", ellipsoid((0.42, 0.95, 0.55), (0.1, 0.28, 0.1), 6, 5, 0, 31, (0, 0, -20)))
        add("accent2", cone((0.51, 1.19, 0.55), 0.1, 0.18, 6, (0, 0, -20)))
        add("glow", cone((0.35, 0.72, 0.55), 0.07, 0.2, 5, (180, 0, -20)))
    elif prop == "bag":
        add("prop", box((0, 0.5, 0.62), (0.46, 0.44, 0.2)))
        add("accent2", box((0, 0.5, 0.725), (0.3, 0.08, 0.01)))
        for dx in (-0.1, 0.1):
            add("accent2", box((dx, 0.78, 0.62), (0.03, 0.14, 0.03)))
        add("accent2", box((0, 0.85, 0.62), (0.23, 0.03, 0.03)))

    mats = {
        "body": dict(c="#17131f", r=0.6), "belly": dict(c=accent, r=0.45, m=0.15),
        "face": dict(c="#2b2438", r=0.55), "eye": dict(c=accent2, e=accent2, ei=0.55, r=0.3),
        "pupil": dict(c="#050407", r=0.2), "beak": dict(c="#c9b2ff", r=0.4),
        "accent": dict(c=accent, r=0.35, m=0.2), "accent2": dict(c=accent2, e=accent2, r=0.4),
        "wing": dict(c="#241b38", r=0.55), "tuft": dict(c="#3a2766", r=0.5), "stand": dict(c="#0b0a0f", r=0.85, m=0.0),
        "glow": dict(c=accent, e=accent, r=0.5), "prop": dict(c="#d9d4e4", r=0.35, m=0.4),
        "screen": dict(c="#120c22", e=accent, r=0.2),
    }
    return P, mats


# ---------- GLB ----------
def write_glb(path, P, mats):
    bin_ = bytearray()
    j = {"asset": {"version": "2.0", "generator": "ADV owl.py"}, "scene": 0, "scenes": [{"nodes": [0]}],
         "nodes": [{"mesh": 0, "name": "ADV_Owl"}], "meshes": [{"primitives": []}], "materials": [],
         "buffers": [], "bufferViews": [], "accessors": []}
    for name, tris in P.items():
        m = mats[name]
        mat = {"name": name, "doubleSided": True, "pbrMetallicRoughness": {"baseColorFactor": hexc(m["c"]) + [1], "metallicFactor": m.get("m", 0.05), "roughnessFactor": m.get("r", 0.5)}}
        if "e" in m:
            mat["emissiveFactor"] = [v * m.get("ei", 0.9) for v in hexc(m["e"])]
        j["materials"].append(mat)
        pos, nor = [], []
        for a, b, c in tris:
            u = [b[i] - a[i] for i in range(3)]
            v = [c[i] - a[i] for i in range(3)]
            n = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
            ln = math.sqrt(sum(x * x for x in n)) or 1
            n = [x / ln for x in n]
            for p in (a, b, c):
                pos.append(p)
                nor.append(n)
        for data, typ in ((pos, "pos"), (nor, "nor")):
            off = len(bin_)
            for p in data:
                bin_ += struct.pack("<3f", *p)
            j["bufferViews"].append({"buffer": 0, "byteOffset": off, "byteLength": len(data) * 12, "target": 34962})
            acc = {"bufferView": len(j["bufferViews"]) - 1, "componentType": 5126, "count": len(data), "type": "VEC3"}
            if typ == "pos":
                acc["min"] = [min(p[i] for p in data) for i in range(3)]
                acc["max"] = [max(p[i] for p in data) for i in range(3)]
            j["accessors"].append(acc)
        n_acc = len(j["accessors"])
        j["meshes"][0]["primitives"].append({"attributes": {"POSITION": n_acc - 2, "NORMAL": n_acc - 1}, "material": len(j["materials"]) - 1})
    j["buffers"].append({"byteLength": len(bin_)})
    js = json.dumps(j, separators=(",", ":")).encode()
    js += b" " * ((4 - len(js) % 4) % 4)
    bin_ += b"\0" * ((4 - len(bin_) % 4) % 4)
    with open(path, "wb") as f:
        f.write(struct.pack("<III", 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(bin_)))
        f.write(struct.pack("<II", len(js), 0x4E4F534A) + js)
        f.write(struct.pack("<II", len(bin_), 0x004E4942) + bin_)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    variants = {
        "owl": dict(),
        "owl-business": dict(prop="laptop"),
        "owl-landing": dict(accent="#7cc22a", accent2="#b6ff3b", prop="rocket"),
        "owl-ecom": dict(accent="#c25cff", accent2="#ffd36b", prop="bag"),
    }
    for name, kw in variants.items():
        P, mats = owl(**kw)
        write_glb(os.path.join(OUT, name + ".glb"), P, mats)
        print("written", name + ".glb", sum(len(t) for t in P.values()), "tris")
