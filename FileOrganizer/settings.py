import json
from typing import Any
from pathlib import Path, PurePath


class CONFIG:
    __instance : "CONFIG"  = None

    __system_path : "Path" = PurePath.joinpath(Path.cwd(), "FileOrganizer")
    __config_fpath : "Path" = PurePath.joinpath(__system_path, "settings.json")

    __default_format : dict[str, Any] = {
        "package_indicator" : '`',
        "sub_package_indicator": '->',
        "cut" : True,
        "listening_dir" : [],
    }

    def __new__(cls : "CONFIG") -> "CONFIG": 
        if cls.__instance is None:
            CONFIG.__create_env()
            cls.__instance = super().__new__(cls)
            with open(CONFIG.__config_fpath, 'r') as f:
                cls.__instance.settings : dict = json.load(f)

        return cls.__instance

    def __create_env() -> None:
        __env_exist : bool = True

        try:
            with open(CONFIG.__config_fpath, 'r') as f: f.close()
        except FileNotFoundError as e:
            __env_exist = False

        if not __env_exist:
            Path(CONFIG.__system_path).mkdir(exist_ok=True)
            with open(CONFIG.__config_fpath, 'w') as f:
                json.dump(CONFIG.__default_format, f)

    def add_dir(self : "CONFIG", dpath : Path) -> None:
        """ Add a new dir to listen """
        if dpath not in self.settings["listening_dir"]:
            self.settings["listening_dir"].append(dpath)

    def remove_dir(self : "CONFIG", dpath : Path) -> None:
        """ remove a new dir to listen """
        self.settings["listening_dir"].remove(dpath)

    def get_registered_dir(self : "CONFIG") -> list[Path]:
        return self.settings["listening_dir"]

    def set_cut_mode(self : "CONFIG", value : bool) -> None:
        self.settings["cut"] = value

    def cut_mode(self : "CONFIG") -> bool:
        return self.settings["cut"]

    def set_indicators(self : "CONFIG", package_indicator : str, sub_package_indicator : str) -> None:
        self.settings["package_indicator"] = package_indicator
        self.settings["sub_package_indicator"] = sub_package_indicator

    def get_indicators(self : "CONFIG") -> dict[str, str]:
        return {
            "package": self.settings["package_indicator"],
            "sub_package": self.settings["sub_package_indicator"]
        }

    def GET(self : "CONFIG", key : str) -> Any:
        """ Get the value for a key from the configuration. """
        return self.settings.get(key, None)

    def GETKEYS(self : "CONFIG") -> list:
        return self.settings.keys()

    def SAVE(self : "CONFIG"):
        """ Write the configuration to a file. """
        with open(CONFIG.__config_fpath, 'w') as f:
            json.dump(self.settings, f)


config : CONFIG = CONFIG()