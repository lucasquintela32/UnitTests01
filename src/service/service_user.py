from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def search_user(self, name):
        for user in self.store.bd:  
            if name == user.name:
                return user
        return None

    def add_user(self, name, job):
        if name is not None and job is not None:  
            if isinstance(name, str) and isinstance(job, str):  
                if self.search_user(name) is None:
                    user = User(name, job)
                    self.store.bd.append(user)
                    return "success: User has been added"
                else:
                    return "error:This user exists in the list"
            else:
                return "error: Invalid, should be String"
        else:
            return "error: Invalid, cannot be None"

    def remove_user(self, name):
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    self.store.bd.remove(user)
                    return "success: User has been removed"
                else:
                    return "error: This user does not exist in the list"
            else:
                return "error: Invalid, should be String"
        else:
            return "error: Invalid, cannot be None"

    def get_user_by_name(self, name): 
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    solution = "success:"+"\n"+"Nome: "+user.name+"\n"+"Work: "+user.job
                    return solution
                else:
                    return "error: This user does not exist in the list"
            else:
                return "error: Invalid, should be String"
        else:
            return "error: Invalid, cannot be None"

def update_user(self, name, new_job): 
        if name is not None:
            if isinstance(name, str):
                user = self.search_user(name)
                if user is not None:
                    user.job = new_job
                    return "success: User has been updated"
                else:
                    return "error: This user does not exist in the list"
            else:
                return "error: Invalid, should be String"
        else:
            return "error: Invalid, cannot be None"