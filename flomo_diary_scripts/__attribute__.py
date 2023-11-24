import re


class Patterns:
    parse_date = re.compile(r'(\d{4})[年/.-]?(\d{2})[月/.-]?(\d{2})[日号]?')


class Path:
    json = "./flomo_diary_scripts/output.json"
