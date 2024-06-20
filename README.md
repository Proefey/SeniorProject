Senior Project For John Oliver

**LINKS:**

Notebooks Link: https://drive.google.com/drive/folders/11KwP2ssLK_C1qvDHPQ_UsKeM4xDRxykh?usp=sharing

Model Guide Link: https://docs.google.com/document/d/1aGZfCvdTmGFCzBJWIljn-4x8hL23RWuC2dhB3J3lHdk/edit?usp=sharing

Tests Spreadsheet Link: https://docs.google.com/spreadsheets/d/1VgxDISm0i45IUAdlZTjAA3WorEQ5AnWhrOyHC4biVhc/edit?usp=sharing

Harvard Magic Wand Dataset Creation Website: https://tinyml.seas.harvard.edu/magic_wand/

Note: These notebooks are practically the same notebooks used from the previous Hardvard Course, will only minor edits.



**REPORT:**


**Datasets**

There are 3 datasets included in the senior project, 2 of which are custom made:
Pete’s Digit
The dataset that the Harvard course uses with the magic wand. Can be found at: 
https://github.com/petewarden/magic_wand_digit_data/
Left & Right
49-50 strokes each for a left stroke and right stroke
Alphabet:
21-22 strokes per letter of the alphabet
Including many null characters that allows the player to reset the wand position without using
The characters are in cursive and the i and j characters do not contain a dot on top of them.


**Tests**

For both Pete’s Digit and Left & Right databases, I decided to test a multitude of models with differing number of nodes and number of layers as they are easy to work with and can create accurate models.

However, for the alphabet database, since the classification is likely too complex to ever get a great model, I decided to pivot the alphabet models to test the effect on the number of epochs it has on the model.
Test Results
I ran various tests with the 3 datasets that included different model sizes, some increasing the amount of layers or nodes, some decreasing the amount of layers or nodes, in an attempt to find correlations between the type of model, the model’s training time, the model’s accuracy, the size of the model, and the power consumption. 

Starting off with training time, the training time seemed to be more tied with the network condition and the dataset used rather than the model used, which makes sense as the training occurs on google collab, which means the training is occurring over a server, Surprisingly enough though, the pete’s digit dataset seemed to have similar training times to the alphabet set, but it may be because pete’s digit dataset has vastly larger amounts of strokes per class as compared to the alphabet dataset, despite having less classes.

Model accuracy and size were both very much tied to the size of the model, some of which were too large for the arduino nano model to work with (And thus did not produce anything). This is the least surprising, although it is worth noting that larger datasets had diminishing returns in terms of accuracy, with the larger models only having a small boost in accuracy compared to the base models.

Finally, power consumption has no conclusion. The hardware I was using to test power consumption (YOJOCK USB Tester Multimeter) was reading the same power consumption regardless of model, but the power reading changed by day. The only result I can suspect that it is likely that the model may use around 0.1W to 0.15W and the size of the model is not a determining part of that power consumption. I can suspect this because the models that did not work due to their size had a base power that is 0.1W to 0.15W lower than when the model was working.

It's also worth noting that the number of epochs in the training time did not increase the size of the model, but did increase the accuracy for the alphabet models they were tested on.


**Limitations**

Custom Set Limitations
Creating the alphabet set came with many limitations, most significant of which was that each dataset had to be created using only 1 stroke. This made printing letters much more difficult as they often required more than 1 stroke to complete. I semi-worked around this by using cursive which did allow most letters to be done in one stroke, although letters i, t, j, and x still presented problems. ‘i’ and ‘j’ were worked around by omitting the dot on top, but t and x had to be worked around by just following the two strokes required, even though it ruins the shape.

Actually creating both the left and right data had various issues that I had to adjust to:
Creating enough strokes, it was clear 20 was not enough
Ensuring that the strokes are different enough from each other, I think this is the main reason why the alphabet database is difficult to train with as letters such as e and i are very similar given the precise nature of the magic wand
Ensuring that the strokes were big enough. I would recommend standing up whenever you are creating the dataset.
Ensuring that the strokes could be reset, it was a major problem that the wand accidentally went off. Although the professor did suggest adding a button or some kind, although I can’t test this by the time it's due, I may come back to this.


**Notebook Limitations**

The only major issue I found with the notebooks is that given a small amount of strokes per class and a lot of classes (Such as alphabet), the number of training datasets and validation datasets would be mismatched, and thus I would often have to re-run the cell under “Take the dataset and shuffle it into the Training/Validation/Test splits” until it worked. I could also change the percentage of Validation sets to help this problem.


**Results**

Overall, using pete’s dataset and the left and right dataset were both fairly successful, although the alphabet one not so much due to its massive size and the amount of time and effort it takes to create the dataset, as well as the similarity of the strokes playing a large factor to its inaccuracies. 
