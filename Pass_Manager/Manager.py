import getpass

from pydb import DB


class MANAGER:
    def __init__(self):
        self.db = DB()
        self.MPWD_Error = f"Invalid/Wrong Master Password !!!"

    def entry_new_data(self, app, pwd):
        self.db.entry({app:pwd})
        return 0

    def update_entry_data(self, master_pwd, app, new_pwd):
        if self.db.is_master_pwd(master_pwd):
            self.db.update_data(app, new_pwd)
            return 0
        else:
            return self.MPWD_Error

    def del_entry_data(self, master_pwd, app):
        if self.db.is_master_pwd(master_pwd):
            self.db.del_data(app)
            return 0 
        else:
            return self.MPWD_Error

    def read_entry_data(self, master_pwd):
        if self.db.is_master_pwd(master_pwd):
            return self.db.get_data()
        else:
            return self.MPWD_Error

    def get_entry_of(self, master_pwd, app):
        if self.db.is_master_pwd(master_pwd):
            return self.db.get_data(key=app)
        else:
            return self.MPWD_Error
