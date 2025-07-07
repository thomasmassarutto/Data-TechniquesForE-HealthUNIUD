# Protocolli e linee guida

I protocolli e le linee guida danno indicazioni comportamentali su cosa fare in determinate situazioni.

In particolare i protocolli sono un insieme di istruzioni che descrivono la maniera ideale di svolgere un compito. Nella pratica il modo migliore non esiste e queste istruzioni sono utilizzate per diagnosticare e curare una certa categoria di malattie in modo standard. Aiutano ad operare in maniera uniforme e tendenzialmente corretta.

Le linee guida sono meno formali rispetto ai protocolli. Questi ultimi necessitano di criteri di ingresso per determinare se è possibile applicarli. Di un protocollo possono nascere diverse varianti che hanno lo scopo di adattarsi a casi particolari come: altre malattie, condizioni particolari, indisponibilità di procedure mediche o fattori esterni in generale.

Un protocollo deve quindi avere dei criteri di ingresso in grado di descrivere il contesto in cui può essere utilizzato e delle azioni da intraprendere che possono essere espresse tramite flowchart o regole logiche. Quando un protocollo è particolarmente complesso può essere spezzato in sotto-protocolli.

Infine è necessario che un protocollo sia:

- utile: va meglio di uno standard
- progettabile: gli eventi non devono essere troppo variabili
- usabile: usarlo deve essere conveniente

## Percorsi di cura

I percorsi di cura prevedono ch ela cura del paziente venga divisa in giorni teorici in base allo stato del paziente. Si crea così una macchina a stati in cui ogni giorno ha un diagramma di flusso che rende la transazione di un paziente da uno stato all'altro più facile.

## Protocolli computerizzati

I protocolli computerizzati possono essere attivi o passivi. Quelli passivi possono essere computer based, ma non interagiscono con i dati contenuti nei sistemi informativi. I protocolli attivi sono sistemi più complessi che prevedono un supporto attivo alle decisioni del personale clinico anche in base a interazioni con le cartelle cliniche dei pazienti. Questi protocolli permettono anche la comunicazione fra la cartella clinica e i macchinari.

## Linee guida

Le linee guida sono delle raccomandazioni a fare o non fare qualcosa. Vengono create in base alla forza dell'evidenza quando una buona quantità di studi supportano una raccomandazione.

## Costruzione e manutenzione di un protocollo

I protocolli sono basati sulla evidence based medicine e sull'analisi scientifica. Sono scritti per essere interpretati da umani, ma, con l'avvento della medicina informatica, devono essere riportati in forma informatica.

L'integrazione con la cartella clinica è fondamentale e permette ad un monitor di eventi di osservare le operazioni eseguite sulle workstation cliniche. In questo modo, quando i dati vengono inseriti in qualche repository, è possibile controllare se questi rappresentano un punto di ingresso di un protocollo. Quando questo accade, il dato viene passato ad un motore di interpretazione di protocolli che fa partire un trigger per il fetch dei dati utili.

Questo iter viene notificato alla workstation, tramite una notifica che fa da supporto alla decisione, e a chiunque sia interessato. Questo accade solo se il protocollo è attivo.

La principale differenza fra un protocollo passivo e uno attivo sta nel fatto che il primo è leggibile, mentre il secondo è anche computabile e necessita quindi di terminazioni, classificazioni e ontologie per essere implementato.

Ogni protocollo deve essere decritto in maniera formale tramite strutture di controllo. Queste possono permettere il parallelismo e l'annidamento di varie fasi.

### Metodologie

Per esprimere le linee guida e i protocolli sono disponibili vari modelli. Ognuna di queste metodologie fornisce le primitive di rappresentazione di ciò che compare in un protocollo, i meccanismi di aggregazione e il modello dei dati dei pazienti.

Un protocollo generale ha bisogno di modellare quali siano i suoi input.

### Primitive di rappresentazione

Le primitive di rappresentazione sono unità fondamentali che descrivono i concetti clinici all’interno di protocolli e linee guida. Permettendo la modellazione formale, e quindi computabile, dei processi decisionali previsti.

- Azioni: azioni cliniche, amministrative, collezione dati o attesa.
- Decisioni: decisioni automatiche o che necessitano l'intervento umano
- Stati: 
  - del paziente: un paziente virtuale è rappresentato con uno stato all'interno di diversi scenari all'interno del protocollo.
  - dell'esecuzione: un protocollo può essere visto come una macchina a stati finiti.

### Dati dei pazienti

La menzione dei dati del paziente deve essere indipendente dal singolo caso. Per fare questo bisogna adottare standard di codifica e modelli per rappresentare un paziente standard.

### Sintassi Arden

Arden è un linguaggio per protocolli eseguibili dal calcolatore. La conoscenza medica è organizzata in moduli logici che servono per prendere una decisione clinica. 

Ogni modulo logico è composto da:

- contesto: contesto che evoca il modulo logico grazie a dei criteri di ingresso
- logica: criteri e algoritmi che implementano la logica del protocollo. Hanno esito vero o falso
- azione: in base al risultato del modulo logico, eseguono un azione
- data slot: fornisce integrazione fra il sistema di gestione protocolli e la cartella clinica

Questa sintassi è limitata dal fatto che descrive solo le azioni e i passi logici senza fornire né un modello dati del paziente, né una terminologia standard.

### GEM

GEM (Guideline Elements Model) è un modello XML sviluppato per rappresentare linee guida cliniche in modo strutturato e interoperabile. Lo schema che permette di rappresentare le informazioni è molto ampio, prevede nesting e il modello permette la parallelizzazione.

## Process modelling

I protocolli e le linee guida sono la traduzione in termini concreti della conoscenza scientifica, ma non tutte le azioni mediche fanno parte di questo insieme: vi sono vincoli clinici/scientifici, aspetti organizzativi e locali da tenere conto.

La descrizione di un processo medico aiuta a risolvere questi problemi tramite process modelling e process mining.

### Business process modelling 

Il business process modelling rappresenta e descrive i processi di un azienda con l'obiettivo di ottimizzarli. Il process modelling è utile in quanto produce documentazione che facilita il lavoro al personale e funge da base per la descrizione dei processi in fase di certificazione. Altri aspetti importanti sono che permette di avere una sicurezza maggiore, aiuta in fase di automatizzazione e migliora la comunicazione fra stakeholders.

L'output di questo processo sono i diagrammi (flowchart, state transition, communication, ...). Questi hanno il compito di descrivere i processi interni ad un organizzazione sanitario nel modo più preciso possibile: ogni organizzazione ha dei requisiti che utilizza per fornire servizi concreti.
