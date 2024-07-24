# Vue + Flask = ❤️

Example of running Vue 3 app with Vite and Flask. Application has multiple entrypoints.

👀 [Original vanilla JS inspiration](https://github.com/tylerlwsmith/vite-with-flask-backend).

## Setup

```sh
npm i
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the app

### Dev mode

```sh
npm run dev
flask --debug --app main run --port 8000
```

### Prod mode

```sh
npm run build
flask --app main run --port 8000
```
