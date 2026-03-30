from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="ai-habitat/hm3d",
    repo_type="dataset",
    local_dir="data/scene_datasets/hm3d",
    allow_patterns="hm3d_train_v0.2/*"
)