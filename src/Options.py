from dataclasses import dataclass


DEFAULT_DIR = "./data/"


@dataclass
class Options:
    is_recursive: bool = False
    recursion_depth: int = 1
    save_dest: str = DEFAULT_DIR
    url: str | None = None
