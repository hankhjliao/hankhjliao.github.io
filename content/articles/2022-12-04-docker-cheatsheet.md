---
Title: Docker Cheatsheet
Date: 2022-12-04 14:20
Category: Cheatsheet
Tags: docker
Slug: docker-cheatsheet
---

[TOC]

## Terminology

![Docker overview (Image from https://docs.docker.com/get-started/overview/)]({attach}/images/docker-overview.png)

Registry: Where you download others’ image.
Image: Read Only. Like Snapshot in Virtual Machine.
Container: Where you run programs.

## Command: Container

- docker (container) run
<br>
- docker container ls -> docker ps
- docker (container) start/stop/restart/kill/rm `<container ID>`
<br>
- docker (container) attach `<container ID>`
- docker (container) exec -it `<container ID>` `[COMMAND]`
<br>
- docker (container) cp `<from host machine>` `<to container>`
- docker (container) commit `<container ID>` `[image tag]`
- docker (container) rename `<old container name>` `<new container name>`

### docker run
```
docker run [OPTION] <image tag> [COMMAND]
```
OPTION:

- `--name <name>`: name the container
- `--gpus all`: passthrough the gpu (need nvidia-container-toolkit)
- `--restart on-failure`: restart the container when it is failure
- `-i`: interactive mode
- `-t`: tty mode (usually with interactive mode)
- `-d`: detach mode
- `-p 8080:80`: port forwarding
- `-e "<name>=<value>"`: set environment variable
- `--rm`: remove container and volume when exit
<br>
- `-v $(realpath .):/code`: bind mount
- `-v [volume name:]/code`: volume

### Docker storages

![Docker storage. (Image from https://docs.docker.com/storage/)]({attach}/images/docker-storages.png)

1. Volume is managed by Docker. (Default: /var/lib/docker/volumes/ on Linux)
2. When the container stops, the tmpfs mount is removed, and files written there won’t be persisted.
3. tmpfs mount is only for linux.

## Command: Image

- docker (image) build -t `<image tag>` .
<br>
- docker image ls -> docker images
- docker image rm `<image ID>` -> docker rmi
<br>
- docker (image) pull/push `<image ID>`
- docker (image) history `<image ID>`
<br>
- docker search `<image name>`

### Dockerfile
- FROM `<image name>`
- ARG `<name>[=<default value>]`: Change by `--build-arg <name>=<value>`. Available only in build time.
- ENV `<key>=<value>`: Available during build time and container runtime.
- RUN `<cmd>`
- WORKDIR `<path>`: Where you run RUN, CMD, ENTRYPOINT, COPY, ADD, etc.
- COPY `<src>` `<dest>`: Copy files from the host machine to the image.
- VOLUME `<mount point>`: Define the mount point.
- EXPOSE `<port>`: Define expose port.

MUST HAVE ONE AT LEAST:

- ENTRYPOINT
- CMD

### CMD and ENTRYPOINT
|                            | No ENTRYPOINT              | ENTRYPOINT exec_entry p1_entry | ENTRYPOINT ["exec_entry", "p1_entry"]          |
| -------------------------- | -------------------------- | ------------------------------ | ---------------------------------------------- |
| No CMD                     | error, not allowed         | /bin/sh -c exec_entry p1_entry | exec_entry p1_entry                            |
| CMD ["exec_cmd", "p1_cmd"] | exec_cmd p1_cmd            | /bin/sh -c exec_entry p1_entry | exec_entry p1_entry exec_cmd p1_cmd            |
| CMD exec_cmd p1_cmd        | /bin/sh -c exec_cmd p1_cmd | /bin/sh -c exec_entry p1_entry | exec_entry p1_entry /bin/sh -c exec_cmd p1_cmd |

P.S. The `[COMMAND]` in `docker run <image tag> [COMMAND]` will replace the CMD in the Dockerfile.

## Command: Misc.

- docker system df -v
<br>
- docker volume ls
- docker volume rm `<volume name>`
- docker volume inspect `<volume name>`

## Docker migration

Image:

- docker (image) save `<image tag>` > image.tar
- docker (image) load < image.tar

Container:

- docker (container) export `<container ID>` > container.tar
- cat container.tar | docker (container) import - `[image tag]`

Volume:

- docker run --rm --volumes-from `<container 1>` -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar `<path to volume>`
- docker run -v `<path to volume>` --name `<container 2>` ubuntu /bin/bash
- docker run --rm --volumes-from `<container 2>` -v $(pwd):/backup ubuntu bash -c "cd `<path to volume>` && tar xvf /backup/backup.tar --strip 1"

## Docker networks

```
docker run --net=<value>
```
value:

- none: No network.
- container: All the container share the same IP.
- host: The IP is same as host. Security concerns.
- bridge: (Default) Use the network card *docker0* to assign the IP to each container.
- overlay: Communicate with containers on other host machine.

## More Information

- Docker Docs: https://docs.docker.com/
- Install Docker: https://docs.docker.com/engine/install/
- Install nvidia-container-toolkit: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#installation-guide
- Docker Registry (Private Docker Hub): https://docs.docker.com/registry/
- Docker Compose (Run several containers at the same time): https://docs.docker.com/compose/
- Podman (An alternative to docker)
