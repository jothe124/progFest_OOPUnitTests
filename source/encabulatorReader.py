import numpy as np
import os


class EncabulatorReader:

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
		self.name, self.extension = self.fullname.split(".")
		self.metadata = {"Nom": self.name, "Date": self.date, "Dossier": tuple(self.parent_directories),
						 "Type": self.extension, "Header": ("Fichier non lu",), "Colonnes": ("Fichier non lu",)}
		self.header_lines = header_lines
		self.data = None

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
		colonnes = lines[self.header_lines].strip().split(",")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(","))))
		self.data = np.array(data)
		return self.data

	def _read_txt(self):
		data = []
		with open(self.filepath, "r") as file:
			lines = file.readlines()
		header = list(map(lambda x: x.strip(), lines[:self.header_lines]))
		colonnes = lines[self.header_lines].strip().split(" ")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(" "))))
		self.data = np.array(data)
		return self.data

	def __str__(self):
		msg = f"EncabulatorReader de `{self.filename}`"
		return msg


class MultipleEncabulatorReader:

	def __init__(self, dir: str, name_metadata_sep: str = "_", header_lines: int = 2):
		self.dir = dir
		self.name_metadata_sep = name_metadata_sep
		self.header_lines = header_lines
		self.encabulator_readers = None

	def read_all(self, exceptions: tuple = ()):
		encabulator_readers = dict()
		all_files = os.listdir(self.dir)
		for file in all_files:
			if file in exceptions:
				continue
			er = EncabulatorReader(os.path.join(self.dir, file), self.name_metadata_sep, self.header_lines)
			er.read_file()
			ers = encabulator_readers.setdefault(er.date, set())
			ers.add(er)
		self.encabulator_readers = encabulator_readers
		return self.encabulator_readers

	def __str__(self):
		if self.encabulator_readers is None:
			return f"Ce MultipleEncabulatorReader est vide ({repr(self)}))"
		return str(self.encabulator_readers)


if __name__ == '__main__':
	path = r"C:\Users\goubi\Documents\GitHub\progFest_OOPUnitTests\data"
	dir = "../data"
	ers = MultipleEncabulatorReader(dir)
	ers.read_all()
	print(ers)
