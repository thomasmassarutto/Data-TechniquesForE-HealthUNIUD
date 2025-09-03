# Fascicolo Sanitario Elettronico

In Italia esiste il Sistema Informativo Socio Sanitario Regionale che mette a disposizione, tramite il portale del cittadino, servizi di report, booking e waiting list.

## Fascicolo Sanitario Elettronico

In Italia esiste il FSE (Fascicolo Sanitario Elettronico) ed è implementato da un sistema integrato che consente la condivisione delle informazioni sanitarie tra diverse strutture, garantendo che i dati siano accessibili in modo sicuro e protetto. Risulta essere molto ingombrante e necessita di tecniche di compressione lossy. La ricerca delle informazioni al suo interno è difficile.

Contiene referti, lettere di dimissione, vaccinazioni, ricoveri, esami specialistici, farmaci prescritti ed eventuali esenzioni. Viene gestito dalle regioni sotto l'infrastruttura del Ministero della Salute e i medici lo possono consultare sotto il permesso dell'interessato. Ogni cittadino vi può accedere via SPID/CIE.

Il DDL sulla sperimentazione clinica del 2012 prevede che il FSE non gravi sulla spesa pubblica.

## Dossier

Il dossier sanitario è un insieme di dati sanitari raccolti a livello locale da una singola struttura sanitaria o gruppo di
strutture (es. un ospedale, una ASL, un'azienda ospedaliera-universitaria).
Contiene le informazioni cliniche prodotte dalla struttura stessa insieme a dati e documenti interni (anche appunti clinici, esami non refertati, ecc.). Viene gestito dal singolo ente sanitario (ospedale, ASL...) ed è generalmente accessibile solo al personale sanitario della struttura. Le informazioni al suo interno possono essere più dettagliate e ha una forma più operativa rispetto al FSE.

### Privacy

Vi è quindi una distinzione fra dossier sanitario e FSE. Il primo riguarda i dati collezionati da una sola istituzione clinica, mentre il secondo è una raccolta di  dati provenienti da più istituzioni. Entrambi devono rispettare le norme di privacy e sottostare al consenso informato. Questo può essere ignorato solo in situazioni di emergenza, quando informazioni cruciali alla vita del paziente sono disponibili nella banca dati.

Al cittadino è data la possibilità di non creare record e/o di oscurare alcuni dati. In questo secondo caso deve essere possibile anche oscurare l'oscuramento rendendo noto a priori che alcuni dati potrebbero non essere disponibili.

### Report online

Prima della firma elettronica, il report online era da considerarsi una semplice preview di quello ufficiale, quindi senza valore legale, mentre al giorno d'oggi è diventata un alternativa al report cartaceo. Eventuali notifiche di report online non devono contenere dati, devono solo svolgere una funzione di notifica.

## Struttura del Fascicolo Sanitario Elettronico

Il FSE è suddiviso in sezioni che contengono ognuna un certo tipo di dato:

- dati identificativi
- dati amministrativi
- documenti sanitari
- profilo sanitario sintetico
- note del cittadino

Il profilo sanitario sintetico sintetizza lo stato di salute del paziente fornendo le informazioni più importanti: serve a promuovere la continuità di cura e risulta essere conciso, non clinicamente specifico e non indirizzato a qualcuno in particolare.

Le note del cittadino sono informazioni generali auto inserite dal cittadino, non sono verificate o certificate.

## Guidelines technologies

Esistono delle guidelines che si occupano di descrivere come immagazzinare, trovare, trasmettere, leggere e capire i dati evitando quindi di trasformare tutto in PDF.

## Modello

L'Infrastruttura tecnologica del FSE (InFSE) definisce le specifiche tecniche per l'interscambio di documenti sanitari tra sistemi territoriali del Fascicolo Sanitario Elettronico garantendo disponibilità, affidabilità, sicurezza e privacy. Ha una struttura federale e prevede un modello architetturale Service Oriented Architecture in cui i nodi possono essere locali o regionali.

Il servizio è diviso in 3 parti fondamentali: business layer, component layer e connectivity layer.

### Requisiti

Questo modello prevede che il FSE debba sottostare ad una serie di requisiti che ne garantiscono l'efficacia e la qualità.

- Disponibilità delle informazioni: il sistema deve recuperare i dati da tutte le regioni, ospedali, ASL, anche se non sono nello stesso posto e deve funzionare come una rete federata, non come un unico database centrale.
- Supporto ai processi di cura: deve collegare tra loro le informazioni relative a singoli episodi clinici (es ricovero, visita, intervento) in modo da aiutare a ricostruire il percorso di cura di un paziente nel tempo.
- Aderenza al modello sanitario attuale: deve rispecchiare la struttura reale del SSN italiano, inclusi i ruoli dei medici di base, specialisti, ospedali, ... allineandosi ai processi clinici ed amministrativi già in uso.
- Facilità di integrazione con le soluzioni esistenti: deve potersi collegare ai software già in uso nelle regioni, ASL e ospedali con l'obiettivo è evitare duplicazioni, migrazioni complesse o sistemi incompatibili.
- Uso del Sistema Pubblico di Connettività: deve sfruttare le infrastrutture pubbliche esistenti per collegare tra loro le istituzioni in modo sicuro.
- Basato su standard aperti: deve utilizzare standard internazionali, documentati e interoperabili (es. HL7, CDA, FHIR, ICD-10, SNOMED) con lo scopo di garantisce la portabilità e l'interscambio tra sistemi diversi.
- Scalabilità e modularità: il sistema deve essere in grado di crescere con l'espansione del numero di utenti e dati, inoltre deve essere possibile aggiungere funzionalità senza rifare tutto da zero.
- Affidabilità: deve essere disponibile 24/7, con bassa probabilità di errore o blocco. I dati devono essere coerenti, accessibili e sicuri anche in caso di guasti
- Prestazioni: il sistema deve essere veloce, reattivo e in grado di rispondere rapidamente anche con grandi
volumi di dati.
- Sicurezza e tutela della privacy: il sistema deve rispettare il GDPR e le norme italiane per la protezione dei dati sanitari grazie a controlli su accesso ai dati, tracciabilità e consenso informato del cittadino

### Component layer

Il component layer è un livello sempre presente in tutti i nodi che al suo interno contiene diversi componenti:

- Interfaccia di accesso che permette l'accesso ai servizi dell'infrastruttura. Gestisce autenticazioni e l'accesso ai documenti.
- Gestore dei documenti che si occupa dello storage e del retrieval dei dati.
- Gestore delle politiche d'accesso che implementa la sicurezza e le policy d'accesso ai dati dell'infrastruttura grazie a meccanismi di autenticazione, identificazione e autorizzazioni
- Registro degli indici federati che mantiene i metadati dei documenti clinici. Ha il compito di rimanere sempre aggiornato.
- Gestore degli eventi che invia notifiche degli eventi sanitari a chi di dovere tramite un meccanismo publish/subscribe. Gli eventi possono essere interni alla struttura federale o di interesse agli utenti dell'infrastruttura.

### Indexing

I dati sono immagazzinati con il formato HL7-CDA, poi vengono indicizzati tramite metadati. Più metadati sono disponibili, più una ricerca può essere precisa, grazie a query articolate. Meno metadati permettono query più lineari, ma risultati meno precisi in fase di ricerca.

## FSE e il cittadino

Non sono presenti specifiche indicazioni su come dare accesso al proprio FSE al cittadino, tuttavia le implementazioni correnti convengono sull'uso di sistemi web-based o applicazioni mobile. Il metodo di autenticazione preferito è lo SPID.

Si sta attualmente lavorando per aumentarne la percentuale di utilizzo in quanto per ora risulta poco usato.

### FSE 2.0

Il FSE 2.0 prevede di acquisire i dati in HL7-FHIR direttamente dai sistemi. Con questo sistema i dati potranno essere inviati tramite metadati presenti in PDF firmati così da rendere leggibile sia alla macchina che all'umano i dati presenti in un documento.

Si cerca di usare sistemi open source.
