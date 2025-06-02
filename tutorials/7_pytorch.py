import torch
import torch.nn as nn
import torch.optim as optim

# Device setup (GPU if available)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 1. Tensor creation and basic operations
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]], device=device)
y = torch.ones_like(x)
z = x + y  # Element-wise addition
print("Tensor addition:\n", z)

# 2. Autograd example
a = torch.tensor(3.0, requires_grad=True)
b = a ** 2 + 2 * a + 1  # b = a^2 + 2a + 1
b.backward()
print("Gradient of b w.r.t a:", a.grad)

# 3. Simple neural network
model = nn.Sequential(
    nn.Linear(2, 4),
    nn.ReLU(),
    nn.Linear(4, 1)
).to(device)

# 4. Loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 5. Fake data and training step
inputs = torch.randn(5, 2).to(device)      # batch of 5 samples, 2 features
targets = torch.randn(5, 1).to(device)     # target values

# Forward pass
outputs = model(inputs)
loss = criterion(outputs, targets)
print("Initial loss:", loss.item())

# Backward pass and optimization
optimizer.zero_grad()
loss.backward()
optimizer.step()
print("Updated weights and bias")

