import torch


def get_device():

    if torch.cuda.is_available():
        return "cuda"

    return "cpu"


def print_device_info():

    print(
        f"PyTorch Version : {torch.__version__}"
    )

    print(
        f"CUDA Available  : {torch.cuda.is_available()}"
    )

    if torch.cuda.is_available():

        print(
            f"GPU Name        : {torch.cuda.get_device_name(0)}"
        )

        print(
            f"CUDA Version    : {torch.version.cuda}"
        )