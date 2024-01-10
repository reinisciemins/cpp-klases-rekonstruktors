import os

def main( ):
    # notira konsoli
    os.system( "cls" )

    print( "C/C++ klases rekonstruktors - Reinis Ciemiņš 231RDB191" )
    print( "------------------------------------------------------" )

    file_name = str( input( "Ievadiet faila nosaukumu: " ) )
    file_name += ".hpp"

    class_name = str( input( "Ievadiet klases nosaukumu: " ) )

    return

if __name__ == "__main__":
    main( )
