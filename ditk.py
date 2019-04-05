'''
Group5. Entity Typing

* Dataset:
1.	Onto Notes
 1-1. OntoNotes text corpus
 1-2. ??? @Gyanesh
2.	Wiki 
3.	Biocreative V Chemical Disease Relation benchmark (CDR)

* Evaluation Metrics:
1.	F-1 score 
2.	MRR 
'''

import abc

class entity_typing(abc.ABC):

	@classmethod
	@abc.abstractmethod
	def read_dataset(cls, dataset_name: string, options=None) -> np.array, np.array:
		''' 
		intput: (String) dataset_name OR dataset_path
		output: 2 things; dataset for train_data/ test_data

			NOTE: we need optional for input ? If not, we can remove "*args, **kwargs"
				  I specifically return np.array type for my train_data set. If others return different types of values then we can add more objects to return. then others can return just default value. 
		'''
		pass

	@classmethod
	@abc.abstractmethod
	def train(cls, dataset_nam: string, options=None) -> String:
		''' 
		intput: (String) dataset_name
		output: nothing and then just save the model on the file OR (String) model_path
		'''
		pass

	@classmethod
	@abc.abstractmethod
	def predict(cls, model_name: string, options=None) -> np.array:
		''' 
		intput: list of input data set [ train OR test input ]
		output: predicted labels (for me, type of label is np.array)
		'''
		pass


	@classmethod
	@abc.abstractmethod
	def evaluate(cls, label: np.array, options=None) -> tuple:
		''' 
		intput: (String) dataset_name
		output: tuple with (f1 score, MRR); set default value if ur code is not applicable
		'''











