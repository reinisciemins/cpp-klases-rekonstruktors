import os

# elementu klase, kas glaba c klases mainiga tipu, nosaukumu un adresi
class c_element:
    # klases konstruktors
    def __init__( self, type, name, offset ):
        self.type = type
        self.name = name
        self.offset = offset

# masivs kas klabas klases c_elementu objektus
class_elements = []

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
    file.write( "#pragma once\n#include <cstdint>\n\nclass " + class_name + " {\npublic:" )

    # cik mainigos nepieciesams pievienot
    member_count = int( input( "-> Ievadiet klases mainīgo skaitu: " ) )

    if member_count > 0:
        for i in range( member_count ):
            # mainiga informacijas ievade
            member_type = str( input( "\t-> Ievadiet mainīgā datu tipu: " ) )
            member_name = str( input( "\t-> Ievadiet mainīgā nosaukumu: " ) )
            member_offset = int( input( "\t-> Ievadiet mainīgā " + member_name + " adresi: " ) )

            # mainiga informacijas izvade lietotajam
            print( "\t-> " + member_type + " " + member_name + "\n\t----------------------------------------------" )
            
            # pievieno mainiga objektu masivam
            class_elements.append( c_element( member_type, member_name, member_offset ) )
    else:
        # ja nav nepieciesami mainigie tad iespejams vajadzigs klases izmers
        class_size = int( input( "-> Ievadiet klases izmēru baitos: "))

        if class_size > 0:
            file.write( "\n\tstd::uint8_t pad_0x0000[" + hex( class_size ) + "];\n};" )
        else:
            file.write( "\n\n};" )

    # aizver izveidoto failu
    file.close( )

    # nosleguma teksts
    print( "------------------------------------------------------" )
    print( file_name + " izveidota klase " + class_name + "!" )
    print( "------------------------------------------------------" )

if __name__ == "__main__":
    main( )
