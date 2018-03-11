build:
	docker build -t equipment-status .

run:
	docker run -p 5000:5000 -d -v `pwd`/app/:/var/www/ equipment-status

dev:
	docker build -t equipment-status .
	docker run -p 5000:5000 -v `pwd`/app/:/var/www/ equipment-status
