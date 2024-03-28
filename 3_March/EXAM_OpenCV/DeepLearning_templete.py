import torch
from torch.utils.data import DataLoader, Dataset
import torch.nn as nn
import torch.optim as optim

DEBUG = True

# 1. Data Load
# TODO: Load your data here

# 2. Dataset and Dataloader
# 2-1. Dataset
x_data = []
y_data = []

class YourDataset(Dataset):
    def __init__(self, x, y):
        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

dataset = YourDataset(x_data, y_data)
if DEBUG:
    print(dataset[0])
    
# 2-2. Dataloader
Batchs = 32
dataloader = DataLoader(dataset, batch_size=Batchs, shuffle=True, drop_last=True)
# - drop_last: 마지막 배치가 batch_size보다 작을 때 버릴지 여부
if DEBUG:
    for x, y in dataloader:
        print(x, y)
        break


# 3. Model
class YourModel(nn.Module):
    def __init__(self, IN, hidden, OUT):
        super(YourModel, self).__init__()
        self.in_layer = nn.Linear(IN, hidden[0])
        self.hidden = nn.ModuleList(
            [nn.Linear(hidden[i], hidden[i+1]) for i in range(len(hidden)-1)]
            )
        self.out_layer = nn.Linear(hidden[-1], OUT)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()
        self.softmax = nn.Softmax(dim=1)
        

    def forward(self, x):
        y = self.relu(self.in_layer(x))
        y = self.relu(self.hidden(y))
        if OUT == 1:
            y = self.sigmoid(self.out_layer(y))   # 이진분류
        else:
            y = self.softmax(self.out_layer(y))   # 다중분류
        return y

len_x = len(x_data[0])
IN, hidden, OUT = len_x, [64, 32, 16], 2
model = YourModel(IN, hidden, OUT)

# 4. Training
def train(model, dataloader):
    
    pass

# 5. Testing
def test(model, dataloader):
    # TODO: Implement your testing loop here
    pass

# TODO: Call the train and test functions with your model and dataloader
