import json


def by_domain(rule):
    return rule['trigger']['if-domain'][0]


def convert():
    rules = []
    in_section = False
    sections = set([
        '#<localhost>', '#</localhost>',
    ])

    with open("hosts") as hosts:
        for entry in hosts:
            entry = entry.strip()

            if entry.startswith('#<') and entry in sections:
                in_section = True

            if entry.startswith('#</') and entry in sections:
                in_section = False

            if in_section:
                continue

            if not entry.startswith('127.0.0.1'):
                continue

            parts = entry.split(None)
            domain = parts[1].lower()

            rules.append({
                "action": {
                    "type": "block",
                },
                "trigger": {
                    "url-filter": ".*",
                    "if-domain": [domain.encode('idna').decode('utf-8')],
                },
            })

    rules.sort(key=by_domain)

    print(json.dumps(rules, indent=2))

if __name__ == "__main__":
    convert()
