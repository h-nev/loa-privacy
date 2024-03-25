updateReqs:
	pip freeze > requirements.txt

updateEnv:
	pip install -r requirements.txt