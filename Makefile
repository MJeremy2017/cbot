dep:
	pip install -r requirements.txt

run:
	python3 app.py

port:
	ngrok http 3000

build:
	docker build -t chatbot .

docker-run:
	docker run -p 3000:3000 -it chatbot