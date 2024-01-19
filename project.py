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

def get_type_size( type ):
    # iznem "std::" prefixu no dota stringa lai spetu apstradat abas opcijas, kad lietotajs
    # ievada so prefixu un kad ne
    if "std::" in type:
        type = type.replace( "std::", "" )

    # norade -> izmers 4 baiti
    if "*" in type:
        return 4

    # 32bitu c/c++ datu tipu izmeri baitos
    if type in { "int8_t", "uint8_t" }:
        return 1
    elif type in { "int16_t", "uint16_t" }:
        return 2
    elif type in { "int32_t", "uint32_t", "uintptr_t", "DWORD", "unsigned long", "long", "float" }:
        return 4
    elif type in { "int64_t", "uint64_t", "vec2d_t" }:
        return 8
    elif type == "vec3d_t":
        return 12
    
    # nezinams datu tips
    return -1

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
        # galvenais cikls klases elementu pievienosanai
        for i in range( member_count ):
            # mainiga informacijas ievade
            member_type = str( input( "\t-> Ievadiet mainīgā datu tipu: " ) )
            member_name = str( input( "\t-> Ievadiet mainīgā nosaukumu: " ) )
            member_offset = int( input( "\t-> Ievadiet mainīgā " + member_name + " adresi: " ) )

            # mainiga informacijas izvade lietotajam
            print( "\t-> " + member_type + " " + member_name )

            if i != member_count - 1:
                print( "\t----------------------------------------------" )
            
            # pievieno mainiga objektu masivam
            class_elements.append( c_element( member_type, member_name, member_offset ) )
        
        # sakarto klases elementus augosa seciba pec to adresem
        class_elements.sort( key=lambda x: x.offset )

        # saglaba ieprieks apskatito elementu objektu
        previous_element = c_element( "", "", 0 )
        pad_location_value = 0
        pad_size_value = 0

        # cikls kas iet cauri sakartotajiem klases elementiem secigi
        for i in range( len( class_elements ) ):
            element = class_elements[i]

            # pirma elementa pievienosana
            if i == 0:
                if element.offset > 0:
                    file.write( "\n\tstd::uint8_t pad_0x0000[" + hex( element.offset ) + "];" )

                file.write( "\n\t" + element.type + " " + element.name + ";" )
            else:
                # parbauda vai nav nepieciesams aizpildijums (padding)
                if get_type_size( element.type ) != element.offset - previous_element.offset:
                    # parveido tuksas vietas izmeru ta lai vienmer butu 4 skaitli
                    pad_location = hex( pad_location_value )
                    pad_location = pad_location.replace( "0x", "" )
                    pad_location = pad_location.zfill( 4 )
                    pad_location = pad_location.upper( )

                    pad_size_value = element.offset - pad_location_value

                    # tikai pirma izmers ir element.offset, nakamajiem janem starpiba
                    file.write( "\n\tstd::uint8_t pad_0x" + pad_location + "[" + hex( pad_size_value ) + "];" )
                    file.write( "\n\t" + element.type + " " + element.name + ";" )

                    # saglaba iepriekseja aizpildijuma lielumu nakamajai lokacijas adresei
                    pad_location_value += pad_size_value
                else:
                    file.write( "\n\t" + element.type + " " + element.name + ";" )

            # saglaba nakama elementa adresi kas ir ieprieksejo elementu tipu izmeri baitos
            pad_location_value += get_type_size( element.type )
            previous_element = element

        file.write( "\n};" )
    else:
        # ja nav nepieciesami mainigie tad iespejams vajadzigs klases izmers
        class_size = int( input( "-> Ievadiet klases izmēru baitos: " ) )

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
