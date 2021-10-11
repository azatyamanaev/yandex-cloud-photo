import boto3
import configparser
import click


def objs_len(objs):
    len = 0
    for o in objs:
        len += 1
    return len

def objs_filter(prefix):
    objs = bucket.objects.filter(Prefix=prefix)
    ar = []
    for o in objs:
        if o.key.split('/')[0] == prefix:
            ar.append(o)
    return ar

def upload_files(path,album):
    try:
        for f in os.scandir(path):
            if f.is_file() and (f.path.split('.')[-1].lower() == 'jpg' or f.path.split('.')[-1].lower() == 'jpeg'):
                with open(f.path, 'rb') as pic:
                    bucket.upload_fileobj(pic,'{}/{}'.format(album,f.name))
    except FileNotFoundError:
        print("cloudphoto: cannot upload from {}: No such file or directory".format(path))

def download_files(path,album):
    ar_objs = objs_filter(album)
    if len(ar_objs) == 0:
        print("cloudphoto: cannot download to {}: Album {} does not exist".format(path,album))
        return
    
    try:
        for o in ar_objs:
            f = open('{}/{}'.format(path,o.key.split('/')[-1]), 'wb')
            binary = o.get()['Body'].read()
            f.write(binary)
            f.close()
    except FileNotFoundError:
        print("cloudphoto: cannot download to {}: No such file or directory".format(path))

def list_albums():
    objs = bucket.objects.all()
    if objs_len(objs) == 0:
        print("cloudphoto: There are no albums")
        return

    folders = set()
    for o in objs:
        if o.size > 0 and '/' in o.key:
            folders.add(o.key[:o.key.rfind('/')])
    
    for dir in sorted(folders):
        print(dir)
    
def list_pics_album(album):
    ar_objs = objs_filter(album)
    
    if len(ar_objs) == 0:
        print("cloudphoto: Album {} does not exist".format(album))
        return
    
    for o in ar_objs:
        print(o.key.split('/')[-1])
        
@click.group()
def main(path='',album=''):
    """
    Yandex Cloud tool that allows you upload, download and show list of existing photos in bucket
    """
    
        
@main.command()
@click.option('-a','--album',help='name of the album')
def list(album):
    """
    Show list of albums or photos in album
    """
    if album != None:
        list_pics_album(album)
    else:
        list_albums()
        
@main.command()
@click.option('-p','--path',help='Path from where to upload',required=True)
@click.option('-a','--album',help='Name of the album',required=True)
def upload(path,album):
    """
    Upload photos to album. If album does not exist - create new album
    """
    upload_files(path,album)
    

@main.command()
@click.option('-p','--path',help='Path where to download',required=True)
@click.option('-a','--album',help='Name of the album',required=True)
def download(path,album):
    """
    Download photos from album
    """
    download_files(path,album)


cfg = configparser.ConfigParser()
cfg.read('/home/monitor/Desktop/yamanaev11-802(workdr)/Studies/Cloud technologies/cloudphoto/cp-env/cloudphoto/aws_cfg/config')
region = cfg['default']['region']
bucket_name=cfg['default']['bucket_name']

cfg.read('/home/monitor/Desktop/yamanaev11-802(workdr)/Studies/Cloud technologies/cloudphoto/cp-env/cloudphoto/aws_cfg/credentials')

session = boto3.session.Session()
key_id = cfg['default']['aws_access_key_id']
secret_key = cfg['default']['aws_secret_access_key']

s3resource = session.resource(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id = key_id,
    aws_secret_access_key = secret_key,
    region_name=region
)

bucket = s3resource.Bucket(bucket_name)

if __name__ == "__main__":
    main()

    
