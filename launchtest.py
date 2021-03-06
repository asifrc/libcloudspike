import os, time
from pprint import pprint
from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver


class StackManager:
    def __init__(self, driver):
        self.driver = driver

    def create_node(self, name, image_id, size_id):
        print "Creating Instance.."
        sizes = self.driver.list_sizes()

        size = [s for s in sizes if s.id == size_id][0]
        image = self.driver.get_image(image_id)

        node = self.driver.create_node(name=name, image=image, size=size)

        print "Instance Created!"
        print node

        print "Starting Instance..."
        nodes_and_ips = self.driver.wait_until_running([node])
        print "Instance runnining at " + nodes_and_ips[0][1][0]
        return nodes_and_ips

    def terminate_node(self, node):
        print "Terminating Instance.."
        self.driver.destroy_node(node)
        print "Instance terminated.."


if __name__ == "__main__":
    ACCESS_ID = os.environ['ACCESS_ID']
    SECRET_KEY = os.environ['SECRET_KEY']

    IMAGE_ID = "ami-e84d8480"
    SIZE_ID = "t1.micro"

    cls = get_driver(Provider.EC2)

    driver = cls(ACCESS_ID, SECRET_KEY)

    manager = StackManager(driver)

    node = manager.create_node("class-libcloud", IMAGE_ID, SIZE_ID)[0][0]

    print "View your instance in the AWS console. The Instance will start shutting down in 30 seconds.."
    time.sleep(30)

    manager.terminate_node(node)
