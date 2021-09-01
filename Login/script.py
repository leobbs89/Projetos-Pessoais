class User():
    """Mantain user information"""

    def __init__(self, name, id, password):
        self.name = name
        self.id = id
        self.password = password

    def check_password(self,password):
        if self.password == password :
            return True
        else:
            return False

#Insert user in DataFrame
def insert_user(user,df):
    df = df.append({"NAME":user.name,"ID":user.id,"PASSWORD":user.password},ignore_index=True,sort=True)
    df = df.sort_values("NAME")
    return df

#Checks if ID is in DataFrame
def check_id(id,df):
    if id in df["ID"].tolist() :
        return True
    else:
        return False

#Return user from DataFrame
def return_user(id,df):
    user_rown = df.loc[df.index[df["ID"] == "camposka88"]]
    user = User(user_rown["NAME"],user_rown["ID"],user_rown["PASSWORD"])
    return user

#Create DataFrame
import pandas as pd
df = pd.DataFrame(columns = ["NAME","ID","PASSWORD"])
user1 = User("Leandro","leobbs89","ima450")
user2 = User("Carolina","camposka88","carol1812")
df = insert_user(user1,df)
df = insert_user(user2,df)
print(df)
