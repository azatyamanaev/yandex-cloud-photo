# Cloudphoto

A simple commandline app for interacting with bucket in yandex cloud

# Установка

```bash
  $ git clone https://github.com/azatyamanaev/yandex-cloud-photo.git
  $ cd yandex-cloud-photo
  $ python setup.py install
```
Перед выполнением команды python setup.py install необходимо заполнить файлы config и credentials в папке cloudphoto/aws_cfg своими данными, где файл credentials содержит данные о статическом ключе доступа сервисного аккаунта на yandex cloud, а файл config содержит данные о регионе и название бакета, с которым будет работать приложение

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

