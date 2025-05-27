
from huggingface_hub import snapshot_download

import os
save_dir = os.path.join(os.path.dirname(__file__), "models/bagel")
repo_id = "callgg/bagel-bf16"
cache_dir = save_dir + "/cache"

snapshot_download(
    cache_dir=cache_dir,
    local_dir=save_dir,
    repo_id=repo_id,
    allow_patterns=["*.json", "*.safetensors", "*.bin", "*.py", "*.md", "*.txt"],
    )
