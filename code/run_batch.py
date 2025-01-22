
# Author: João Fernando Mari
# joaofmari.github.io
# https://github.com/joaofmari

import os
import time
import datetime
import argparse
import shutil

parser = argparse.ArgumentParser()

parser.add_argument('--ds', help='Dataset name.', type=str, default='Weeds')
parser.add_argument('--ds_split', help='How ds is split: ["train-val-test", "train-test", "no-split"].', type=str, default='no-split')

args = parser.parse_args()

EXP_PATH_MAIN = f'exp_hp_{args.ds}'

# TTA strategy
dapred = 0

arch_list = [#'alexnet',
             'vit_b_16', 
             #'efficientnet_v2_s',
             #'resnet50', 

             # Incluir mais arquiteturas...
            ]

# Estratégias de aumento de dados. Verificar arquivo 'data_aug_3.py'
# (Listas devem ser do mesmo tamanho.)
# datrain_list = [2,3] 
# daval_list = [1,1]
# datest_list = [1,1]
datrain_list = [3] 
daval_list = [1]
datest_list = [1]

# Total de épocas de treinamento.
epochs = 200
num_workers = 0

# Replace by the best hyperparameter values:
bs_dict = { 
             'vit_b_16': 16, 
             'efficientnet_v2_s':16,
             'resnet50': 16,
           # Para outras arquiteturas
           } 

lr_dict = {'resnet50': 0.0001,
             'vit_b_16': 0.0001, 
             'efficientnet_v2_s':0.0001,
           # Para outras arquiteturas
           } 

ec = 0
for arch in arch_list:
    # ec = 0
    for datrain, daval, datest in zip(datrain_list, daval_list, datest_list):

        cmd_str = f'nohup python train_model.py --ds {args.ds} --ds_split {args.ds_split} ' + \
                  f'--arch {arch} --num_workers {num_workers} ' + \
                  f'--bs {bs_dict[arch]} --lr {lr_dict[arch]} --ep {epochs} --optimizer "Adam" ' + \
                  f'--datrain {datrain} --daval {daval} --datest {datest} --ec {ec} '  

        print(cmd_str)
        ec = ec + 1

        os.system(cmd_str)

if os.path.exists('./nohup.out'):
    suffix = ''
    while True:
        if os.path.exists(os.path.join(EXP_PATH_MAIN, 'nohup' + suffix + '.out')):
            suffix += '_'
        else:
            break

    shutil.move('./nohup.out', os.path.join(EXP_PATH_MAIN, 'nohup' + suffix + '.out'))

print('Done! (run_batch)')


