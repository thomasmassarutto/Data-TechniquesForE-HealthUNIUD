# Note sul ragionamento medico

Bisogna discernere fra dato, informazione e conoscenza. La differenza fra le tre sta nel fatto che usando la conoscenza si è in grado di estrarre informazioni dai dati.

Il selezionamento dei dati è quindi una fase critica che deve essere ottimizzata per selezionare solo i dati necessari. Questo processo non è mai completo e dipende dalla situazione e dall'esperienza del medico.

## Ragionamento ipotetico-deduttivo

Un osservazione fatta sui dati genera un ipotesi. Un set di ipotesi è detta diagnosi differenziale ed è dettata sia dall'esperienza del medico, sia da un set minimo di informazioni. Queste informazioni vengono rinforzate o scartate in base alla selezione di altre osservazioni finché un'ipotesi raggiunge un adeguato livello di certezza.

Questo processo è knowledge-based in quanto necessita delle conoscenze riguardanti fatti o informazioni sul paziente, modelli diagnostici/terapeutici ed euristiche generate in base all'esperienza del medico.

Tutti i dati clinici hanno un certo livello di incertezza che deve essere espresso in termini di probabilità

Si divide in 3 fasi: valutazione iniziale, test diagnostici e osservazioni approfondite.

### Valutazione iniziale

Nel processo di diagnosi, un primo set di possibili malattie viene definito nella diagnosi differenziale, ognuno con un certo grado di probabilità. Questo primo set di ipotesi viene analizzato in base a valutazioni soggettive o euristiche del medico, rapppresentatività del paziente come soggetto tipico, presenza di eventi correlati nella storia clinica del paziente ed effettiva probabilità dell'ipotesi.

Le stime oggettive vengono basate su studi pregressi che prendono in considerazione il soggetto in base al gruppo di appartenenza o alla sua storia clinica. Possono comunque essere affette da bias.

#### Test diagnostici

Per confermare o confutare le ipotesi formulate nello step precedente vengono eseguiti uno o più test diagnostici. Questi sono spesso semplici da eseguire poco costosi e il loro risultato può essere espresso in forma binaria come negativo o positivo.

Anche questo tipo di test non è esente da errori ed ha una certa precisione: può ritornare falsi positivi o falsi negativi con una certa probabilità, quindi bisogna conoscere la sensibilita del test, ovvero la capacità di rilevare la corretta positività di pazienti malati espressa tramite la formula $\frac{TP}{TP+FN}$, e bisogna conoscere la specificità del test, ovvero la capacità di rilevare la corretta negatività in pazienti sani espressa tramite la formula $\frac{TN}{TN+FP}$.

Oltre a questi indici è necessario conoscere la prevalenza della malattia all'interno di una popolazione per poter tarare meglio i risultati del test. L'indice di accuratezza è infatti espresso in relazione al totale dei casi tramite la formula: $\frac{TP+TN}{\text{TOT CASI}}$.

### Osservazioni approfondite

Dopo una prima scrematura delle ipotesi si procede con test più approfonditi. Questi possono essere più invasivi, rischiosi e costosi rispetto ai primi, ma i loro risultati hanno comunque una soglia di incertezza e bisogna quindi scegliere i test adatti in base alla specificità e alla sensibilità. Per patologie severe si cerca di minimizzare i falsi negativi, mentre per le patologie lievi si cerca di minimizzare i falsi positivi.


## Qualità di un test

In fase di ricerca, per valutare la qualità di un test, questo viene confrontato con una procedura esistente che fa da ground truth. Questa procedura viene considerata il gold standard che però non è sempre applicabile.

Vari studi possono valutare un test e quando ne sono presenti abbastanza è possibile eseguire una meta analisi riguardanti tutti gli studi condotti.

## Decisione del trattamento

Per una malattia sono presenti diversi trattamenti, ma il risultato non è mai certo e dipende da molti fattori quali l'incertezza intrinseca dei test, la probabilità di sopravvivenza e le preferenza del paziente.

La sopravvivenza è usata come metrica per misurare la bontà di una terapia come tempo di vita del paziente dopo la terapia. Spesso si cerca di massimizzare questo indice, ma sono presenti altre variabili che possono influenzare la decisione come le scelte del paziente o i costi. Un indice più rappresentativo della bontà di una terapia potrebbe essere QUALY che rappresenta la qualità degli anni di vita del paziente dopo il ricovero.

## Comunicazione

Le informazioni devono essere comunicate in maniera efficiente sia al medico che al paziente in quanto la struttura del messaggio può influire sulle decisioni. Questo deve essere costruito facendo assunzioni sul tipo di conoscenza disponibile al ricevente.

Bisogna quindi generare due messaggi, uno per il medico e uno per il paziente tenendo conto di variabili come bias cognitivi, span di attenzione o percezione dei simboli.

## Ricerca clinica

La ricerca medica produce nuovi metodi per diagnosi, terapie e metodi per la valutazione delle prognosi. Il processo è comunque lungo e perché uno studio provochi cambiamenti a livello pratico possono volerci anni durante i quali lo studio viene letto, compreso e accettato dai medici.

Il paradigma utilizzato nella ricerca è quello della Evidence Based medicine che colleziona e formalizza i risultati delle ricerche mediche secondo il ciclo ipotetico deduttivo.

