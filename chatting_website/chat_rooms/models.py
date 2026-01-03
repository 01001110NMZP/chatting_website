from django.db import models

class Message(models.Model):
    message_text = models.TextField(null=False,
                                    default="")

    date_posted  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.message_text) >= 40:
            return f"{self.message_text[:40]}..."

        else:
            return self.message_text
