# Fascicolo Sanitario Elettronico

In Italia esiste il Sistema Informativo Socio Sanitario Regionale che mette a disposizione, tramite il portale del cittadino, servizio di report, booking e waiting list.

## FSE: Fascicolo Sanitario Elettronico

Il FSE esiste in Italia ed è implementato come un sistema di copie ridondanti in ogni ospedale. Risulta essere molto ingombrante e necessita di tecniche di compressione lossy. La ricerca delle informazioni al suo interno è difficile.

Il DDL sulla sperimentazione clinica del 2012 prevede che il FSE non gravi sulla spesa pubblica.

### Privacy

In Italia vi è una distinzione fra dossier sanitario e FSE. Il primo riguarda i dati collezionati da una sola istituzione clinica, mentre il secondo è una raccolta di  dati provenienti da più istituzioni. Entrambi devono rispettare le norme di privacy e sottostare al consenso informato. Questo può essere ignorato solo in situazioni di emergenza, quando informazioni cruciali alla vita del paziente sono disponibili nella banca dati.

Al cittadino è data la possibilità di non creare record e/o di oscurare alcuni dati. In questo secondo caso deve essere possibile anche oscurare l'oscuramento rendendo noto a priori che alcuni dati potrebbero non essere disponibili.

### Report online

Prima della firma elettronica, il report online era da considerarsi una semplice preview di quello ufficiale, e quindi senza valore legale, mentre al giorno d'oggi è diventata un alternativa al report cartaceo.

Eventuali notifiche di report online non devono contenere dati, devono solo svolgere una funzione di notifica.

## Struttura del Fascicolo Sanitario Elettronico

Il FSE è suddiviso in sezioni che contengono ognuna un certo tipo di dato:

- dati identificativi
- dati amministrativi
- documenti sanitari
- profilo sanitario sintetico
- note del cittadino

Il profilo sanitario sintetico sintetizza lo stato di salute del paziente fornendo le informazioni più importanti. Serve a promuovere la continuità di cura e risulta essere conciso, non clinicamente specifico e non indirizzato a qualcuno in particolare.

Le note del cittadino sono informazioni generali auto inserite dal cittadino, non sono verificate o certificate.

## Guidelines technologies

Esistono delle guidelines che si occupano di descrivere come immagazzinare, trovare, trasmettere, leggere e capire i dati evitando quindi di trasformare tutto in PDF.

## Modello

L'Infrastruttura tecnologica del FSE (InFSE) definisce le  specifiche tecniche per l'interscambio di documenti sanitari tra sistemi territoriali di Fascicolo Sanitario Elettronico garantendo disponibilità, affidabilità, sicurezza e privacy.

Questo prevede un modello architetturale Service Oriented Architecture in cui i nodi possono essere locali o regionali.

Il servizio è diviso in 3 parti fondamentali: business layer, component layer e connectivity layer.

### Component layer

Questo livello è sempre presente in tutti i nodi e al suo interno sono presenti più componenti:

- Interfaccia di accesso che permette l'accesso ai servizi dell'infrastruttura. Gestisce autenticazioni e l'accesso ai documenti.
- Gestore dei documenti che si occupa dello storage e del retrieval dei dati.
- Gestore delle politiche d'accesso che implementa la sicurezza e le policy d'accesso ai dati dell'infrastruttura grazie a meccanismi di autenticazione, identificazione e autorizzazioni
- Registro degli indici federati che mantiene i metadati dei documenti clinici. Ha il compito di rimanere sempre aggiornato
- Gestore degli eventi che invia notifiche degli eventi sanitari a chi di dovere tramite un meccanismo publish/subscribe. Gli eventi possono essere interni alla struttura federale o di interesse agli utenti dell'infrastruttura.

### Indexing

I dati sono immagazzinati con il formato HL7-CDA, poi vengono indicizzati tramite metadati. Più metadati sono disponibili, più una ricerca può essere precisa, grazie a query pesanti. Meno metadati permettono query più lineari ma risultati meno precisi in fase di ricerca.

## FSE e il cittadino

Non sono presenti specifiche indicazioni su come dare accesso al proprio FSE al cittadino, tuttavia le implementazioni correnti convengono sull'uso di sistemi web-based o applicazioni mobile. Il metodo di autenticazione preferito è lo SPID.

Si sta attualmente lavorando per aumentarne la percentuale di utilizzo in quanto per ora risulta poco usato.

### FSE 2.0

Il FSE 2.0 prevede di acquisire i dati in HL7 FHIR direttamente dai sistemi. Con questo sistema i dati potranno essere inviati tramite metadati presenti in PDF firmati così da rendere leggibile sia alla macchina che all'umano i dati presenti in un documento.

Si cerca di usare sistemi open source.
