.PHONY: rules

rules: hosts
		python3 convert.py > SomeoneWhoCares/Hosts/blockerList.json

hosts:
		curl --silent --location --output hosts https://someonewhocares.org/hosts/hosts


