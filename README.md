# ChatBot para Twitch usando Docker

Este ChatBot es una herramienta paraimplementar en el chat de Twitch, las funcionalidades por el momento se encuentran limitadas y en proceso de desarrollo, pero se irán implementando funcionalidades internas y externas como complemeno para el bot.

## Requisitos para ejecutar el Bot
- `docker`: Tener instalado Docker, independientemente del sistema operativo que tengas.

## Instalación de Docker
- Windows
`getwin install Docker.Docker`

- Mac
`none`

-Linux
Debian, Ubuntu, Mint
```
apt install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release
```

```
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

```
apt update
```

```
sudo apt remove docker docker-engine docker.io containerd runc
```

```
apt install docker-ce docker-ce-cli containerd.io
```

Arch, Manjaro
`sudo pacman -S docker`

Fedora, Redhad
`sudo dnf install dnf-plugins-core`

`sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo`

`sudo dnf install docker-ce docker-ce-cli containerd.io`

## Creación de Imagen y Contenedor Docker

`docker build -t bot .`

`docker run --privileged --name bot -v /sys/fs/cgroup:/sys/fs/cgroup:ro -ti -d bot`

`docker ps`

`docker exec -it bot /bin/bash`
