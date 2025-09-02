# Ontologie biomediche 

Le ontologie studiano le componenti aprioristiche della realtà. Sono un meccanismo di rappresentazione della conoscenza con fondamenti di logica che associano un termine ad un concetto standard. 

Una semantica mappa gli oggetti e i concetti da un modello al mondo reale.

OWL (Ontology Web Language) è lo standard per rappresentare le ontologie.

## Ontologie e semantica

Una semantica è implicita in quanto si basa sul consenso generale e informale ed è una descrizione testuale. Bisogna tener conto che la formalità intesa per gli umani è diversa rispetto a quella intesa per le macchine: per queste ultime c'è bisogno che sia eseguibile. Per usare una semantica c'è bisogno di un ontologia di base.

Le ontologie sono una rappresentazione esplicita di una concettualizzazione. Le basi di conoscenza sono le regole non incluse nelle ontologie e gli agenti sono il software in grado di usare ontologie e basi di conoscenza.

Il web semantico è un tipo di web in cui l'informazione ha un significato ben preciso. Viene implementato tramite OWL e RDF (Resource Description Framework).

## Ontologie formali

Nei documenti clinici è presente molto testo scritto che rende complesso lo sviluppo di vocabolari controllati. Risulta necessario introdurre classificazioni e terminologie per stabilire un linguaggio comune. Queste ultime sono numerose anche nello stesso dominio e non completamente sovrapponibili, per questo l'integrazione di dati fra fonti diverse risulta difficile. L'introduzione di questi nuovi meccanismi comporta una maggiore difficoltà nell’integrare i dati rispetto al testo libero.

Per chiarire termini altrimenti ambigui vengono introdotte le ontologie formali che hanno il compito di specificare il significato dei termini e di rendere chiaro di cosa si parlando. Gli usi di un ontologia formale sono multipli: può essere usata per rappresentare conoscenza, termini, concetti e/o entità. Le ontologie mediche sono tutte ontologie formali.

## Ontologia vs rappresentazione conoscenza

Ogni espressione appartiene a uno dei quattro tipi di statements/asserzioni:

- universali: asserzioni sempre vere
- terminologiche: relative a termini linguistici
- assertive: fanno riferimento a istanze
- contingenti: descrivono proprietà e relazioni riguardo ad una classe in generale. Potrebbero non essere vere per ogni istanza della classe, ma solo per un sottoinsieme

Un'espressione, il più delle volte, è scomponibile in triple composte da soggetto, verbo e oggetto, ma non sempre la singola espressione basta per capire di che si parla.

## Logica descrittiva

La logica descrittiva è un linguaggio formale che permette di descrivere logicamente le asserzioni riguardo alla conoscenza, in modo che poi queste possano essere utilizzate da motori di inferenza logica. Questo strumento è utilizzato per descrivere classi (es. tipi di malattie o parassiti) e non è altrettanto efficace nel descrivere istanze singole.

In ambito medico alcune asserzioni sono complesse da tradurre (rischi, piani, disposizioni, ...) e possono risultare ostiche da rendere dal punto di vista logico. Ad esempio un espressione disgiunta non implica esclusività fra le classi:

$$
A: x \lor r \lor z
$$ 

$A$ esprime mutua esclusività solo se specificato per tutte le permutazioni possibili, ovvero 

$$
A: x \land \neg(y \lor z) , \dots
$$

## Terminologie vs ontologia

Le ontologie, rispetto alle terminologie, non possono essere ambigue: il nome delle classi deve essere chiaro e rappresentare entità in modo non ambiguo. Questo comporta che le etichette assegnate alle classi non sempre risultino particolarmente naturali, poiché si privilegia la precisione nella loro definizione per evitare interpretazioni errate.

Nel linguaggio naturale sono presenti sinonimi e preferred terms che possono complicare la creazione di ontologie. I sinonimi possono generare confusione, mentre i termini preferiti aiutano a stabilire una terminologia standardizzata.

## Descrizione delle istanze di una classe

Descrivere le istanze non è il caso d'uso per cui sono nate le ontologie, ma è comunque possibile esprimere un'istanza in modo ontologicamente coerente. Questo risulta utile nelle ontologie biomediche in cui un'istanza può essere un'osservazione su di un paziente.

Spesso, però, la conoscenza interessante e/o utile è poco ontologica e per essere espressa richiede metodi meno formali. Il concetto di probabilità è un aspetto utile su cui avere informazioni, ma non è facilmente esprimibile con le ontologie, inoltre ci sono anche alcuni casi speciali in cui la conoscenza riguardo ad un aspetto non è universalmente ontologica.

## Ontologie superiori

Le ontologie superiori esprimono concetti molto generici. Le principali sono SUMO, BFO e DOLCE. Rispetto alle ontologie generiche descrivono in modo logico il mondo e fanno da ponte fra le varie ontologie specifiche.

SUMO (Suggested Upper Merged Ontology) è un ontologia prodotta dalla IEEE che contiene 20 mila concetti diversi, è stata mappata su Wordnet e può essere connessa a ontologie di medio livello. Wordnet è un vocabolario formale che contiene circa 15 mila termini con le relative connessioni fra sinonimi, atonimi e definizioni. Serve a discriminare la semantica della parola.

BFO e DOLCE sono delle ontologie upper level formali che distinguono oggetti e processi.

## Ontologie mediche

Le ontologie biomediche sono nate per descrivere esperimenti e risultati con lo scopo di facilitare lo scambio di informazioni in maniera precisa. Possono fornire supporto in 2 aree di primaria importanza nel campo della biomedicina: interoperabilità e supporto decisionale. Trattano anche gli aspetti clinici, ma questi sono espressi in maniera meno formale.

Alcuni dei principali attori sono OBO Foundry, Gene Ontology, Biotop, FMA e Bioportal, anche se quest'ultima è meno formale.

OBO Foundry deriva da BFO e non è ancora completa, ma copre diversi livelli di granularità, partendo da entità complesse come organi, passando per cellule e componenti cellulari, fino ad arrivare alle molecole.

Gene Ontology è un ontologia che produce codici usabili per annotare articoli scientifici e viene utilizzata per reperire in maniera più precisa le informazioni.

Biotop è un ontologia biomedica fondata su BFO di medio/alto livello.

FMA (Foundational Model of Anatomy) modella simbolicamente il corpo umano grazie a 75 mila classi, 120 mila termini e più di 2 milioni di asserzioni. Questa può essere considerata anche una partonomia e una tassonomia delle parti del corpo. Questa ontologia è divisa in vari componenti.

La tassonomia anatomica (AT) è la classificazione delle entità anatomiche in base alle caratteristiche condivise.
(Es.: organi raggruppati secondo la forma, funzione, tessuto, ecc.)
L'astrazione strutturale anatomica (ASA) rappresenta le relazioni di tipo parte-tutto e le relazioni spaziali tra le entità presenti nella tassonomia anatomica (AT). (Es.: “il cuore fa parte del torace”, “il rene è laterale rispetto alla colonna vertebrale”). L'astrazione delle trasformazioni anatomiche (ATA) descrive le trasformazioni morfologiche (cioè i cambiamenti di forma/struttura) delle entità anatomiche tra lo sviluppo prenatale e la vita postnatale. (Es.: come si sviluppa il cervello dal feto all’età adulta), la meta conoscenza (MK) include i principi, le regole e le definizioni con cui vengono rappresentate le classi e le relazioni nelle componenti sopra elencate. (Serve per dare coerenza e formalismo all’intera ontologia anatomica.)
