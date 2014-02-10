django-mongodb-cache
==================

This is a fork from sicarrots orginal django-mongo-cache backend.
Most important changes/improvements:

1. Cache contens are compressed, you can specify compression level in cache OPTIONS.
2. Cached content can be of any size - this implementation vercomes 16MB BSON document size limit by chunking compressed contents.
3. You can explicitly specify connection and socket timeouts in your OPTIONS.
4. You can specify login/password to your mongoDB instance using your OPTIONS.
5. Cache keys are stored in '_id' field which have automatic index, so it's faster and takes less space than original implementation.
6. Replacing special characters (i.e. '.' and '$') using regex was removed as this may cause some security issues - from now on you are solely responsible of providing key function that creates key which doesn't contain any special characters.
