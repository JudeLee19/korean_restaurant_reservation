# Korean Restaurant Reservation Dialogue System
Implement korean restaurant reservation dialogue system based on hybrid code network(https://github.com/johndpope/hcn).
<br>Add post processing and edit templates to adjust korean dataset which we created. 759 training dialogue data and 190 test dialogue data were used for Korean restaurant reservation dialogue system model. <br>Experimental results show that the proposed system has 95% accuracy of per-response and 63% accuracy of per-dialogue.
<br><br>
## Download Word2vec Trained with Korean Data 
1. ```cd data/ ```
2. [Downalod word2vec](https://koreaoffice-my.sharepoint.com/personal/judelee93_office365_korea_ac_kr/_layouts/15/guestaccess.aspx?docid=0bb7c7215512c45dda72a0ac5a01c4175&authkey=Aa9oWjzy0H6efrc04edY8rY)
3. ```tar -xvf korean_word2vec.tar.gz```

## Train
```
python3 train.py
```
## Building the Dialogue Corpus
The Korean dataset is consist of 1000 dialogues.(data/korean_train)
### Restaurant Reservation System Data Translation
![150](./img/data_table_1.png)

### Variation of Speech Patterns according to Purpose of Utterance in Korean
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
