# Emotion Recognition Web Demo

This repository is the web-only version of the FER emotion recognition project.
It contains only the files needed to run the browser demo on a hosted backend such as Render:

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
- `render.yaml`

## Local Run

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m uvicorn app:app --reload
```

Then open:

```text
http://127.0.0.1:8000
```

## Render Deployment Notes

This repo is prepared for Render with:

- `app.py` as the FastAPI entrypoint
- `render.yaml` as a Render Blueprint
- `.python-version` to keep Render from using its current default Python `3.14.3`
- a CPU-only PyTorch install path in `requirements.txt`
- `/health` endpoint for Render HTTP health checks

You can deploy it in either of these ways:

1. Blueprint flow:
   - Connect the GitHub repo to Render.
   - Let Render detect `render.yaml`.
   - Review the generated web service and deploy.

2. Manual web service flow:
   - Runtime: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app:app --host 0.0.0.0 --port $PORT`

Render docs I matched this to:

- FastAPI quickstart: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- Python build command: `pip install -r requirements.txt`
- `.python-version` support for pinning Python
- `healthCheckPath` in `render.yaml`

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
