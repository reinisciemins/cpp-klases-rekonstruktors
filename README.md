# Python -> WIN32 C/C++ klases rekonstruktors
* Programma ģenerē C/C++ klasi, pamatojoties uz lietotāja ievadi, kur lietotājam tiek piedāvāts sniegt informāciju par klasi: klases nosaukumu, klases elementu skaitu un informāciju par katru elementu (tips, nosaukums un nobīde, jeb adrese), kā rezultātā programma izveido C++ galvenes failu (.hpp), kas satur klases definīciju.

* Programma **pašlaik** paredzēta **Windows** operētājsistēmai **32-bitu** arhitektūras datu tipiem, tā atvieglo apgrieztās inžinierijas klases vai struktūru rekonstrukciju, ja zināmas ir elementu statiskās adreses .text atmiņas sektorā.

## Programmas izpildes piemērs:
* **.text. IDA 7.3. ģenerētais asamblervalodas** piemērs no spēlētāja klases spēlē **Counter-Strike: Source**:

    ![variable_example](https://i.ibb.co/zsr45yV/image-2024-01-19-131903402.png)
    
* Programmas ievades piemērs klases elementam **"m_iHealth"** (jāņem vērā, ka programma adresi pieņem **decimālajā skaitīšanas sistēmā 0x94 = 148**):

    ![input_example](https://i.ibb.co/3h6kp8Z/image-2024-01-19-132138738.png)
    
* Programmas izpildīšanas rezultāts, gatavs fails **player_class.hpp** un tās pielietojums:

    ![output_example](https://i.ibb.co/LvKyJjT/image-2024-01-19-132553836.png)
    ![usage_example](https://i.ibb.co/5k4Bq4b/Capture.png)
