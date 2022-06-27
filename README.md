#### KovvyChatbot
Covid-19 FAQ Chatbot - New Zealand

<img width="1020" alt="Main" src="https://user-images.githubusercontent.com/72056829/175912025-f5a715aa-f0ae-460c-a905-2086db941e54.png">

Installations: 

	- IDE: PyCharm (https://www.jetbrains.com/pycharm/download/#section=windows)

	- Anaconda Navigator (https://www.anaconda.com/products/distribution#windows)

	- Visual Studio Distribution & C++ Desktop Development Package (https://docs.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170)

	- Python Version: 3.8 or 3.7 (https://www.python.org/downloads/)


Commands in Anaconda Prompt: 

	- conda create --name KovvyChatbot python==3.8
	- conda activate KovvyChatbot 
	- conda install ujson
	- conda install tensorflow
	- pip install rasa 
	- rasa run -m models --enable-api --cors "*" 


Running system: 

	- Copy the local path of index.html file e.g (C:\Users\rawin\Desktop\KovvyChatbot\index.html)
	- Open Google Chrome browser 
	- Paste local path of index.html file and run
	
<img width="1020" alt="Demo" src="https://user-images.githubusercontent.com/72056829/175914292-9b7fe50b-8614-4611-a206-4cd20c2df3c1.png">



Societies’ dependence on data is expanding daily, and as this happens the platform’s data is accessible through becoming increasingly complex. Artificial Intelligence-powered Chatbots have recently become a critical tool for businesses and organizers to assist their users with answering questions, arranging items, providing service, retrieving data, or making API calls such as subscriptions. This report will focus on a recently develop Chatbot – Kovvy. It will cover the intent, domain service, user cases, dialogue flow, deployment policy, limitations, and improvements made to the Chatbot implementation.

Kovvy is a personal FAQ-based Chatbot that is designed to represent the Ministry of Health NZ. Its purpose is to remove users’ dependency on human-powered call centers and to provide relative Covid-19 related information concisely. Current alternatives have become overwhelmingly complex and overwhelming as there is an information overload. One search about a simple question such as “What are the daily case numbers?” has hundreds of results. Alongside this, the rules and regulations issued by the New Zealand government are changing rapidly to deal with the recent Omicron outbreak. This has meant these rules and regulations are hard to keep track of for users.

The Kovvy Chatbot is built using Rasa which is an open-source tool to build custom A.I. Chatbots using Natural Language Understanding. The Chatbot is written using Python; A general-purpose programming language that allows for easy integration with Rasa. In addition to this, HTML a standard language for web development is used to deploy the Chatbot on the web and allow for greater accessibility.

Kovvy is designed as a user-initiated chatbot thus it requires users to ask questions, to which it responds with clear and concise answers. First and foremost, Kovvy is designed to provide up-to-date information about Covid-19 in New Zealand. This is information such as current alert level, isolation rules, daily case numbers count, and guidance to Government approved scientific information regarding the SARS-CoV-2 mRNA vaccine. Secondly, Kovvy can assist users by providing them the ability to book in for a vaccination session. Finally, Kovvy will act as a companion in these challenging times and be able to cheer up the users.

To ensure that Kovvy caters to its users and follows the Human-Centered Design process, it is vital to first understand the users and develop a user persona. The name of Kovvy’s’ User Persona is Katie, who is a 25-year-old retail worker, who lives a part of a 4-person flat and has recently tested positive for Covid-19. She likes to ensure that she complies with all government rules and regulations, as she believes in the best interest of her personal, and flatmates’ health. Katie has an above-average understanding of technologies and can make her way through using Chatbots.



Rawinder Singh 

rawinder457@gmail.com


----------------------------------------- Disclaimer ------------------------------------------- 

The Content has been made available for informational and educational purposes only. We do not make any representation or warranties with respect to the accuracy, applicability, fitness, or completeness of the Content. We do not warrant the performance, effectiveness or applicability of any sites listed or linked to in any Content.

The Content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. Never disregard professional medical advice or delay in seeking it because of something you have read or seen on the Site.

We hereby disclaims any and all liability to any party for any direct, indirect, implied, punitive, special, incidental or other consequential damages arising directly or indirectly from any use of the Content, which is provided as is, and without warranties.

 


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
