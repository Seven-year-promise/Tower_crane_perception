from diffusers import AutoPipelineForText2Image, StableDiffusionPipeline
import torch
from diffusers.utils import load_image
import random


pipeline = StableDiffusionPipeline.from_single_file("/home/weights/sd1-5/juggernaut.safetensors", # "/home/weights/sd1-5/runwayml/stable-diffusion-v1-5/", 
                                                      use_safetensors=True,
                                                      torch_dtype=torch.float32).to("cuda")
pipeline.load_ip_adapter("/home/weights/trained_models/ip_adapter_mic_only2/", subfolder="checkpoint-3000/", weight_name="ip_adapter.bin")
#print(pipeline)
pipeline.set_ip_adapter_scale(0.48)

image = load_image("/home/tower_crane_data/gen_dataset/333-v2/train/images/hik_11_png.rf.8f08b79aea46d27122c064d8710083b0.jpg")
seed = random.randint(1, 44455201144)
print(seed)
generator = torch.Generator(device="cuda").manual_seed(seed) 
images = pipeline(
    prompt='A Modular Integrated Construction on the construction site',
    ip_adapter_image=image,
    negative_prompt="",
    num_inference_steps=50,
    generator=generator,
    guidance_scale=5,
).images[0]
images.save("tower_crane.png")


# model_id = "/home/weights/sd1-5/runwayml/stable-diffusion-v1-5/"
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
# pipe = pipe.to("cuda")

# prompt = "a photo of an astronaut riding a horse on mars"
# image = pipe(prompt).images[0]  
    
# image.save("astronaut_rides_horse.png")