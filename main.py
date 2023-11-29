from diffusers import DiffusionPipeline, LCMScheduler
import torch


# model_id = "stabilityai/stable-diffusion-xl-base-1.0"
# lcm_lora_id = "latent-consistency/lcm-lora-sdxl"
SDXL_PATH = './dataroot/models/stabilityai/stable-diffusion-xl-base-1.0'
LORA_PATH = './dataroot/models/latent-consistency/lcm-lora-sdxl'

pipe = DiffusionPipeline.from_pretrained(SDXL_PATH, variant="fp16")

pipe.load_lora_weights(LORA_PATH)
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
pipe.to(device="mps", dtype=torch.float16)

prompt = "close-up photography of old man standing in the rain at night, in a street lit by lamps, leica 35mm summilux"
images = pipe(
    prompt=prompt,
    num_inference_steps=4,
    guidance_scale=1,
).images[0]

images.save('result.png')