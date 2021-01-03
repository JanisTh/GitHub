**Code Dokumentation Informatik Auftrag: Janis 1e**
 
Mein «Snake» Code ist folgendermassen aufgebaut:

Im obersten Teil des Codes sind allgemeine Personalisierungen der «Snake turtle», der «Appleturtle», der «Stone turtle», sowie des Frames.
Kurz darunter kommen die Essentiell wichtigen Eigenschaften, welche die Basis für die danach folgenden Funktionen, sowie bspw. Die Danger Zone Grösse oder die Points, welche anfangs auf null stehen.

Im Mittelteil kommt der definitiv wichtigste Teil: «Die Funktionen».
Hierbei werden die einzelnen Funktionen definiert, wobei der Begriff (def) gebraucht wird.
Die Funktionen sind das wichtigste in einem derartigen Code, weil sie aussagen was und wie ein Objekt etwas zu tun hat.
Unter diesen Funktionen befinden sich unter anderem play () und main (), welche die meisten anderen Funktionen in einer unterbringt und somit sicher geht, dass die der Reihe nach ausgeführt wird.
Um eine Funktion auszuführen wird ihr Name mit «()» ohne irgendetwas an den passenden Punkt gesetzt.

Zum Schluss kommt noch die «While-Schleife» mit der Steuerung, sowie einigen zusätzlichen Funktionen, welche immer wieder wiederholt werden sollen, solange die Snake (Turtle) lebt.
Um sicherzustellen, dass die Snake (Turtle) noch lebt, wurde auch noch eine wichtige Funktion definiert (snakeTurtleIsAlive ()), die durch anfordern der Koordinaten der verschiedenen Turtles bestimmt, ob die turtle noch lebt oder ob sie tot ist.



Spezielle Funktion genau erklärt:

```def statusbar ():
global high score
if points < high score:
           high score = points 
```
    
``` setStatusText ("Player name: "+name +" | Game: "+ str(points)+" points |     High score: "+ str (high score))```

In diesem Code wird die sogenannte Statusbar definiert. Auf den ersten Blick sieht sie relativ unscheinbar oder unwichtig aus, jedoch wertet sie in einem solchen Game das Aussehen bzw. das Spielerlebnis stark auf. Speziell für diese Funktion gibt es den Code «str(points)», welcher dafür verantwortlich ist, dass die Punkte welche beim Einsammeln der «Apples» gezählt werden, für Phyton sozusagen in Buchstaben umgeformt werden und somit ebenfalls für die Statusbar verwendet werden können.                                                                    Dies ist wichtig, da man in der Statusbar normalerweise nur Buchstaben einfügen kann.
