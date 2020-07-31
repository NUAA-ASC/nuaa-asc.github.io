from collections import defaultdict as dd
out = ''


a = dd(list)

for paper in open('papers.txt').read().split('#'):
    content = list(filter(len, paper.split('\n')))
    if len(content) == 5:
        year, cont = int(content[0]), content[1:]
        html = '<li>{}, <a href="{}">{}</a>, <i>{}</i>.</li>'.format(
            cont[0], cont[3], cont[1], cont[2])
        a[year].append(html)

for year in sorted(list(a.keys()))[::-1]:
    out += '<h3>{}</h3><ol><table><tr><td style=''text-align:justify;''>'.format(year) + '\n'.join(a[year]) + '</td></tr></table></ol>'

fp = open('publication.html', 'w')

fp.write(open('matter/publication-head.html').read() +
         '\n<div class="container" id="papers">\n')
fp.write(out)
fp.write('</div>\n' + open('matter/foot.html').read())
