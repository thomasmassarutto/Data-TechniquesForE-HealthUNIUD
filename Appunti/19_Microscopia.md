# Microscopia

I microscopi ottici possono essere a luce trasmessa, riflessa, a fluorescenza o confocale. Ognuna di queste tipologie è in grado di raggiungere dettagli diversi con risoluzioni diverse.

## Il microscopio ottico

I principali tipi di microscopio ottico sono quelli a luce trasmessa, in cui la luce è posizionata dietro il semi trasparente, e quelli a luce riflessa, in cui la luce viene usata per illuminare il campione.

Cosa si vede dipende dall'obiettivo e dalla lunghezza d'onda della luce. Per quanto riguarda l'obiettivo è necessario conoscere l'ingrandimento, la distanza di lavoro, l'indice di campo (l'area visibile dall'oculare) e l'apertura. Quest'ultima indica la capacità di raccogliere la luce e risolvere i dettagli più fini dell'immagine descrivendo quindi il dettaglio visibile. Dipende dall'ingrandimento e dalla tecnologia usata per realizzare la lente.

La tecnologia ottica di realizzazione di un obiettivo gioca un ruolo fondamentale nella sua qualità.

### Risoluzione

La risoluzione è una metrica che descrive la distanza minima che si riesce a distinguere tra due punti e indica il dettaglio minimo visibile. Formalmente è descritta come $R=\lambda \cdot NA$. $\lambda$ indica la lunghezza d'onda della luce (verde ha $\lambda = 500\,\mathrm{nm}$).

### Il campione

Il campione, se usato con microscopi a luce trasmessa, deve essere semi trasparente. Viene posizionato su vetrini standard e coperto dal copri oggetti. Ci sono due principali tipi di campione: quelli istologici e quelli citologici.

I campioni istologici sono prelevati tramite biopsia o tramite interventi dal tessuto di interesse, hanno uno spessore di circa quattro micron e la loro struttura cellulare viene mantenuta.

I campioni citologici sono delle cellule isolate o sfuse che non hanno struttura di supporto, come liquidi o apposizioni, e sono più facili da ottenere rispetto ai precedenti. Questo genere di campione viene lasciato solidificare in formalina e poi viene incorporato in paraffina per sezionarlo. Alternativamente può venire congelato, anche se la struttura corre il rischio di rovinarsi. I campioni citologici principali sono cellule isolate, PAP test o il sangue.

### Colorazione

Il campione può venire colorato per far risaltare le caratteristiche di interesse. La colorazione più utilizzata è quella ad ematocilina/eusina che serve a distinguere le cellule dal citoplasma, è una colorazione morfologica che evidenzia le caratteristiche strutturali e la forma delle cellule e dei tessuti.

La colorazione immunoistochimica evidenza la presenza o la localizzazione di alcune sostanze o proteine nei tessuti delle cellule. Generalmente questa viene eseguita tramite anticorpi.

La fluorescenza permette di evidenziare alcuni cromosomi specifici dentro i nuclei delle cellule isolate o tessuti.

## Il microscopio confocale

Il microscopio confocale a fluorescenza è in grado di illuminare un punto alla volta. La luce che questo riflette viene poi raccolta da uno scintillatore. Questo tipo di microscopio consente di focalizzare anche sull'asse z le immagini e permette di ricostruire immagini tridimensionali dettagliate. 

I fluorocromi usati nella colorazione per questo metodo decadono e i campioni devono essere esaminati velocemente oppure ricolorati.

## Acquisizione 

I problemi dell'acquisizione di un immagine sono la vignettatura, il centraggio della luce, come acquisire immagini tridimensionali e il fatto di acquisire solo porzioni di un immagine completa.

L'acquisizione può avvenire tramite microscopio meccanico tradizionale o tramite microscopio con scanner. Nel primo caso lo strumento si sposta sul campione acquisendo immagini a tiles, mentre nel secondo, lo scanner effettua una scansione lineare del campione.

Fochettare, ovvero mettere a fuoco attraverso piccoli movimenti, può essere utile per acquisire immagini con messe a fuoco differenti per rendere meglio la tridimensionalità, tuttavia questa tecnica è dispendiosa in termini di tempo.

Una volta acquisita l'immagine, questa può essere usata per studi morfologici, ovvero sulla forma delle cellule, per fare valutazioni istochimiche o per altro.

Il campo visivo è un area circolare che al centro risulta più definita. I vetrini digitali sono in grado di acquisire quasi tutto il vetrino e generano immagini molto grandi, di solito si usa un obiettivo 40x e queste immagini possono essere salvate a risoluzioni differenti per facilitare la visualizzazione.

## Messa a fuoco

La messa a fuoco di un campione può risultare problematica in quanto nei campioni è presente della variabilità come il coperchio inclinato o il campione non perfettamente piatto. Per aiutare nel compito i microscopi dispongono di sistemi di autofocus che possono essere attivi, tramite la misurazione della distanza con infrarossi, o passivi, quando catturano più immagini e scelgono quella più a focus. Quest'ultima tecnica utilizza la deviazione standard per capire quale dei tentativi mostra più dettagli, tuttavia, acquisire più foto è dispendioso e sono nate tecniche che ottimizzano il numero di tentativi.

## Riconoscimento tessuti

Il riconoscimento dei tessuti può avvenire via software e permette di capire automaticamente dove si trova del tessuto da scannerizzare. Il software traccia delle bounding box dentro cui viene acquisita l'immagine d'interesse e la messa a fuoco viene fatta in base al contenuto che si trova dentro di queste.

## Memorizzazione

Le immagini vengono memorizzate in vari formati:

- jpeg: è possibile usarlo, ma con molti compromessi in quanto è lossy
- tiff: si tratta di un formato multi immagine
- jpeg2000: è lo standard per grandi immagini e permette il caricamento e la lettura di solo parti dell'immagine
- DICOM e supplementi: non viene ancora adottato, ma dispone di identificatori che permettono di identificare in modo univoco il percorso che porta ad un immagine ed è possibile utilizzarli per identificare il campione. Questo formato supporta risoluzioni diverse.
