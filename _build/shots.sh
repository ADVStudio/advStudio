#!/bin/zsh
# Оновлює превʼю концептів для блоку «Концепти» на головній (assets/img/concepts/*.webp).
# Потрібен запущений локальний сервер:  python3 -m http.server 5173   (з кореня сайту)
# Запуск:  zsh _build/shots.sh
set -e
ROOT="${0:A:h:h}"
TMP="$(mktemp -d)"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for s in budmist kava-lab dentalia flowdesk; do
  for l in "" "en/"; do
    n="$s${l:+-en}"
    "$CHROME" --headless=new --disable-gpu --hide-scrollbars --user-data-dir="$TMP/p-$n" \
      --window-size=1440,900 --virtual-time-budget=20000 \
      --screenshot="$TMP/$n.png" "http://localhost:5173/concepts/$s/$l?shot=1&t=$(date +%s)" >/dev/null 2>&1
  done
done
python3 -I - "$TMP" "$ROOT/assets/img/concepts" <<'EOF'
import sys, glob, os
from PIL import Image
src, out = sys.argv[1:]
os.makedirs(out, exist_ok=True)
for p in glob.glob(src + '/*.png'):
    im = Image.open(p).convert('RGB'); w, h = im.size
    im = im.crop((0, 0, w, int(w * 9 / 16))).resize((1280, 720), Image.LANCZOS)
    im.save(os.path.join(out, os.path.basename(p)[:-4] + '.webp'), 'WEBP', quality=82, method=6)
    print('updated', os.path.basename(p)[:-4])
EOF
echo "Готово. Збільште VERSION у _build/build.py і запустіть python3 _build/build.py, щоб скинути кеш браузера."
