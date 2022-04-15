
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db")

db_name = "sqlite:///" + db_path + "/init.db"
print(db_name)

def  balanced(s):

    if len(s) % 2 != 0:
        return False
    opening  = set('([{')
    matches = set([('(',')'), ('[',']'), ('{','}')])
    stack = []
    for i in s:
        if i in opening:
            stack.append(i)
        else:
            if len(stack) == 0:
                return False

            last_open = stack.pop()

            if (last_open,i) not in matches:
                return False

    return len(stack) == 0


if __name__ == "__main__":
    print(balanced('{}()'))