from models import Base
from pprint import pprint

def main():
    pprint(Base._decl_class_registry.__dict__)

if __name__ == '__main__':
    main()
