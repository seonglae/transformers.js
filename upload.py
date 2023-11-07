from huggingface_hub import HfApi
from fire import Fire


def upload(token: str, model: str, repo_type: str = 'model', user='texonom'):
  api = HfApi(token=token)
  api.create_repo(repo_type=repo_type, repo_id=f"{user}/{model}", exist_ok=True)
  api.upload_folder(folder_path=f"models/{model}",
                    repo_type=repo_type, repo_id=f"{user}/{model}")


Fire(upload)
