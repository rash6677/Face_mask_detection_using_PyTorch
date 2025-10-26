import os

print('Train mask:', len(os.listdir('Train_Model/data/train/mask/WithMask')))
print('Train no_mask:', len(os.listdir('Train_Model/data/train/no_mask/WithoutMask')))
print('Test mask:', len(os.listdir('Train_Model/data/test/mask/WithMask')))
print('Test no_mask:', len(os.listdir('Train_Model/data/test/no_mask/WithoutMask')))