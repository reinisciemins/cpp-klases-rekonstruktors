import os

def main( ):
    # notira konsoli
    os.system( "cls" )

    # sakuma teksts
    print( "C/C++ klases rekonstruktors - Reinis Ciemiņš 231RDB191" )
    print( "------------------------------------------------------" )

    # faila nosaukuma iegusana
    file_name = str( input( "-> Ievadiet faila nosaukumu: " ) )
    file_name += ".hpp"

    # tiek izveidots fails
    file = open( file_name, "w+" )

    # pievieno klases definiciju
    class_name = str( input( "-> Ievadiet klases nosaukumu: " ) )
    file.write( "#pragma once\n\nclass " + class_name + " {\npublic:" )

    # cik mainigos nepieciesams pievienot
    member_count = int( input( "-> Ievadiet klases mainīgo skaitu: " ) )

    # aizver izveidoto failu
    file.close( )

    # nosleguma teksts
    print( "------------------------------------------------------" )
    print( file_name + " izveidota klase " + class_name + "!" )
    print( "------------------------------------------------------" )

if __name__ == "__main__":
    main( )
