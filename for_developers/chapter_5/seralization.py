import pickle

try:
    setup = pickle.load(open("setup.pkl","r"))
    print(setup)
except:
    setup = {"timeout":10,"server":"10.0.0.1","port":80}
    pickle.dump(setup,open("setup.pkl","wb"))