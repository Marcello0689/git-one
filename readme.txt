Qui puoi trovare un file test.py che permette di scrivere valori randomici su una database SQLite_Python.db su cui hai creato tre tabelle in questo modo:

CREATE TABLE `table1` (
	`id`	integer,
	`valore`	decimal(4,8),
	PRIMARY KEY(id)
);

Ve ne sono tre e lo script le riempie con diecimila record tramite un cursore per sqlite3.

Invece sul file per Jupyter troverai una lavorazione tale per cui viene preso il database e tramite il cursore messi i valori in una lista (ricorda che il cursore restituisce un tuple per riga).

Successivamente uso i valori della lista per realizzare un istogramma.

