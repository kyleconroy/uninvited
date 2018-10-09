rules.json: hosts
		python3 convert.py > rules.json

hosts:
		curl --silent --location --output hosts https://someonewhocares.org/hosts/hosts


