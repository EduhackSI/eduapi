from treebeard.mp_tree import MP_Node

from django.db import models


class Node(MP_Node):
    slug = models.SlugField()

    def __str__(self):
        return "Node:"+self.slug

class Item(models.Model):
    node = models.ForeignKey(Node)

class UrlItem(Item):
    url = models.URLField()
