from treebeard.mp_tree import MP_Node

from django.db import models


class Node(MP_Node):
    slug = models.SlugField()
    name = models.CharField(max_length=50)
    url = models.URLField(null=True)

    def __str__(self):
        return "Node:"+self.slug
