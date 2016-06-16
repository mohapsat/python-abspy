import sys
import json

mail_accounts = []
da = {}
try:
    s = '[{"i":"imap.gmail.com","p":"aaaa"},{"i":"imap.aol.com","p":"bbbb"},{"i":"333imap.com","p":"ccccc"},{"i":"444ap.gmail.com","p":"ddddd"},{"i":"555imap.gmail.com","p":"eee"}]'
    jdata = json.loads(s)
    for d in jdata:
        for key, value in d.iteritems():
            if key not in da:
                da[key] = value
            else:
                da = {}
                da[key] = value
        mail_accounts.append(da)
except Exception, err:
    sys.stderr.write('Exception Error: %s' % str(err))

print mail_accounts
