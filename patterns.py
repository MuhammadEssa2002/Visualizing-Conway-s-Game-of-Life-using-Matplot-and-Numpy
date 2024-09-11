from dataclasses import dataclass
import collections
import tomllib
from pathlib import Path

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"
def get_pattern(name, filename=PATTERNS_FILE):
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])

@dataclass
class Pattern:
    name: str
    alive_cells: set[tuple[int, int]]
    @classmethod
    def from_toml(cls, name, toml_data):
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )

def main():
    a = Pattern("Blinker", {(0, 0), (0, 1), (0, 2)})
    c = a.alive_cells & ((0, 0), (0, 4), (0, 5))
    print(c)


if __name__ == "__main__":
    main()