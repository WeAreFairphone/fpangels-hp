import dominate, json, os.path, requests, yaml
from dominate.tags import *
from dominate.util import raw

# list of columns for table, sortable or non sortable
columns = [["Flag", "nosort"], ["City", "sort"], ["Angels", "sort"]]

# Get Angels YAML
response = requests.get('https://forum.fairphone.com/raw/48676/1')

if response.status_code == requests.codes.ok:
    heavens = yaml.safe_load(response.text)['heavens']
    doc = dominate.document(title='Fairphone Angels')

    with doc.head:
        link(rel='stylesheet', href='style.css')
#        script(type='text/javascript', src='https://twemoji.maxcdn.com/v/latest/twemoji.min.js', crossorigin='anonymous')
#        script(type='text/javascript', src='script.js')
        script(type='text/javascript', src='sorttable.js')

    # Skeleton
    header = doc.add(header()).add(div(cls='wrapper'))
    map = doc.add(div(cls='map'))
    list2 = doc.add(section(cls='wrapper')).add(table(cls='sortable'))
    with list2.add(thead()).add(tr()):
        for column1, column2 in columns:
            if column2=="nosort":
                td(cls='sorttable_nosort').add(column1)
            else:
                th(column1)
    footer = doc.add(footer()).add(tr(cls='wrapper'))

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
    list2 = list2.add(tbody())
    for heaven in heavens:
        print(heaven.keys())
        if 'exists' and 'active' in heaven:
            with list2.add(tr()):
                td(heaven['country'])
                td(heaven['location'])
                n = len(heaven['angels'])
                td(a('📧 Contact {n} 👼 Angel{s}'.format(n=n, s='s' if len(heaven['angels'])>1 else ''),
                  cls='button btn-angels', data_location=heaven['location']))

    # Footer
    with footer:
        with ul():
            li().add(a('Contribute to this website on Github', href='https://github.com/WeAreFairphone/fpangels-hp'))


    with open('index2.html', 'w', encoding='utf8') as file:
        file.write(str(doc))
