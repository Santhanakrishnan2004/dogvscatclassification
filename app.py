from fastai.vision.all import *
import gradio as gr

# Load the trained model
learn = load_learner('models.pkl')

categories = ('Dog', 'Cat')

def classify_images(img):
    pred, idx, probs = learn.predict(img)
    return {categories[i]: float(probs[i]) for i in range(len(categories))}

# Use new Gradio components (not gr.inputs / gr.outputs)
image = gr.Image(type="pil")
label = gr.Label()
examples = ['dog.jpg', 'cat.jpg', 'dunno.jpg']

intf = gr.Interface(
    fn=classify_images,
    inputs=image,
    outputs=label,
    examples=examples,
    title="Dog vs Cat Classifier"
)

intf.launch()
