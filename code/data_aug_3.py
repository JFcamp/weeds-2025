# Author: João Fernando Mari
# joaofmari.github.io
# https://github.com/joaofmari


from torchvision import transforms


def get_da(da, DS_MEAN=[0.485, 0.456, 0.406], DS_STD=[0.229, 0.224, 0.225]):
    """
    """
    if da == 0:  
        # Resize(224)
        data_transforms = transforms.Compose([
            transforms.Resize(size=(224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(DS_MEAN, DS_STD)
        ])

    elif da == 1: 
        # Resise(256) + CenterCrop(224)
        data_transforms = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(DS_MEAN, DS_STD)
        ])

    elif da == 2: # **** HP optmization AND Without DA  ****
        # RandomResizedCrop (224). 
        data_transforms = transforms.Compose([
            transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
            transforms.ToTensor(),
            transforms.Normalize(DS_MEAN, DS_STD)
        ])
        
    # **** DATA AUGMENTATION ****
    elif da == 3: 
        # Data augmentation base
        data_transforms = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
            transforms.ToTensor(),
            transforms.RandomErasing(p=0.5, scale=(0.02, 0.25)),
            transforms.Normalize(DS_MEAN, DS_STD),
        ])

    elif da == 4: # **** With DA ****
        # Data augmentation base. NO HUE. 
        data_transforms = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
            ### transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.ToTensor(),
            transforms.RandomErasing(p=0.5, scale=(0.02, 0.25)),
            transforms.Normalize(DS_MEAN, DS_STD),
        ])

    elif da == 5: 
        # Data augmentation base. NO HUE, NO RandomErasing.
        data_transforms = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
            ### transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
            transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
            transforms.ToTensor(),
            ### transforms.RandomErasing(p=0.5, scale=(0.02, 0.2)),
            transforms.Normalize(DS_MEAN, DS_STD),
        ])
        
    elif da == 6: 
        # Data augmentation base. NO Jitter, NO RandomErasing.
        data_transforms = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomRotation(15),
            transforms.RandomResizedCrop(224, scale=(0.8, 1.0)),
            ###transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
            transforms.ToTensor(),
            ###transforms.RandomErasing(p=0.5, scale=(0.02, 0.25)),
            transforms.Normalize(DS_MEAN, DS_STD),
        ])
 

    return data_transforms

