# Cartella medica elettronica

La cartella medica di un paziente contiene tutti gli episodi medici relativi ad esso nel sistema sanitario. Si sta cercando di renderla elettronica per migliorarne l'uso. Può essere organizzata in base al tempo (time-oriented) o in base al problema (problem-oriented), ma sono presenti anche casi ibridi.

## Funzioni

Le funzioni di una cartella clinica sono molteplici:  

- metodo di comunicazione fra il personale medico 
- modalità di accesso ai dati
- spazio di lavoro condiviso per la comunicazione, anche informale, per il team medico che ha in cura il paziente
- crea una visione globale del paziente tramite note e narrative raccolte da più punti di vista
- archivio permanente che contiene tutti i dati riguardanti la storia clinica di una persona che può anche essere usata a fini di ricerca

## Registro cartaceo vs registro elettronico

Il registro cartaceo spesso è organizzato in maniera time-oriented, anche se alcuni dipartimenti hanno la loro sotto sezione. Permette un accesso alla volta, è ingombrante, la ricerca risulta difficile e il supporto cartaceo risulta fragile.

Il registro elettronico sostituisce quello cartaceo migliorandone, o in alcuni casi ampliandone, le funzioni. Necessita di un alto grado di formalizzazione e di meccanismi avanzati per garantire la sicurezza dei dati. Non può essere una repository di PDF in quanto i dati devono poter essere analizzati e processati. Per fare ciò sono codificati in base ad uno standard.

Una cartella medica tradizionale è detta passiva e funge da semplice record per gli eventi clinici di un paziente, mentre una cartella medica elettronica può essere attiva, ovvero, se sono disponibili abbastanza dati, può essere usata come strumento in grado di integrare le decisioni mediche tramite suggerimenti.

## Componenti funzionali

Una cartella clinica elettronica può inglobare diversi componenti funzionali non presenti nella sua controparte cartacea.

- Fornire una visuale integrale di tutti i dati del paziente aggregando varie fonti di provenienza dei dati in modo da presentarle in modo corretto e informativo.

- Fornire supporto alla decisione clinica mostrando dati rilevanti ad un certo caso come protocolli da seguire, test, trattamenti, statistiche, ... Il suo scopo deve comunque limitarsi al supporto e non alla sostituzione del medico.

- Gestire in automatico le prescrizioni di esami, medicinali o visite specialistiche comunicando automaticamente fra vari istituti. Un meccanismo del genere permette di cambiare dinamicamente le regole in base al caso specifico e alle nuove scoperte mediche.

- Accesso a fonti di conoscenza come la bibliografia necessaria riguardo ad un caso medico.

- Metodo di comunicazione per facilitare lo scambio di informazioni fra istituti medici e paziente.

## Features e problemi

L'inserimento e l'acquisizione dei dati sono i punti critici di un sistema clinico elettronico. 

Per quanto riguarda l'inserimento, questo può essere macchinoso e causare un aumento del carico di lavoro, inoltre non sempre risulta chiaro chi ha il compito e la responsabilità di aggiornarlo. 

Per quanto riguarda l'acquisizione dei dati, la criticità principale risiede nell'interoperabilità di questi fra le varie figure o le varie organizzazioni quali ospedali, medici e laboratori.

### Input dati

L'input dei dati all'interno di un sistema informativo è prono agli errori, bisogna quindi attuare delle politiche di error detection nonostante possano non essere sicure al 100%. Tra i controlli più comuni ci sono quelli di range, che verificano se i valori rientrano in un intervallo predefinito, i controlli di pattern, che assicurano che i dati seguano un formato specifico, i controlli grammaticali, che esaminano la correttezza linguistica, i controlli di coerenza, che confrontano i valori calcolati con i dati di base, i controlli di consistenza, che verificano la congruenza tra diversi set di dati, e i controlli per variazioni improvvise, che identificano cambiamenti anomali nei dati.

L'inserimento dei dati richiede un notevole investimento di tempo. Quando questo è effettuato da un medico, risulterà affidabile, ma costoso. Nel caso venga eseguita da parte di segretari, l'operazione è meno costosa, ma i dati corrono il rischio di essere meno affidabili in quanto la catena di comunicazione si allunga e diventa più prona agli errori.

### Data visualization

Una cartella clinica elettronica implementa la visualizzazione di dati in maniera dinamica ed interattiva.

### Ricerca e prevenzione

Una cartella clinica elettronica permette un migliore monitoraggio del paziente.

### Problemi per gli sviluppatori

Dal punto di vista di uno sviluppatore i problemi principali riguardati la costruzione di un sistema del genere derivano dagli standard da rispettare, dalla privacy, dal rapporto costi benefici e dalle interfacce da rispettare.
