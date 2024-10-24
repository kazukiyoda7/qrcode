from torch.utils.data import DataLoader
import torch
from torch import nn, optim
from torchvision.utils import save_image
from torchvision import transforms
from dataset import QRCodeDataset
from transformers import ViTForImageClassification, ViTFeatureExtractor


# データローダーの作成
transform = transforms.Compose(
    [
        transforms.Resize((224, 224)), # Resize the image for VIT
        transforms.ToTensor(),
    ]
)

dataset = QRCodeDataset("qr_data.csv", "data", transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)


if __name__ == "__main__":

    feature_extractor = ViTFeatureExtractor.from_pretrained(
        "google/vit-base-patch16-224-in21k"
    )

    model = ViTForImageClassification.from_pretrained(
        "google/vit-base-patch16-224-in21k",
        num_labels=len(dataset.labels["label"].unique()),
    )

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.AdamW(model.parameters(), lr=5e-5)
    epochs = 10
    
    for epoch in range(epochs):
        model.train()
        for images, labels in dataloader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images).logits
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

    print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')
