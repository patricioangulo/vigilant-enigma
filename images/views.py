from django.shortcuts import redirect, render
from .models import Image
from .helper import humansize, len_wav
from google.cloud import storage
# Create your views here.


def addImage(request):

    if request.method == 'POST':
        data = request.POST
        # file = request.FILES.get('files')
        files = request.FILES.getlist('files')
        blob = request.FILES['files']
        size = len(blob)
        filesize = humansize(size)

        # print('nombre :', blob.name)


        # print('data: ', data)
        # print('file: ', file)
        # print('File Size: ', filesize)

        for file in files:
            image = Image.objects.create(
                file = file,
                name = blob.name,
            )
        return redirect('add')

    ###
    bucket_name = "rec-bucket-0"
    storage_client = storage.Client()   
    blobs_cloud = storage_client.list_blobs(bucket_name)
    size_blobs_cloud = storage_client.list_blobs(bucket_name)
    
    
    
    
    totalsize=0
    totallen=0
    for size_blob_cloud in size_blobs_cloud:
        # print(blob_cloud.name)
        # print(blob_cloud.size)
        totallen +=len_wav(blobs_cloud)
        
        
        totalsize +=size_blob_cloud.size
    ts = humansize(totalsize)
    tl = totallen
    # print('Total Size', totalsize)
    # print('Total Size', ts) 
    ##
    return render(request, 'images/add.html',{
        "blobs_cloud": blobs_cloud,
        "ts": ts,
        "tl": tl,
    })