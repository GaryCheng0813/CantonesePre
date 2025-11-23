import csv
import json

INPUT_FILE = 'dict.csv'       # 你的原始字典 CSV 文件
OUTPUT_FILE = 'char2jp.json'  # 输出的繁体字 → Jyutping 映射

mapping = {}

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        trad = (row.get('繁體') or '').strip()
        jp = (row.get('拼音') or '').strip()
        if not trad or not jp:
            continue
        # 只要单个繁体字
        if len(trad) != 1:
            continue
        # 已经记录过的字就不再覆盖（避免多音字冲掉第一条）
        if trad in mapping:
            continue
        mapping[trad] = jp

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)

print(f'共导出 {len(mapping)} 个繁体字到 {OUTPUT_FILE}')