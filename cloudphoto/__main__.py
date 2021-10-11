import click
from cloudphoto import cp

        
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
        cp.list_pics_album(album)
    else:
        cp.list_albums()
        
@main.command()
@click.option('-p','--path',help='Path from where to upload',required=True)
@click.option('-a','--album',help='Name of the album',required=True)
def upload(path,album):
    """
    Upload photos to album. If album does not exist - create new album
    """
    cp.upload_files(path,album)
    

@main.command()
@click.option('-p','--path',help='Path where to download',required=True)
@click.option('-a','--album',help='Name of the album',required=True)
def download(path,album):
    """
    Download photos from album
    """
    cp.download_files(path,album)


if __name__ == "__main__":
    main()

    
