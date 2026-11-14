from django.conf import settings
from django.db import models


class Ticket(models.Model):
    class Category(models.TextChoices):
        HELPDESK = "helpdesk", "Helpdesk"
        IAM = "iam", "IAM"
        PROJECT_TASK = "project_task", "Project Task"

    class Status(models.TextChoices):
        OPEN = "open", "Open"
        IN_PROGRESS = "in_progress", "In Progress"
        CLOSED = "closed", "Closed"

    title = models.CharField(max_length=150)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=Category.choices)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="submitted_tickets",
    )

    def __str__(self):
        return self.title