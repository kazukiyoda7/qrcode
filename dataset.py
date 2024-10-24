import pandas as pd
from torchvision import transforms
from PIL import Image
from torch.utils.data import Dataset, DataLoader
import numpy as np


class QRCodeImageDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.labels = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        img_name = f"{self.root_dir}/{self.labels.iloc[idx, 0]}"
        image = Image.open(img_name)
        # pixel_data = list(image.getdata())
        # print(pixel_data)
        # print("Image Size:", image.size)
        # print("Image Mode:", image.mode)
        label = self.labels.iloc[idx, 1]

        if self.transform:
            image = self.transform(image)

        return image, label


class QRCodeBinaryDataset(Dataset):
    def __init__(self, csv_file, root_dir, transform=None):
        self.labels = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        data_name = f"{self.root_dir}/{self.labels.iloc[idx, 0]}"
        data = np.load(data_name)
        label = self.labels.iloc[idx, 1]

        if self.transform:
            data = self.transform(data)

        return data, label
