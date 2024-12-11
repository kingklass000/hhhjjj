from django.db import models
from django.contrib.auth.models import AbstractUser



class UserProfile(AbstractUser):
    CHOICES_ROLE = (
        ('teacher', 'teacher'),
        ('student', 'student'),
    )
    user_role = models.CharField(choices=CHOICES_ROLE, default='student', max_length=12)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_picture/')

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'



class Category(models.Model):
    category_name = models.CharField(max_length=32)


    def __str__(self):
        return self.category_name



class Course(models.Model):
    course_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    CHOICES_LEVEL = (
        ('начальный', 'начальный'),
        ('средный', 'средный'),
        ('продвинутый','продвинутый'),
    )
    level = models.CharField(choices=CHOICES_LEVEL, max_length=32, default='начальный')
    price = models.PositiveSmallIntegerField()
    created_by = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image  = models.ImageField(upload_to='course_images/')


    def __str__(self):
        return f'{self.course_name}-{self.category}'


    def get_avg_rating(self):
        ratings = self.course_reviews.all()
        if ratings.exists():
            return round(sum(i.rating for i in ratings) / ratings.count(), 1)
        return 0


    def get_count_people(self):
        ratings = self.course_reviews.all()
        if ratings.exists():
            return ratings.count()
        return  0



class Lesson(models.Model):
    title = models.CharField(max_length=32)
    video_url = models.URLField()
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_content')


    def __str__(self):
        return self.title



class Assignment(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    due_date = models.DateTimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return  self.title



class Exam(models.Model):
    title = models.CharField(max_length=32)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 101)])
    duration = models.DateTimeField()
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.title



class Question(models.Model):
    course = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.TextField()


    def __str__(self):
            return self.question



class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateTimeField()
    certificate_url = models.URLField()


    def __str__(self):
        return f'{self.student}-{self.course}'



class CourseReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name='course_reviews')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()


    def __str__(self):
        return f'{self.user}-{self.course}'



class TeacherReview(models.Model):
    user = models.ForeignKey(UserProfile, on_delete= models.CASCADE, related_name='review_user')
    teacher  = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='teacher_review')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()


    def __str__(self):
        return f'{self.user}-{self.teacher}'