import pandas as pd
import ServerAPI as server_api
import sys
sys.path.append('../')

class Trainer ():
    def __init__(self,DownloadTrainingDataset) :
        self.TrainingDataSet = pd.read_csv(DownloadTrainingDataset)
       
    def callExtractor(ExtractData):
        return Extractor(ExtractData)
        
    def train_gini_decision.fit(data,labels) :
        // doubt
    
class Extractor():
    def __init__(self,ExtractData):
        self.ExtractData = ExtractData
    
    def FeatureExtraction(ExtractData):
        return df[self.ExtractData]



if __init__ == '__main__':
    tt  = Trainer('dataset.csv')
    tt
    
