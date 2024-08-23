from .interfaces.adapter import CloudAdapterInterface

# NOTE: Openstack images are never imported or published because there's
#   no actual cloud provider associated with them.

class OpenstackAdapter(CloudAdapterInterface):

    def get_latest_imported_tags(self, project, image_key):
        return None

    def import_image(self, ic):
        pass

    def delete_image(self, config, image_id):
        pass

    def publish_image(self, ic):
        pass

def register(cloud, cred_provider=None):
    return OpenstackAdapter(cloud, cred_provider)
