# Elasticsearch Tester - ET
This is a repo to easily test the issues reported in elastic search and document the test case for others to view any time.

## Why did I do this ?
When ever some issue is reported in elastic search I used to go to
some rest client installed some where and test it to reproduce the issue.
And then come and record the result in the issue. 
Here only the result is documented and not the test procedure.So the test procedure vanishes.
I did not like it as I was not able to reuse the test procedure that even I did previously.

So wanted to come up with a easy solution for me to use. So I came up with the 'ET' module.

This is a way to document the test procedure so that people 
can comment on whether the test case is right or wrong.
Also to maintain the history, so that when ever someone wants to reproduce the issue they can come and clone 
the repo as

```
  git clone https://github.com/HarishAtGitHub/elasticsearch-tester
 ```

and

run the script as

```
python <issue-id>.py
```

and get the results.

If you feel the test case is wrong you can change the code and give  a pull request saying why it is 
wrong .

If you don't find the {{ issue-id }}.py in this repo , but you want it, please create it and commit it in 
this repo.

### Ok.. How to write the {{ issue-id }}.py ?
The module 'ET' has easy abstracted way to make get, post ,put calls.

Just do
```python
   from ET import *
   get(url, data)
   post(url, data)
   put(url, data)
```
  
Thats it. In general it is callname(url, data). It is that simple.

The data is a normal json.

### How did I handle the mapping between True , False in python and true , false in json ?

I have a 2 global variables in ET module 
```
   true
   false
```
which internally points to pythons boolean True and False.
So now you are free to have json as it is.

### Do I need to know python ? If so, Can I have a sample file and start writing the script  ?
To be frank you need not know any python, because it is abstracted so that no one
needs to know the language. It is just functions + json. It is just like psuedo-code.


Here is the sample file :
<a href="https://github.com/HarishAtGitHub/elasticsearch-tester/blob/master/12523.py">12523.py</a>

If in case you are stuck in a place while writing issue-id.py , where you are forced to know python, please log an issue. We shall discuss and fix it to make it easy(may be by abstracting it).


### Requirements to use it
1. install python 
2. sudo pip install requests  (If you don't have pip pls refer:https://pip.pypa.io/en/stable/installing.html)

If you still have trouble installing it . Please contact me.
