import requests
import pygal

from pygal.style import LightenStyle as LS, LightColorizedStyle as LCS

url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print('Status Code: ', r.status_code)

response_dict = r.json()

# print(response_dict.keys())
# print('Total repositories: ', response_dict['total_count'])
# print('Repositories returned: ', len(response_dict['items']))

repo_dicts = response_dict['items'] 
# print(repo_dicts[0].keys())

repos, names = [], []
for repo_dict in repo_dicts:
    # names.append(repo_dict['name'])

    # repo = {
    #     'value': repo_dict['stargazers_count'],
    #     'label': repo_dict['description'],
    # }

    # repos.append(repo)
    
    repo = {}
    try:
        repo['label'] = repo_dict['description'].encode('utf-8')
    except AttributeError:
        pass
    else:
        repo['value'] = repo_dict['stargazers_count']
        repo['xlink'] = repo_dict['html_url']
        names.append(repo_dict['name'])
        repos.append(repo)
        print(repo)
    
# 可视化
style = LS('#336699', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add('', repos)
chart.render_to_file('Web API/python_repos.svg')