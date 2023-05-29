from fire import Fire

import src

if __name__ == '__main__':
    Fire({
        'lidar_check': src.operations.lidar_check,
        'cumsum_check': src.operations.cumsum_check,
        'train': src.training.train,
        'eval_model_iou': src.operations.eval_model_iou,
        'viz_model_preds': src.operations.viz_model_preds,
    })