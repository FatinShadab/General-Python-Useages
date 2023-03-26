import os
import re
import shutil
from settings import config
from pathlib import Path, PurePath, PosixPath

class PROTOCOL:
    __instance : "PROTOCOL"  = None

    def __new__(cls : "PROTOCOL") -> "PROTOCOL":
        if PROTOCOL.__instance == None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def is_organized(self : "PROTOCOL", root : PosixPath, fname : str) -> bool:
        return str(root).split('/')[-1] == fname.split('.')[-1].upper()
    
    def handleFile(self: "PROTOCOL", dstPath: Path, currentPath: Path, fname: str, package: "re.Match" = None) -> None:
        if package:
            sub_package_separator = config.get_indicators()["sub_package"]
            sub_packages = package.group(1).split(sub_package_separator)
            sub_dir = dstPath.parent

            for sub_package in sub_packages:
                sub_dir = sub_dir / sub_package
                sub_dir.mkdir(exist_ok=True)

            new_fname = sub_dir / fname.replace(package.group(0), "")
        else:
            new_fname = dstPath / fname

        shutil.copy2(PurePath.joinpath(currentPath, fname), new_fname)

        if config.cut_mode():
            os.remove(PurePath.joinpath(currentPath, fname))

    def organize(self : "PROTOCOL", dpath : Path) -> None:
        package_list : list[str] = []
        catagory_list : list[str] = []
        indicators : dict[str, str] = config.get_indicators()

        for root, dirs, files in os.walk(dpath):
            root = Path(root)
            for _file in files:
                if not self.is_organized(root, _file):
                    has_package : bool = False
                    if root == dpath:
                        package = re.search(f"{indicators['package']}(.*?){indicators['package']}", _file)
                        if package:
                            if package.group(1) not in package_list:
                                package_list.append(package.group(1))
                            has_package = True

                        if _file.split('.')[-1].upper() not in catagory_list and not has_package:
                            catagory_list.append(_file.split('.')[-1].upper())
                            PurePath.joinpath(root, catagory_list[-1]).mkdir(exist_ok=True)

                        dstPath = PurePath.joinpath(root, _file.split('.')[-1].upper() if not has_package else package.group(1))
                        self.handleFile(dstPath, root, _file, package)


system = PROTOCOL()

if __name__ == "__main__":
    test_path = "/home/eaegon/Documents/GITHUB/General-Python-Useages/FileOrganizer/TEST"
    system.organize(PurePath(test_path))