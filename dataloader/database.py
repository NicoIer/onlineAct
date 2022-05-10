from torch.utils.data import Dataset
from torchvision.datasets import UCF101
from setting.const import UCF101_ROOT, UCF101_SPLIT

ucf101 = UCF101(root=UCF101_ROOT,  # root 数据集根目录
                annotation_path=UCF101_SPLIT,  # annotation_path 数据集划分文件根目录
                frames_per_clip=5,  # 几帧一剪
                step_between_clips=1  # 每一剪之间隔几帧
                )

a, b, c = ucf101[0]  # 返回Tensor Tensor int


class SelfDataSet(Dataset):
    """后期用于构建用户输入数据的 数据集类 """

    def __init__(self):
        pass

    def __getitem__(self, item):
        pass

    def __len__(self):
        pass
