# elasticsearch-tester - E
This is a repo to easily test the issues reported in elastic search and document the test case for others to view any time.

## Why did I do this ?
When ever some issue is reported in elastic search I used to go to
some rest client installed some where and test it to reproduce the issue.
And then come and record the result in the issue. 
Here only the result is documented and not the test procedure.So the test procedure vanishes.
I did not like it as I was not able to reuse the test procedure that even I did previously.

So wanted to come up with a easy solution for me to use. So I came up with the 'E' module.

This is a way to document the test procedure so that people 
can comment on whether the test case is right or wrong.
Also to maintain the history, so that when ever someone wants to reproduce the issue they can come and
run the script as

```
python <issue-id>.py
```

and get the results.

If you feel the test case is wrong you can change the code and give  a pull request saying why it is 
wrong .


The module has easy abstracted way to make get, post ,put calls.

Just do
```python
   from E import *
   get(url, data)
   post(url, data)
   put(url, data)
```
  
Thats it.

The data is a normal json.

### How did I handle the mapping between True , False in python and true , false in json ?

I have a 2 global variables in E 
```
   true
   false
```
which internally points to pythons boolean True and False.
So now you are free to have json as it is.
