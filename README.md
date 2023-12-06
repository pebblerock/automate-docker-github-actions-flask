## Demo

Find the demo in the [infrastructure repository](https://github.com/pebblerock/terraform-deployment).

# CI/CD pipeline to automate Docker image build with GitHub Actions

This is a simple Flask app that transliterates text from Latin script to [Osmanya script](https://en.wikipedia.org/wiki/Osmanya_(Unicode_block)). It provides a web interface where users can enter text and select the desired transliteration direction, Latin to Osmanya and Osmanya to Latin. Using Github Actions, the app is containerised and pushed to the Docker registry, Docker Hub.

## CI/CD pipeline diagram

![AWS Diagram](/images/pipeline-diagram.png)

## Prerequisites

1. Docker: Make sure you have Docker installed on your machine. You can download it from the official [Docker](https://docker.com/) website.

## Getting Started

1. Clone the repository to your local machine:


```bash
docker pull pebblerock/osmanya-flask
```
2. Build the Docker image:
```bash
docker build -t osmanya-flask .
```
3. Run the Docker container:
```bash
docker run -p 5000:5000 osmanya-flask
```
4. Access the app in your web browser:

Open your web browser and go to [localhost:5000](http://localhost:5000).
## License

[MIT](https://choosealicense.com/licenses/mit/)


