from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djazcentral' # Must be replaced by your <storage_account_name>
    account_key = 'vkhuvnSwNcPBxGLVgpM0F+w3ukgdJIzMWUEG+mWuNSxPAYIiMbC8XGkT5/ZAGArP/lAX7aRZj/eFLR4VbSlcFw==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djazcentral' # Must be replaced by your storage_account_name
    account_key = 'vkhuvnSwNcPBxGLVgpM0F+w3ukgdJIzMWUEG+mWuNSxPAYIiMbC8XGkT5/ZAGArP/lAX7aRZj/eFLR4VbSlcFw==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None