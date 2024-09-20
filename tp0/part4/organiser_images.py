from pathlib import Path
import shutil

for input_filename in Path("images").iterdir():
    _, month, day, obj, i = input_filename.stem.split("_")
    output_dir = Path("clean") / month / obj
    output_dir.mkdir(exist_ok=True, parents=True)
    output_filename = output_dir / f"{i}.jpg"
    shutil.copy(input_filename, output_filename)
