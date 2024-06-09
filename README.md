# pdmdtable

pdmdtable generates ASCII tables compatible with Pandoc's Markdown extensions. In particular, it generates [grid tables](https://pandoc.org/MANUAL.html#extension-grid_tables).

## Example Usage:

The following code should print the table below:

```python
from pdmdtable import build_table

columns = ["Name", "Race", "Class\n(Base)"]
rows = [
    ["Shadowheart", "Half-Elf\n(High Elf)", "Cleric"],
    ["Lae'zel", "Githyanki", "Fighter"],
    ["Astarion", "Elf\n(High Elf)", "Rogue"],
    ["Gale", "Human", "Wizard"],
    ["Wyll", "Human", "Warlock"],
    ["Karlach", "Tiefling\n(Zariel)", "Barbarian"],
]
table = build_table(columns, rows)
print(table)
```

```
+-------------+------------+-----------+
| Name        | Race       | Class     |
|             |            | (Base)    |
+=============+============+===========+
| Shadowheart | Half-Elf   | Cleric    |
|             | (High Elf) |           |
+-------------+------------+-----------+
| Lae'zel     | Githyanki  | Fighter   |
+-------------+------------+-----------+
| Astarion    | Elf        | Rogue     |
|             | (High Elf) |           |
+-------------+------------+-----------+
| Gale        | Human      | Wizard    |
+-------------+------------+-----------+
| Wyll        | Human      | Warlock   |
+-------------+------------+-----------+
| Karlach     | Tiefling   | Barbarian |
|             | (Zariel)   |           |
+-------------+------------+-----------+
```
