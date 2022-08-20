import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
import string
import matplotlib.pyplot as plt
from simple_tokenizer import tokenize, detokenize
# from torch.nn import functional as F
from einops import rearrange,repeat



use_gpu = True if torch.cuda.is_available() else False # 如果GPU显存不够，可以手动设置为False
device_id = torch.device("cuda" if use_gpu else "cpu")
# device_id = torch.device("cpu")
print('Device:', device_id)


sonnet_list = [] # 列表中的每一个元素是一首诗的字符串
with open('C:/Users/34323/vs_python/pytest/rnn练习/shakespeares_sonnets.txt', 'r') as f:
    while True:
        text = ''
        line1 = f.readline() # ignore the first line
        if not line1:
            break
        assert eval(line1) == len(sonnet_list) + 1
        line2 = f.readline() # ignore the second line
        while True:
            line = f.readline()
            if line == '\n' or not line:
                break
            text += line.lower().strip() + '\n'
        sonnet_list.append(text)
print('first sonnet:\n%s' % sonnet_list[0])


tokens = tokenize(sonnet_list[0])
print('Number of words in first sonnet: ', len(tokens))
print(tokens[:10]) # 打印前10个token
string = detokenize(tokens)
print('Reconstructed text:\n%s' % string)
    
sonnets_in_tokens = [] # 每一个元素是一个token列表
vocab = set()          # 词表先采用set数据结构来构建，方便去重
max_length = 0         # 按token数量来计算，最长的诗的长度
for son in sonnet_list:
    tokens = tokenize(son)
    sonnets_in_tokens.append(tokens)
    for tok in tokens:
        vocab.add(tok)
    length = len(tokens)
    if length > max_length:
        max_length = length

vocab = list(vocab)   # 词表转换为列表，方便索引
vocab += ['<PAD>', '<START>', '<END>'] # 添加三个特殊token
print('Number of unique words in the vocabulary:', len(vocab))
print('Maximum length of tokens of sonnets in dataset:', max_length)


token_to_id = {tok: i for i, tok in enumerate(vocab)} # 用dict结构构造反向索引
sonnets_in_ids = []  # 每一个元素是一个id列表
for son in sonnets_in_tokens:
    ids = []
    for tok in son:
        # 请完善此处代码，将诗歌数据集中的token转换为id
        ids.append(token_to_id[tok])
    sonnets_in_ids.append(ids)    


def decode(ids):
    tokens = []
    for i in ids: 
        tok = vocab[i]
        if tok in ['<START>']:
            continue
        if tok in ['<END>', '<PAD>']:
            break
        tokens.append(tok)
    string = detokenize(tokens)
    return string
print(decode(sonnets_in_ids[0]))

class dataset(Dataset):
    def __init__(self, sonnets_in_ids, vocab, max_seq_length):
        super().__init__()
        self.data = sonnets_in_ids
        self.vocab = vocab
        self.vocab_size = len(vocab)
        self.pad_id = self.vocab.index('<PAD>')
        self.start_id = self.vocab.index('<START>')
        self.end_id = self.vocab.index('<END>')
        self.max_seq_length = max_seq_length + 2
    
    def __len__(self):
        """返回数据集大小"""
        return len(self.data)
    
    def __getitem__(self, index):
        """抽取第index个样本，对其进行处理（加上`<START>`，`<END>`和`<PAD>`相应的id），
        然后转化为torch.LongTensor（维度为[max_seq_length]），最后返回该tensor
        """
        x = self.data[index]# 取data中的第index个元素
        x = [self.start_id] + x + [self.end_id]
        x += [self.pad_id] * (self.max_seq_length - len(x))
        x = torch.LongTensor(x)# 转化为torch.LongTensor
        return x

BATCH_SIZE = 4  # 可以自行调整batch size
train_set = dataset(sonnets_in_ids, vocab, max_length)
assert train_set[0].shape == torch.Size([max_length + 2])
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True, num_workers=0, drop_last=True)


class SonNet(nn.Module):
    def __init__(self, vocab_size, hidden_size, output_size, num_layers=1):
        super().__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        # self.hidden = torch.randn(hidden_size,hidden_size)
        # self.c0 = torch.randn(self.num_layers, self.batch_size, self.hidden_size)
    def forward(self, inputs, hidden=None):
        """完成模型的前向传播过程
        输入
        inputs: tensor，维度为`[batch_size, max_seq_length]`
        hidden: tuple，仅在采样时使用，包含了LSTM的初始隐状态向量和细胞状态向量，见输出`hidden`的说明
        输出
        outputs: tensor，维度为`[batch_size, max_seq_length, vocab_size]`，值域为$\mathbb{R}$
        hidden: tuple，包含了LSTM的最终隐状态向量和细胞状态向量，仅在采样时使用，一次`forward`的hidden输出作为
            下一次forward的`hidden`输入（第一次仍然输入`None`）
        """
        # b,max_seq_length = inputs.size()
        # h0 = torch.rand(self.num_layers,BATCH_SIZE,self.hidden_size,device=device_id)
        # c0 = torch.rand(self.num_layers,BATCH_SIZE,self.hidden_size,device=device_id)
        # hc = (h0,c0)
        # hc.to(device_id)
        # hc = torch.randn(self.hidden_size,self.hidden_size)
        # if hidden == None:
        #     hidden = torch.randn([batch_size, hidden_size)
        inputs = self.embedding(inputs) # [batch_size, max_seq_length, hidden_size]
        if inputs.ndim == 2:
            inputs = repeat(inputs, 'a b -> c a b', c=1)
        # inputs.to(device_id)
        # outputs, self.hidden = nn.LSTM(inputs,self.hidden)
        outputs, hidden = self.lstm(inputs, hidden)
        # outputs, (hidden,C) = nn.LSTM(inputs,(hidden,C))


        # self.hidden = torch.randn(self.num_layers, self.batch_size, self.hidden_size)
        # self.c0 = torch.randn(self.num_layers, self.batch_size, self.hidden_size)
        # outputs, (self.hidden,self.c0) = nn.LSTM(inputs, (self.hidden,self.c0))
        logits = self.fc(outputs)
        
        return logits, hidden



HIDDEN_SIZE = 256
LR = 0.001
EPOCHS = 20  # 可以自行调整训练轮数，建议先设置较少轮数验证实现的准确性，再调整轮数使模型loss收敛
model = SonNet(vocab_size=len(vocab), hidden_size=HIDDEN_SIZE, output_size=len(vocab))
model.to(device_id)
optimizer = torch.optim.Adam(model.parameters(), lr=LR)
criterion = nn.CrossEntropyLoss(ignore_index=train_set.pad_id)


loss_cache = []
print(1)
for epoch in range(EPOCHS):
    # print(2)
    epoch_loss_sum = 0
    # print(3)
    for i, batch in enumerate(train_loader):
        batch = batch.to(device_id)
        inputs = batch[:, :-1].contiguous()
        labels = batch[:, 1:].contiguous()
        # print(inputs,labels)
        logits, _ = model(inputs)
        # print(logits)
        # 完成loss的计算，反向传播和权重更新
        # loss = 0
        # for x in range(170):
        #     loss = loss + criterion(logits[:,x,:], labels[:,x,:])
        # loss / len(170)

        logits = rearrange(logits, 'a b c -> a c b')
        loss = criterion(logits, labels).mean()
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        # print(i,loss)
        loss_cache.append(loss.item())
        epoch_loss_sum += loss.item()
        # print(4)
    epoch_loss_avg = epoch_loss_sum / len(train_loader)
    print('Epoch: {}, Loss: {}'.format(epoch, epoch_loss_avg))


# 画出loss曲线
plt.plot(loss_cache)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.show()


@torch.no_grad()
def generate(model, start_token='<START>', max_length=500, temperature=1.0):
    model.eval()
    start_id = token_to_id[start_token]
    x = torch.LongTensor([start_id]).to(device_id)
    hidden = None
    ids = []
    logprob = 0.
    for i in range(max_length):
        logits, hidden = model(x, hidden)
        logits = logits.view(-1)
        probs = torch.softmax(logits / temperature, dim=-1)
        next_id = torch.multinomial(probs, 1)
        next_id = next_id.item()
        next_prob = probs[next_id]
        logprob += torch.log(next_prob)
        ids.append(next_id)
        x = torch.LongTensor([next_id]).to(device_id)
        if next_id == token_to_id['<END>']:
            break
    string = decode(ids)
    return string, logprob.item()


string, logprob = generate(model, temperature=0.3)
print('Logprob of generated string:', logprob)
print('Generated string:\n%s' % string)

string, logprob = generate(model, temperature=0.5)
print('Logprob of generated string:', logprob)
print('Generated string:\n%s' % string)

string, logprob = generate(model, temperature=0.1)
print('Logprob of generated string:', logprob)
print('Generated string:\n%s' % string)