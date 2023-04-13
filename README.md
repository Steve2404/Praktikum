# Praktikum: Kategorisierung von WebSeite 
## Software zum durchsuchen des Internets und Kategorisieren der durchsuchten Webseiten  

Ziel ist es eine Software zu entwickeln die selbstständig anhand einer Ausgangsliste von Webseiten bzw. URL's beginnt das Internet zu durchsuchen und dabei den Inhalt der besuchten Webseiten, mithilfe einer Liste von vorgegebenen Kategorien, einzuordnen.  
Um den Inhalt der besuchten Webseiten einzuordnen soll außerdem sogenanntes "Maschinelles Lernen" zum Einsatz kommen. Die angestrebte Genauigkeit der Kategorisierung beträgt dabei zunächst 75%, soll jedoch im Verlauf der Weiterentwicklung auf >= 95% gesteigert werden.  
Dazu soll die Möglichkeit bestehen entsprechende Modelle zu Trainieren, z.B. durch supervised training oder reinforcement training.
Umsetzung.    
Als Programmiersprache zur Umsetzung soll dabei Python 3 zum Einsatz kommen. Python 3 hat sich im laufe der Entwicklung verschiedener arten des maschinellen Lernens als der defacto Standard etabliert und es existieren dementsprechend viele Frameworks für maschinelles Lernen.  
Die Entwicklung kann dabei in verschiedene Stufen aufgeteilt werden:  
    1. Web-Crawling  
    2. Inhaltsanalyse  
    3. Kategorisierung  
    4. Parallelisierung  
    
1 Web-Crawling  
Vorstufe der Inhaltsanalyse oder Kategorisierung durch eine KI ist zunächst das durchsuchen des Internets nach Internetadressen von Webseiten und ihren Unterseiten ausgehend von einer Liste von Webadressen.
Dabei sollen die aufgerufenen Webseiten nach weiterführenden Links zu Unterseiten der selben Domain und Internetadressen zu externen Domains durchsucht werden.  

2 Inhaltsanalyse  
Ist die Software in der Lage selbst durch das Internet zu navigieren, kann damit begonnen werden den Inhalt einer aufgerufenen Webseite zu analysieren. Mit welcher Methode der Inhalt analysiert wird ist dabei dem Entwickler überlassen.
Denkbar wäre zumindest aber, in einer ersten Vorstufe, die Verwendung typischer Schlagworte die zu einer der Hauptkategorien gehören.
In einer weiteren Stufe kann dann eine Gewichtung der Schlagworte erfolgen um eine Kategorisierung nur anhand der Mehrheit von Schlagworten einer Kategorie zu vermeiden und die Trefferquote zu seigern. 

3 Kategorisierung  
Kann die Software nun durch das Internet navigieren und den Inhalt der aufgerufenen Seiten oberflächlich analysieren, gilt es eine Schnittstelle zu schaffen um diese Analyse an einen "machine learning" Algorithmus auszulagern. 

4 Parallelisierung  
Nicht zwangsläufig in dieser Reihenfolge einzuhalten, ist es das Ziel die Schritte 1-3 anhand der auf einem Rechner oder Server zur Verfügung stehenden Ressourcen (Physische, Logische Kerne) entsprechend zu Parallelisieren. Ziel ist es dabei während der Laufzeit mehrere Webseiten und ihre Unterseiten zu Analysieren und Kategorisieren zu können.  

