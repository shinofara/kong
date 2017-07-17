# kong

https://getkong.org/install/docker/


## backend-api

```
$ curl http://localhost:8080/items
{"tags": [{"name": "Python", "versions": []}, {"vresions": [], "name": "Falcon"}], "title": "Python+FalconでWebAPI"}
```

## Add API

```
curl -i -X POST \
  --url http://localhost:8001/apis/ \
  --data 'name=shinofara' \
  --data 'domain=shinofara.com' \
  --data 'upstream_url=http://backend-api:8080'
```

### Call API

Kong経由でのAPIリクエスト

```
$ curl http://localhost:8000/items --header 'Host: shinofara.com'
{"tags": [{"name": "Python", "versions": []}, {"vresions": [], "name": "Falcon"}], "title": "Python+FalconでWebAPI"}
```