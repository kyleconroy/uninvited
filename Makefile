.PHONY: rules

rules: hosts
		python3 convert.py > univited/Uninvited/blockerList.json

hosts:
		curl --silent --location --output hosts https://someonewhocares.org/hosts/hosts


