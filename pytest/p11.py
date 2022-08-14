import torch
import clip
from PIL import Image
import numpy as np

device = "cuda"
model, preprocess = clip.load("ViT-B/32", device=device)
image = preprocess(Image.open("test11.png")).unsqueeze(0).to(device)
text = clip.tokenize(["plane","nut","car","bird"])
with torch.no_grad():
    image_feature = model.encode_image(image)
    text_feature = model.encode_text(text)

    logits_per_image, logits_per_text = model(image,text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

print("Label:",probs)