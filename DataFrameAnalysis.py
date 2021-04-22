import pandas as pd
import openpyxl

df = pd.read_excel("dataset1and2.xlsx",engine="openpyxl")
print(df.head())
print(df.keys())

df.columns = [c.lower().replace(' ', '_') for c in df.columns]
years = df.year.unique()
chinese_entity = df.chinese_entity.unique()
regions = df.region.unique()
qinmillions = df.quantity_in_millions.unique()
share_size = df.share_size.unique()
tparty = df.transaction_party.unique()
sector = df.sector.unique()
subsector = df.subsector.unique()
country = df.country.unique()
regions = df.region.unique()
bri = df.bri.unique()
greenfield = df.greenfield.unique()

uniques = [years, chinese_entity, regions, qinmillions, share_size,
           tparty, sector, subsector, country, regions, bri, greenfield]

for x in uniques:
    print(x)
#Chinese entity is extremely long, this would be good to cross verify
#Years span between 2005 and 2020

for x in regions:
    print(x + " is:")
    print(df[df.region == x].country.unique())

region_averages = {}

for x in regions:
    regional_average = int(df[df.region == x].quantity_in_millions.mean())
    region_averages[x] = regional_average

print(region_averages)
