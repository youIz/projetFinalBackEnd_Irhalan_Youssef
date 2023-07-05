
import django 
django.setup()
from MyApp.seed import run
if __name__=="__main__":
    run()

