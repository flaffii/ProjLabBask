# Projektēšanas laboratorija - Basketbols.......

**projektēsanas laboratorijas grupas darbs par basketbola spēles rezultāta prognozēšanu.**

Dalībnieki:

* Niks Bugnēvics
* Aleksis Boters
* Oskars Orinskis
* Mārcis Ābols
* Deniss Ņikitins

# līdzīgo risinājumu pārskats.

| Risinājums | Īss apraksts | Svarīgākās iezīmes | Ierobežojumi |
|---|---|---|---|
| **Elo vērtēšanas sistēma**  | Elo vērtēšanas sistēma balstās uz iepriekšējo spēļu rezultātiem, lai novērtētu komandu spēku. Katrai komandai ir piešķirts Elo reitings, kas tiek koriģēts pēc katras spēles – ja komanda uzvar, tā iegūst punktus, bet ja zaudē, tos zaudē. Spēcīgākas komandas uzvara pret vājāku komandu dod mazākus punktus, savukārt, ja vājāka komanda pārspēj spēcīgāku, tā iegūst vairāk punktu. | * Balstās uz uzvarām/zaudējumiem<br> * Reitingu pielāgojumi pēc katras spēles<br> * Vienkārša matemātiska pieeja  | * Neņem vērā traumas vai ārējos faktorus |
| **Poisson sadalījuma modelis**  | Matemātiska metode, kas izmanto vēsturiskos punktu gūšanas datus, lai prognozētu iespējamos punktu skaitus spēlē. Pamatojoties uz pagātnes rezultātiem, modelis aprēķina varbūtību, ka komanda spēlē gūs noteiktu skaitu punktu, izmantojot Poisson sadalījumu, kas ir noderīgs gadījuma mainīgo prognozēšanai. Modelis darbojas vislabāk situācijās, kur rezultāti ir relatīvi regulāri un paredzami.| * Balstās uz vēsturiskajiem punktiem<br> * Prognozē noteiktu punktu diapazonu spēlei | * Grūti modelēt nepastāvīgas komandas<br> * Nereālistiski precīzi pie mainīgiem faktoriem |
| **Montekarlo simulācijas**  | Statistiska metode, kas balstīta uz nejaušu scenāriju modelēšanu. Tūkstošiem reižu tiek simulētas spēles, katrā izmēģinot dažādus iznākumus, pamatojoties uz vēsturiskajiem datiem, piemēram, komandu sniegumu un punktu gūšanas tendencēm. No visiem simulētajiem iznākumiem tiek izveidota prognoze, aprēķinot katra scenārija varbūtību, ļaujot izteikt prognozes par spēles rezultātu. | * Simulē vairākus scenārijus<br> * Aprēķina izredzes uzvarēt | * Prasa lielu skaitļošanas jaudu<br> * Atkarīgs no ievades datu kvalitātes |
| **Mašīnmācīšanās algoritmi**  | Izmanto lielu vēsturisko datu apjomu, lai trenētu algoritmiskus modeļus prognozēšanai. Šie algoritmi analizē dažādus faktorus, piemēram, spēlētāju statistiku, komandu sniegumu, traumas un pat ārējos faktorus, kā spēles vietu un laiku. Laika gaitā modeļi kļūst gudrāki, jo tie mācās no jauniem datiem, uzlabojot prognožu precizitāti. | * Apstrādā lielus datu apjomus<br> * Prognozē dažādus mainīgos (spēlētāju statistiku, traumas, u.c.)<br> * Pašapmācības algoritms uzlabo prognozes laika gaitā | * Nepieciešams liels datu apjoms<br> * Sarežģīta modelēšana |
| **ESPN Basketball Power Index (BPI)**| ESPN izstrādāts, sarežģīts algoritms, kas analizē dažādus spēles aspektus, piemēram, tempa un efektivitātes rādītājus, aizsardzības un uzbrukuma statistiku. Tas ņem vērā faktorus kā mājas laukuma priekšrocības un komandas atpūtas ilgumu pirms spēles. Šīs metodes mērķis ir sniegt reāllaika prognozes par komandu varbūtību uzvarēt, pamatojoties uz statistiku un citām spēles dinamikām. | * Integrē komandu un spēlētāju statistiku<br> * Ietver faktorus, piemēram, mājas laukuma priekšrocības un atpūtas laiku | * Pieejams tikai ESPN sistēmās<br> * Ierobežots modeļa pielāgojums ārkārtas situācijām (piem. traumas)|

Koncepta modeļa diagramma
![image](https://github.com/user-attachments/assets/64a0e2ab-09fa-4ea9-afeb-9944040f817e)

Lietotājs, izmantojot klientu, nosūta pieprasījumu. Serveris apstrādā pieprasījumu. Servera daļā dzinējs apstrādā datus no datubāzes un apstrādātos datus nosūta algoritmam. Algoritms veic savu prognozi un nosūta rezultātu lietotājam.

(Lietotāju stāsti)
-Kā lietotājs es vēlos: 
redzēt labākās komandas.
redzēt spēļu rezultātu prognozi.
mainīt sākumlapas tēmu.
visas laika gaitā pieprasītās prognozes.
redzēt komandas, kuru prognozes esmu pieprasījis.
Sekot līdzi konkrētām komandām un saņemt paziņojumus, kad pieejama jauna prognoze.
Redzēt detalizētus iemeslus, kāpēc tika prognozēts konkrētais spēles iznākums.
Uzzināt par izmaiņām spēles prognozē.
apskatīt iepriekšējās prognozes precizitāti salīdzinājumā ar reālo spēles iznākumu.
