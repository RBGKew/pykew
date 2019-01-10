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

class Filters(Enum):
    accepted = "accepted_names"
    has_images = "has_images"
    families = "families_f"
    genera = "genus_f"
    species = "species_f"
    infraspecies = "infraspecific_f"
