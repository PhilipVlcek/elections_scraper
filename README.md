# Elections scraper
The third project to the Engeto Python Academy.

## Project description
This project is used to extract results from the 2017 parliamentary elections.

## Installing libraries
The libraries that are used in this code are stored in the **requirements.txt** file. For installation, I recommend using a new virtual environment and running it as follows with the manager installed:

    $ pip3 -- version                       # version verification

    $ pip3 install -r requirements.txt      # install the libraries

## Starting the project
Running the **elections_scraper.py** file from the command line requires two arguments.

    python elections_scraper.py "<region link>" <file_name>

the results are then downloaded to a **file_name.csv** file.

## Demonstration of project
Voting results for Zlín district:

    1.argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204

    2.argument: zlin.csv

Starting the program:

    python elections_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7204" zlin.csv

Download progress:

    The scraping process has been started . . .

    The obtained data was downloaded to the file: "zlin.csv"

    The process is over
    
Partial output:

    Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
    588318,Bělov,257,174,174,25,0,0,8,0,14,20,1,0,2,0,0,14,0,6,51,0,0,9,4,0,0,20,0
    585076,Biskupice,564,314,314,17,1,0,16,0,15,34,2,6,15,0,0,16,0,1,102,0,1,38,2,0,2,42,4
    557102,Bohuslavice nad Vláří,315,201,201,19,1,0,24,1,8,13,2,3,1,1,0,16,0,2,65,1,0,22,0,0,3,18,1
    585092,Bohuslavice u Zlína,637,399,397,32,0,0,28,0,36,24,6,5,5,0,0,21,0,8,125,0,3,40,1,2,0,54,7
    585106,Bratřejov,640,422,419,20,12,0,34,0,29,35,7,5,3,0,0,35,0,4,97,1,0,76,1,0,1,55,4
    585114,Brumov-Bylnice,4 531,2 599,2 582,158,7,1,239,1,159,159,19,12,41,2,1,160,1,38,765,0,3,495,23,2,4,282,10
    538744,Březnice,1 032,687,681,82,0,2,36,0,49,33,4,4,23,0,0,45,1,22,212,0,0,70,0,0,1,91,6
    585131,Březová,375,262,261,18,1,0,14,0,16,24,3,4,1,0,0,23,0,4,71,0,0,44,0,1,0,33,4
    585149,Březůvky,567,359,356,23,3,0,18,0,16,19,3,3,4,0,0,36,2,8,102,0,0,41,0,2,0,74,2

