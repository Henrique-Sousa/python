py_file = open("py.txt", "r")
java_file = open("java.txt", "r")
php_file = open("php.txt", "r")

py_file_str = py_file.read().split("\n")
java_file_str = java_file.read().split("\n")
php_file_str = php_file.read().split("\n")

java_not_php = {x for x in java_file_str if x not in php_file_str}
java_not_py = {x for x in java_file_str if x not in py_file_str}
py_not_java = {x for x in py_file_str if x not in java_file_str}
php_not_java = {x for x in php_file_str if x not in java_file_str}
py_not_php = {x for x in py_file_str if x not in php_file_str}
php_not_py = {x for x in php_file_str if x not in py_file_str}

print("java_not_php:")
print(java_not_php)
print("\n")
print("java_not_py:")
print(java_not_py)
print("\n")
print("py_not_java:")
print(py_not_java)
print("\n")
print("php_not_java:")
print(php_not_java)
print("\n")
print("py_not_php:")
print(py_not_php)
print("\n")
print("php_not_py:")
print(php_not_py)
print("\n")
