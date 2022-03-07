import numpy as np
import os


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
		self.name, self.extension = self.fullname.split(".")
		self.metadata = {"Nom": self.name, "Date": self.date, "Dossier": tuple(self.parent_directories),
						 "Type": self.extension, "Header": ("Fichier non lu",), "Colonnes": ("Fichier non lu",)}
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
		colonnes = lines[self.header_lines].strip().split(",")
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
		colonnes = lines[self.header_lines].strip().split(" ")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(" "))))
		return np.array(data)


if __name__ == '__main__':
	path = r"C:\Users\goubi\Documents\GitHub\progFest_OOPUnitTests\data"
	for file in os.listdir(path):
		newName = file.replace(".txt", ".csv")
		if "31" not in file:
			continue
		with open(os.path.join(path, file), "r") as _file:
			lines = _file.readlines()
			writelines = [*lines[:2]]
			for line in lines[2:]:
				new_line = line.replace(" ", ",")
				writelines.append(new_line)
		with open(os.path.join(path, newName), "w") as _file:
			_file.writelines(writelines)

