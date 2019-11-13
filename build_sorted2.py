import dominate, json, os.path, requests, yaml
from dominate.tags import *
from dominate.util import raw

# Get Angels YAML
response = requests.get('https://forum.fairphone.com/raw/48676/1')

if response.status_code == requests.codes.ok:
    heavens = yaml.safe_load(response.text)['heavens']
    doc = dominate.document(title='Fairphone Angels')

    with doc.head:
        link(rel='stylesheet', href='style.css')
        script(type='text/javascript', src='https://twemoji.maxcdn.com/v/latest/twemoji.min.js', crossorigin='anonymous')
        script(type='text/javascript', src='script.js')

    # Skeleton
    header = doc.add(header()).add(div(cls='wrapper'))
    map = doc.add(div(cls='map'))
    list = doc.add(section(cls='wrapper')).add(div(cls='annotated-list', id='heavens'))
    footer = doc.add(footer()).add(div(cls='wrapper'))

    # Header
    header.add(h1('Fairphone Angels'))
    header.add(a('More Info', cls='button btn-info', href='https://forum.fairphone.com/t/the-fairphone-angels-program-local-support-by-community-members/33058?u=stefan'))

    # Map
    map.add(raw("""
        <iframe src="https://map.fairphone.community/?show=angels" allowfullscreen="true" frameborder="0">
            <p><a href="https://map.fairphone.community/?show=angels" target="_blank">See the Fairphone Community Map!</a></p>
        </iframe>
        """))

    # List
    list.add(raw("""
        <input class="search" placeholder="Search">
        <button class="sort asc" data-sort="location">Sort by name</button>
        <button class="sort" data-sort="country">Sort by country</button>"""))
    with list.add(div(cls='list')):
        for heaven in heavens:
            print(heaven.keys())
            if 'exists' and 'active' in heaven:
             with div(cls='heaven'):
               div(heaven['country'], cls='country')
               div(heaven['location'], cls='location')
               n = len(heaven['angels'])
               a('📧 Contact {n} 👼 Angel{s}'.format(n=n, s='s' if len(heaven['angels'])>1 else ''),
                  cls='button btn-angels', data_location=heaven['location'])
    list.add(raw("""
        <script src="list.js"></script>
        <script src="main.js"></script>"""))

    # Footer
    with footer:
        with ul():
            li().add(a('Contribute to this website on Github', href='https://github.com/WeAreFairphone/fpangels-hp'))


    with open('index2.html', 'w', encoding='utf8') as file:
        file.write(str(doc))
