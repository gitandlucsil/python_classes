import os
print(os.listdir("."))
print(os.listdir("complet_curs"))
os.mkdir("test_dir")
print(os.listdir("."))
print(os.getcwd())
#os.chdir("test_dir")
#print(os.getcwd())
os.rename("test_dir", "test_")
os.rmdir("test_")
print(os.listdir("."))