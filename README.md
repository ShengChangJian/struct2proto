# struct2proto
A method to transform C++ struct to google procolbuffer.Please install toml module firstly like this: `pip install toml`.
Then exec follow cmd.

```shell
python3 ./StructToProtocol.py ./struct
```

example:
+ input struct file with ".struct" extend in struct fold.
+ config file like config.toml in struct fold.
+ output file is in proto folder.

support:
+ struct not inherit class with data member.
+ enum in struct.
+ enum const replace and calculate.
+ it can filter function, note.
+ it support vector, set, list, map etc.
+ it support config as follow: proto\_header, types, RPCs, option, const etc.

not support:
+ const var in struct or out
