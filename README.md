### Wuwuzela

## How to

### Generate python parser files

Run

```
antlr4 -Dlanguage=Python3 Wuwuzela_Grammar.g4
```

inside `/grammar`, you can use `py3antlr4/bin/antlr-4.9.2-complete.jar` from this repo.

```
java -jar ../py3antlr4/bin/antlr-4.9.2-complete.jar -Dlanguage=Python3 Wuwuzela_Grammar.g4
```

Make sure generated files are inside `/grammar` directory

### Running program

`python script.py input.wuw`

### Display parse tree from input

`python tree.py input.wuw`

## Development

### Structure

- `script.py` - collects generated files, builds a tree, starts a listener
- `WuwuzelaListener.py` - listens for parse trees enteres and exits
- `statements` - defines classes that receive tree context in constructor and execute accordingly
- `types` - defines base types used in language, receive their context in constructor
- `expressions` - defines expressions, receive context in contructor, parse
  it accordingly, save result in value, e.g. (`LogicalExpression(ctx).value` to
  get boolean result of parsed context)
- `VariableTracker.py` - utility class that stores variables based on name, and value of `Variable` (or extending children)

### Misc

[Antlr python book](https://github.com/jszheng/py3antlr4book) reference
