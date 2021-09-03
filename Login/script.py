import pandas as pd


class User:
    """Maintain user information"""

    def __init__(self, name: str, id: str, password: str):
        self.name = name
        self.id = id
        self.password = password

    def check_password(self, password: str) -> bool:
        if self.password == password:
            return True
        else:
            return False


# Insert user in DataFrame
def insert_user(user: User, df: pd.DataFrame) -> pd.DataFrame:
    df = df.append({"NAME": user.name, "ID": user.id, "PASSWORD": user.password}, ignore_index=True, sort=True)
    df = df.sort_values("NAME")
    return df


# Checks if ID is in DataFrame
def check_id(id: str, df: pd.DataFrame) -> bool:
    if id in df["ID"].tolist():
        return True
    else:
        return False


# Return user from DataFrame
def return_user(id: str, df: pd.DataFrame) -> User:
    user_rown = df.where(df['ID'] == id)
    user_rown = user_rown.dropna()
    user_rown = user_rown.values.tolist()
    user = User(user_rown[0][1], user_rown[0][0], user_rown[0][2])
    return user


# MAIN FUNCTION
def main() -> int:
    # Create DataFrame
    df = pd.DataFrame(columns=["NAME", "ID", "PASSWORD"])
    user1 = User("Leandro", "leobbs89", "ima450")
    user2 = User("Carolina", "camposka88", "carol1812")
    df = insert_user(user1, df)
    df = insert_user(user2, df)
    return 0


if __name__ == "__main__":
    main()
