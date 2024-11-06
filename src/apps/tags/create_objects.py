from apps.tags.models import Tag

tags_name = [
    'technic',
    'home',
    'garden',
    'programming',
    'sport',
    'books',
    'music',
    'cinema',
    'cooking',
    'fashion',
    ]

def generate_tags(tags_name):
    tags = []
    for tag_name in tags_name:
        tag = Tag(name=tag_name, is_active=True)
        tags.append(tag)
    Tag.objects.bulk_create(tags)