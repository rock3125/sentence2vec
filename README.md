<h1>Sentence 2 vec</h1>

Simple Python 3.5/3.6 implementation of the algorithm by Sanjeev Arora, Yingyu Liang, and Tengyu Ma

example usage, see `spacy_sentence2vec_demo.py` which reads the text file `semantic_test_text.txt` and displays the similarity score between each sentence in that file.

Sample output of this program:
```
I like my phone :: I like my phone => distance = 0.0
I like my phone :: my phone I like => distance = 0.0
I like my phone :: My phone is not good . => distance = 2.010060652006318
I like my phone :: Your cellphone looks great . => distance = 2.3985695492804
I like my phone :: Will it snow tomorrow ? => distance = 3.12213627358705
I like my phone :: Recently a lot of hurricanes have hit the US => distance = 2.9026474926300305
I like my phone :: Global warming is real => distance = 4.251977606682901
I like my phone :: An apple a day keeps the doctors away => distance = 2.851633708928399
I like my phone :: Eating strawberries is healthy => distance = 4.321134787988386
I like my phone :: Is paleo better than keto ? => distance = 3.5363370607353235
I like my phone :: How old are you ? => distance = 2.7340841031141716
I like my phone :: what is your age ? => distance = 2.9649910826697106
my phone I like :: my phone I like => distance = 0.0
my phone I like :: My phone is not good . => distance = 2.010060652006318
my phone I like :: Your cellphone looks great . => distance = 2.3985695492804
my phone I like :: Will it snow tomorrow ? => distance = 3.12213627358705
my phone I like :: Recently a lot of hurricanes have hit the US => distance = 2.9026474926300305
my phone I like :: Global warming is real => distance = 4.251977606682901
my phone I like :: An apple a day keeps the doctors away => distance = 2.851633708928399
my phone I like :: Eating strawberries is healthy => distance = 4.321134787988386
my phone I like :: Is paleo better than keto ? => distance = 3.5363370607353235
my phone I like :: How old are you ? => distance = 2.7340841031141716
my phone I like :: what is your age ? => distance = 2.9649910826697106
My phone is not good . :: My phone is not good . => distance = 0.0
My phone is not good . :: Your cellphone looks great . => distance = 1.5524571077712057
My phone is not good . :: Will it snow tomorrow ? => distance = 2.493190775736282
My phone is not good . :: Recently a lot of hurricanes have hit the US => distance = 2.287748889805466
My phone is not good . :: Global warming is real => distance = 3.3686135143818015
My phone is not good . :: An apple a day keeps the doctors away => distance = 2.084245349694273
My phone is not good . :: Eating strawberries is healthy => distance = 3.655992611251389
My phone is not good . :: Is paleo better than keto ? => distance = 2.818197185369856
My phone is not good . :: How old are you ? => distance = 2.141447417146291
My phone is not good . :: what is your age ? => distance = 2.0759725481356064
Your cellphone looks great . :: Your cellphone looks great . => distance = 0.0
Your cellphone looks great . :: Will it snow tomorrow ? => distance = 2.7298513560471536
Your cellphone looks great . :: Recently a lot of hurricanes have hit the US => distance = 2.5246406338042937
Your cellphone looks great . :: Global warming is real => distance = 3.498414079708524
Your cellphone looks great . :: An apple a day keeps the doctors away => distance = 2.329530271355813
Your cellphone looks great . :: Eating strawberries is healthy => distance = 3.803350471259557
Your cellphone looks great . :: Is paleo better than keto ? => distance = 3.0684892914114417
Your cellphone looks great . :: How old are you ? => distance = 2.408540229930858
Your cellphone looks great . :: what is your age ? => distance = 2.3154809495988946
Will it snow tomorrow ? :: Will it snow tomorrow ? => distance = 0.0
Will it snow tomorrow ? :: Recently a lot of hurricanes have hit the US => distance = 2.6173830231596162
Will it snow tomorrow ? :: Global warming is real => distance = 3.566124820806414
Will it snow tomorrow ? :: An apple a day keeps the doctors away => distance = 2.5436350275856254
Will it snow tomorrow ? :: Eating strawberries is healthy => distance = 3.7928064821902328
Will it snow tomorrow ? :: Is paleo better than keto ? => distance = 3.0043821287395365
Will it snow tomorrow ? :: How old are you ? => distance = 2.395394786711788
Will it snow tomorrow ? :: what is your age ? => distance = 2.4906178000371915
Recently a lot of hurricanes have hit the US :: Recently a lot of hurricanes have hit the US => distance = 0.0
Recently a lot of hurricanes have hit the US :: Global warming is real => distance = 3.1196681040661454
Recently a lot of hurricanes have hit the US :: An apple a day keeps the doctors away => distance = 2.0265563510558318
Recently a lot of hurricanes have hit the US :: Eating strawberries is healthy => distance = 3.7632797839807632
Recently a lot of hurricanes have hit the US :: Is paleo better than keto ? => distance = 3.0051299998349834
Recently a lot of hurricanes have hit the US :: How old are you ? => distance = 2.2909659610956608
Recently a lot of hurricanes have hit the US :: what is your age ? => distance = 2.531567324374016
Global warming is real :: Global warming is real => distance = 0.0
Global warming is real :: An apple a day keeps the doctors away => distance = 3.2971455317645044
Global warming is real :: Eating strawberries is healthy => distance = 4.247857707450735
Global warming is real :: Is paleo better than keto ? => distance = 3.567217222960459
Global warming is real :: How old are you ? => distance = 3.5173015140857786
Global warming is real :: what is your age ? => distance = 3.2550002139172594
An apple a day keeps the doctors away :: An apple a day keeps the doctors away => distance = 0.0
An apple a day keeps the doctors away :: Eating strawberries is healthy => distance = 3.2718770906341246
An apple a day keeps the doctors away :: Is paleo better than keto ? => distance = 2.9017468809523868
An apple a day keeps the doctors away :: How old are you ? => distance = 2.383066835485839
An apple a day keeps the doctors away :: what is your age ? => distance = 2.3234352848419304
Eating strawberries is healthy :: Eating strawberries is healthy => distance = 0.0
Eating strawberries is healthy :: Is paleo better than keto ? => distance = 3.3200451747571376
Eating strawberries is healthy :: How old are you ? => distance = 3.720474209081014
Eating strawberries is healthy :: what is your age ? => distance = 3.665004580981702
Is paleo better than keto ? :: Is paleo better than keto ? => distance = 0.0
Is paleo better than keto ? :: How old are you ? => distance = 2.735344809108005
Is paleo better than keto ? :: what is your age ? => distance = 2.728333667047685
How old are you ? :: How old are you ? => distance = 0.0
How old are you ? :: what is your age ? => distance = 1.6852340096863747
what is your age ? :: what is your age ? => distance = 0.0
```
