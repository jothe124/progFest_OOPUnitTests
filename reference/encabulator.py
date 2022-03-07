import numpy as np
import matplotlib.pyplot as plt
import typing
import os


class EncabulatorData:

	def __init__(self, filepath: str):
		self.filepath = filepath
		if "\\" in self.filepath:
			dir_sep = "\\"
		else:
			dir_sep = "/"
		split = self.filepath.split(dir_sep)
		self.parent_directories = split[:-1]
		self.filename = split[-1]
		self.date, self.fullname = self.filename.split("_")
		self.name, self.extension = self.fullname.split(".")
		self.metadata = {"Nom": self.name, "Date": self.date, "Dossier": tuple(self.parent_directories),
						 "Type": self.extension, "Header": ("Fichier non lu",), "Colonnes": ("Fichier non lu",),
						 "Apparatus": "Fichier non lu"}
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
		header = list(map(lambda x: x.strip(), lines[:2]))
		colonnes = lines[2].strip().split(",")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
		for line in lines[3:]:
			data.append(list(map(float, line.split(","))))
		self.data = np.array(data)
		return self.data

	def _read_txt(self):
		data = []
		with open(self.filepath, "r") as file:
			lines = file.readlines()
		header = list(map(lambda x: x.strip(), lines[:2]))
		colonnes = lines[2].strip().split(" ")
		self.metadata["Colonnes"] = tuple(colonnes)
		self.metadata["Header"] = tuple(header)
		self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
		for line in lines[3:]:
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
		msg = f"EncabulatorData de `{self.filename}`"
		return msg


class EncabulatorDataset:

	def __init__(self, dir: str):
		self.dir = dir
		self.encabulator_readers = None

	def read_all(self, exceptions: tuple = ()):
		encabulator_readers = dict()
		all_files = os.listdir(self.dir)
		for file in all_files:
			if file in exceptions:
				continue
			er = EncabulatorData(os.path.join(self.dir, file))
			er.read_file()
			apparatus = er.metadata["Apparatus"]
			ers = encabulator_readers.setdefault(apparatus, set())
			ers.add(er)
		self.encabulator_readers = encabulator_readers
		return self.encabulator_readers

	def __str__(self):
		if self.encabulator_readers is None:
			return f"Ce EncabulatorDataset est vide ({repr(self)}))"
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

	def plot(self, save_name: str = None, show: bool = True):
		fig, axes = plt.subplots(1, len(self.data))
		axes = np.ravel(axes)
		count = 0
		for apparatus, readers in self.data.items():
			if isinstance(readers, EncabulatorData):
				readers = [readers]
			print(readers)
			for reader in readers:
				axes[count].scatter(reader.time, reader.encabulator_data, label=reader.date, alpha=0.2)
			axes[count].legend()
			axes[count].set_xlabel("Temps [ns]")
			axes[count].set_ylabel("Encabulator []")
			axes[count].set_title(apparatus)
			count += 1
		if show:
			plt.show()
		if save_name is not None:
			plt.savefig(save_name)

	def plot_avg(self, save_name: str = None, show: bool = True):
		# TODO save
		pass


class EncabulatorStats:

	def __init__(self, encabulator_readers: EncabulatorDataset, exceptions: tuple = ()):
		encabulator_readers.read_all(exceptions)
		self.data = encabulator_readers.encabulator_readers

	def average(self):
		averages = []
		for apparatus, readers in self.data.items():
			y_s = []
			for reader in readers:
				y_s.append(reader.encabulator_data)
			averages.append(np.mean(y_s, 0))
		return averages

	def median(self):
		medians = []
		for apparatus, readers in self.data.items():
			y_s = []
			for reader in readers:
				y_s.append(reader.encabulator_data)
			medians.append(np.median(y_s, 0))
		return medians

	def std_dev(self):
		std_devs = []
		for apparatus, readers in self.data.items():
			y_s = []
			for reader in readers:
				y_s.append(reader.encabulator_data)
			std_devs.append(np.std(y_s, 0))
		return std_devs


if __name__ == '__main__':
	dir = "../data"
	ers = EncabulatorDataset(dir)
	ers.read_all()
	ep = EncabulatorPlotter(ers)
	ep.plot()
	path = "../data/2022-02-30_experiment1.txt"
	er = EncabulatorData(path)
	ep =EncabulatorPlotter(er)
	ep.plot()
