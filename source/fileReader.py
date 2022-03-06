import pandas as pd


class FileReader:

	def __init__(self, filepath: str, name_metadata_sep: str = "_"):
		self._filepath = filepath
		if "\\" in self._filepath:
			dir_sep = "\\"
		else:
			dir_sep = "/"
		split = self._filepath.split(dir_sep)
		self._parent_directories = split[:-1]
		self._filename = split[-1]
		self._date, self._fullname = self._filename.split(name_metadata_sep)
		self._name, self._extension = self._fullname.split(".")

	def read_file(self):
		if self._extension.lower() == "csv":
			return CSVReader(self._filepath)
		elif self._extension.lower() == "txt":
			return TXTReader(self._filepath)


class CSVReader:

	def __init__(self, filepath:str):
		self._data = pd.read_csv(filepath)

class TXTReader:

	def __init__(self, filepath:str):
		self._data = None  # TODO

if __name__ == '__main__':
	f = r"test\test.txt"
