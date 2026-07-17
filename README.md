# Emotion Recognition Web Demo

This repository is the web-only version of the FER emotion recognition project.
It contains only the files needed to run the browser demo:

- FastAPI backend
- trained `ResNet18` checkpoint
- webcam snapshot UI
- Grad-CAM visualization for the predicted class

The goal of this smaller repository is to make deployment easier than the full course project repository, which also includes training scripts, evaluation scripts, datasets, and local outputs.

## Included Files

- `app.py`
- `web_app.py`
- `image_preprocessing.py`
- `models.py`
- `best_resnet18.pt`
- `requirements.txt`
- `vercel.json`

## Local Run

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m uvicorn web_app:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Vercel Deployment Notes

This repo is prepared for Vercel with:

- `app.py` as the FastAPI entrypoint
- `vercel.json` with `fluid: true`
- a CPU-only PyTorch install path in `requirements.txt`

If Vercel still reports a function bundle that is too large, the next step would be converting the model to ONNX and replacing the server-side PyTorch runtime.

## How The Demo Works

1. The browser starts the webcam.
2. The user takes a picture and confirms it.
3. The confirmed photo is sent to the FastAPI backend.
4. The backend preprocesses the image, runs the trained model, and computes Grad-CAM.
5. The page shows:
   - predicted emotion
   - confidence
   - top predictions
   - processed model input image
   - Grad-CAM overlay
