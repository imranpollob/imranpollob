link = input('Enter project link: ')
project = input('Enter about the project: ')
logo = input('Enter project logo: ')
color = input('Enter label color: ')

color = color.replace('#', '')
project = project.replace('-', '')
project = " ".join(i.capitalize() for i in project.split())

tag = '''
<a href="{link}">
  <img src="https://img.shields.io/badge/{project}-white?style=flat&logo={logo}&logoColor=white&labelColor={color}" />
</a>
'''.format(link=link, project=project, logo=logo, color=color)

print(tag)
