from notes.models import Note
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


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tags']

        labels = {
            'title': 'Title',
            'content': 'Content',
            'category': 'Category',
            'tags': 'Tags',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter your title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your content', 'rows': 6}),
            'category': forms.Select(),
            'tags': forms.SelectMultiple(),
        }

    def clean_title(self):
        title = self.cleaned_data['title'].strip()

        if title.lower().startswith('test'):
            raise forms.ValidationError('Please enter a valid title.')
        return title

