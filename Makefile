updateReqs:
	pip freeze > requirements.txt

updateEnv:
	pip install -r requirements.txt

updateTree:
	find . \( -path './bin' -o -path './include' -o -path './lib' -o -path './share' -o -path './python3.12' -o -path './.git' -o -path './.github' \) -prune -o -name '.DS_Store' -prune -o -name 'pyvenv.cfg' -prune -o -print | sed -e "s/[^-][^\/]*\//  |/g" -e "s/|\([^ ]\)/|-\1/" > tree.txt