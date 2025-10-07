# Bioimmagini

Le bioimmagini forniscono informazioni che non possono essere ottenute dai soli biosegnali e possono essere sia analogiche che digitali. Su di esse possono essere svolte varie operazioni con lo scopo di aumentare la qualità delle informazioni estraibili. 

## Immagini

Ogni immagine digitale può essere vista come una funzione in cui il valore del pixel ($a(x,y)$) è una proiezione di uno spazio tridimensionale sulla matrice che compone l'immagine.

Data un'immagine: l'elaborazione permette di modificarne l'aspetto per migliorarla, l'analisi di estrapolare dell'informazione quantitativa e l'interpretazione fornisce dell'informazione qualitativa.

Le immagini sono ottenute grazie all'interazione di onde elettromagnetiche con un corpo: tipicamente vengono attenuate, assorbite o deviate dai tessuti di esso. In ambito medico vengono utilizzati diversi tipi di onde, a seconda dell'esame da effettuare. Ad esempio, per le ecografie si impiegano gli ultrasuoni, mentre in altri casi si ricorre a onde dello spettro elettromagnetico, a fasci di elettroni o a potenziali elettrici. La scelta viene presa in base alla precisione necessaria, al costo e ad eventuali controindicazioni.

A volte i fenomeni di interesse non sono direttamente visibili e bisogna trasformare il campione tramite colorazione di cellule o con mezzi di contrasto per renderne visibili le caratteristiche.

### Modalità di acquisizione

Un'immagine può essere acquisita tramite luce riflessa o luce trasmessa. 

Con il metodo della luce riflessa gli oggetti di interesse vengono colpiti da una fonte di luce di cui ne assorbono una quota e ne riflettono un altra. Questo è il tipico modo di lavorare delle fotocamere. 

Per quanto riguarda la modalità a luce trasmessa, la fonte luminosa si trova dietro l'oggetto che si vuole riprendere e il sensore riceve i segnali della fonte alterati dal passaggio attraverso l'oggetto stesso. Questo è il metodo più comune in medicina: viene utilizzato nelle radiografie.

### Campionamento

Le immagini acquisite sono un campionamento di punti: l'immagine è divisa in una griglia di elementi atomici, ovvero i pixel, che rappresentano il valore medio del colore nell'area scannerizzata. Il colore viene poi quantizzato per passare da una scala analogica a infiniti valori ad una scala digitale con valori discreti e limitati in grado di essere rappresentati in un calcolatore. Vi è quindi una doppia approssimazione: valore medio di colore in un pixel e quantizzazione di esso.

### Approssimazione

In base all'utilizzo dell'immagine bisogna scegliere un livello accettabile di approssimazione tenendo conto anche del rumore. Secondo il teorema di Shannon-Nyquist è necessario campionare al doppio del dettaglio minimo che si vuole vedere.

Per migliorare la precisione è possibile acquisire lo stesso campo visivo con un sensore più prestante o produrre un'immagine della stessa grandezza, ma con un campo visivo più piccolo avvicinandosi al soggetto con il sensore o con strumenti ottici.

### Quantizzazione

Le immagini possono essere di vari tipi: binarie, a toni di grigio o multispettrali.

Le immagini binarie sono dette maschere e dispongono di 2 livelli per rappresentare l'informazione, mentre le immagini a toni di grigio hanno a disposizione $2^{n}$ livelli e sono semplici da rappresentare. Le immagini multispettrali sono composte da pixel che contengono informazioni provenienti da più lunghezze d'onda, questi possono essere visti come degli array la cui lunghezza dipende da quanti canali sono stati registrati: le immagini a colori hanno 3 livelli, ma esistono situazioni in cui vengono registrati anche 10 livelli.

### Modelli del colore

L'occhio umano è formato da una struttura a coni e bastoncelli. I coni sono sensibili al colore, specialmente al verde.

Ogni immagine a colori usa un modello specifico per rappresentare il colore, ci sono 2 principali modelli, ma non sono gli unici. Quello additivo (RGB) rappresenta i colori primari aggiungendoli ad un ipotetico sfondo nero, mentre quello sottrattivo (CMGK) sottrae i colori da uno sfondo bianco. Questi modelli sono facilmente intercambiabili e permettono di cogliere dettagli diversi.

Ogni immagine a colori può essere scomposta in varie immagini a toni di grigio in base al canale selezionato. Queste immagini sono facilmente lavorabili e permettono di riconoscere determinati aspetti difficili da distinguere nella controparte a colori.

## Sensori

I sensori permettono di trasformare il segnale continuo naturale in una bitmap digitale. Possono misurare l'ampiezza d'onda e il tempo di ritorno del segnale. Le tecnologie principali per l'acquisizione delle immagini sono CCD/CMOS e fotomoltiplicatori.

### CCD e CMOS 

CCD e CMOS sono tipi di sensore costituiti da una griglia di elementi sensibili alla quantità di luce, questa viene vista come un insieme di particelle, fotoni, che vengono contate dal sensore per capire l'intensità del segnale. Dal punto di vista commerciale le dimensioni della griglia sono espresse in pollici e il numero dei sensori è il megapixel.

Ogni elemento della griglia è sensibile alla luce, non al colore che viene selezionato tramite micro lenti e filtri cromatici. Questi servono sia ad ottenere immagini a colori, sia a filtrare le frequenze indesiderate come infrarossi o ultravioletti.

La differenza tra CCD e CMOS risiede nel modo in cui i dati vengono trasferiti dalla griglia dei sensori al processore. Le fotocamere CCD utilizzano una metodologia di trasferimento seriale in cui le informazioni di ciascun sensore vengono inviate una dopo l'altra al processore. Al contrario, le fotocamere CMOS sono dotate di elementi sensibili con digitalizzatori integrati che permettono una lettura simultanea dei dati. Questo approccio consente di trattare l'immagine come una sorta di memoria RAM con la possibilità di leggere solo una parte dell'immagine, tuttavia, può verificarsi una leggera variabilità nei colori tra i diversi sensori a causa delle differenze nelle loro caratteristiche di risposta.

### CCD e rumore

Vi sono vari tipi di rumore presenti. Il rumore termico è generato dall'agitazione termica delle particelle, il rumore fotonico dipende dal numero dei fotoni che arrivano al sensore, il readout noise è il rumore introdotto durante il processo di lettura dei segnali da parte di un sensore e dipende dalla variabilità nella conversione dei dati, infine il rumore di quantizzazione è quello generato digitalizzando un segnale analogico.

Più grande è l'elemento sensibile, più basso è il rumore in quanto il sensore è in grado di catturare più fotoni e di discriminare più livelli di luce. Tuttavia le dimensioni maggiori garantiscono una risoluzione inferiore rispetto a elementi più piccoli.

### CCD e acquisizione del colore

Idealmente il segnale di output del sensore dovrebbe essere linearmente proporzionale all'input che riceve, ma non sempre è così. La funzione di gamma esprime la non linearità dei sensori e, se nota, può essere usata per rendere lineare l'immagine acquisita.

I due principali metodi per acquisire colore con le fotocamere CCD sono 3CCD e MONOCCD. 

La tecnica 3CCD prevede la presenza di 3 sensori indipendenti che ricevono la stessa luce filtrata da un prisma. Ogni sensore dispone di un filtro per un dato colore e le immagini così prodotte sono di buona qualità, tuttavia la tecnica è poco sensibile alle basse luminosità poiché la luce viene divisa dal prisma. 

La tecnica MONOCCD si basa sul mosaico di Bayer: davanti ad ogni sensore vi è un filtro colorato rosso, verde e blu. In un quadrato 4x4 vi sono due sensori per il verde, uno per il rosso e uno per il blu. Ogni pixel ha un filtro per un colore apposito e usa l'interpolazione con i valori pixel vicini per sopperire alla mancanza di informazione riguardante i colori mancanti. La resa dei colori è inferiore rispetto a 3CCD, ma le fotocamere sono più economiche da produrre.

## Sensori ad uso scientifico

Per garantire risultati attendibili, un sensore utilizzato in ambito scientifico deve avere tutte le specifiche tecniche ben definite. Inoltre, è fondamentale che il sensore sia tarato per determinare la sua risoluzione reale. Per fare ciò, vengono ripresi oggetti di caratteristiche note con il fine di controllare nell'immagine digitale il dettaglio acquisito.

In ambito scientifico vengono spesso usati sensori CCD, ma ultimamente anche i sensori CMOS hanno trovato spazio. 

Le immagini statiche possono essere raccolte tramite un sensore CCD posto dietro ad una ruota di filtri.

Per quanto riguarda i video, deve essere nota anche la velocità di trasferimento dei dati della fotocamera. Per ottenere un certo framerate potrebbe essere necessario manipolare la risoluzione: una risoluzione maggiore richiede un volume di dati più elevato da elaborare e trasferire, il che può influenzare la fluidità del video se la larghezza di banda non è sufficiente.

### Efficienza quantica

Non sempre tutti i fotoni vengono tradotti in segnale: l'efficienza quantica misura la percentuale di fotoni tradotti in segnale. Questa misura dipende dalla lunghezza d'onda: non ci sono sensori che rispondono linearmente a tutte le frequenze sensibili e questa misura varia dal 20% al 80%. Quando è alta è possibile percepire segnali molto deboli.

### Full well capacity

Ogni elemento ha una capacità massima di fotoni che è in grado di acquisire. La full well capacity serve a capire quanti livelli il sensore riesce a discriminare a livello teorico, tuttavia i livelli reali sono di meno a causa del rumore.

Il dynamic range è la relazione fra full well capacity e readout noise. Descrive i livelli effettivi ed è indipendente dalla rappresentazione in pixel: $\text{dynamic range} = \frac{\text{FWC}}{\text{readout noise}}$.

### Fotomoltiplicatori e scintillatori

I fotomoltiplicatori sono particolari sensori che registrano un segnale alla volta registrando un solo fotone. In pratica fotografano un solo pixel alla volta. Il loro elemento sensibile riceve la luce e causa una cascata di elettroni che viene moltiplicata fino a renderlo percepibile.

Sono molto sensibili al rumore, in particolare a quello termico, e devono essere usati in ambienti controllati. 

Un caso d'uso prevede il loro utilizzo in microscopi confocali in cui il campione viene illuminato un punto alla volta. Questo processo è lento, ma molto preciso. I fotomoltiplicatori sono usati in medicina di laboratorio o in citofluoremtria.

I scintillatori sono dispositivi che emettono luce quando colpiti da particelle. Sono composti da materiali in grado di convertire l'energia delle particelle in segnali luminosi facilmente rilevabili.

## Qualità dell'immagine

La qualità complessiva di un'immagine dipende sia dal sensore che da fonti di errori come i vari tipi di rumore, difetti ottici o di illuminazione che si combinano assieme. 

Bisogna essere in grado di distinguere variabilità biologica da errore di misurazione. Una tecnica per ridurre la possibilità di errore prevede la ripetizione delle misurazioni, ma non sempre è possibile.

Nelle immagini il rumore si vede sotto forma di puntini e sono state sviluppate delle tecniche di noise reduction che modificano l'immagine per eliminarlo.

Nei microscopi altri artefatti possono essere generati dalla luce che colpisce il centro del campione in maniera più forte rispetto ai bordi, o dall'ottica che è più precisa al centro. Una tecnica per ridurre questi artefatti prevedere di acquisire una foto del solo sfondo, così poi da poter sottrarre eventuali artefatti dalle immagini con i campioni.

## Fonti di bioimmagini

### Ultrasuoni

Gli ultrasuoni sono uno dei sistemi più utilizzati per acquisire bioimmagini. Il principio è simile a quello del radar e del sonar: viene generato un segnale e si registra il suo eco. Differenti tipologie di lunghezze d'onda vengono riflesse in modi diversi dai vari organi, questo permette di misurare la distanza tra la sonda e l'organo, la densità dei tessuti attraversati, ecc.

Vengono usate onde tra i 2 e i 10 MHz ed è considerato un metodo sicuro e portatile.

### Radiografia

La radiografia sfrutta le proprietà di attenuazione dei raggi X attraverso vari materiali. Viene emesso un raggio con una frequenza tra il $10^{15}$ e $10^{20}$ Hz che passa attraverso il paziente per raggiungere un sensore posto dietro di esso. Questo è solitamente uno schermo fluoroscopico che espone una pellicola o consente l'acquisizione digitale.

La mammografia è una tipologia di raggi x applicati alla mammella che viene tenuta ferma da una pinza. Lo scopo è quello di rilevare tumori e micro-calcificazioni. La risoluzione delle immagini è molto alta e la grandezza dei file prodotti è sull'ordine dei 160MB.


### Tomografia computerizzata

La tomografia computerizzata (TC) è una tecnica che utilizza una serie di raggi X lineari posizionati attorno all'organo d'interesse, con l'obiettivo di generare una ricostruzione accurata dei contributi all'attenuazione del raggio da parte delle unità di volume che compongono i vari organi.

Questi raggi attraversano i tessuti e vengono attenuati in base alla densità del materiale che attraversano (ossa, muscoli, organi, ecc.).

I dati raccolti da un rilevatore vengono poi elaborati da un computer, che ricostruisce immagini tridimensionali (o sezioni bidimensionali) dell'interno del corpo. Ogni piccolo volume (detto voxel) viene analizzato per determinare quanto ha attenuato i raggi, permettendo di mappare con precisione la struttura interna degli organi.

Come risultato, otteniamo immagini delle diverse sezioni del corpo acquisite a breve distanza lungo l'asse z, il che permette una ricostruzione tridimensionale dettagliata del corpo.

## Elaborazione delle bioimmagini

Le operazioni di elaborazione delle immagini sono solitamente definite per immagini a toni di grigio. Le immagini a colori vengono trattate come tre immagini a toni di grigio separate, se il modello è a colori saranno presenti tanti canali quante sono le colorazioni.

Un buon modo per sintetizzare il contenuto di un'immagine a toni di grigio è l'istogramma.

## Regioni di interesse

Un'immagine può contenere delle sotto-immagini che rappresentano degli oggetti (possono essere d'interesse o meno).Solitamente per rappresentare questo tipo di informazione vengono utilizzate le immagini binarie (0,1) e il dato importante non è rappresentato dal valore del pixel ma dalla sua presenza.

## Operazioni sulle immagini

Le operazioni sulle immagini vengono eseguite come operazioni tra matrici e funzioni matematiche che possono dare in output altre immagini o trasformarle direttamente. Queste operazioni possono essere categorizzate in:

- Point operations: la funzione viene applicata a tutti i punti della matrice di input. L'output dipende solo dal pixel di input e dalla funzione su di lui applicata, riguardano quindi il singolo pixel.
- Local operations: coinvolgono un intorno del pixel di input e i valori dell'output dipendono dai punti ad esso vicini.
- Global operations: l'output dipende dall'intera immagine.

### Operazioni locali

Le operazioni locali dipendono dal vicinato relativo al pixel di interesse, esistono due principali tipi di vicinato: 4 vicini in cui è presente un lato in comune e 8 vicini in cui contano anche i vertici in comune.

### Luminosità e contrasto

Per incrementare o decrementare luminosità e contrasto delle immagini è necessario conoscere l'istogramma che compone l'immagine. Se il range dei valori è molto stretto, è possibile espanderlo senza perdere informazioni.

Per aumentare la luminosità, ad ogni pixel viene sommata una costante, mentre per aumentare il contrasto si moltiplica il valore dei pixel per una costante.

Modificare il contrasto o la luminosità delle immagini può portare ad una perdita di dettaglio nelle zone più scure o più chiare.

Il contrasto dipende dall'uniformità dei toni di grigio presenti nell'immagine.

### Componenti connesse

Data un'immagine binaria b(m,n), due pixel sono 4-vicini se esiste un 4-path, ovvero un percorso continuo fatto solo di pixel adiacenti in orizzontale o verticale (non diagonale), tutti con valore 1 che collega i due pixel. L'insieme dei pixel connessi viene definito come componente connessa.

In un'immagine binaria che rappresenta delle regioni d'interesse ci saranno delle componenti connesse.

Per determinare le componenti connesse, si scansiona l'immagine da sinistra a destra e dall'alto verso il basso, etichettando ogni pixel con valore 1 con l'etichetta del vicino già etichettato, se presente. Altrimenti, gli si assegna una nuova etichetta.

### Convoluzione

La convoluzione è un'operazione matematica in cui una piccola matrice (detta kernel o filtro) viene fatta scorrere su tutta l'immagine e a ogni passo calcola un nuovo valore del pixel centrale combinando i valori dei pixel vicini. Il suo obiettivo è trasformare un'immagine in un'altra evidenziando o modificando certe caratteristiche locali (come bordi, texture, rumore, ecc.) grazie alla matrice di kernel. Svolgere quindi azioni di filtering.

Matematicamente: 

$$
 a'(x,y) = k \cdot \sum_{i,j=-R}^{R} a(i+x,j+y) \cdot f(i,j)
$$

in cui:

- $a$: immagine originale
- $a'$: immagine filtrata
- $f$: matrice di convoluzione o filtro o maschera o kernel, fatto da pesi
- $R$: mask radius (half side)
- $k$: costante di normalizzazione

### Operazioni globali

Le operazioni globali traducono l'intera rappresentazione di un'immagine in un altro dominio. L'operazione più importante è la trasformata di Fourier che, invece di considerare l'immagine come una griglia di pixel (spazio), la rappresenta come somma di onde di diverse frequenze. Le frequenze basse corrispondono alle forme generali e alle aree uniformi dell'immagine, mentre le frequenze alte rappresentano i dettagli fini, i bordi e i cambiamenti repentini di colore.

Una volta ottenuta l'immagine sotto forma di frequenze è possibile rimuovere il rumore (frequenze alte non desiderate), evidenziare i bordi e comprimere l'immagine.

Dopo aver effettuato le modifiche nel dominio delle frequenze, si può utilizzare la trasformata inversa di Fourier per ricostruire l'immagine modificata nello spazio originale, restituendola come una normale immagine composta da pixel.

### Segmentazione

La segmentazione è un'operazione che consiste nel suddividere un'immagine in aree omogenee, chiamate regioni, in base a un certo criterio che può essere di colore, intensità, texture, ecc. Queste regioni sono gruppi di pixel che si assomigliano tra loro rispetto a un certo attributo come ad esempio intensità luminosa o colore. Una volta segmentate, le regioni possono essere analizzate e misurate per scopi diagnostici, statistici o di classificazione.

Questa operazione risulta complessa e può essere eseguita in modi diversi:

- Histogram thresholding: la segmentazione avviene in base a soglie di intensità nel diagramma dell'istogramma. L'immagine
è divisa in base a gruppi di pixel che si trovano al di sopra o al di sotto a certe soglie nell'istogramma.
- Region growing: ad un punto punto vengono aggiungi pixel simili fino a che la regione è omogenea.
- Region splitting: divide l'immagine in parti sempre più piccole fino a trovare discontinuità ovvero i bordi tra oggetti o regioni diverse.
- Snakes and balloons: una tecnica più avanzata che prevede curve deformabili che si adattano ai contorni di un oggetto. Viene usata spesso per segmentazioni precise, come ad esempio nei contorni di organi nelle immagini mediche.

Il risultato potrebbe non essere un'immagine, ma un elenco di regioni descritte matematicamente o tramite metadati (coordinate, etichette, proprietà, ecc.).

### Sogliatura

Con la sogliatura viene prodotta una nuova immagine binaria basandosi su un'immagine a toni di grigio presa in input.

$$
b(m, n) =
\begin{cases}
1 &se \ tmin \leq a(m, n) \leq tmax\\
0 &altrimenti
\end{cases}
$$

In cui: 

- $a(m,n)$: immagine a toni di grigio.
- $b(m,n)$: immagine binaria in output.
- $tmin$ e $tmax$: soglie.

Questa tecnica permette di rappresentare le regioni quando le immagini hanno un istogramma bimodale.

### Region features

Quando si segmenta un'immagine in regioni, è utile descriverle numericamente per analizzarle, confrontarle, o fare diagnosi. Queste descrizioni numeriche si chiamano feature o caratteristiche. Queste caratteristiche aiutano a identificare e classificare le regioni in base alla loro forma,dimensione, colore, texture, ecc.

Esistono due categorie principali di feature: quelle riguardanti la forma e quelle riguardanti il colore.  

Le caratteristiche morfometriche si occupano dello studio e della misurazione della forma.  Analizzano parametri quali l'area, il perimetro, il diametro minimo e massimo e fattori di regolarità della forma. Un tumore benigno può avere una forma regolare, uno maligno irregolare.

Le caratteristiche colorimetriche riguardano la valutazione del colore o della scala di grigi. Queste caratteristiche considerano la media e la deviazione standard dei livelli di grigio (o colore) e possono quantificare quanto sia uniforme o complessa la distribuzione dei toni e dei grigi.

Le caratteristiche possono essere anche di basso livello, ad esempio ottenute con filtri di convoluzione.

Alcune feature si calcolano applicando filtri matematici direttamente sull'immagine, per rilevare bordi, angoli, texture, ecc. Queste sono caratteristiche più “grezze” ma molto utili, ad esempio nel machine learning.

## Bidimensionalità e tridimensionalità

Molte tecniche di analisi sono pensate per immagini bidimensionali, ma in medicina le immagini sono spesso tridimensionali. Il passaggio da 2D a 3D complica i calcoli e l'interpretazione delle feature, ma è necessario per analisi più realistiche.

## Misure quantitative

Quando si lavora con immagini digitali a volte è fondamentale misurare con precisione. Per ottenere misure quantitative affidabili, bisogna assicurarsi che ciò che appare nell'immagine corrisponda alla realtà fisica, questo equivale a domandarsi quanto valga un pixel nelle direzioni X e Y. Questa misura è relativamente semplice da calcolare se si conosce la risoluzione del sensore o del sistema di acquisizione. Conoscere questo dato serve per misurare distanze, superfici e volumi.

In alcune situazioni risulta importante conoscere a quale intensità luminosa reale corrisponde il valore di un pixel. Il valore di luminosità del pixel dipende da molti fattori quali illuminazione, sensibilità del sensore o tipo di oggetto.

Conoscere questa metrica ha senso solo se l'intensità del colore ha un significato fisico reale (es. concentrazione di una sostanza, intensità di fluorescenza…).

Può essere necessario eseguire la calibrazione per mettere in relazione l'immagine digitale con valori reali e misurabili. Ciò è possibile farlo mettendo un oggetto di dimensioni note nell'immagine o utilizzare cartoncini di grigio calibrati per collegare il valore dei pixel all'intensità
luminosa reale.