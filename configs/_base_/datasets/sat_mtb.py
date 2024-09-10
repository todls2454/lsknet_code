# 새로운 설정은 기본 설정을 상속하여 필요한 수정 사항을 강조합니다
_base_ = '/home/hansujung2339/Large-Selective-Kernel-Network/configs/rotated_retinanet/rotated_retinanet_hbb_r50_fpn_1x_dota_oc.py'

# 1. 데이터셋 설정
dataset_type = 'SATMTBDataset'  # 데이터셋 타입을 sat-mtb에 맞게 수정
classes = ('train', 'ship', 'airplane')  # 클래스 이름 수정
data = dict(
    samples_per_gpu=4,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        # `classes` 필드에 사용자 정의 클래스 이름을 명시적으로 추2가합니다
        classes=classes,
        ann_file='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/train/annotation_data',  # 실제 경로로 수정
        img_prefix='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/train/image_data'  # 실제 경로로 수정
    ),
    val=dict(
        type=dataset_type,
        # `classes` 필드에 사용자 정의 클래스 이름을 명시적으로 추가합니다
        classes=classes,
        ann_file='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/val/annotation_data',  # 실제 경로로 수정
        img_prefix='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/val/image_data'  # 실제 경로로 수정
    ),
    test=dict(
        type=dataset_type,
        # `classes` 필드에 사용자 정의 클래스 이름을 명시적으로 추가합니다
        classes=classes,
        ann_file='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/test/annotation_data',  # 실제 경로로 수정
        img_prefix='/home/hansujung2339/Large-Selective-Kernel-Network/data/sat_mtb2/test/image_data'  # 실제 경로로 수정
    )
)

# 2. 모델 설정
model = dict(
    bbox_head=dict(
        type='RotatedRetinaHead',
        # 기본값 15에서 4로 `num_classes` 필드를 명시적으로 변경합니다.
        num_classes=3  # 클래스 수를 4로 수정
    )
)
