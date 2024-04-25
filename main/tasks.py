from celery import shared_task
import requests
import os
import base64
import json

API_KEY = os.environ.get("STABILITY_API_KEY")

if not API_KEY: 
    raise ValueError("API key not set")

TASK_LIMIT = 5  
task_counter = 0 

@shared_task(bind=True)
def generate_image(self,prompt):
    TASK_LIMIT = 5
    task_counter = 0
    if task_counter >= TASK_LIMIT:
        return
    api_url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "content-type": "application/json",
    }
    json = {
        "text_prompts": [
            {
                "text": prompt
            }

        ],
        "cfg_scale": 7,
        "height": 1024,
        "width": 1024,
        "samples": 1,
        "steps": 30,
    }
    
    try:
        response = requests.post(api_url, headers=headers, json=json)
        response.raise_for_status()
    except Exception as e:
        logger.error("Error making API call: %s", str(e))
        raise
    
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    if not os.path.exists("./out"):
        os.makedirs("./out")
    for i, image in enumerate(data["artifacts"]):
        with open(f'./out/{prompt}.png', "wb") as f:
            f.write(base64.b64decode(image["base64"]))
        print("Image successfully generated and saved.")
    task_counter += 1
