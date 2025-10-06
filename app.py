from fastai.vision.all import *
import gradio as gr
from huggingface_hub import hf_hub_download

# ✅ Download the model from Hugging Face model repo
model_path = hf_hub_download(repo_id="VSakhi/dogvcat", filename="models.pkl")

# ✅ Load the trained model
learn = load_learner(model_path)

# ✅ Define your labels
categories = ('Dog', 'Cat')

# ✅ Define prediction function
def classify_images(img):
    pred, idx, probs = learn.predict(img)
    return {categories[i]: float(probs[i]) for i in range(len(categories))}

# ✅ Gradio components
image = gr.Image(type="pil", label="Upload an image")
label = gr.Label(num_top_classes=2)
examples = ['dog.jpg', 'cat.jpg']

# ✅ Gradio interface
intf = gr.Interface(
    fn=classify_images,
    inputs=image,
    outputs=label,
    examples=examples,
    title="🐶 Dog vs 🐱 Cat Classifier",
    description="Upload an image and see whether it's a Dog or a Cat!"
)

# ✅ Launch the app
intf.launch()
