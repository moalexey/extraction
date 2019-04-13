html = '''h1="title start";
FOX Sports is dé live sportzender van Nederland. Iedere speelronde van de Eredivisie worden op FOX 

/* Record ID 1912828 */'''

left_border = '";\n'
right_border = '\n\n/*'

text = html[html.index(left_border)+len(left_border):html.index(right_border)]

