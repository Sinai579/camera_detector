from pathlib import Path

labels_dir = Path("camera_detector\Husky")

for txt_file in labels_dir.rglob("*.txt"):
    with open(txt_file, "r") as f:
        lines = f.readlines()

    new_lines = []

    for line in lines:
        parts = line.strip().split()

        if parts and parts[0] == "15":
            parts[0] = "2"

        new_lines.append(" ".join(parts))

    with open(txt_file, "w") as f:
        f.write("\n".join(new_lines) + "\n")

print("Conversión terminada.")