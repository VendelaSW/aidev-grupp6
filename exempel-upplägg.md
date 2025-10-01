Detta är ett exempel upplägg för hur vi kan göra projektet så alla får visa sina kunskaper utan att vi krockar med varandra.

Så vi har flera filer som jobbar ihop istället för att ha hela programmet i en fil.



 	**main.py** # Detta är huvud filen som kommer köra spelet.



 	**player.py** # Detta är en fil som innehåller en player class med information om namn, poäng, progress osv



 	**questions.py** # Detta är en fil som hanterar frågorna i form av en class osv



&nbsp;		**individuella-frågor.py** # Vi kan också ha egna filer där vi lägger in våra frågor i en class 



 	**quiz.py** # Detta är en fil som har själva quiz Classen med game loop logic i sig



 	**scoreboard.py** # Detta är en fil som har en class som hanterar scoreboard med resultat, highscore osv



Låter kanske lite repetativt med en massa filer där alla har en class men som jag förstod det så ska alla göra 1 egen fil och 1 egen class så detta är mitt förslag // Vendela

Tänker också att vi förvarar frågorna i en json fil som questions.py kan plocka från.

