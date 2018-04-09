import os
for x in range(1,10):
    print('clean tmp')
    os.system('bash cleantmp.sh')
    print(x)
    print('python generateFeatures.py {}'.format(x))
    os.system('python generateFeatures.py {}'.format(x))
    print('python xgb_train_cvBodyId.py {}'.format(x))
    os.system('python xgb_train_cvBodyId.py {}'.format(x))
