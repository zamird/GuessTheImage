# GuessTheImage

Example file (tiger):
1uIDZvtEKvVIUak8wv_qrE-wNTSb3cf4a


Example folder (DDG):
1W9QPPgnXqJkY4pk0Wcx0m427JNT1Hwer


Currently supported requests:

Get list of files within folder: 
GET /folder/folder_id

Guess content of image, based on file_id: 
GET /folder/folder_id/file/file_id
GET /file/file_id

Get cache
GET /file/file_id/cache

Clear cache
GET /file/file_id/cache/clear
