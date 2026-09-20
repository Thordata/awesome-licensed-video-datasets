from pathlib import Path
import json
import sys

import yaml
from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "dataset-entry.schema.json"


def main():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        schema,
        format_checker=FormatChecker(),
    )
    failures = []

    for path in sorted((ROOT / "datasets").rglob("*.yml")):
        try:
            entry = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception as exc:
            failures.append(f"{path}: YAML error: {exc}")
            continue

        for error in validator.iter_errors(entry):
            location = ".".join(str(part) for part in error.absolute_path)
            failures.append(f"{path}:{location}: {error.message}")

    if failures:
        print("Catalog validation failed:")
        print("\n".join(failures))
        return 1

    print("Catalog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
