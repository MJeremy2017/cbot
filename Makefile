dep:
	pip install -r requirements.txt

run:
	python3 app.py

port:
	ngrok http 3000