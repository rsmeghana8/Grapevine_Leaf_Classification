# Classification of Grapevine species using leaf images
### Objective

The objective of this project is to implement an image classifier to identify grapevine species using their leaf images.

## Documentation
### Dataset description
Get the dataset here: [Grapevine_leaf_detection](https://www.kaggle.com/datasets/muratkokludataset/grapevine-leaves-image-dataset)

Dataset has total of 500 leaf images belonging to 5 different grapevine species namely AK, Ala_Idris, Buzgulu, Dimnit and Nazil. The dataset is balanced with each species having 500 images.

### Installing requirements
To install all the dependencies,after cloning the repository run the following command:
```
    pip install -r requirements.txt
```

### Training
we are usingcVGG16 model thats pretrained on the Imagenet dataset from keras API
Change the hyper-parameters in the 'params.yaml' file to fine-tune and train by running 
```
    python stage_02_training.py
```
Best model weights will be saved at 
```
    artifacts/training
```
### Evaluation
To evaluate model on Validation data run
```
   python stage_03_evaluation.py
```
* Note- Alternative to running Data Ingestion ,training and evaluation pipelines seperatly, they can be run together using 'main.py'

```
     python main.py
``` 

### Experiments and Results

Here are the model scores when ran for different epochs

|      Epochs   |  Val Accuracy   |   Val Loss  |
| :------------ |:---------------:| -----------:|
|       100     |      69.9       |    2.80     |
|       200     |      86.6       |    0.46     |

The model that's trained for 200 Epochs looks promising. lets check out its loss and accuracy curves- 
- ![#7cb342](https://placehold.co/15x15/c5f015/c5f015.png) `Train`
- ![#e8710a](https://placehold.co/15x15/1589F0/1589F0.png) `Val`
- 
![epochs vs loss](https://github.com/rsmeghana8/Grapevine_Leaf_Classification/assets/57563443/554dd0f5-6190-4189-89ce-947d5d51c6e9)



![epochs_vs_accuracy](https://github.com/rsmeghana8/Grapevine_Leaf_Classification/assets/57563443/d02f9d7c-79da-47ef-a72d-7014c1e5e9dd)



The model looks balanced as the val curves follows train curves closely


Let's look at the confusion matrix for model trained for 200 Epochs

![CM - instasize](https://github.com/rsmeghana8/Grapevine_Leaf_Classification/assets/57563443/ac8f4890-4560-4068-8c52-cd7c4de13f92)


The model seems to perfrom well for all the classes but the class Ala_idris seems to be bit behind the rest with more false positives

### To furthur improve the model performance
* Trying different architecture
* Training for more Epochs
* Changing the augmentation
