import numpy as np
import matplotlib.pyplot as plt

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
            self.metadata = {"Name": self.name, "Date": self.date, "Folder": tuple(self.parent_directories),
                            "Type": self.extension, "Header": ("File not read",), "Columns": ("File not read",),
                            "Apparatus": "File not read"}
            self.data = None

    def read_file(self):
            if self.extension.lower() == 'txt':
                return self._read_txt()
            if self.extension.lower() == 'csv':
                return self._read_csv()


    def _read_txt(self):
            data = []
            with open(self.filepath, "r") as file:
                lines = file.readlines()
            header = list(map(lambda x: x.strip(), lines[:2]))
            colonnes = lines[2].strip().split(" ")
            self.metadata["Columns"] = tuple(colonnes)
            self.metadata["Header"] = tuple(header)
            self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
            for line in lines[3:]:
                if 'dust' not in line:
                    data.append(list(map(float, line.split(" "))))
            self.data = np.array(data)
            return self.data


    def _read_csv(self):
            data = []
            with open(self.filepath, "r") as file:
                lines = file.readlines()
            header = list(map(lambda x: x.strip(), lines[:2]))
            colonnes = lines[2].strip().split(",")
            self.metadata["Columns"] = tuple(colonnes)
            self.metadata["Header"] = tuple(header)
            self.metadata["Apparatus"] = header[-1].split(" = ")[-1]
            for line in lines[3:]:
                data.append(list(map(float, line.split(","))))
            self.data = np.array(data)
            return self.data

    @property
	def time(self):
		return self.data[:, 0]

	@property
        def encabulation(self):
            return self.data[:, 1]

        def __str__(self):
            msg = f"EncabulatorData from file `{self.filename}`"
            return msg
