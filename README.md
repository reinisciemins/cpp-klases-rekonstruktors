# Python -> WIN32 C/C++ klases rekonstruktors
* **Projekta uzdevums**: uzrakstīt programmu, kas ģenerē **C/C++ klasi**, pamatojoties uz lietotāja ievadi, kur lietotājam tiek piedāvāts sniegt **informāciju par klasi**: klases nosaukumu, klases elementu skaitu un informāciju par katru elementu (tips, nosaukums un nobīde, jeb adrese), kā rezultātā programma izveido C++ galvenes failu (.hpp), kas satur **klases definīciju**.

* Programma **pašlaik** paredzēta **Windows** operētājsistēmai **32-bitu** arhitektūras datu tipiem, tā atvieglo apgrieztās inžinierijas klases vai struktūru rekonstrukciju, ja zināmas ir elementu statiskās adreses .text atmiņas sektorā.

* Reāllaika programmas **izpildes** un **pielietojuma piemērs** spēlei Counter-Strike: Source **(YouTube video)**:

    [![video_example](https://i.ibb.co/FqCPTrF/thumbnail.png)](https://www.youtube.com/watch?v=ntRcPG-U2Eg)

## Programmas izpildes piemērs:
* **.text. IDA 7.3. ģenerētais asamblervalodas** piemērs no spēlētāja klases spēlē **Counter-Strike: Source**:

    ![variable_example](https://i.ibb.co/zsr45yV/image-2024-01-19-131903402.png)
    
* Programmas ievades piemērs klases elementam **"m_iHealth"** (jāņem vērā, ka programma adresi pieņem **decimālajā skaitīšanas sistēmā 0x94 = 148**):

    ![input_example](https://i.ibb.co/3h6kp8Z/image-2024-01-19-132138738.png)
    
* Programmas izpildīšanas rezultāts, gatavs fails **player_class.hpp** un tās pielietojums:

    ![output_example](https://i.ibb.co/LvKyJjT/image-2024-01-19-132553836.png)
    ![usage_example](https://i.ibb.co/5k4Bq4b/Capture.png)
    
## Izmantotās Python bibliotēkas:
* **OS bibliotēka** - izmantota, lai notīrītu konsoles ekrānu, lai nodrošināt tīru un sakārtotu lietotāja interfeisu. Notīrot konsoli, programma sākas ar tukšu termināli/konsoli, atvieglojot lietotāja mijiedarbību ar programmas datu ievadi un izvadi.

## Programmas satura apraksts:

1. **Importē bibliotēkas:** tiek importēts `os` modulis, lai veiktu mijiedarbību ar operētājsistēmu.
2. **Definē klasi (`c_element`):** tiek definēta klase ar nosaukumu `c_element`, lai saglabātu C++ klases elementus. Katram elementam ir atribūti, piemēram, datu tips (`type`), mainīgā nosaukums (`name`) un nobīde (`offset`).
3. **Izveido tukšu sarakstu:** tiek izveidots tukšs saraksts (`class_elements`), lai glabātu objektus, kas ar C++ klases elementiem.
4. **Definē funkciju (`get_type_size`):** funkcija izmantota, lai noteiktu C++ datu tipu izmēru baitos.
5. **Definē galveno funkciju (`main`):** mijiedarbojas ar lietotāju, lai dinamiski ģenerētu C++ klasi.
6. **Notīra konsoles ekrānu:** programma notīra konsoles ekrānu, lai panāktu tīrāku lietotāja saskarni.
7. **Iegūst ievadi faila nosaukumam, faila izveidei:** lietotājam tiek prasīts ievadīt faila nosaukumu, tam tiek pielikts ".hpp" faila veids, un tas tiek atvērts rakstīšanai.
8. **Pievieno klases definīciju failam:** prasa lietotājam klases nosaukumu un ieraksta klases definīciju failā, iekļaujot nepieciešamos galvenes failus.
9. **Pievieno mainīgos klasei:** prasa lietotājam ievadīt klases mainīgo skaitu, un programma iteratīvi iegūst informāciju par katru mainīgo (tips, nosaukums, nobīde).
10. **Sakārto un ģenerēt klases elementus failā:** sakārto klases elementus pēc nobīdēm un ģenerē atbilstošo klases definīciju failā, nodrošina precīzu izkārtošanu atmiņā, pievienojot aizpildījumus starp klases elementiem.
11. **Aizver failu un parāda paziņojumu:** fails tiek aizvērts, un tiek rādīts izpildes paziņojums ar izveidoto faila nosaukumu un klases nosaukumu.

## Papildus piezīmes:
* **Aizpildījuma**, jeb **"paddinga"** nosaukuma adrese ir heksadecimālajā skaitīšanas sistēmā, un tā norāda elementa adresi sākot no 0 formātā **0xXXXX** (aizpildījums ir klases nezināmie elementi, kas lietotājiem nav nepieciešami, tie ir jāiekļauj, lai saskaņotu klases vai struktūras datu elementus atmiņā).
* Programmu iespējams uzlabot pievienot atbalstu 64-bitu arhitektūrai un pievienojot opciju ievadīt pašizveidotus datu tipus, kā piemēram **3x4 matriksas** norādot to izmēru baitos, bet tas autora ietvaros pašlaik nav vajadzīgs.
* Programmas pielietojums ir ļoti specifisks noteiktai **nozarei**, jeb virzienam **datorzinātnēs** un, lai tas būtu noderīgs lietotājam ir jāzin pamati **apgrieztajā inžinierijā** par **datu struktūrām, norādēm, adresēm un referencēm** un to izskatu dekompilējot programmatūru.
