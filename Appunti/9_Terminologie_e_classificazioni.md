# Terminologie e classificazioni

Gli standard come HL7 e CDA hanno bisogno di terminologia specifica per essere utilizzati in modo ottimale. Il problema risiede nel fatto che è possibile esprimere lo stesso concetto in forme testuali differenti che possono essere soggette a errori grammaticali o tipografici.

## Codici

Bisogna quindi formalizzare il linguaggio naturale per avere un terreno comune su cui aggregare eventi e situazioni. A questo scopo sono nate liste di termini standard che facilitano la comparazione, l'aggregazione e la trasmissione dei dati. Queste liste di vocaboli propongono un'aggregazione gerarchica dei termini/concetti sotto un unico termine all'interno di un vocabolario. 

I concetti possono essere codificati tramite astrazioni, che ne mantengono solo le parti più importanti, o tramite rappresentazioni, che mantengono una forma più ampia possibile. In entrambi i casi è possibile che si verifichi una perdita di informazioni dato che si tratta di semplificazioni.

### Problemi di codificazione

La qualità della codificazione dipende da molti fattori come la bravura del codificatore o la distanza temporale fra acquisizione e codifica. L'input del codice può essere libero, semi-strutturato o automatizzato.

## Origine delle classificazioni

Le classificazioni in ambito medico sono nate circa nel 1700 come metodo per avere dati statistici sulle malattie. Le classificazioni attuali (ICD, DRG, SNOMED(? non è classificazione)) sono utilizzate per la raccolta sistematica e l’analisi statistica dei dati sanitari.

## Terminologia delle terminologie

Lo standard ISO1087 è una terminologia delle terminologie che descrive:

- Oggetto: qualsiasi parte del mondo percepibile o concepibile  
- Nome: espressione linguistica che designa un oggetto  
- Concetto: unità di pensiero costituita da un'astrazione basata sulle proprietà comuni di un insieme di oggetti  
- Termine: espressione linguistica che designa un concetto in un linguaggio specialistico  
- Terminologia: insieme di termini che rappresentano il sistema di concetti di un determinato dominio  
- Nomenclatura: sistema di termini sviluppato secondo regole precise di denominazione  
- Dizionario: raccolta strutturata di unità lessicali con informazioni linguistiche su ciascuna di esse  
- Vocabolario: dizionario che contiene la terminologia di un dominio  

## Terminologia vs classificazione

Una terminologia è una lista di espressioni definite, possibilmente accompagnate da codici. Ogni concetto è unico e il vocabolario utilizzato è limitato. Le terminologie sono dette enumerative quando sono un elenco esaustivo di tutti i termini utilizzabili o combinatorie nel caso vengano usate combinazioni di termini per definire un concetto complesso.

Le classificazioni sono gerarchie che partono da un concetto astratto e giungono ad un concetto specifico tramite la specializzazione dei concetti. Le classi sono mutualmente esclusive e coprono tutto l'insieme delle possibilità, eventualmente con residuali.

Per riassumere: una terminologia medica è un vocabolario medico, mentre una classificazione medica associa ad una classe il contenuto di una cartella clinica. Copre in modo completo il dominio di interesse, eventualmente con classi residuali, è mutualmente esclusiva, dispone di criteri per discriminare situazioni di confine e deve avere il giusto livello di dettaglio. Utilizzando una classificazione è possibile specificare un concetto solo con le foglie dell'albero delle gerarchie.

Vi può comunque essere una interazione fra classificazioni e terminologie e l'introduzione di nuove terminologie può avvenire da zero o con riferimenti a alla letteratura.

## Classificazioni biomediche

Le classificazioni possono essere eseguite in base a punti di vista diversi detti assi. I più comuni in ambito medico sono i sintomi, le cause e la posizione. Le classificazioni biomediche si dividono in tre grandi famiglie: tassonomie, partonomie e classificazioni causali. Le tassonomie classificano i concetti secondo relazioni di specializzazione andando dal generale verso lo specifico, mentre le partonomie vengono usate per le descrizioni anatomiche e descrivono relazioni parte-tutto partendo da un'entità complessa per arrivare alle sue componenti, infine, le classificazioni causali, rappresentano relazioni di causa-effetto descrivendo catene causali tra eventi o condizioni. 

Le classificazioni moderne prevedono parentela multipla e i codici alfanumerici delle classi possono essere generati casualmente o in maniera ordinata.

### Ciclo di vita

Solitamente una classificazione biomedica viene creata da un gruppo chiuso, mentre la manutenzione e la transizione viene affidata ad un gruppo aperto.

#### Esempio: ICD

La versione ICD10 ha passato 8 conferenze di revisione dal 1990 in cui sono state coinvolte dalle 17 alle 58 nazioni alla volta. 

La diffusione di una nuova versione non è sempre semplice e possono passare anni da una versione all'altra, la versione ICD11 è stata ultimata nel 2019, ma non è ancora stata adottata nonostante renda più semplice la migrazione e la diffusione delle informazioni. Il collo di bottiglia resta quello dell'adozione umana.

ICD11 nasce in versione totalmente digitale per semplificarne la manutenzione anche grazie a tool online. Una modifica può essere proposta da chiunque e può essere rifiutata, rimandata o accettata dopo un processo di revisione.

La sua natura digital first permette l'esistenza di API a cui vi si può accedere online.
