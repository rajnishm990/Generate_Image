# Image Generation Using Stability AI
## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- Stability AI API key
- Redis installed and running (for Celery task queue)

### Installation Steps

1. Clone the repository to your local machine:

``` git clone https://github.com/rajnishm990/text-to-image-app.git ```
or\
Download the zip file 

2. Navigate to the project directory:

``` bash
cd text-to-image-app 
```

3. Install dependencies using pip:

``` bash
pip install -r requirements.txt
```
4. Set up environment variables:

- `STABILITY_API_KEY`: Your Stability AI API key
- `CELERY_BROKER_URL`: URL for your Redis instance (e.g., redis://localhost:6379/0)

## Configuration

### API Authentication

Set the `STABILITY_API_KEY` environment variable to your Stability AI API key. This key is used for authentication when making requests to the Stability AI API. 


### Celery Configuration

1. Set the `CELERY_BROKER_URL` environment variable to the URL of your Redis instance. This URL specifies the location of the Celery message broker.

2. Configure Celery in your Django project's settings file (`settings.py`) by adding the following lines:

```python
# settings.py

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

```

### Running the Application

1.Start the Django development server:
``` bash
python manage.py runserver
 ```
This command will start the Django server on ``` http://127.0.0.1:8000/ ```
Access the application in your web browser by navigating to the server address.
Celery Workers

2.Start Celery workers to handle asynchronous tasks:

``` bash
celery -A image_generation worker --pool=solo -l info
```
This command starts Celery workers using the configuration specified in the Django project.

### Usage
Access the application's endpoint in your web browser or using an HTTP client (e.g., cURL):
``` bash
GET /generate-images/
```

This endpoint triggers the generation of images based on predefined text prompts. Each time the endpoint is accessed, it initiates the Celery task to generate images asynchronously.
Monitor the Celery worker logs for task execution and any errors encountered during image generation.


### Output 
The generated image will be stored inside ``` root_directory/out/the-prompt.png ```
