# 8.1 定义函数示例
# def greet_user():
#     """显示简单的问候语"""
#     print("Hello!")
#
# greet_user()

# 8.1.1 向函数传递信息
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")

greet_user('dora')
