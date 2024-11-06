from django.db import models


class CommentManager(models.Manager):
    def get_queryset(self):
        """
        Custom queryset to exclude sof-deleted comments.

        This method ensures that only active comments (those not marked as deleted)
        are retrieved in queries. It utilizes soft-deletion by checking the 'is_deleted' flag,
        which hides the comments from view without actually removing them from the database.

        Why Soft-Deletion:
        - Soft-deletion is used to maintain data integrity and avoid breaking
            comment threads when parent comments are deleted.
        - Even if a parent comment is deleted, its replies (children) remain intact
            and visible, ensuring a seamless conversation flow.

        @return: QuerySet of comments where 'is_deleted' is False.
        """
        return super().get_queryset().filter(is_deleted=False)