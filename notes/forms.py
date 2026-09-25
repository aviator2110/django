from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label='Name',
        max_length=100,
        min_length=1,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        label='Message',
        min_length=10,
        max_length=1000,
        required=True,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message', 'rows': 5})
    )


class NoteForm(forms.Form):
    CATEGORY_CHOICES = [
        ('study', 'Study'),
        ('work', 'Work'),
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('other', 'Other'),
    ]
    title = forms.CharField(
        label='Title',
        min_length=1,
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your title'})
    )
    content = forms.CharField(
        label='Content',
        min_length=1,
        max_length=1000,
        widget=forms.Textarea(attrs={'placeholder': 'Enter your content', 'rows': 6})
    )
    tags = forms.CharField(
        label='Tags',
        min_length=1,
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your tags. Example: django python...'})
    )
    category = forms.ChoiceField(
        choices=CATEGORY_CHOICES,
        label='Category',
    )

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if title.lower().startswith('test'):
            raise forms.ValidationError('Please enter a valid title.')
        return title

