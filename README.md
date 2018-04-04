# Korean Restaurant Reservation Dialogue System
An implementation of a korean restaurant reservation dialogue system based on a hybrid code network(https://github.com/johndpope/hcn).
<br>Post processing was added and templates were edited to adjust the korean dataset that we created. 
759 instances of training dialogue data and 190 instances of test dialogue data were used for the system model. <br>Experimental results showed that the proposed system has 95% accuracy per-response and 63% accuracy per-dialogue.
<br><br>
## Download Word2vec Trained with Korean Data 
1. ```cd data/ ```
2. [Download word2vec](https://koreaoffice-my.sharepoint.com/personal/judelee93_office365_korea_ac_kr/_layouts/15/guestaccess.aspx?docid=0bb7c7215512c45dda72a0ac5a01c4175&authkey=Aa9oWjzy0H6efrc04edY8rY)
3. ```tar -xvf korean_word2vec.tar.gz```

## Train
```
python3 train.py
```
## Building the Dialogue Corpus
The Korean dataset consists of 1000 dialogues.(data/korean_train)
### Restaurant Reservation System Data Translation
![150](./img/data_table_1.png)

### Variation of Speech Patterns according to Intonation in Korean
![](./img/data_table_2.png)

## System Architecture
![250](./img/proposed_methods.png)

## Interaction
![250](./img/example.png)

## Result
![](./img/interact_2.png)

### Hyper-parameter
![50](./img/hyper.png)

### Evaluation
- Per-response Accuracy : 95%<br>
- Per-dialogue Accuracy : 71%
