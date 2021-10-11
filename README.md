# Cloudphoto

A simple commandline app for interacting with bucket in yandex cloud

# Установка

```bash
  $ git clone https://github.com/azatyamanaev/yandex-cloud-photo
  $ cd cloudphoto
  $ python setup.py install
```
После скачивания репозитория необходимо заполнить файлы config и credentials своими данными

# Использование

```bash
$ cloudphoto
```

## Просмотр списка альбомов
`list`

```bash
$ cloudphoto list
```

## Просмотр списка фотографий в альбоме
`list -a <album>`

```bash
$ cloudphoto list -a album
```


## Загрузить фотографии в облако

`upload -p <path> -a <album>`

```bash
$ cloudphoto upload -p path -a album
```


## Скачать фотографии из облака

`download -p <path> -a <album>`

```bash
$ cloudphoto download -p path -a album
```

