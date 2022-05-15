Installations: 

	- IDE: PyCharm (https://www.jetbrains.com/pycharm/download/#section=windows)

	- Anaconda Navigator (https://www.anaconda.com/products/distribution#windows)

	- Visual Studio Distribution & C++ Desktop Development Package (https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)

	- Python Version: 3.8 or 3.7 (https://www.python.org/downloads/)


Commands in Anaconda Promt: 

	- conda create --name KovvyChatbot python==3.8
	- conda activate KovvyChatbot 
	- conda install ujson
	- conda install tensorflow
	- pip install rasa 
	- rasa run -m models --enable-api --cors "*" 


Running system: 

1: Copy the local path of index.html file e.g (C:\Users\rawin\Desktop\KovvyChatbot\index.html)
2: Open Google Chrome browser 
3: Paste local path of index.html file and run


Policy: 

TED Policy#
The Transformer Embedding Dialogue (TED) Policy is a multi-task architecture for next action
prediction and entity recognition. The architecture consists of several transformer encoders
which are shared for both tasks. A sequence of entity labels is predicted through a Conditional 
Random Field (CRF) tagging layer on top of the user sequence transformer encoder output
corresponding to the input sequence of tokens. For the next action prediction, the dialogue
transformer encoder output and the system action labels are embedded into a single semantic 
vector space. We use the dot-product loss to maximize the similarity with the target label and
minimize similarities with negative samples.