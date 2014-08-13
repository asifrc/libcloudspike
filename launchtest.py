import os
from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

import libcloud.security

libcloud.security.VERIFY_SSL_CERT = False

class StackManager:
    def __init__(self, driver):
        self.driver = driver

    @classmethod
    def EC2_stack(cls):
        ACCESS_ID = os.environ['ACCESS_ID']
        SECRET_KEY = os.environ['SECRET_KEY']

        ec2 = get_driver(Provider.EC2)

        driver = ec2(ACCESS_ID, SECRET_KEY)

        return cls(driver)

    @classmethod
    def OpenStack(cls):
        OS = get_driver(Provider.OPENSTACK)
        driver = OS("admin", "nomoresecrete", ex_tenant_name="admin", ex_force_auth_url="http://10.1.12.16:5000",
                    ex_force_auth_version="2.0_password")
        return cls(driver)

    def create_node(self, name, image_id, size_id):
        print "Creating Instance.."
        # sizes = self.driver.list_sizes()
        #
        # size = [s for s in sizes if s.id == size_id][0]
        size = self.driver.ex_get_size(size_id)

        image = self.driver.get_image(image_id)

        node = self.driver.create_node(name=name, image=image, size=size)

        print "Instance created!"
        print node

        print "Instance starting..."
        nodes_and_ips = self.driver.wait_until_running([node])
        # print "Instance runnining at " + nodes_and_ips[0][1][0]
        print nodes_and_ips
        return nodes_and_ips

if __name__ == "__main__":
    IMAGE_ID = "ami-e84d8480"
    SIZE_ID = "t1.micro"

    # manager = StackManager.EC2_stack()
    # node = manager.create_node("class-libcloud", IMAGE_ID, SIZE_ID)

    manager = StackManager.OpenStack()
    node = manager.create_node("class-libcloud", "a2aad0e8-0c68-4eac-a22f-ae23d7cc7bf2", "2")

# node = driver.list_nodes()
# node[1].destroy()
# print 'destroyed'