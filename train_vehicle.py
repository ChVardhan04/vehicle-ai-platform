import torch
import torchvision
from torchvision import datasets, transforms
from torch import nn, optim
from torchvision.models import resnet18, ResNet18_Weights
import os

os.makedirs("models", exist_ok=True)

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

dataset_path = "datasets/Vehicle Image Classification/Vehicles"

dataset = datasets.ImageFolder(dataset_path, transform=transform)

loader = torch.utils.data.DataLoader(dataset, batch_size=16, shuffle=True)

print("Classes found:", dataset.classes)
print("Total images:", len(dataset))

model = resnet18(weights=ResNet18_Weights.DEFAULT)


model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("Training started...")

for epoch in range(2):

    running_loss = 0

    for images, labels in loader:

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    print("Epoch", epoch+1, "Loss:", running_loss)

torch.save(model.state_dict(), "models/vehicle_model.pth")

print("Training finished")
print("Model saved at models/vehicle_model.pth")