from sys import exit,argv
from memory_manager import MemoryManager

def main(num):

    print("*"*30)
    print("""Bienvenido al simulador de tipos de datos :D Happy coding\n""")
    my_manager=MemoryManager(num)
    while True:
        my_input=input(">> ")
        my_input=my_input.upper()
        elems=my_input.split(" ")
        command=elems[0]
        if command=="SALIR":
            exit(0)
        elif command=="ATOMICO" and len(elems)==4:
            pass
        elif command=="STRUCT" and len(elems)>1:
            pass
        elif command=="UNION" and len(elems)>1:
            pass
        elif command=="DESCRIBIR" and len(elems)==2:
            pass
        else:
            print_help()

def print_help():
    """ Print help for user """

    response="""i. ATOMICO \<nombre> \<representacion> \<alineacion>

    Define un nuevo tipo atómico de nombre \<nombre>, cuya representación ocupa
    \<representación> bytes y debe estar alineado a \<alineación> bytes.

    ii. STRUCT \<nombre> \[\<tipo>]

    Define un nuevo registro de nombre \<nombre>. La definición de los campos del registro viene dada por la lista en \[\<tipo>].


    iii. UNION \<nombre> \[\<tipo>]

    Define un nuevo registro de nombre \<nombre>. La definición de los campos del registro viene dada por la lista en \[\<tipo>].


    iV. DESCRIBIR \<nombre>

    Debe dar la información correspondiente al tipo con nombre \<nombre>.

    v. SALIR

    Para salir del simulador.\n"""

    print(response)


if __name__ == "__main__":
    try:
        my_space=int(argv[1])
    except:
        my_space=input("¿Cuánta memoria desea?: ")
        my_space=int(my_space)
    
    main(my_space)