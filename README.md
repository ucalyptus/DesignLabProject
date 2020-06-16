[![Run on Repl.it](https://repl.it/badge/github/ucalyptus/DesignLabProject)](https://repl.it/github/ucalyptus/DesignLabProject)
[](images/MavenLogo.png)
# Team Maven : Credit Card Approval System
Design Lab Project . Watch the **technical demo** [here](https://youtu.be/8bPrCyUI_rU)
# Team
- Muskan - Project Manager
- Sayantan Das - Lead Developer
- Sheetal Kumari - QA Manager
- Soujannya Roy - QA Engineer
- Md Salman - Developer
- Debankan Ganguly - Developer
# Problem Statement
Small businesses must seek credit approval to obtain funds from lenders, investors, and vendors, and also grant credit approval to their customers. Banking industries receive so many applications for credit card request. Going through each request manually can be very time consuming, also prone to human errors. 
# Solution Statement
- **I** : Building a probabilistic statistical model that looks into historical data to find patterns in what parameters lie in decision making behind the approval of a credit model.
- **II** : Deploying a trained model.The bank server makes a FTP request to Maven , sending it their list of applications for the day. Maven's AI cron job does the predictions and sends it back to the bank.
- **III** : To ensure model robustness, model is refreshed every 5 days by developers working on Maven. They employ public/privatised data and a myriad of boosted trees and other advanced algorithms to make sure misclassification can be avoided as much as possible during inference phase. 

# Initial Setup

`sh setup.sh` <br>

If you are running on Anaconda follow these instructions,
```
conda create -n mavenlab python=3.6
conda activate mavenlab
```

# Quick Run
```
 cd src/
 sh run.sh
```
# Tests
```
cd tests/
sh runtest.sh
```

## FTP instructions are posted [here](FTP_INST.md)
# Model Creation
Preconfigured Notebook can be viewed [here.](https://github.com/ucalyptus/DesignLabProject/blob/master/Maven%20System.ipynb%20-%20Colaboratory.pdf)

# Use Case Diagram
![](images/uc.png)

# Class Diagram
![](images/ClassDiagram.png)

# Sequence Diagrams
![Sanitizing the Data](images/SanitizingTheData.png)
![Performing Prediction](images/PerformingThePrediction.png)
![Get Predicted Output](images/GetPredictionOutput.png)
![Train Model](images/TrainModelMaven.png)

# WBS
![](images/WBS.png)
