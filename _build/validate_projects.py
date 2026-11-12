"""Перевіряє data/projects.json: валідний JSON, обов'язкові поля, унікальні slug, існування обкладинок.
   python3 _build/validate_projects.py      (запускається й автоматично на GitHub — див. .github/workflows)"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATS = {"business", "landing", "ecommerce", "app", "bot", "other"}
TYPES = {"client", "concept"}
errors, warns = [], []

try:
    data = json.load(open(os.path.join(ROOT, "data", "projects.json"), encoding="utf-8"))
except json.JSONDecodeError as e:
    print(f"❌ data/projects.json — помилка JSON у рядку {e.lineno}, позиція {e.colno}: {e.msg}")
    print("   Найчастіше: пропущена кома між проєктами або зайва кома після останнього поля.")
    sys.exit(1)

seen = set()
for i, p in enumerate(data.get("projects", []), 1):
    name = f"проєкт #{i} ({p.get('slug') or p.get('title') or '?'})"
    for f in ("slug", "title", "type", "category", "cover", "summary"):
        if not p.get(f):
            errors.append(f"{name}: немає поля «{f}»")
    slug = p.get("slug", "")
    if slug and not re.fullmatch(r"[a-z0-9-]+", slug):
        errors.append(f"{name}: slug лише малими латинськими літерами, цифрами й дефісом")
    if slug in seen:
        errors.append(f"{name}: slug «{slug}» вже використано")
    seen.add(slug)
    if p.get("type") and p["type"] not in TYPES:
        errors.append(f"{name}: type має бути одним із {sorted(TYPES)}")
    if p.get("category") and p["category"] not in CATS:
        errors.append(f"{name}: category має бути одним із {sorted(CATS)}")
    cover = p.get("cover", "")
    if cover and not cover.startswith("http") and not os.path.exists(os.path.join(ROOT, cover)):
        errors.append(f"{name}: файл обкладинки не знайдено — {cover}")
    s = p.get("summary")
    if isinstance(s, dict) and not (s.get("uk") and s.get("en")):
        warns.append(f"{name}: бажано заповнити summary і uk, і en")
    if not p.get("url"):
        warns.append(f"{name}: немає url — картка не вестиме на сайт проєкту")

for w in warns: print("⚠️ ", w)
if errors:
    for e in errors: print("❌", e)
    sys.exit(1)
print(f"✅ data/projects.json у порядку: {len(seen)} проєктів")
