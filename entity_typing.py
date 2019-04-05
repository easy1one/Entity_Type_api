'''
Group5. Entity Typing 
'''

import abc

class entity_typing(abc.ABC):

	@abc.abstractmethod
	def read_dataset(self, file_names, options=None):
		''' 
		input: List of Strings file_names OR file_paths to each file needed for the module
		output: a tuple of lists containing the dataset for train_data(tasks) and test_data(tasks) each as lists and other data as needed per project

		'''
		pass

	@abc.abstractmethod
	def train(self, train_data, options=None) :
		''' 
		input: train_data a list of all the data returned from the read_dataset method required for the module
		output: None or optionally model details if it's not returned then it will save the model into a file OR store within the system module
		'''
		pass

	@abc.abstractmethod
	def predict(self, test_data, optional model_details, options=None) :
		''' 
		input: list of input data set containing the test input
		output: predicted labels 
		'''
		pass


	@abc.abstractmethod
	def evaluate(self, test_files, options=None) :
		''' 
		input: list containing the data set containing the test input 
		output: list contatining all output data including (f1 score, and MRR if present); set default value if the code is not applicable
		'''

		pass
