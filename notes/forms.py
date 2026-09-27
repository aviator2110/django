from django import forms

FORBIDDEN_WORDS = ['spam', 'scam', 'hack', 'idiot', 'stupid', 'fake']


class ContactForm(forms.Form):
    FORBIDDEN_WORDS = FORBIDDEN_WORDS

    name = forms.CharField(
        label='Name',
        min_length=2,
        max_length=50,
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

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError('Name must contain at least 2 characters.')
        if len(name) > 50:
            raise forms.ValidationError('Name cannot exceed 50 characters.')
        return name

    def clean_email(self):
        return self.cleaned_data.get('email', '').strip()

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()

        if not message:
            raise forms.ValidationError('Message cannot consist only of spaces or be empty.')

        if len(message) < 10:
            raise forms.ValidationError('Message must contain at least 10 characters.')

        if len(message) > 1000:
            raise forms.ValidationError('Message cannot exceed 1000 characters.')

        message_lower = message.lower()
        for word in self.FORBIDDEN_WORDS:
            if word in message_lower:
                raise forms.ValidationError(f'Message contains forbidden word: {word}.')

        return message


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

