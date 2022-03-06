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
		self.date = datetime.date(*map(int, self.date.split("-")))
		self.name, self.extension = self.fullname.split(".")
		self.metadata = {"Nom": self.name, "Date": self.date, "Dossier": tuple(self.parent_directories),
						 "Type": self.extension, "Header": None, "Colonnes": None}
		self.header_lines = header_lines

	def read_file(self):
		if self.extension.lower() == "csv":
			return self._read_csv()
		elif self.extension.lower() == "txt":
			return self._read_txt()

	def _read_csv(self):
		data = []
		with open(self.filepath, "r") as file:
			lines = file.readlines()
		header = list(map(lambda x: x.strip(), lines[:self.header_lines]))
		colonnes = lines[self.header_lines + 1].strip().split(",")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(","))))
		return np.array(data)

	def _read_txt(self):
		data = []
		with open(self.filepath, "r") as file:
			lines = file.readlines()
		header = list(map(lambda x: x.strip(), lines[:self.header_lines]))
		colonnes = lines[self.header_lines + 1].strip().split(" ")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(" "))))
		return np.array(data),


if __name__ == '__main__':
	f = r"2022-03-06_test.csv"
	fr = FileReader(f)
	print(fr.metadata)
	print(fr.read_file())
	print(fr.metadata)
