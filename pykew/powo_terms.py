from enum import Enum

class Name(Enum):
    full_name = "name"
    common_name = "common name"
    kingdom = "kingdom"
    family = "family"
    genus = "genus"
    species = "species"
    author = "author"

class Characteristic(Enum):
    summary = "summary"
    appearance = "appearance"
    characteristic = "characteristic"
    flower = "flower"
    fruit = "fruit"
    leaf = "leaf"
    inflorescence = "inflorescence"
    seed = "seed"
    cloning = "cloning"
    use = "use"

class Geography(Enum):
    distribution = "location"
