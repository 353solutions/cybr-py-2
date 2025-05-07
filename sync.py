# Sync content of two directories
# Copy over files that are missing or newer
from pathlib import Path
from datetime import datetime
from shutil import copy

# Files:
# Path (/var/log/http.log) - pathlib
# File on dist (content) - open

pid_file = Path('/var/run/docker.pid')
print(pid_file)
print('name:', pid_file.name)  # base name
run_dir = pid_file.parent
print('parent:', run_dir)
print('suffix:', pid_file.suffix)

pid2_file = run_dir / 'app.pid'
print(pid2_file)
print('exists:', pid_file.exists())

# ~ stands for "user home directory"
ignore_file = Path('~/.config/git/ignore')
print('ignore:', ignore_file.exists())

ignore_file_expanded = Path('~/.config/git/ignore').expanduser()
print('ignore:', ignore_file_expanded.exists())

for csv_file in Path('data').glob('*.csv'):
    print(csv_file)

# recursive glob
for csv_file in Path('.').glob('**/*.csv'):
    print(csv_file)

info = csv_file.stat()
print(info)
# files on Linux has 3 times:
# - ctime: creation time
# - mtime: modification time
# - atime: access time
# st_mtime, st_atime and st_ctime are numbers (seconds since epoch)
print(datetime.fromtimestamp(info.st_mtime))


def should_copy(src_file: Path, dest_file: Path):
    if not dest_file.exists():
        return True

    src_mtime = src_file.stat().st_mtime
    dest_mtime = dest_file.stat().st_mtime
    return src_mtime > dest_mtime


# IRL: Use the "rsync" utility
def sync(src: Path | str, dest: Path | str):
    """Copy new or non-existing files from src to dest"""
    src, dest = Path(src), Path(dest)
    assert src.is_dir(), f'"{src}" does not exist or is not a directory'

    # if not src.is_dir():
    #     raise ValueError(f'"{src}" does not exist or is not a directory')

    dest.mkdir(exist_ok=True, parents=True)

    for src_file in src.glob('**/*'):
        if src_file.is_dir():
            continue

        dest_file = dest / src_file.relative_to(src)
        if should_copy(src_file, dest_file):
            print(f'{src_file} -> {dest_file}')
            # TODO: Actually copy
            dest_file.parent.mkdir(exist_ok=True, parents=True)
            copy(src_file, dest_file)


sync('data', '/tmp/backup/data')
