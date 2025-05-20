# Ontologie biomediche 

Le ontologie studiano le componenti aprioristiche della realtà. Sono un meccanismo di rappresentazione della conoscenza con fondamenti di logica che associano un termine ad un concetto standard. 

Una semantica mappa gli oggetti e i concetti da un modello al mondo reale.

OWL (Ontology Web Language) è lo standard per rappresentare le ontologie.

## Ontologie e semantica

Una semantica è implicita in quanto si basa sul consenso generale e informale in quanto è una descrizione testuale. Bisogna tener conto che la formalità intesa per gli umani è diversa rispetto a quella intesa per le macchine: per queste ultime c'è bisogno che sia eseguibile. Per usare una semantica c'è bisogno di un ontologia di base.

Le ontologie sono una rappresentazione esplicita di una concettualizzazione. Le basi di conoscenza sono le regole non incluse nelle ontologie e gli agenti sono il software in grado di usare ontologie e basi di conoscenza.

Il web semantico è un tipo di web in cui l'informazione ha un significato ben preciso. Viene implementato tramite OWL e RDF (Resource Description Framework)

## Ontologie formali

Nei documenti clinici c'è molto testo e sono presenti classificazioni e terminologie. Queste ultime sono numerose anche nello stesso dominio e non completamente sovrapponibili, per questo l'integrazione di dati fra fonti diverse risulta difficile.

Gli usi di un ontologia formale sono multipli: può essere usata per rappresentare conoscenza, termini, concetti e/o entità. Le ontologie mediche sono tutte ontologie formali.

## Ontologia vs rappresentazione conoscenza

Ogni espressione appartiene a uno dei quattro tipi di statements/asserzioni:

- universali: asserzioni sempre vere
- terminologiche: relative a termini linguistici
- assertive: fano riferimento a istanze
- contingenti: descrivono proprietà e relazioni riguardo ad una classe in generale. Potrebbero non essere vere per ogni istanza della classe, ma solo per un sottoinsieme

Un'espressione, il più delle volte, è scomponibile in triple composte da soggetto, verbo e oggetto, ma non sempre la singola espressione basta per capire di che si parla.

## Logica descrittiva

La logica descrittiva descrive logicamente le asserzioni riguardo alla conoscenza in modo che poi queste possano essere utilizzate da motori di inferenza logica.

In ambito medico alcune asserzioni sono complesse da tradurre: rischi, piani, disposizioni, ... possono risultare ostici dal punto di vista logico.

### Regole logica descrittiva

Un espressione disgiunta non implica esclusività fra le classi:

$$
A: x \lor r \lor z
$$ 

esprime mutua esclusività solo se specificato per tutte le permutazioni possibili, ovvero 

$$
A: x \land \neg(y \lor z) , \dots
$$

## Terminologie vs ontologia

Le ontologie non possono essere ambigue: il nome delle classi deve essere comprensibile e rappresentare entità in modo non ambiguo. Questo comporta che le etichette a loro assegnate non sempre sono molto naturali in quanto si predilige la precisione.

Nel linguaggio naturale sono presenti sinonimi e preferred terms.

## Descrizione delle istanze di una classe

Descrivere le istanze non è il caso d'uso per cui sono nate le ontologie, ma è comunque possibile esprimere un istanza in modo ontologicamente coerente. Questo risulta utile nelle ontologie biomediche in cui un istanza può essere un'osservazione su di un paziente.

Spesso, però, la conoscenza interessante e utile è poco ontologica e deve essere espressa con altri metodi formali o meno: il concetto di probabilità è un aspetto utile su cui avere informazioni, ma non è facilmente esprimibile con le ontologie. Ci sono anche alcuni casi speciali in cui la conoscenza riguardo ad un aspetto non è universalmente ontologica.

## Ontologie superiori

Le ontologie superiori esprimono concetti molto generici. Le principali sono SUMO, BFO e DOLCE. Rispetto alle ontologie generiche descrivono in modo logico il mondo e fanno da ponte fra le varie ontologie specifiche.

### SUMO

SUMO (Suggested Upper Merged Ontology) è un ontologia prodotta dalla IEEE che contiene 20 mila concetti diversi ed è stata mappata su Wordnet che è un vocabolario formale. Può essere connessa a ontologie di medio livello.

Wordnet contiene circa 15 mila termini con le relative connessioni fra sinonimi, atonimi e definizioni. Serve a discriminare la semantica della parola.

### BFO e DOLCE

BFO e DOLCE sono delle ontologie upper level formali che distinguono oggetti e processi.

## Ontologie mediche

Le ontologie biomediche sono nate per descrivere esperimenti e risultati con lo scopo di facilitare lo scambio di informazioni in maniera precisa. Trattano anche gli aspetti clini, ma questi sono espressi in maniera meno formale.

Alcuni dei principali attori sono OBO Foundry, Gene Ontology, Biotop, FMA e Bioportal, anche se quest'ultima è meno formale.

OBO Foundry deriva das BFO e non è ancora completa, ma copre diversi livelli di granularità, partendo da entità complesse come organi, passando per cellule e componenti cellulari, fino a molecole.

Gene Ontology è un ontologia che produce codici usabili per annotare articoli scientifici e viene utilizzata per reperire in maiera più precisa le informazioni.

Biotop è un ontologia biomedica fondata su BFO di medio/alto livello.

FMA (Foundational Model of Anatomy) modella simbolicamente il corpo umano grazie a 75 mila classi, 120 mila termini e più di 2 milioni di asserzioni. Questa può essere considerata anche una partonomia e una tassonomia delle parti del corpo.