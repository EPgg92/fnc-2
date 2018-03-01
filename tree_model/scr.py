import os
for x in range(10):
    print(x)
    print('python generateFeatures.py {}'.format(x))
    os.system('python generateFeatures.py {}'.format(x))
    print('python xgb_train_cvBodyId.py {}'.format(x))
    os.system('python xgb_train_cvBodyId.py {}'.format(x))
