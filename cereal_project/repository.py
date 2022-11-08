from dagster import repository


# ---------------------------------------------------
# Option 1, import assets by name individually

from cereal_project.assets.cereal_assets import cereals, nabisco_cereals


@repository
def cereal_project():
    return [cereals, nabisco_cereals]


# ---------------------------------------------------
# Option 2: import all assets 

from dagster import load_assets_from_modules

# list each file in assets as an import and in the load modules call
from cereal_project.assets import cereal_assets 
all_assets = load_assets_from_modules([cereal_assets])

@repository
def cereal_project2():
    return [all_assets]