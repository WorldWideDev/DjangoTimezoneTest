from django.db import models
import bcrypt
from django.core.validators import validate_email, ValidationError
# Create your models here.
class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = "First Name must be 2 or more characters"
        if len(form['last_name']) < 2:
            errors['last_name'] = "First Name must be 2 or more characters"
        try:
            validate_email(form['email'])
        except ValidationError:
            errors['email'] = "Please enter a valid email address"
        if len(self.filter(email=form['email'])) > 0:
            errors['email'] = "Email already in use"
        if len(form['password']) < 8:
            errors['password'] = "Password field must be 8 or more characters"
        return errors
    def register(self, form):
        hashed = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            password=hashed
        )
    def authenticate(self, email, password):
        try:
            user = self.get(email=email)
        except:
            return False
        return bcrypt.checkpw(password.encode(), user.password.encode())

class User(models.Model):
    # here's where the fields go!
    # first_name VARCHAR(255)
    # id
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField
    # posts
    objects = UserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

