import numpy as np
import matplotlib.pyplot as plt
import typing
import os


class EncabulatorData:

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
						 "Type": self.extension, "Header": ("Fichier non lu",), "Colonnes": ("Fichier non lu",),
						 "Apparatus": "Fichier non lu"}
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
		self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
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
		self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
		for line in lines[self.header_lines + 1:]:
			data.append(list(map(float, line.split(" "))))
		self.data = np.array(data)
		return self.data

	@property
	def time(self):
		return self.data[:, 0]

	@property
	def encabulator_data(self):
		return self.data[:, 1]

	def __str__(self):
		msg = f"EncabulatorReader de `{self.filename}`"
		return msg


class EncabulatorDataset:

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
			er = EncabulatorData(os.path.join(self.dir, file), self.name_metadata_sep, self.header_lines)
			er.read_file()
			apparatus = er.metadata["Apparatus"]
			ers = encabulator_readers.setdefault(apparatus, set())
			ers.add(er)
		self.encabulator_readers = encabulator_readers
		return self.encabulator_readers

	def __str__(self):
		if self.encabulator_readers is None:
			return f"Ce MultipleEncabulatorReader est vide ({repr(self)}))"
		return str(self.encabulator_readers)


class EncabulatorPlotter:

	def __init__(self, encabulator_reader: typing.Union[EncabulatorData, EncabulatorDataset], exceptions: tuple = ()):
		if isinstance(encabulator_reader, EncabulatorData):
			encabulator_reader.read_file()
			data = {encabulator_reader.metadata["Apparatus"]: encabulator_reader}
		elif isinstance(encabulator_reader, EncabulatorDataset):
			encabulator_reader.read_all(exceptions)
			data = encabulator_reader.encabulator_readers
		else:
			raise TypeError(f"Type `{type(encabulator_reader)}` n'est pas supporté.")
		self.data = data

	def plot(self, savename: str = None, show: bool = True):
		# TODO save
		fig, axes = plt.subplots(len(self.data))
		axes = np.ravel(axes)
		count = 0
		for apparatus, readers in self.data.items():
			for reader in readers:
				axes[count].plot(reader.time, reader.encabulator_data, label=reader.date)
			axes[count].legend()
			axes[count].set_xlabel("Temps [ns]")
			axes[count].set_ylabel("Encabulator []")
			axes[count].set_title(apparatus)
			count += 1
		if show:
			plt.show()
		if savename is not None:
			plt.savefig(savename)

	def plot_avg(self, ax: plt.Axes = None):
		# TODO save
		pass


class EncabulatorStats:

	def __init__(self, encabulator_reader: typing.Union[EncabulatorData, EncabulatorDataset]):
		pass


if __name__ == '__main__':
	path = r"C:\Users\goubi\Documents\GitHub\progFest_OOPUnitTests\data"
	dir = "../data"
	ers = EncabulatorDataset(dir)
	ers.read_all()
	ep = EncabulatorPlotter(ers)
	ep.plot()
