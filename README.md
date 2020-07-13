# caesarcipher
A simple Caesar cipher just for fun

# How to use
Clone the repo and
```
chmod +x caesar.py
```
Then write something in a file and type:
```
./caesar.py enc <yourfile> 
```
If you want, you can save the ciphred message into a file:
```
./caesar.py enc <yourfile> > <anotherfile> 
```
So, if you want to decode such file, just:
```
./caesar.py dec <anotherfile> 
```

## Shift number
You can choose the shift number with just:
```
./caesar.py -s <n> enc <yourfile>
```

## Help
You can get help with:
```
./caesar.py -h
```
