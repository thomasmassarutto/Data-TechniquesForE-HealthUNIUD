# Classificazioni OMS

L'OMS ha delle classificazioni ufficiali che vengono usate a fini statistici. ICD viene usata per tenere traccia delle malattie, ICFDH per le disabilità, ICHI per gli interventi. Da queste spesso derivano specializzazioni come ICDO per l'uso clinico.

## ICD

ICD (International Classification of Diseases) è la classificazione più usata per le malattie e i suoi casi d'uso riguardano i certificati di morte a fini statistici e la scheda di dimissione ospedaliera ai fini di rimborso. Durante gli anni ha avuto varie versioni con le quali è stata ampliata:

- ICD1: 1900 $\rightarrow$ 179 items
- ICD6: 1948 $\rightarrow$ 954 items
- ICD9: 1975 $\rightarrow$ 1164 items

La variante nazionale USA ICD9-CM-USA ha 8179 items.

### ICD9-CM

La versione ICD9-CM è la variante statunitense che descrive i ricoveri ospedalieri, diagnosi e procedure dal punto di vista assicurativo/finanziario. Nel 2017 è stata ritirata, ma resta ancora utilizzata.

Consta di 17 capitoli, che traducono in codici diagnosi, problemi di salute, procedure mediche, ...

I codici sono caratteri alfanumerici. Le diagnosi sono definite con 3/5 caratteri, hanno una gerarchia e usano il punto come delimitatore. Le procedure sono definite da 2/4 caratteri.

La distribuzione avviene tramite manuali su carta compresi di indice alfabetico.

#### Capitoli

I capitoli organizzano le diagnosi in base alla sede (sistema respiratorio, endocrino, ...), ma non mancano eccezioni: i primi capitoli sono ordinati per causa dalla patologia e altri ancora trattano alcune patologie in base allo stato del paziente (gravidanza, ...).

Sono presenti capitoli speciali per condizioni esterne, come le ferite o le ustioni, e anche capitoli per sintomi e segni.

#### Indice sistematico/alfabetico

L'indice è indispensabile per organizzare la classificazione. Viene strutturato in:

- capitoli che coprono macro aree
- blocchi che raggruppano condizioni simili usando 3 caratteri
- categorie che dividono il blocco aggiungendo un quarto carattere dopo un punto
- sotto categorie
- sotto classificazioni che aggiungono un altro carattere

Per codificare vengono usate solo le foglie, questo è possibile anche grazie all'esistenza di classi residuali.

### ICD10

ICD10 conta circa 15 mila categorie e le malattie sono simili a quelle di ICD9. Anche questa classificazione è stata distribuita in maniera cartacea in tre volumi.

Il primo volume è l'indice sistematico che contiene una gerarchia con le descrizioni della patologia. Comprende eventuali esclusioni.

Il terzo volume è l'indice alfabetico che codifica i termini utilizzati dal codificatore. Progettato per l'uso umano può essere ambiguo e molto complesso, per questo è quasi impossibile da automatizzare, è poco informatizzabile ed è stato praticamente abbandonato.

Di questa versione esistono varianti nazionali, in Italia esiste un ICD10-IT, ma non è stato completato, per questo si usa la versione ICD9 o per i certificati di morte ICD10.

### ICD11

ICD11 è presente dal 2019, con adozione dal 2022, ma non viene ancora usato. Similmente a SNOMED cerca di ampliare l'uso delle classificazioni mediche per l'uso all'interno di sistemi informativi e viene mantenuto tramite crowdsourcing di esperti.

La sua architettura è pesata per il digital first e prevede una struttura a due livelli: foundation e linearization. Si tratta anche di una ontologia che rappresenta formalmente il dominio della malattia. Ha una struttura ad albero che permette la genitorialità multipla. Quando non c'è bisogno di dettaglio viene creata una shoreline che divide la classificazione dai narrower terms.

Nella foundation non sono presenti categorie residuali, mentre nelle linearization queste vengono generate automaticamente così da garantire l’esaustività della classificazione.

Gli identificatori univoci delle foundation e delle linearization sono URI.

#### Foundation vs linearization

La foundation è la base concettuale di ICD11 che contiene tutti i concetti medici organizzati in maniera ontologica. I termini sono 80 mila e prevedono la genitorialità multipla, non è quindi una classificazione. Non è ancora completa.

La linearization è una vista sulla foundation che genera una classificazione monogenitoriale, con mutua esclusione con copertura esaustiva grazie anche ai residuali.

Le due parti sono separate da una shoreline.

Sono presenti varie linearization, ma tutte devono essere interoperabili.

#### Codici di estensione

I codici di estensione usati per aggiungere dettaglio a un codice principale. Possono essere di pre-coordinazione di post-coordinazione. I codici pre-coordinati sono singoli e vengono usati peri casi più comuni, mentre quelli post-coordinati possono venire concatenati tramite i caratteri '/' per la clusterizzazione e '&' per l'estensione.

#### Piattaforma

La natura digital first di ICD11 mette a disposizione una piattaforma ufficiale online con delle API che permettono l'accesso diretto o la ricerca di dati. Queste sono in formato REST, gratuite dietro registrazione e ben documentate

Esiste un Embedded Classification Tool che offre delle librerie per applicazioni web che garantiscono l'integrazione nei sistemi informativi aziendali e una piattaforma di manutenzione.

Al developer sono quindi forniti molti strumenti per interfacciarsi con IDC11, è anche permesso il deploy locale tramite Docker o servizi Windows e Linux. Le classificazioni rimangono comunque immutabili in quanto il codice non è open source.

## ICHI

ICHI (International Classification of Health Interventions) si occupa degli interventi e delle procedure sanitarie comprese campagne di sanità e visite.

Ha una struttura a tre assi in cui vengono specificati il target (l'entità su cui agisce l'intervento), l'azione (l'azione eseguita sul target) e i mezzi (i mezzi usati durante l'azione). Un codice ICHI è quindi strutturato in 3 parti in base alle informazioni contenute negli assi, ma sono comunque possibili estensioni.

## ICFDH

ICFDH (International Classification of Functioning, Disability and Health) si occupa della classificazione delle disabilità.

Una condizione di salute può causare dei problemi al corpo umano, una disabilità, che in base a fattori contestuali o ambientali può a sua volta causare delle limitazioni alle attività della persona. Vengono quindi presi in considerazione i fattori ambientali quali famiglia, scale, farmaci, ... per classificare barriere e facilitatori. Il suo focus è quindi la capacità di produrre una performance da parte di una persona in determinate condizioni ambientali.

Non viene utilizzata spesso, include ICHI e vi sono tentativi di armonizzazione.