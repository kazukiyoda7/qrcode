from torch.utils.data import DataLoader
import torch
from torch import nn, optim
from torchvision.utils import save_image
from torchvision import transforms
from dataset import QRCodeBinaryDataset
from transformers import ViTForImageClassification, ViTFeatureExtractor


dataset = QRCodeBinaryDataset("qr_binary_data.csv", "data_binary")
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)


if __name__ == "__main__":
    for batch_idx, (data, label) in enumerate(dataloader):
        print(data.shape)
        print(label.shape)