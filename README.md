# Dockerized Flask App

This is a Dockerized Flask app that transliterates text from Latin script to Osmanya script. It provides a web interface where users can enter text and select the desired transliteration direction. The app then returns the transliterated text.

## Prerequisites

1. Docker: Make sure you have Docker installed on your machine. You can download it from the official [Docker](https://docker.com/) website.

## Getting Started

1. Clone the repository to your local machine:


```bash
docker pull pebblerock/osmanya-flask
```
2. Build the Docker image:
```bash
docker build -t osmanya-flask.
```
3. Run the Docker container:
```bash
docker run -p 5000:5000 osmanya-flask
```
4.Access the app in your web browser:

Open your web browser and go to [localhost:5000](http://localhost:5000).
## License

[MIT](https://choosealicense.com/licenses/mit/)