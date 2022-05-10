from dataloader.database import UCF101DataSet

ucf101 = UCF101DataSet(frame_per_clip=16, step_per_clip=4, train_percentage=0.8)  # 数据集的读取 预处理 完毕

for tensor,label in ucf101.train_items():
    break

print(tensor.shape)