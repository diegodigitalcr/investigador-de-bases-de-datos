"""Create one Claude upload ZIP for each language using only the standard library."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist"
PACKAGES = {
    "investigador-de-bases-de-datos": ROOT,
    "company-database-researcher": ROOT / "en" / "company-database-researcher",
}
INCLUDED_FILES = ("SKILL.md", "references/workbook-spec.md", "LICENSE")


def main() -> None:
    OUTPUT.mkdir(exist_ok=True)
    for name, source_dir in PACKAGES.items():
        archive_path = OUTPUT / f"{name}.zip"
        with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
            for relative_path in INCLUDED_FILES:
                source = source_dir / relative_path
                if not source.is_file():
                    raise FileNotFoundError(source)
                archive.write(source, arcname=f"{name}/{relative_path}")
        print(archive_path)


if __name__ == "__main__":
    main()
