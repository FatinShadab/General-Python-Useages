import os
import json
import hashlib


class DB:
    def __init__(self):
        self.db_path = f"{os.getcwd()}\\DB.json"
        self.encode = "utf-8"
        self.master_key = 'master_pwd'

    def _hashed_data(self, data):
        if self.master_key in data.keys():
            return {key: hashlib.md5(data[key].encode(self.encode)).hexdigest() for key in data.keys()}
        else:
            return {key: data[key].encode(self.encode).hex() for key in data.keys()}

    def _all_data(self):
        try:
            with open(self.db_path, "r") as db:
                data = json.load(db)
                return data[0]
        except FileNotFoundError as e:
            return None

    def is_master_pwd(self, pwd):
        try:
            return hashlib.md5(pwd.encode(self.encode)).hexdigest() == self._all_data()[self.master_key]
        except (TypeError, KeyError) as e:
            return None

    def _save_updated_data(self, data):
        with open(self.db_path, 'w') as db:
            json.dump([data], db)
        
    def entry(self, pwd):
        try:
            with open(self.db_path, "r") as db:
                try:
                    data = json.load(db)
                    if data[0] == None:
                        data = []
                except:
                    data = []
                if len(data) > 0:
                    data[0].update(self._hashed_data(pwd))
                else:
                    data.append(self._hashed_data(pwd))
                with open(self.db_path, "w") as db:
                    json.dump(data, db)
        except FileNotFoundError as e:
            with open(self.db_path, 'x') as db:
                data = []
                data.append(self._hashed_data(pwd))
                json.dump(data, db)
        return 0

    def get_data(self, key=None):
        try:
            all_pwds = self._all_data()
            if key == self.master_key:
                return f"Master PWD can't be revealed !!!"
            if key is not None:
                if key in all_pwds.keys():
                    return f"{key}: {bytes.fromhex(all_pwds[key]).decode(self.encode)}"
                else:
                    return f"No password saved of {key}!"
            else:
                return {key : bytes.fromhex(all_pwds[key]).decode(self.encode) for key in all_pwds.keys() if key != self.master_key}
        except TypeError as e:
            return None

    def del_data(self, key):
        if key == self.master_key:
            return "*** Master PWD can't be deleted !"
        data = self._all_data()
        try:
            del data[key]
            self._save_updated_data(data)
            return 0
        except KeyError as e:
            return f"No password has saved of {key}!"

    def update_data(self, key, pwd):
        data = self._all_data()
        if key == self.master_key:
            data[key] = hashlib.md5(pwd.encode(self.encode)).hexdigest()
            self._save_updated_data(data)
            return 0
        else:
            try:
                data[key] = pwd.encode(self.encode).hex()
                self._save_updated_data(data)
                return 0
            except KeyError as e:
                self.entry({key:pwd})
                return 0

    def reset(self, master_pwd):
        if self.is_master_pwd(master_pwd):
            data = self._all_data()
            for key in list(data):
                if key != self.master_key:
                    del data[key]
            self._save_updated_data(data)
        return 0

    def format(self):
        data = None
        self._save_updated_data(data)
        return 0