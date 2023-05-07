from django.db import models

# Create your models here.
class QuesModel(models.Model):
    question = models.TextField("題目",max_length=2000,null=True)
    qid = models.IntegerField("題號",default=0)
    op1 = models.CharField("A",max_length=200,null=True)
    op2 = models.CharField("B",max_length=200,null=True)
    op3 = models.CharField("C",max_length=200,null=True)
    op4 = models.CharField("D",max_length=200,null=True)
    op5 = models.CharField("E",max_length=200,null=True)
    ans = models.CharField("答案(A、B、C、D、E)",max_length=200,null=True)
    det = models.TextField("詳解",max_length=4000,null=True)
    
    def __str__(self):
        return self.question