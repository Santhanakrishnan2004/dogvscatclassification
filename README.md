
# 🐶 Dog vs 🐱 Cat Classifier

A simple yet powerful image classification web app built with **FastAI** and **Gradio**, deployed on **Hugging Face Spaces**.

This model can predict whether the uploaded image is of a **Dog** or a **Cat** 🐾

---

## 🚀 Demo
👉 Try it live here: [Dog vs Cat Classifier on Hugging Face Spaces](https://huggingface.co/spaces/VSakhi/dogvcat)

---

## 🧠 Model Details

- **Framework:** [FastAI](https://docs.fast.ai/)
- **Model Type:** CNN (trained on images of dogs and cats)
- **Training:** Used transfer learning with a pre-trained backbone (ResNet34 or similar)
- **Exported File:** `models.pkl`

The model was trained locally and exported with `learn.export()` from FastAI.  
It is hosted on [Hugging Face Hub](https://huggingface.co/VSakhi/dogvcat).

---

## 🧩 Tech Stack

| Tool | Purpose |
|------|----------|
| **FastAI** | Model training and inference |
| **PyTorch** | Deep learning backend |
| **Gradio** | Web app interface |
| **Hugging Face Hub** | Model hosting and deployment |
| **Python 3.10** | Runtime environment |

---

## 🧰 Project Structure

```

dogvcat/
│
├── app.py               # Main Gradio application
├── requirements.txt     # Dependencies for Hugging Face build
├── runtime.txt          # (Optional) Python version spec
└── README.md            # You're reading this file 😄

````

---

## 🖼️ How to Use

1. Upload an image of a **dog** or **cat**.
2. The model will predict which it is.
3. You’ll see a confidence score for both categories.

---

## 🧪 Run Locally

If you want to test it before deploying:

```bash
pip install -r requirements.txt
python app.py
````

Then open your browser at **[http://127.0.0.1:7860](http://127.0.0.1:7860)**

---

## ✨ Example Predictions

| Example    | Prediction      |
| ---------- | --------------- |
| 🐶 dog.jpg | **Dog (99.2%)** |
| 🐱 cat.jpg | **Cat (98.7%)** |

---

## 🙌 Credits

Developed by **VSakhi (Sandy / Macha)** 💻
Built with ❤️ using **FastAI**, **Gradio**, and **Hugging Face Spaces**.

---

## 📜 License

MIT License — free to use and modify with credit.


