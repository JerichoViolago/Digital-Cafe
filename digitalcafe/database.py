import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

branches_db = myclient["branches"]
products_db = myclient["products"]
order_management_db = myclient["order_management"]


def get_branch(code):
    branches_coll = branches_db["branches"]
    branch = branches_coll.find_one({"code":code})
    return branch

def get_branches():
    branch_list = []
    branches_coll = branches_db["branches"]
    for b in branches_coll.find({}):
        branch_list.append(b)
    return branch_list
    for i,v in branches.items():
        branch = v
        branch.setdefault("code",i)
        branch_list.append(name)
    return branch_list



def get_product(code):
    products_coll = products_db["products"]

    product = products_coll.find_one({"code":code},{"_id":0})

    return product

def get_products():
    product_list = []

    products_coll = products_db["products"]

    for p in products_coll.find({},{"_id":0}):
        product_list.append(p)

    return product_list





def get_user(username):
    customers_coll = order_management_db['customers']
    user=customers_coll.find_one({"username":username})
    return user

def get_password(username):
    return get_user(username)["password"]


def create_order(order):
    orders_coll = order_management_db['orders']
    orders_coll.insert(order)

def get_pastorders():
    pastorder_list = []
    orders_coll = order_management_db["orders"]

def update_password(username,newpassword):
    customers_coll = order_management_db["customers"]
    updatepassword = customers_coll.update_one({"username":username}, {"$set":{"password":newpassword}})
    return updatepassword
