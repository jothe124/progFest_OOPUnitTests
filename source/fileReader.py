import numpy as np
import pandas as pd
import datetime


class FileReader:

	def __init__(self, filepath: str, name_metadata_sep: str = "_", header_lines: int = 2):
		self.filepath = filepath
		if "\\" in self.filepath:
			dir_sep = "\\"
		else:
			dir_sep = "/"
		split = self.filepath.split(dir_sep)
		self.parent_directories = split[:-1]
		self.filename = split[-1]
		self.date, self.fullname = self.filename.split(name_metadata_sep)
		self.date = datetime.date(*self.date.split("-"))
		self.name, self.extension = self.fullname.split(".")
		self.metadata = {"Nom": self.name, "Date": self.date, "Dossier": tuple(self.parent_directories)}
		self.header_lines = header_lines

	def read_file(self):
		if self.extension.lower() == "csv":
			return self._read_csv()
		elif self.extension.lower() == "txt":
			return self._read_txt()

	def _read_csv(self):
		data = pd.read_csv(self.filepath, header=self.header_lines)
		data = data.to_numpy()
		return data

	def _read_txt(self):
		data = []
		with open(self.filepath, "r") as file:
			lines = file.readlines()
		header = lines[:self.header_lines]
		for line in lines[self.header_lines:]:
			data.append(list(map(float, line.split(" "))))
		return np.array(data), header

if __name__ == '__main__':
	f = r"test\test.txt"
