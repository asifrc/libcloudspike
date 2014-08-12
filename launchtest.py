import os
from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

ACCESS_ID = os.environ['ACCESS_ID']
SECRET_KEY = os.environ['SECRET_KEY']

IMAGE_ID = "ami-e84d8480"
SIZE_ID = "t1.micro"

cls = get_driver(Provider.EC2)

driver = cls(ACCESS_ID, SECRET_KEY)

sizes = driver.list_sizes()
size = [s for s in sizes if s.id == SIZE_ID][0]
print size

image = driver.get_image(IMAGE_ID)
print image

# node = driver.create_node(name="asif-libcloudtest", image=image, size=size)
# print node
node = driver.list_nodes()
node[1].destroy()
print 'destroyed'