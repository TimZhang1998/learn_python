import json
import pygal

from countries import get_country_code
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

filename = 'Population/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 打印每个国家2010年的人口数量
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            # print(country_code + ': ', population)
            cc_populations[country_code] = population
        else:
            # print('ERROR - ' + country_name)
            continue

cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "Wolrd Population in 2010, by country"
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('Population/world_population.svg')