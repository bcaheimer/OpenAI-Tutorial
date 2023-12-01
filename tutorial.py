import requests
from PIL import Image, ImageDraw 
import io


image_API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
caption_API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
# TODO put in access token
headers = {"Authorization": "Bearer ACCESS_TOKEN"}


""" Generates image base on text prompt
	Parameters
    ----------
	prompt | str
		text feed for image generation

	Returns
    -------
    bytes
		bytes corresponding to generated image
"""
def generate_image(prompt):
	payload = {"inputs": prompt,}
	response = requests.post(image_API_URL, headers=headers, json=payload)
	return response.content

""" Generates caption based on image
	Parameters
    ----------
	prompt | str
		text to prompt fun fact (e.g "A fun fact about frogs is")

	Returns
    -------
    str
		text with fun fact
"""
def generate_caption(prompt):
	# TODO implement function
	# hint: should use json() to get dictionary from response
	pass

def main():
	while True:
		animal = input("Please input an animal, or \"Quit\": ")
		if animal == "Quit":
			break
		try:
			image_bytes = generate_image(animal+" wearing a funny hat")
			image = Image.open(io.BytesIO(image_bytes))
			image.show()

			# TODO create a fun_fact about the animal using the text generation model
			# draw = ImageDraw.Draw(image)
			# draw.text((0, 0), fun_fact,(255,255,255))
			# image.show()
			
		except Exception as error:
			print("error: ", error)

if __name__ == "__main__":
	main()