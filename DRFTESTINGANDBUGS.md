# Testing and Bugs (Backend)

## Testing 


## Bugs 


### Issue [#19 Unable to Upload Video to Cloudinary](https://github.com/JamieB92/Gamer-Connect-Backend-PP5/issues/19)

#### Problem
When uploading a video file to Cloudinary, I get the following error when adding a clip to a post through the API:

    Request Method: POST
    Request URL:  http://8000-jamieb92-gamerconnectba-uknrxeyki12.ws-eu106.gitpod.io/posts/?vscodeBrowserReqId=1700389889051
    Django Version: 3.2.23
    Exception Type: Error
    Exception Value: Invalid image file
    Exception Location: /workspace/.pip-modules/lib/python3.9/site-packages/cloudinary/uploader.py, line 527, in call_api

The Model is set to handle an upload to a file using FileField.

#### Expected outcome
- Create a new post
- Enter form information
- Add video clip
- POST
- HTTP 200 ok
- View post from postlist
- View clip

#### Fix:

The issue was I hadn't setup Cloudinary to handle Videos in the model as per this documentation:
https://pypi.org/project/django-cloudinary-storage/#usage-with-video-files

#### Steps to fix:

- run the following in the terminal - pip install django-cloudinary-storage[video]
- Import the following to the top of posts model :

        from cloudinary_storage.storage import VideoMediaCloudinaryStorage
        from cloudinary_storage.validators import validate_video

- create two separate fields for the image upload and video upload
- in the video upload create as following:
        
        upload_clip = models.FileField( upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(), validators=[validate_video])

- in the image upload set as the following:

        upload_image = models.ImageField(upload_to='images/', blank=True)

- Save and make migrations


#### Testing Expected Outcome

I am now able to upload a Video and a Image vie the following steps in the API:

- Go to posts URL
- Fill out the form and add a image using upload image
- POST
- View post and click on image URL
- Go back to posts URL
- Fill out form again but add a clip using upload clip
- POST
- View post and click on video URL
- Both display the Video or Image uploaded via the API