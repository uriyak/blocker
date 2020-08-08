import re
HOSTS_PATH = r'C:\Windows\System32\drivers\etc\hosts'
PATTERN_TEMPLATE = '127\.0\.0\.1.+({domains})'
DOMAINS = ['facebook.com', 'ynet.co.il', 'walla.co.il']
BLOCK_LINES = '127.0.0.1 {d}\n127.0.0.1 www.{d}'
NL = '\n'

pattern = PATTERN_TEMPLATE.format(domains='|'.join(map(re.escape, DOMAINS)))

with open(HOSTS_PATH, 'r+',) as f:
    data = f.read()
    f.seek(0)
    if re.search(pattern, data):
        new_data = re.sub(pattern, '', data)
    else:
        new_data = data + NL + NL.join(BLOCK_LINES.format(d=d) for d in DOMAINS)
    new_data = re.sub(r'\n{3,}', NL+NL, new_data).strip()
    f.write(new_data)
    f.truncate()
