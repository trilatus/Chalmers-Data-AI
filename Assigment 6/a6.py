# -*- coding: utf-8 -*-
"""a6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Suygoeh7bFPXc-GJdjWBPP52LLSSnt7b
"""

plot_samples = False
import torchvision.datasets.mnist
import matplotlib.pyplot as plt
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.optim

transform = transforms.ToTensor()

# load the mnist dataset, training and testsplit
mnist_train = torchvision.datasets.MNIST(root='/content/data', train=True, download=True, transform=transform)
mnist_test = torchvision.datasets.MNIST(root='/content/data', train=False, download=True, transform=transform)

# plot an image from the training and testing set
train_sample = mnist_train[0]
test_sample = mnist_test[0]
if plot_samples:
    plt.imshow(train_sample[0].squeeze(), cmap="grey")
    plt.savefig("train_sample")
    plt.imshow(test_sample[0].squeeze(), cmap="grey")
    plt.savefig("test_sample")

train_dataloader = DataLoader(mnist_train)
test_dataloader = DataLoader(mnist_test)

for X, y in test_dataloader:
    print(f"Shape of X [N, C, H, W]: {X.shape}")
    print(f"Shape of y: {y.shape} {y.dtype}")
    break

class NeuralNetwork(nn.Module):
    def __init__(self, topology):
        super().__init__()
        self.flatten = nn.Flatten()
        match topology:
            case "single_hidden_layer":
                self.linear_relu_stack = nn.Sequential(
                nn.Linear(28*28, 512),
                nn.ReLU(),
                nn.Linear(512, 512),
                nn.ReLU(),
                nn.Linear(512, 10)
            )
            case "two_layers":
                self.linear_relu_stack = nn.Sequential(
                nn.Linear(28*28, 500),
                nn.ReLU(),
                nn.Linear(500, 300),
                nn.ReLU(),
                nn.Linear(300, 512),
                nn.ReLU(),
                nn.Linear(512, 10)
            )
            case "cnn":
                # TODO


    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits

"""The only parameters that I chose were the input/output features. I chose 512 output features from the inputlayer and 512 output feauters again, from the hidden layer to the output layer. The only real reason I chose this value was because it was the one that they used in the PyTorch tutorial. Since they were using the Fashion-MNIST dataset, in which the pictures have the same dimension and channels as the ones in regular MNIST, I figured that these values would be appropriate."""

def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        pred = model(X)
        loss = loss_fn(pred, y)

        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            #print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()
    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")

model = NeuralNetwork(topology="single_hidden_layer")
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

epochs = 10
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
print("Done!")

"""Epoch 1
-------------------------------
Test Error:
 Accuracy: 92.0%, Avg loss: 0.268380

Epoch 2
-------------------------------
Test Error:
 Accuracy: 94.3%, Avg loss: 0.185549

Epoch 3
-------------------------------
Test Error:
 Accuracy: 95.5%, Avg loss: 0.143503

Epoch 4
-------------------------------
Test Error:
 Accuracy: 96.4%, Avg loss: 0.118555

Epoch 5
-------------------------------
Test Error:
 Accuracy: 97.0%, Avg loss: 0.102227

Epoch 6
-------------------------------
Test Error:
 Accuracy: 97.2%, Avg loss: 0.091949

Epoch 7
-------------------------------
Test Error:
 Accuracy: 97.4%, Avg loss: 0.084933

Epoch 8
-------------------------------
Test Error:
 Accuracy: 97.5%, Avg loss: 0.080052

Epoch 9
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.076061

Epoch 10
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.073988
"""

model = NeuralNetwork(topology="two_layers")
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3, weight_decay=0.0005)

epochs = 40
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train(train_dataloader, model, loss_fn, optimizer)
print("Done!")

"""
=======================================TWO_LAYERS=======================================

Epoch 1
-------------------------------
Test Error:
 Accuracy: 91.4%, Avg loss: 0.278967

Epoch 2
-------------------------------
Test Error:
 Accuracy: 94.7%, Avg loss: 0.173336

Epoch 3
-------------------------------
Test Error:
 Accuracy: 96.0%, Avg loss: 0.129509

Epoch 4
-------------------------------
Test Error:
 Accuracy: 96.6%, Avg loss: 0.105004

Epoch 5
-------------------------------
Test Error:
 Accuracy: 97.1%, Avg loss: 0.093644

Epoch 6
-------------------------------
Test Error:
 Accuracy: 97.2%, Avg loss: 0.087248

Epoch 7
-------------------------------
Test Error:
 Accuracy: 97.3%, Avg loss: 0.085166

Epoch 8
-------------------------------
Test Error:
 Accuracy: 97.4%, Avg loss: 0.082628

Epoch 9
-------------------------------
Test Error:
 Accuracy: 97.3%, Avg loss: 0.083641

Epoch 10
-------------------------------
Test Error:
 Accuracy: 97.4%, Avg loss: 0.082626

Epoch 11
-------------------------------
Test Error:
 Accuracy: 97.5%, Avg loss: 0.080177

Epoch 12
-------------------------------
Test Error:
 Accuracy: 97.5%, Avg loss: 0.078681

Epoch 13
-------------------------------
Test Error:
 Accuracy: 97.6%, Avg loss: 0.079203

Epoch 14
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.075715

Epoch 15
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.075144

Epoch 16
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.073845

Epoch 17
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.073529

Epoch 18
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.073852

Epoch 19
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.073472

Epoch 20
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.073709

Epoch 21
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.074024

Epoch 22
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.073715

Epoch 23
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.074576

Epoch 24
-------------------------------
Test Error:
 Accuracy: 97.7%, Avg loss: 0.073206

Epoch 25
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.070811

Epoch 26
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.070414

Epoch 27
-------------------------------
Test Error:
 Accuracy: 97.8%, Avg loss: 0.069112

Epoch 28
-------------------------------
Test Error:
 Accuracy: 97.9%, Avg loss: 0.067155

Epoch 29
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.065977

Epoch 30
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.065002

Epoch 31
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.066218

Epoch 32
-------------------------------
Test Error:
 Accuracy: 98.1%, Avg loss: 0.064178

Epoch 33
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.065483

Epoch 34
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.064749

Epoch 35
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.064682

Epoch 36
-------------------------------
Test Error:
 Accuracy: 98.1%, Avg loss: 0.063898

Epoch 37
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.064737

Epoch 38
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.064277

Epoch 39
-------------------------------
Test Error:
 Accuracy: 98.0%, Avg loss: 0.064417

Epoch 40
-------------------------------
Test Error:
 Accuracy: 98.1%, Avg loss: 0.063805"""