import json
import os
from pathlib import Path

from flask import Blueprint

# Get environment variables.
FLASK_DEBUG = os.getenv("FLASK_DEBUG", "0")
VITE_ORIGIN = os.getenv("VITE_ORIGIN", "http://localhost:5173")

# Set application constants.
is_production = FLASK_DEBUG != "1"
project_path = Path(os.path.dirname(os.path.abspath(__file__)))

# Create a blueprint that stores all Vite-related functionality.
assets_blueprint = Blueprint(
    "assets_blueprint",
    __name__,
    static_folder="dist/bundles",
    static_url_path="/assets/bundles",
)

# Load manifest file in the production environment.
manifest = {}
if is_production:
    manifest_path = project_path / "dist/manifest.json"
    try:
        with open(manifest_path, "r") as content:
            manifest = json.load(content)
    except OSError as exception:
        raise OSError(
            f"Manifest file not found. Run `npm run build`."
        ) from exception


# Add `asset()` function and `is_production` to app context.
@assets_blueprint.app_context_processor
def add_context():
    def dev_asset(file_path):
        return f"{VITE_ORIGIN}/{file_path}"

    def prod_asset(file_path):
        try:
            return f"/assets/{manifest[file_path]['file']}"
        except:
            return "asset-not-found"

    return {
        "asset": prod_asset if is_production else dev_asset,
        "is_production": is_production,
    }
