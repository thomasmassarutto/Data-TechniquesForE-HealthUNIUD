# Biosegnali e bioimmagini

I biosegnali sono segnali che vengono emessi da un essere vivente e possono essere elettrici, meccanici o chimici. Spesso sono espressi in funzione del tempo.

Una sottocategoria dei biosegnali sono le bioimmagini. In questo tipo di dato il segnale è organizzato in più dimensioni (2, 3, 4, ...) ed è ottenuto modulando raggi oppure onde che entrano in contatto con il corpo umano.

Biosegnali e bioimmagini possono esaminare aspetti difficilmente misurabili in altri modi, come organi interni o aspetti microscopici o cellulari.

Normalmente vengono prodotti molti biosegnali che, se non filtrati correttamente, possono risultare come rumore al segnale di interesse. Solitamente vengono presi in considerazione pochi segnali alla volta per determinare un caso clinico.

Lo scopo è monitorare oggettivamente il funzionamento del corpo umano.

## Terminologia 

- Elaborazione: un biosegnale viene elaborato quando su di esso vengono eseguite delle trasformazioni che lo modificano aggiungendo informazioni con miglioramenti ed evidenziature. Il biosegnale rimane dello stesso tipo di quello originale.
- Analisi: le operazioni eseguite su di un biosegnale ritornano qualcosa di più semplice dal punto di vista dei dati.
- Interpretazione: le operazioni eseguite su di un biosegnale estraggono informazioni di tipo qualitativo.

## Fasi di elaborazione

Prima di poter essere utilizzato, un biosegnale passa attraverso varie fasi.

### Acquisizione

Durante l'acquisizione il biosegnale viene misurato attraverso dei sensori e poi viene digitalizzato. Questo processo è però soggetto a rumore che diventa parte integrante della misurazione.

La digitalizzazione prevede che un segnale analogico venga trasformato in un segnale digitale rappresentato da valori discreti. Prima di questa fase bisogna decidere quanto spesso campionare il dato e che livello di quantizzazione utilizzare in base all'accuratezza necessaria. Queste due metriche devono essere scelte accuratamente in quanto influenzano le capacità di discriminare i segnali: troppo dettaglio rileva troppo rumore e rallenta il sistema nelle applicazioni real time, mentre troppo poco dettaglio implica perdita di informazioni. Bisogna quindi capire qual'è il livello di precisione adeguato per discriminare il livello giusto di dettaglio. 

Il biosegnale digitalizzato diventa un array lungo tanto quanti sono i campionamenti eseguiti: $\text{frequenza campionamento} \times \text{durata segnale}$.

### Trasformazione

Durante la fase di trasformazione vengono eseguite varie operazioni atte a migliorare l'immagine. Le tecniche di restoration permettono di ristrutturare l'immagine per farla sembrare più simile possibile all'originale senza artefatti, mentre le tecniche di enhancement ne migliorano alcuni aspetti per evidenziare situazioni di interesse.

Bisogna tenere conto che ogni operazione di elaborazione fa perdere informazioni originali dell'acquisizione, anche la restoration che, di fatto, crea dati sintetici.

### Riduzione

Durante la fase di riduzione vengono mantenute solo le parti del biosegnale che interessano.

### Interpretazione

La fase di interpretazione prevede la computazione di parametri significativi e la loro classificazione. Questa fase funge da aiuto alla diagnosi cercando di classificare automaticamente le parti più importanti del biosegnale.

## Analisi e utilizzo dei biosegnali

I biosegnali sono principalmente espressi in funzione del tempo e nei casi più fortunati corrispondono a funzioni matematiche esprimibili conoscendo frequenza e ampiezza delle varie componenti. Ciò non accade sempre a causa del rumore o dei parametri che variano nel tempo.

### Il rumore

Diverse fonti generano vari tipi di rumore, quelli principali sono: rumore termico, elettronico e ambientale. Quando si tratta di rumore additivo è possibile sottrarlo semplicemente, ma questo genere di rumori non generalmente causa di problemi. 

Una tecnica per ridurre il rumore, che però non sempre è possibile, consiste nell'eseguire più misurazioni e utilizzare poi la media come dato ufficiale.

### Applicazioni

I biosegnali possono essere usati per eseguire diverse analisi. L'analisi funzionale permette di identificare il funzionamento degli organi che li emettono. L'analisi in tempo reale permette di monitorare l'andamento di un paziente per guidare le apparecchiature su cui fa affidamento, come ad esempio le protesi o sistemi di supporto vitale. L'analisi può essere utilizzata per lo studio di argomenti poco noti.

### Tipi di segnale

Vi sono varie tipologie di biosegnali:

- puro output: il segnale viene registrato, ma non si ha conoscenza del processo che lo genera.
- evocati: si usano degli input noti che danno inizio al processo su cui si vuole registrare un biosegnale,come ad esempio il martelletto per testare i riflessi.
- provocativi: il processo che determina un biosegnale è conosciuto e ci si aspetta un dato output, come ad esempio nei test sotto sforzo.
- modello: un processo conosciuto e stabile può essere simulato dando gli stessi input al paziente e alla simulazione per valutarne poi le differenze.

## Tecniche di elaborazione e analisi

Un istogramma è in grado di rappresentare l'immagine sotto forma di una distribuzione di densità utile per capire la distribuzione dei valori.

Due biosegnali possono essere comparati per valutare le differenze.

Tramite la trasformata di Fourier è possibile determinare quali frequenze compongono il segnale e poi studiarne il dominio.

I filtraggi che possono essere eseguiti sui biosegnali possono essere eseguiti tramite dei filtri passa alto/basso/banda e/o tramite media mobile.

Lo scopo principale di un biosegnale è quello di essere poi interpretato dallo staff medico o da un sistema automatico.