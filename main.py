from torch.utils.data import DataLoader
from torchvision.utils import save_image
from torchvision import transforms
from dataset import QRCodeDataset

transform = transforms.Compose(
    [
        transforms.Resize((224, 224)),  # ViTの入力サイズに合わせる
        transforms.ToTensor(),
    ]
)

dataset = QRCodeDataset("qr_data.csv", "data", transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)


if __name__ == "__main__":
    for batch_idx, (data, labels) in enumerate(dataloader):
        print(f"Batch {batch_idx + 1}:")
        save_image(data, f"batch_{batch_idx + 1}.png")
        print("Labels:", labels)
        print() 
