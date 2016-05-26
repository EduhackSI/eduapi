from treebeard.mp_tree import MP_Node

from django.db import models


class Node(MP_Node):
    slug = models.SlugField()
