# Bioimmagini

Le bioimmagini forniscono informazioni che non possono essere ottenute dai soli biosegnali e possono essere si analogiche che digitali. Su di esse possono essere svolte varie operazioni con lo scopo di aumentare la qualità delle informazioni estraibili. 

## Immagini

Ogni immagine digitale può essere vista come una funzione in cui il valore del pixel ($a(x,y)$) è una proiezione di uno spazio tridimensionale sulla matrice che compone l'immagine.

L'elaborazione permette, data un immagine, di modificarne l'aspetto per migliorarla. L'analisi permette di estrapolare da un immagine dell'informazione quantitativa, mentre l'interpretazione fornisce dell'informazione qualitativa.

Le immagini sono ottenute grazie all'interazione di onde elettromagnetiche con un corpo: tipicamente vengono attenuate, assorbite o deviate dai tessuti di esso. Le onde utilizzate in medicina sono varie e cambiano in base al tipo di esame, per le ecografie si usano gli ultrasuoni, ma per altri casi d'uso vengono usate altri tipi di onda come lo spettro elettromagnetico, un fascio elettronico o del potenziale elettrico. La scelta viene fatta in base alla precisione necessaria, al costo e ad eventuali controindicazioni.

A volte i fenomeni di interesse non sono direttamente visibili e bisogna trasformare il campione tramite colorazione di cellule o mezzi di contrasto per renderne visibili le caratteristiche.

### Modalità di acquisizione

Un'immagine può essere acquisita tramite luce riflessa o luce trasmessa. 

Con il metodo della luce riflessa gli oggetti di interesse vengono colpiti da una fonte di luce di cui ne assorbono una quota e ne riflettono un altra. Questo è il tipico modo di lavorare delle fotocamere. 

Per quanto riguarda la luce trasmessa, la fonte luminosa si trova dietro l'oggetto che si vuole riprendere  e lo attraversa. Il sensore riceve i segnali della fonte luminosa che sono stati alterati dal passaggio dell'oggetto, questo è il metodo più utilizzato in medicina e un esempio di applicazione sono le radiografie.

### Campionamento

Le immagini acquisite sono un campionamento di punti: l'immagine è divisa in una griglia di elementi atomici, ovvero i pixel, che rappresentano il valore medio del colore dell'area scannerizzata. Il colore viene poi quantizzato per passare da una scala analogica a infiniti valori ad una scala digitale con valori discreti e limitati in grado di essere rappresentata in un calcolatore. Vi è quindi una doppia approssimazione: valore medio di colore in un pixel e quantizzazione di esso.

### Approssimazione

In base all'utilizzo dell'immagine bisogna scegliere un livello accettabile di approssimazione tenendo conto anche del rumore. Secondo il teorema di Shannon-Nyquist è necessario campionare al doppio del dettaglio minimo che si vuole vedere.

Per migliorare la precisione è possibile acquisire lo stesso campo visivo con un sensore più prestante o produrre un immagine della stessa grandezza, ma con un campo visivo più piccolo, avvicinandosi al soggetto con il sensore o con strumenti ottici.

### Quantizzazione

Le immagini possono essere di vari tipi: binarie, a toni di grigio o multispettrali.

Le immagini binarie sono dette maschere e dispongono di 2 livelli per rappresentare l'informazione.

Le immagini a toni di grigio hanno a disposizione $2^{n}$ livelli, sono semplici dsa rappresentare.

Le immagini multispettrali sono composte da pixel che contengono informazioni provenienti da più lunghezze d'onda, questi possono essere visti come degli array la cui lunghezza dipende da quanti canali sono stati registrati: le immagini a colori hanno 3 livelli, ma esistono situazioni in cui vengono registrati anche 10 livelli.

### Modelli del colore

Ogni immagine a colori usa un modello per rappresentare il colore basato sulla struttura a coni e bastoncelli del nostro occhio. I coni sono sensibili al colore, specialmente al verde.

Ci sono 2 principali modelli per rappresentare il colore, ma non sono gli unici.

Il modello additivo (RGB) rappresenta i colori primari aggiungendoli ad un ipotetico sfondo nero, mentre quello sottrattivo (CMGK) sottrae i colori da uno sfondo bianco. Questi modelli sono facilmente intercambiabili e permettono di cogliere dettagli diversi.

Ogni immagine a colori può essere scomposta in varie immagini a toni di grigio in base al canale selezionato. Le immagini a toni di grigio sono facilmente lavorabili e permettono di riconoscere determinati aspetti che nella controparte a colori non sarebbero distinguibili.

## Sensori

I sensori permettono di trasformare il segnale continuo naturale in una bitmap digitale. Possono misurare l'ampiezza d'onda e il tempo di ritorno del segnale. Le tecnologie principali per i sensori sono CCD/CMOS e fotomoltiplicatori.

### CCD e CMOS 

CCD e CMOS sono tipi di sensore è costituiti da una griglia di elementi sensibili alla quantità di luce che arriva su ogni elemento. In pratica la luce viene vista come un insieme di particelle, fotoni, che vengono contati dal sensore per capire l'intensità del segnale. Dal punto di vista commerciale le dimensioni della griglia sono espresse in pollici e il numero dei sensori è il megapixel.

Ogni elemento della griglia è sensibile alla luce, non al colore, che viene selezionato tramite micro lenti e filtri cromatici. Questi servono sia ad avere immagini a colori, sia a filtrare le frequenze indesiderate come infrarossi o ultravioletti.

La differenza fra CCD e CMOS sta nel trasferimento dei dati dalla griglia al processore. Le fotocamere CCD adottano una metodologia seriale in cui le informazioni di ogni sensore vengono passate una dopo l'altra al processore. Le fotocamere CMOS sono dotate di elementi sensibili con digitalizzatori autonomi. In questo modo l'immagine viene letta come se fosse una sorta di ram con la possibilità di leggere solo parte dell'immagine, ma vi può essere presente una leggera variabilità fra i colori dei sensori.

### CCD e rumore

Vi sono vari tipi di rumore presenti. Il rumore termico è generato dalla agitazione termica delle particelle, il rumore fotonico dipende dal numero dei fotoni che arrivano al sensore, il readout noise dipende dalla variabilità nella conversione dei dati e il rumore di quantizzazione viene generato digitalizzando un segnale analogico.

Più grande è l'elemento sensibile, più basso è il rumore in quanto un sensore di dimensioni maggiori è in grado di catturare più fotoni e di discriminare più livelli di luce, ma, di contro, permette una risoluzione inferiore.

### CCD e acquisizione del colore

Idealmente il segnale di output del sensore dovrebbe essere linearmente proporzionale all'input che riceve, ma non sempre è così. La funzione di gamma esprime la non linearità dei sensori e, quando nota, può essere usata per rendere lineare l'immagine acquisita.

I due principali metodi per acquisire colore con le fotocamere CCD sono 3CCD e MONOCCD. 

La tecnica 3CCD prevede la presenza di 3 sensori indipendenti che ricevono la stessa luce filtrata da un prisma e ogni sensore ha un filtro per un dato colore. Le immagini prodotte sono di buona qualità, ma la tecnica è poco sensibile alle basse luminosità in quanto la luce viene divisa dal prisma. 

La tecnica MONOCCD si basa sul mosaico di Bayer: davanti ad ogni sensore vi è un filtro colorato rosso, verde oppure blu. In un quadrato 4x4 vi sono due sensori per il verde, uno per il rosso e uno per il blu. Ogni pixel ha un filtro per un colore apposito e viene colorato tramite interpolazione con i colori dei pixel vicini. La resa dei colori è inferiore rispetto a 3CCD, ma le fotocamere sono più economiche da produrre.

## Sensori ad uso scientifico

Per fornire risultati attendibili, un sensore ad uso scientifico deve fornire tutte le specifiche tecniche. I sensori devono anche essere tarati per conoscere la loro risoluzione reale e, per fare ciò, vengono ripresi oggetti di caratteristiche note per andare a controllare nell'immagine digitale il dettaglio.

In ambito scientifico vengono spesso usati sensori CCD, ma ultimamente anche CMOS. 

Le immagini statiche possono essere raccolte tramite un sensore CCD posto dietro ad una ruota di filtri.

Per quanto riguarda i video deve essere nota anche la velocità di trasferimento dei dati: per avere un certo framerate può essere necessario manipolare la risoluzione.

### Efficienza quantica

Non sempre tutti i fotoni vengono tradotti in segnale, l'efficienza quantica misura la percentuale di fotoni tradotti in segnale. Questa misura dipende dalla lunghezza d'onda: non ci sono sensori che rispondono linearmente a tutte le frequenze sensibili e varia dal 20% al 80%. Quando è alta è possibile percepire segnali molto deboli.

### Full well capacity

Ogni elemento ha una capacità massima di fotoni che è in grado di acquisire. La full well capacity serve a capire quanti livelli il sensore riesce a discriminare a livello teorico. I livelli reali sono di meno a causa del rumore.

Il dynamic range è la relazione fra full well capacity e readout noise. Descrive i livelli effettivi ed è indipendente dalla rappresentazione in pixel: $\text{dynamic range} = \frac{\text{FWC}}{\text{readout noise}}$.

### Fotomoltiplicatori e scintillatori

I fotomoltiplicatori sono particolari sensori che registrano un segnale alla volta registrando un solo fotone. In pratica fotografano un solo pixel alla volta. Il loro elemento sensibile riceve la luce e causa una cascata di elettroni che viene moltiplicata fino a renderlo percepibile.

Sono molto sensibili al rumore, in particolare a quello termico, e devono essere usati in ambienti controllati. 

Un caso d'uso prevede il loro utilizzo in microscopi confocali in cui il campione viene illuminato un punto alla volta. Questo processo è lento, ma molto preciso. I fotomoltiplicatori sono usati in medicina di laboratorio o in citofluoremtria.

I scintillatori sono dispositivi che emettono luce quando colpiti da particelle.

## Qualità dell'immagine

La qualità complessiva di un immagine dipende dal sensore e da altre fonti di errori come i vari tipi di rumore, difetti ottici o di illuminazione che si combinano assieme. 

Bisogna comunque essere in grado di distinguere variabilità biologica da errore di misurazione. Una tecnica per ridurre la possibilità di errore prevede la ripetizione delle misurazioni, ma non sempre è possibile.

Nelle immagini il rumore si vede sotto forma di puntini e sono state sviluppate delle tecniche di noise reduction che modificano l'immagine per eliminare il rumore.

Altri artefatti possono essere generati dalla luce che colpisce il centro del campione in maniera più forte rispetto ai bordi, o dall'ottica che è più precisa al centro. Una tecnica per ridurre questi artefatti prevedere l'acquisizione solo dello sfondo, così è poi possibile sottrarre gli artefatti dalle immagini.