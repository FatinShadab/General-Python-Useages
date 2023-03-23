import os
import re
from settings import config
from pathlib import Path, PurePath

class PROTOCOL:
    __instance : "PROTOCOL"  = None

    def __new__(cls : "PROTOCOL") -> "PROTOCOL":
        if PROTOCOL.__instance == None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance

    def copyFile(self : "PROTOCOL", dstPath : Path, currentPath : Path, fname : str) -> None:
        pass

    def moveFile(self : "PROTOCOL", dstPath : Path, currentPath : Path, fname : str) -> None:
        pass

    def organize(self : "PROTOCOL", dpath : Path) -> None:
        package_list : list[str] = []
        catagory_list : list[str] = []
        sub_dir_list : list[Path] = []
        indicators : dict[str, str] = config.get_indicators()
        
        for root, dirs, files in os.walk(dpath):
            root = Path(root)
            for _file in files:
                has_package : bool = False
                if root == dpath:
                    package = re.search(f"{indicators['package']}(.*?){indicators['package']}", _file)

                    if package:
                        if package.group(1) not in package_list:
                            package_list.append(package.group(1))
                            PurePath.joinpath(root, package.group(1)).mkdir(exist_ok=True)
                        has_package = True

                    if _file.split('.')[-1].upper() not in catagory_list and not has_package:
                        catagory_list.append(_file.split('.')[-1].upper())
                        PurePath.joinpath(root, catagory_list[-1]).mkdir(exist_ok=True)

                    dstPath = PurePath.joinpath(root, _file.split('.')[-1].upper() if not has_package else package.group(1))
                    self.copyFile(dstPath, root, _file) if not config.cut_mode() else self.moveFile(dstPath, root, _file)
                else:
                    sub_dir_list.append(root)

        print(catagory_list, package_list)

        for subDir in sub_dir_list:
            self.organize(subDir)

        for package in package_list:
            self.organize(package)
            

system = PROTOCOL()
system.organize(Path.cwd())