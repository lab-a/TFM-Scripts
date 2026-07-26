
from trainDetectronkCV import run_training_pipeline
from preProcessFunctions import *
from divisionDataset import dividir_y_mover_val_simple
from processMasks import batch_masks_to_single_json
import os

def main():
        
    config_dict50 = {
        'modalidad': 'FLAIR',
        'modelo': 'mask_rcnn_R_50_FPN_3x.yaml',
        'flip': 'vertical',
        'batch_size': 4,
        'gamma': 0.05,
        'base_lr': 0.001,
        'weight_decay': 0.0001,
        'maxiter': 5000,
        'steps': [2500],
        'roi_batch_size_per_image': 256,
        'roi_positive_fraction': 0.7,
        'rpn_fg_iou_thresh': 0.5,
        'rpn_bg_iou_thresh': 0.5,
        'lr_scheduler': 'WarmupMultiStepLR'
    } 

    config_dict101 = {
        'modalidad': 'FLAIR',
        'modelo': 'mask_rcnn_R_101_FPN_3x.yaml',
        'flip': 'none',
        'batch_size': 4,
        'gamma': 0.05,
        'base_lr': 0.00095935,
        'weight_decay': 0.00010362,
        'maxiter': 5000,
        'steps': [2500],
        'roi_batch_size_per_image': 256,
        'roi_positive_fraction': 0.5,
        'rpn_fg_iou_thresh': 0.7,
        'rpn_bg_iou_thresh': 0.5,
        'lr_scheduler': 'WarmupMultiStepLR'
    } 

    config_dictX101 = {
        'modalidad': 'FLAIR',
        'modelo': 'mask_rcnn_X_101_32x8d_FPN_3x.yaml',
        'flip': 'none',
        'batch_size': 1,
        'gamma': 0.05,
        'base_lr': 0.001,
        'weight_decay': 0.0001,
        'maxiter': 5000,
        'steps': [2500],
        'roi_batch_size_per_image': 256,
        'roi_positive_fraction': 0.5,
        'rpn_fg_iou_thresh': 0.5,
        'rpn_bg_iou_thresh': 0.5,
        'lr_scheduler': 'WarmupMultiStepLR'
    } 

    configs = [config_dict50, config_dict101, config_dictX101]  # Aquí puedes añadir más configuraciones si lo deseas
    base_dir_kcv = '/mnt/Data1/MSLesSeg-Dataset/5kfold_FLAIR/'
    modalidad =['1CrossVal', '2CrossVal', '3CrossVal', '4CrossVal', '5CrossVal'] 

    for conf in configs:
        for fold in modalidad:
            print(f"Procesando fold: {fold}")
            conf['modalidad'] = fold
            print(f"Configuración actualizada con fold: {base_dir_kcv + conf['modalidad']}")
            print(f"Entrenando con configuración: {conf}")
            # Ejecutar el pipeline de entrenamiento
            run_training_pipeline(conf)


if __name__ == "__main__":
    main()