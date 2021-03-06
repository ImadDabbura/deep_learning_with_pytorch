"""
Fitting a random data using fully connected network with one hidden layer.
"""


import torch


device = torch.device('gpu:0' if torch.cuda.is_available() else 'cpu')

# Define dimensions
N, D_IN, H, D_OUT = 64, 1000, 100, 10

# Create random data
X = torch.randn(N, D_IN, device=device, dtype=dtype, requires_grad=False)
y = torch.randn(N, D_OUT, device=device, dtype=dtype, requires_grad=False)

# Initialize weights randomly
w_1 = torch.randn(D_IN, H, device=device, dtype=dtype, requires_grad=True)
w_2 = torch.randn(H, D_OUT, device=device, dtype=dtype, requires_grad=True)

# Define learning rate
lr = 1e-6

# Loop over number of epochs to fit the data to nn
for epoch in range(50):
    # Forward pass
    h = X.mm(w_1)
    h_relu = torch.clamp(h, 0)
    y_pred = h_relu.mm(w_2)

    # Compute loss
    loss = (y_pred - y).pow(2).sum()
    print(f'Loss {epoch} : {loss.item():.4f}')

    # Use autograd to compute gradients
    loss.backward()

    # Update wights using gradient descent
    # w_1.data -= lr * w_1.grad.data
    # w_2.data -= lr * w_2.grad.data

    with torch.no_grad():
        w_1 -= lr * w_1.grad
        w_2 -= lr * w_2.grad

    # Zero the gradients
    w_1.grad.zero_()
    w_2.grad.zero_()
