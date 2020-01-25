import requests

class Marknife():

    def __init__(self, user=None, key=None):
        self.token      = user;
        self.user       = user;
        self.key        = key;
        self.method     = 'GET';
        self.version    = 1;
        self.authtype   ='Bearer';
        super(Marknife, self).__init__()

    def SayHello(self):
        return 'Hello World!'

    def Help(self, callback=None, params=None):
        self.Read('/help', callback, params);
    def Me(self, callback=None, params=None):
        self.Read('/me', callback, params);
    def Contacts(self, callback=None, params=None):
        self.Read('/contacts', callback, params);
    def Messages(self, callback=None, params=None):
        self.Read('/messages', callback, params);
    def Forms(self, callback=None, params=None):
        self.Read('/forms', callback, params);
    def Books(self, callback=None, params=None):
        self.Read('/books', callback, params);
    def Qrs(self, callback=None, params=None):
        self.Read('/qrs', callback, params);
    def Events(self, callback=None, params=None):
        self.Read('/events', callback, params);
    def Resources(self, callback=None, params=None):
        self.Read('/resources', callback, params);

    def Read(self, path=None, callback=None, params=None):
        self.method = 'GET';
        self.Call(path, callback, params);
    def Save(self, path=None, callback=None, params=None):
        self.method = 'POST';
        self.Call(path, callback, params);
    def Delete(self, path=None, callback=None, params=None):
        self.method = 'DELETE';
        self.Call(path, callback, params);
    def Update(self, path=None, callback=None, params=None):
        self.method = 'PUT';
        self.Call(path, callback, params);
    def Patch(self, path=None, callback=None, params=None):
        self.method = 'PATCH';
        self.Call(path, callback, params);
    def Purge(self, path=None, callback=None, params=None):
        self.method = 'PURGE';
        self.Call(path, callback, params);
    def Call(self, path=None, callback=None, params=None):
        if self.token == None:
            return callback('Marknife Invalid Token');
        if path == None:
            return callback('Invalid Path');

        bearer = self.authtype + ' ' + self.token;

        headers = {
            'user-agent': 'Marknife Python'
        }

        if len(bearer) > 0:
            headers['Authorization'] = bearer;

        if params:
            params = {params : params};
            headers['Content-Type'] = 'application/json';
            #headers['Content-Length'] = Buffer.byteLength(JSON.stringify(params));

        print(path)

        payload = {
            'some': 'data'
        }
        url = 'https://api.marknife.com/v' + str(self.version) + path
        r = requests.get(url, headers=headers, json=payload)

        if callback != None:
            callback(None, r.json())
        else:
            return r.json()
