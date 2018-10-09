import json


def by_domain(rule):
    return rule['trigger']['if-domain'][0]


def convert():
    rules = []
    with open("hosts") as hosts:
        for entry in hosts:
            entry = entry.strip()

            if not entry.startswith('127.0.0.1'):
                continue

            parts = entry.split(None)

            rules.append({
                "trigger": {
                    "url-filter": ".*",
                    "if-domain": [parts[1]],
                },
                "action": {
                    "type": "block",
                },
            })

    rules.sort(key=by_domain)

    print(json.dumps(rules, indent=2))


if __name__ == "__main__":
    convert()
