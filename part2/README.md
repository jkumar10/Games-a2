# a2 - Tweet Classification
The Process for estimation of location based on tweet has been done using following steps-

**STEP 1:** The training and test dataset have been cleaned using the code<br>
		`cat tweets.test1.txt | tr '\200-\377' '*' | tr '\r' ' '   > tweets.test1.clean.txt`<br>
		`cat tweets.train.txt | tr '\200-\377' '*' | tr '\r' ' '   > tweets.train.clean.txt`<br>

**STEP 2:** Functions defined along with their operation are:<br>
		**word_prob**: Function takes in a list and a word as an input and returns the frequency of word in the passed list<br>
		**clean**: Function takes word as an input, removes the punctuations and converts into lowercase and return the cleaned word<br>
		**data_clean**: Function takes in a lists of tweets, cleans one word at a time by calling the 'clean' function and returns the cleaned tweets<br>
	Steps taken to clean are as follows<br>
		1. All the punctuations, #s and @s are removed<br>
		2. All the words are converted to lowercase<br>

**STEP 3:** Locations(output classes) are extracted from the input data and stored in variable **'target'**

**STEP 4:** Tweets are extracted from the input data and stored in variable **'data'**

**STEP 5:** Tweets stored in variable data are cleaned by calling the function **'data_clean'**

**STEP 6:** **'Bag of Words**' is creating by taking unique words from the stored tweets

**STEP 7:** Probability of each location is stored in the variable **'prior'**. This is the prior probability of each class (P(l)) and it is calculated using the frequency of tweets from that location over total number of tweets

**STEP 8:** Dataframe for likelihood estimations(P(w|l)) is constructed. This is done using following steps-<br>
		1. For each location, bag of words is contructed along with its frequency of occurrence for that location. This is stored in a dictionary.<br>
		2. A dataframe is contructed into a dataframe. The column of the dataframe is the different location and the row is for different word. The element stored at a cell is probability of that word for corresponding location P(w|l)<br>
		3. All the values in the dataframe are converted to log for calculating posterior probabilities<br>

**STEP 9:** Following steps are taken to find out most **'distinctive'** words for each location<br>
		1. For each row in **'likelihood'** dataframe. The location for which the value is highest in the row is stored in the column 'max_location' and the value is stored in **'max_likelihood'**<br>
		2. The words are then grouped by **'max_location'** column and top 5 are chosen based on their **'max_likelihood'** value.<br>

**STEP 10:** Prediction is done for a particular word using the formula P(l|w)=P(l).P(w|l) where P(l) is stored in the variable 'p_class' and P(w|l) is obtained from the dataframe **'likelihood_df'**. Given a set of words in a tweet, P(l|w1 w2 w3 .. wn) is calculated for a location using the formula:<br>
	P(l|w1 w2 w3 ... wn) = P(l)P(w1|l).P(w2|l).P(w3|l)....P(wn|l)<br>
	Taking log on both sides<br>
	log(P(l|w1 w2 w3 ... wn)) = log(P(l))+log(P(w1|l))+log(P(w2|l))+ ... + log(P(wn|l))<br>
	We calculate the log of probability for each loaction and take the location with best score.<br>

**STEP 11:** The code takes input the test and train file and gives an output file with predicted location, actual location and tweet. Top 5 'distinctive' words displayed for each loaction.

Data Cleaning and procedural steps references-
* https://pythonmachinelearning.pro/text-classification-tutorial-with-naive-bayes/
* https://towardsdatascience.com/multinomial-naive-bayes-classifier-for-text-analysis-python-8dd6825ece67
