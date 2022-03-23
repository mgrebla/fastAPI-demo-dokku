docker container run \
  --env DOKKU_HOSTNAME=dokku.me \
  --env DOKKU_HOST_ROOT=/var/lib/dokku/home/dokku \
  --detach \
  --rm \
  --name dokku \
  --publish 3022:22 \
  --publish 8080:80 \
  --publish 8443:443 \
  --volume /var/lib/dokku:/mnt/dokku \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  dokku/dokku:0.27.0