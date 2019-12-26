from models import Base
from pprint import pprint

def main():
    pprint(Base._decl_class_registry.__dict__)
    Base.metadata.create_all()

if __name__ == '__main__':
    main()
