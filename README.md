# madlibs
Flask App which simulates a madlib game!


## **Set Up **

```bash
$python3 -m venv venv
```

Start using your venv:

```bash
$source venv/bin/activate
(env) $

```

Install Flask:

```bash
(env) $pip3 install flask
...

```

Make a “requirements.txt” file in this directory with a listing of all the software needed for this project:
```
(env) $pip3 freeze > requirements.txt
```

### **Usage Instructions **
- Update stories inside the data folder
- prompts are found using regex and looking for the string inside curly brackets {}


### **Future update considerations**

1. Implement additional JS to allow users to create their own madlibs
2. clean up html and improve css