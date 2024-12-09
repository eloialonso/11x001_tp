import os


GREEN = '\033[92m'
BLUE = '\033[94m'
ENDC = '\033[0m'


# Decorator to print a header before an exercice. 
# Makes the assumption that function name is exerciceX
def exercice(func):
    def wrapper():
        n = func.__name__.split("exercice")[-1]
        s = f"##### EXERCICE {n} #####"
        h = "#" * len(s)
        header = h + "\n" + s + "\n" + h + "\n"
        os.system("clear")
        print(header)        
        func()
        print("\n\n")
        input("--> Appuyer sur 'Entrée' pour passer à l'exercice suivant")
    return wrapper

