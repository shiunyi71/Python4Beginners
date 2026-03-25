import json
with open("example/HP12_example.ipynb", "r", encoding="utf-8") as f:
    data = json.load(f)
for i, c in enumerate(data["cells"]):
    cell_id = c.get("id", "no-id")
    cell_type = c.get("cell_type", "?")
    source_preview = str(c.get("source", [""])[:2])[:50]
    print(f"{i}: id={cell_id} type={cell_type} src={source_preview}")
