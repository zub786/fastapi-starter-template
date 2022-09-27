from pymongo import MongoClient

from app.config import settings

__mongo_client__ = None


# connects to a mongo db server (if there isn't a connection yet)
# based on working environment variable env
# returns a mongo connection
def get_connection():
    global __mongo_client__
    if __mongo_client__ is not None:
        return __mongo_client__
    if settings.env == "local":
        __mongo_client__ = MongoClient('localhost', 27017)
    elif settings.env == "develop" or settings.env == "stage":
        uri = "mongodb+srv://maincluster.ejwys.mongodb.net/myFirstDatabase?authSource=%24external&authMechanism" \
              "=MONGODB-X509&retryWrites=true&w=majority "
        __mongo_client__ = MongoClient(uri,
                                       tls=True,
                                       tlsCertificateKeyFile='developer-cert.pem')
    elif settings.env == "prod":
        __mongo_client__ = MongoClient('')
    else:
        print(settings.env)
        raise Exception("other environments are not ready yet")
    return __mongo_client__

