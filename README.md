Messenger Hook
==============

Description
-----------

This is a basic implementation of a facebook messenger Hook.
It's working with falcon but should be easily modify to work with Flask or Django.

Install
-------

You can run `pip install messenger_hook` to install it.

Build a ping application
------------------------

```python
import falcon
from messenger_hook import FalconMessenger

app = Falcon()
hook = FalconMessenger('verify_key', 'your_token')
app.add_route('/hook/', hook)
```

You can launch it with gunicorn or uwsgi


Transform message
-----------------

```python
import falcon
from messenger_hook import FalconMessenger

class MyMessenger(FalconMessenger):
    def transform_message(self, message):
        return 'You sent {}'.format(message)

app = Falcon()
hook = FalconMessenger('verify_key', 'your_token')
app.add_route('/hook/', hook)
```
