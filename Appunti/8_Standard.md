# Standard

In ambito clinico esistono vari standard che permettono la comunicazione fra sistemi sanitari. I più importanti sono  HL7 (Health Level 7), CDA (Clinical Document Architecture), FHIR (Fast Healthcare Interoperability Resources) e DICOM (Digital Imaging and COmmunications in Medicine).

## HL7

HL7 (Health Level Seven) è un organizzazione che sviluppa standard di interoperabilità improntati allo scambio di informazioni cliniche e amministrative tra sistemi informatici in ambito sanitario. Definisce formati e protocolli per la trasmissione di messaggi, non di interi documenti.

La situazione tradizionale prevede che due reparti si passino i dati a mano, HL7 si pone da intermediario facendo le veci del passaggio manuale. Funge da interfaccia per sistemi informativi che così possono scambiarsi messaggi dopo eventi predefiniti anche in maniera automatica.

Ogni messaggio ha un tipo definito da un codice a tre lettere ed è diviso in segmenti che, a loro volta, possono essere divisi in parti. Ogni messaggio è inviato dopo un trigger che puo essere anche automatico.

Al giorno d'oggi convivono due versioni di protocolli HL7: V2 e V3, non sono però compatibili

### HL7 V2

HL7 V2 si occupa di standardizzare la struttura, le regole di codifica/decodifica e gli eventi trigger riguardanti un messaggio. I trigger sono eventi del mondo reale che vengono standardizzati per permettere la comunicazione fra più sistemi.

#### Messaggi

I messaggi possono essere di due tipi: non sollecitati o query. Quelli di tipo non sollecitato sono spediti automaticamente dopo un evento e vengono elaborati dal destinatario con un ACK o con altre azioni, mentre le query sono una richiesta di informazioni ad un destinatario.

Ogni messaggio ha un codice che può essere standardizzato o libero, questo risulta sempre leggibile ad un essere umano in quanto si tratta di testo ASCII. Ogni messaggio è composto da segmenti che possono essere di 120 tipi diversi, ognuno con la sua semantica. Il tipo MSH rappresenta i metadati, PID le informazioni relative al paziente e PVI le informazioni relative all'episodio. 

Ogni segmento è composto da campi separati dal carattere '|', ogni campo può essere ulteriormente suddiviso in maniera gerarchica tramite '^' o '&'.

Lo scambio di messaggi avviene tramite un architettura modellata in modo non stringente che prevede principalmente quattro ruoli principali:

- order: vengono effettuate le richieste di materiali o servizi
- observation: il risultato di un order
- placer: applicazione che produce ordini
- filler: applicazione che produce osservazioni

Ogni tipo di scambio di messaggi ha poi i suoi segmenti tipici. Un segmento molto usato è OBX che permette lo scambio di dati clinici, questo non è il documento completo, ma solo i dati intermedi.

### HL7 V3

Hl7 V3 promuove una maggiore uniformità fra i messaggi grazie ad un grado di formalità più elevato rispetto al suo predecessore che gli permette di esprimersi con definizioni più precise e object oriented. Le differenze sono tali che vi è poca retrocompatibilità.

#### Principi HL7 V3

HL7 V3 è stato creato prendendo spunto da casi d'uso da cui viene generato un modello informativo generale su cui poi gli esperti di dominio si occupano di definire i dettagli.

Per astrarre ciò che ha a che fare con la comunicazione, i casi d'uso vengono modellati tramite UML così da capire le figure chiave che compaiono più spesso. Da queste vengono creati gli oggetti usati per definire i messaggi.

Un modello di messaggio astratto è il risultato dell'unione fra il modello di referenza, le specifiche comuni e le specifiche di domino. Una volta chiariti questi nodi, sarà possibile passare all'implementazione fisica tramite XML o altri linguaggi di markup.

#### Scambio di messaggi

Il diagramma che specifica come si muovono i messaggi vene standardizzato sotto forma di un copione. Questo può non essere lineare e presentare diramazioni.

RIM (Reference Information Model) definisce uno schema per tutti i possibili scambi di messaggi ed è basato su un modello object oriented che collega le entità ai loro ruoli. Ogni ruolo è collegato ad una partecipazione per svolgere un atto e ha link con altri ruoli. Ad esempio, l'entità aspirina ha il ruolo di agente terapeutico e partecipa come consumabile, insieme al paziente, all'atto della somministrazione.

Ogni specialità medica ha un dominio specifico gestito da comitati che generano specifiche per i messaggi.

#### Implementazione

Una volta generati dei modelli abbastanza specifici, si passa all'implementazione che può essere char based, object oriented o di qualche altro standard utilizzabile. In questa fase viene scelta la tecnologia di comunicazione che può essere varia: CD, TCP/IP, ...

## CDA

CDA (Clinical Document Architecture) è uno standard basato su HL7 che definisce la struttura e il contenuto dei documenti clinici elettronici. Si occupa della rappresentazione e dello scambio di documenti clinici completi e quindi con valore legale: questi devono essere autentici leggibili e completi.

### Struttura CDA

Un documento che segue questo standard è composto da un'intestazione che contiene metadati e dal corpo che contiene il documento clinico.

L'informazione può essere strutturata secondo tre livelli con precisioni differenti.

Il primo livello rappresenta l'informazione in modo generico senza semantica nei termini usati: rappresenta solo la struttura e il contenuto del documento. La semantica è presente solo nell'intestazione, il corpo non ha vincoli ed è fatto per la lettura umana.

Il secondo livello risulta più strutturato e per alcuni domini specifici vengono definite le forme che il documento deve avere, l'ordine e la gerarchia delle varie sezioni.

Il terzo livello prevede la semantica completa del documento, questo permette l'etichettatura per i sistemi informatici grazie al fatto che ogni sezione esprime il suo contenuto in modo formale.

## FHIR

FHIR (Fast Healthcare Interoperability Resources) è uno standard sviluppato da HL7, introdotto nel 2012, che mira a migliorare l'interoperabilità nel settore sanitario combinando i principi della messaggistica HL7 con approcci moderni basati sul web.

Utilizza un'architettura basata su REST (REpresentational State Transfer), che consente l'interazione tra sistemi attraverso web services e supporta formati di dati come JSON e XML. Per la trasmissione sicura usa HTTPS e per l'autenticazione e l'autorizzazione degli accessi OAuth. 

### Risorse

FHIR definisce un insieme di risorse, che rappresentano categorie di dati comunemente utilizzate negli scambi di informazioni tra sistemi. Queste risorse possono essere utilizzate singolarmente o in combinazione e sono formate da elementi, vincoli e relazioni che le legano le une alle altre. Ognuna di queste è identificata da un URI univoco e nascono per essere più generali possibile. In base alla necessità possono essere combinate, estese e modificate.

Un esempio di risorsa è il paziente.

### API FHIR

FHIR utilizza API REST come base per lo scambio di dati. Questo approccio consente una comunicazione semplice e intuitiva tra i sistemi informatici nel settore sanitario. I dati sanitari, come farmaci, osservazioni e informazioni sui pazienti, sono rappresentati da risorse specifiche. Ogni tipo di dato ha la propria risorsa che definisce la struttura e il contenuto delle informazioni. 

Le risorse possono essere richieste tramite comandi HTTP RESTful: gli sviluppatori possono utilizzare metodi HTTP standard (come GET, POST, PUT, DELETE) per interagire con le risorse FHIR. Una richiesta FHIR può restituire una singola risorsa, come le informazioni di un singolo paziente, oppure può restituire un bundle di informazioni, come tutti i dati relativi a tutti i pazienti in un sistema di cartelle cliniche elettroniche. Questo metodo consente di ottenere informazioni aggregate in un'unica risposta.

### FHIR e il Fascicolo Sanitario Elettronico 2.0

Il FSE 2.0 dovrebbe adottare FHIR, ma attualmente risulta un progetto con poca adozione a causa di vari fattori:

- Livello di maturità inadeguato dei sistemi informativi ospedalieri: la produzione di dati risulta solo parziale e non sempre conforme agli standard.
- Architettura di riferimento non omogenea a livello regionale: sono presenti disomogeneità nei sistemi e nei processi e questo rende difficile l'integrazione e la condivisione dei dati tra le varie strutture sanitarie.
- Servizi inefficienti: sia i servizi orientati ai cittadini che quelli orientati al supporto della ricerca e delle attività di governance limitano la crescita e l'adesione alla nuova versione del FSE.

Il ruolo di FHIR nel FSE 2.0 è quello di fungere da ponte, a livello regionale, fra il sistema nazionale e la struttura ospedaliera. Un gateway per l'acquisizione e la validazione dei dati che si occupa di garantire che i dati siano conformi a vari criteri tecnici (dati siano correttamente formattati e compatibili), sintattici, semantici e di privacy.

## DICOM

DICOM (Digital Imaging and COmmunications in Medicine) è uno standard per la trasmissione, lo storage e la visualizzazione di immagini nato per la radiografia che poi si è espanso ad altri ambiti medici. Standardizza sulla base di HL7 anche gli schermi ed è stato sviluppato sia da radiologi che e da aziende tecniche del settore.

Lo standard è definito in 15 parti/documenti interconnessi fra loro ed è aggiornato periodicamente da esperti suddivisi in working group che propongono correzioni o supplementi. Il processo di approvazione prevede 4 fasi che una modifica deve passare: work, draft, commenti e votazione.

I documenti principali che un'implementazione deve avere sono l'introduzione, la conformance per dimostrare l'interoperabilità, la definizione degli oggetti, i metodi degli oggetti e le strutture dati con i supplementi di cui i working group si occupano dei dettagli specifici.

### Comunicazione e modelli 

Lo standard prevede che entità specifiche interagiscano fra loro tramite metodi tipici: i dati di un immagine sono descritti tramite un modello object data e lo standard prevede un dizionario dei dati e delle classi di servizio.

### File DICOM

I file DICOM sono costituiti da un header con i metadati e da delle immagini. Le informazioni contenute nell'header possono essere varie, fra cui le dimensioni dell'immagine, i bit per pixel, la gamma e la modalità di acquisizione.

## IHE

L'IHE (Integrating the Healthcare Enterprise) è un associazione che cerca di tradurre in regole pratiche i vari standard disponibili. Per fare ciò cerca di promuovere e verificare l'interoperabilità fra sistemi tramite l'utilizzo di profili di integrazione che definiscono gli standard da utilizzare, in base al caso d'uso specifico, fra sistemi informativi. Vengono coperti sia i casi d'uso intra-struttura che inter-struttura.

Il sui compito è quindi quello di descrivere i casi d'uso e mappare su di essi gli standard.

Un sistema viene progettato secondo i profili di integrazione e poi viene testato con i sistemi preesistenti, in eventi quali  i connectathlon, per testare la sua interoperabilità.

